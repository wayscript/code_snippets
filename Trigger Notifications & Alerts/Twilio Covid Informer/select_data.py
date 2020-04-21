state = variables['Column_1_Item']
data = variables['data_to_pass']

print(state)

info_to_send = data.get(state)

variables['info'] = info_to_send
