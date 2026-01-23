from rest_framework.decorators import api_view
from rest_framework.response import Response

NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

ENHARMONIC_MAP = {
    "DB": "C#",
    "EB": "D#",
    "GB": "F#",
    "AB": "G#",
    "BB": "A#",
}

def normalize(note):
    note = note.upper()
    return ENHARMONIC_MAP.get(note, note)

@api_view(["POST"])
def calculate_transpose(request):
    original = normalize(request.data.get("original"))
    target = normalize(request.data.get("target"))

    original_index = NOTES.index(original)
    target_index = NOTES.index(target)

    diff = target_index - original_index

    if diff > 6:
        diff -= 12
    if diff < -6:
        diff += 12

    new_key_index = (original_index + diff) % 12

    return Response({
        "semitons": diff,
        "transposer": diff,
        "capo": diff if diff >= 0 else diff + 12,
        "new_key": NOTES[new_key_index]
    })
