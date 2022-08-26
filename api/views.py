from http import client
from rest_framework.response import Response
from rest_framework.decorators import api_view

from . import jsmutil

@api_view(['GET'])
def getClientes(request):

    # lê arquivo json
    data = jsmutil.open_json('db.json')

    # se não informou parametro, retorna todos os clientes
    params = request.GET
    if not 'type' in params:
        return Response(data)

    #  retorna apenas os elegiveis
    elegiveis = []
    for cliente in data:
        if cliente['type'] == request.GET['type']:
            elegiveis.append(cliente)
    return Response(elegiveis)