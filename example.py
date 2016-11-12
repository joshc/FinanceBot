import json
from watson_developer_cloud import ConversationV1

conversation = ConversationV1(
  	username='0796628a-8eb1-4ddf-b570-3229ba90960f',
  	password='1Z27UooowstD',
  	version='2016-11-12')

workspace_id = '412de3bd-3d93-44ee-ac1a-0b82ab31d618'

response = conversation.message(workspace_id=workspace_id, message_input={'text': 'Where\'s the closest ATM?'})
print(json.dumps(response, indent=2))
while True:
	response = conversation.message(workspace_id=workspace_id, message_input={'text': raw_input('>>>\t')})
	print(json.dumps(response['output']['text'], indent=2))