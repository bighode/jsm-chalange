from rest_framework.response import Response
from rest_framework.decorators import api_view

from . import jsmutil
               
def getError(err_param):
    err_msg = { 'erro': 'Parâmetro inválido: ' + err_param }
    return err_msg

def getTotalCount(pageSize, dbLength):
    mod_div = dbLength % pageSize
    int_div = dbLength // pageSize
    totalCount = int_div if mod_div == 0 else int_div + 1
    return totalCount

@api_view(['GET'])
def getClientes(request):

    # obtem parâmetros
    params = request.GET

    # lê arquivo json
    db = jsmutil.open_json('db.json')

    # se não informou parametro 'type', retorna erro
    if ('type' in params):
        if not (params['type'] in ['especial', 'normal', 'trabalhoso']):
            return Response(getError('type')) 
    else:
        return Response(getError('type')) 

    #  se não informou parâmetro 'region' retorna erro
    if ('region' in params):
        if not (params['region'] in ['Centro-Oeste','Nordeste', 'Norte', 'Sudeste', 'Sul']):
            return Response(getError('region'))
    else:
        return Response(getError('region'))
    
    #  filtra bd
    clientes = [c for c in db if (c['type'] == params['type'] and c['region'] == params['region'])]
    
    #  calcula o número de páginas
    totalCount = getTotalCount(10, len(clientes))
    
    # Além da lista dos usuários elegíveis, para permitir navegação entre os registros, deve ser implementado os seguintes metadados de paginação:
    # cria este dicionário (response)
    res =  {
        'pageNumber': 1,
        'pageSize': 10,
        'totalCount': totalCount,
        'users': []
    }

    # pageSize deve ser um número inteiro maior que zero 
    if ('pageSize' in params):
        try:
            ps = int(params['pageSize'])
            totalCount = getTotalCount(ps, len(clientes))
            
            if (ps > 0):       
                ps = totalCount if ps > totalCount else ps      
                res['pageSize'] = ps
                res['totalCount'] = totalCount
            else:
                return Response(getError('pageSize'))
        except:
            return Response(getError('pageSize'))

    # pageNumber deve ser maior que zero
    # pageNumber deve ser menor ou igual ao total de registros
    if ('pageNumber' in params):
        try:
            pn = int(params['pageNumber'])
            if (pn > 0) and pn <= totalCount:
                res['pageNumber'] = pn
            else:
                return Response(getError('pageNumber'))
        except:
            return Response(getError('pageNumber'))
    
    start_reg = (res['pageNumber'] - 1) * res['pageSize']    
    end_reg = (res['pageSize'] * res['pageNumber'])
    
    #  pagina
    res['users'] = clientes[start_reg : end_reg]

    # response
    return Response(res)

@api_view(['GET'])
def getHome(request):
    return Response({'pagina de ajuda aqui'})