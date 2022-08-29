from . import jsmcsv, jsmjson, jsmutil

# trata os dois arquivos e salva em um arquivo chamado db.json
clientesjson = jsmjson.parse_json()
clientescsv = jsmcsv.parse_csv()
db = clientesjson + clientescsv
jsmutil.save_json(db,'db.json')