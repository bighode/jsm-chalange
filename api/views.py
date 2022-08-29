from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.serializers import serialize

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

    # # se não tem registros, adianta o lado
    # if not db:
    #     return Response(db)

    # se não informou parametro 'type', retorna todos os clientes 
    clientes = db
    if ('type' in params):
        if params['type'] in ['especial', 'normal', 'trabalhoso']:
            clientes = [c for c in db if c['type'] == params['type']]
        else:
            return Response(getError('type'))       
    
    #  calcula o número de páginas
    totalCount = getTotalCount(10, len(clientes))

    # cria este dicionário (response)
    res =  {
        'pageNumber': 1,
        'pageSize': 10,
        'totalCount': totalCount,
        'users': []
    }

    # pageSize deve ser um número inteiro maior que zero 
    # e menor ou igual ao total de páginas
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
    
    #  define inicio e fim da paginação
    print('pageNumber: ', res['pageNumber'])
    print('pageSize: ', res['pageSize'])

    start_reg = (res['pageNumber'] - 1) * res['pageSize']    
    end_reg = (res['pageSize'] * res['pageNumber'])
  
    print('start_reg: ', start_reg)
    print('end_reg', end_reg)

    res['users'] = clientes[start_reg : end_reg]

    # response
    return Response(res)

@api_view(['GET'])
def getHome(request):
    return Response({'pagina de ajuda aqui'})