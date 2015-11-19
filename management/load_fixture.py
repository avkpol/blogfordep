from django.shortcuts import render
import json
from collections import OrderedDict

from django.http import HttpResponse
# from management.models import user_model
# from management import load_fixture

path = 'management/test.json'


def load_fixture1(request):

	with open(path,'r+') as json_file:
	    json_data = json_file.read()
	    json_dict = json.loads(json_data)

	    first_name = json_dict[0]['fields']['first_name']
	    last_name = json_dict[0]['fields']['last_name']
	    date = json_dict[0]['fields']['last_login']
	    email = json_dict[0]['fields']['email']
	    
	    
	    
	    context={
	      	'first_name':first_name,
	      	'last_name':last_name,
	      	'date':date,
	      	'email':email
	    }
	    
        template = 'create.html'

	return render (request ,template, context)

	







