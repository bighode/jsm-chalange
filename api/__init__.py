from . import jsmcsv, jsmjson, jsmutil

# trata os dois arquivos e salva em um arquivo chamado db.json
clientescsv = jsmcsv.get_clientes()
clientesjson = jsmjson.get_clientes()
json_content = clientescsv + clientesjson
jsmutil.save_json(json_content,'db.json')