NOTAS = [
    "C", "C#", "D", "D#", "E",
    "F", "F#", "G", "G#", "A", "A#", "B"
]

BEMOIS_PARA_SUSTENIDOS = {
    "Db": "C#",
    "Eb": "D#",
    "Gb": "F#",
    "Ab": "G#",
    "Bb": "A#"
}

SUSTENIDOS_PARA_BEMOIS = {
    "C#": "Db",
    "D#": "Eb",
    "F#": "Gb",
    "G#": "Ab",
    "A#": "Bb"
}


def normalizar_nota(nota):
    return BEMOIS_PARA_SUSTENIDOS.get(nota, nota)


def calcular_transposicao(nota_original, nota_desejada):
    nota_original = normalizar_nota(nota_original)
    nota_desejada = normalizar_nota(nota_desejada)

    pos_origem = NOTAS.index(nota_original)
    pos_destino = NOTAS.index(nota_desejada)

    transposer = pos_destino - pos_origem

    if transposer > 6:
        transposer -= 12
    elif transposer < -6:
        transposer += 12

    return transposer


def obter_tonalidade_final(nota_original, transposer, usar_bemois=False):
    nota_original = normalizar_nota(nota_original)
    pos = NOTAS.index(nota_original)
    nova_pos = (pos + transposer) % 12
    nota_final = NOTAS[nova_pos]

    if usar_bemois:
        return SUSTENIDOS_PARA_BEMOIS.get(nota_final, nota_final)

    return nota_final


def sugerir_capotraste(nota_original, nota_desejada, limite=7):
    transposer = calcular_transposicao(nota_original, nota_desejada)

    if transposer < 0:
        return {
            "casa": None,
            "mensagem": "Capotraste não é indicado para baixar o tom"
        }

    if transposer > limite:
        return {
            "casa": None,
            "mensagem": "Capotraste muito alto, considere mudar a tonalidade base"
        }

    return {
        "casa": transposer,
        "mensagem": f"Capotraste sugerido na casa {transposer}"
    }


def sugerir_tonalidade_alternativa(nota_original):
    alternativas = ["C", "D", "E", "G", "A"]

    if nota_original in alternativas:
        return None

    return {
        "mensagem": f"No violão, a tonalidade {nota_original} pode ser difícil. "
                    f"Considere usar uma base em C, D, E, G ou A com capotraste."
    }
