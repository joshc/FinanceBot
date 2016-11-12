import json
import time
from watson_developer_cloud import ConversationV1
import capitalone

if __name__ == '__main__':
	# Input credentials for ConversationV1 and Workspace.
	conversation = ConversationV1(
	  	username='0796628a-8eb1-4ddf-b570-3229ba90960f',
	  	password='1Z27UooowstD',
	  	version='2016-11-12')
	workspace_id = 'b517747a-0164-45cc-a5d4-773365f2e1f1'

	# Display instructions to quit.
	print('Type \'q\' or \'quit\' to exit.')
	time.sleep(1)

	# Start up conversation with FinanceBot.
	response = conversation.message(workspace_id=workspace_id, 
									message_input={'text': ''})
	print('FinanceBot >>> ' + ''.join(eval(json.dumps(response['output']['text'], indent=2))))

	while True:
		# Get user-inputted message.
		in_message = raw_input('You        >>> ')
		# Add method to quit.
		if (in_message in {'q', 'quit'}):
			raise SystemExit
		# Get response from FinanceBot with user-inputted message.
		response = conversation.message(workspace_id=workspace_id, 
										message_input={'text': in_message}, 
										context=response['context'])
		# Format result (from JSON to string).
		result = ''.join(eval(json.dumps(response['output']['text'], indent=2)))
		
		# Handle ATM result.
		if result is 'ATM':
			# Get an address and a range from the user.
			print('FinanceBot >>> Please input an address and a range ...')
			time.sleep(0.5)
			address = raw_input("           >>> Enter an address [default]: ")
			rad = raw_input("           >>> Enter the range [default=1]: ")
			# Get the nearest ATM
			atm = capitalone.run_atm(rad, address)
			result = 'The nearest ATM within %s mile(s) of this location is at %s.' % (atm[0], atm[1])

		# Handle BRANCH result.
		if result is 'BRANCH':
			# Get an address and a range from the user.
			print('FinanceBot >>> Please input an address and a range ...')
			time.sleep(0.5)
			address = raw_input("           >>> Enter an address [default]: ")
			rad = raw_input("           >>> Enter the range [default=1]: ")
			# Get the nearest branch
			branch = capitalone.run_branch(rad, address)
			result = 'The nearest branch within %s mile(s) of this location is at %s.' % (branch[0], branch[1])

		# Print FinanceBot's message
		print('FinanceBot >>> ' + result)
