from . import jsmcsv, jsmjson, jsmutil

# O carregamento dos dados de input deve ser por meio de request HTTP ao subir a sua aplicação, ou seja, antes do seu App estar ready

# trata os dois arquivos e salva em um arquivo chamado db.json
clientesjson = jsmjson.parse_json()
clientescsv = jsmcsv.parse_csv()

db = clientesjson + clientescsv

# Os dados devem ser armazenados conforme o contrato de OUTPUT também.
jsmutil.save_json(db,'db.json')