# from django.shortcuts import render
# from collections import OrderedDict
# from django.http import HttpResponse
import json

'''getting data from json file on disk'''

def model_from_json():
	path = 'management/test.json'

	with open(path,'r+') as json_file:
	    json_data = json_file.read()
	    json_dict = json.loads(json_data)

	   
	    first_name = json_dict[0]['fields']['first_name']
	    last_name = json_dict[0]['fields']['last_name']
	    email = json_dict[0]['fields']['email']
	    skype = json_dict[0]['fields']['skype']
	 
	    	
	return {'last_name':last_name,'first_name':first_name, 'email':email, 'skype':skype }


	'''
	returns formatted json
	'''

	# r = json.load(open(path,'r+'), object_pairs_hook=OrderedDict)
	# dic =  json.dumps(r, indent=2)
	# name = dic['fields'][0]['username']
	# # d = json.loads(dic)
	# # c = dic['fields'][0]['username']

	# return HttpResponse(name)


