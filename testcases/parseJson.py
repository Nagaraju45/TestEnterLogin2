import json

odics = '{"K1":"Val1", "K2":"Val2", "K3":"Val3"}'
json_result = json.loads(odics)
print(json_result)
print(json_result['K1'])
print(json_result.keys())
print(json_result.values())