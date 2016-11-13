import json
import time
from watson_developer_cloud import ConversationV1
import capitalone

#flags for different lookup fields for atm and branch queries
is_address_atm = False
address_atm = ''

is_rad_atm = False
rad_atm = ''

is_address_branch = False
address_branch = ''

is_rad_branch = False
rad_branch = ''

#first message with no previous response, to generate a new response
def first_message():
	conversation = ConversationV1(
	  	username='0796628a-8eb1-4ddf-b570-3229ba90960f',
	  	password='1Z27UooowstD',
	  	version='2016-11-12')
	workspace_id = 'b517747a-0164-45cc-a5d4-773365f2e1f1'

	response = conversation.message(workspace_id=workspace_id, 
										message_input={'text': ''})
	result = ''.join(eval(json.dumps(response['output']['text'], indent=2)))
	return (['FinanceBot', result], response)

# evaluates a message from the user and outputs the appropriate response

# return: bot_message, response
def evaluate_message(in_message, old_response):
	global is_address_atm
	global address_atm
	global is_rad_atm
	global rad_atm
	global is_address_branch
	global address_branch
	global is_rad_branch
	global rad_branch
	# Input credentials for ConversationV1 and Workspace.
	conversation = ConversationV1(
	  	username='0796628a-8eb1-4ddf-b570-3229ba90960f',
	  	password='1Z27UooowstD',
	  	version='2016-11-12')
	workspace_id = 'b517747a-0164-45cc-a5d4-773365f2e1f1'
	bot_message = []

	if in_message is '':
		(bot_arr, response) = first_message()
		bot_message = bot_arr
		return (bot_message, response)

	if is_address_atm:
		address_atm = in_message
		is_address_atm = False
		is_rad_atm = True
		bot_message = ['FinanceBot', 'Enter the range [default=1]:']
		return (bot_message, old_response)
	if is_rad_atm:
		rad_atm = in_message
		is_rad_atm = False
		atm = capitalone.run_atm(rad_atm, address_atm)
		if atm[1] == '':
			result = 'There is no branch within %s mile(s) of this location' % atm[0]
		else:
			result = 'The nearest ATM within %s mile(s) of this location is at %s.' % (atm[0], atm[1])
		bot_message = ['FinanceBot', result]
		return (bot_message, old_response)
	if is_address_branch:
		address_branch = in_message
		is_address_branch = False
		is_rad_branch = True
		bot_message = ['FinanceBot', 'Enter the range [default=1]:']
		return (bot_message, old_response)
	if is_rad_branch:
		rad_branch = in_message
		is_rad_branch = False
		branch = capitalone.run_branch(rad_branch, address_branch)
		if branch[1] == '':
			result = 'There is no branch within %s mile(s) of this location' % branch[0]
		else:
			result = 'The nearest branch within %s mile(s) of this location is at %s.' % (branch[0], branch[1])
		bot_message = ['FinanceBot', result]
		return (bot_message, old_response)

	# Get response from FinanceBot with user-inputted message.
	response = conversation.message(workspace_id=workspace_id, 
										message_input={'text': in_message}, 
										context=old_response['context'])
	# Format result (from JSON to string).
	result = ''.join(eval(json.dumps(response['output']['text'], indent=2)))

	# Handle ATM result.
	if result is 'ATM':
		# Get an address and a range from the user.
		result = 'Enter an address [default]:'
		bot_message = ['FinanceBot', result]
		is_address_atm = True
		return (bot_message, response)

	# Handle BRANCH result.
	if result is 'BRANCH':
		result = 'Enter an address [default]:'
		bot_message = ['FinanceBot', result]
		is_address_branch = True
		return (bot_message, response)

	bot_message += ['FinanceBot', result]
	# Get user-inputted message.
	return (bot_message, response)
# bot_message, response = evaluate_message('', None)
# print bot_message
# bot_message, response = evaluate_message('atm', response)
# print bot_message
# bot_message, response = evaluate_message('berkeley', response)
# print bot_message
# bot_message, response = evaluate_message('123', response)
# print bot_message
