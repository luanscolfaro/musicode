from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .services.music_theory import (
    calcular_transposicao,
    obter_tonalidade_final,
    sugerir_capotraste,
    sugerir_tonalidade_alternativa
)


@api_view(['POST'])
def calcular_musica(request):
    try:
        nota_original = request.data.get("nota_original")
        nota_desejada = request.data.get("nota_desejada")
        instrumento = request.data.get("instrumento")
        usar_bemois = request.data.get("usar_bemois", False)

        if not nota_original or not nota_desejada:
            return Response(
                {"erro": "Notas são obrigatórias"},
                status=status.HTTP_400_BAD_REQUEST
            )

        transposer = calcular_transposicao(nota_original, nota_desejada)

        resposta = {
            "transposer": transposer,
            "tonalidade_final": obter_tonalidade_final(
                nota_original,
                transposer,
                usar_bemois
            ),
            "instrumento": instrumento
        }

        if instrumento == "violao":
            resposta["capotraste"] = sugerir_capotraste(
                nota_original,
                nota_desejada
            )

            sugestao = sugerir_tonalidade_alternativa(nota_original)
            if sugestao:
                resposta["sugestao"] = sugestao

        return Response(resposta)

    except Exception as e:
        return Response(
            {"erro": str(e)},
            status=status.HTTP_400_BAD_REQUEST
        )
