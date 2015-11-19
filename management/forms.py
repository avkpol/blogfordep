from django.shortcuts import render_to_response
import json
from django import forms
# from management.views import load_fixture
from management.models.user_model  import User
from django.template import RequestContext
# from management.create import model_from_json

# class UserDataForm(ModelForm):
#     """Auto generated form to create User model"""
#     class Meta:
#     	model = User


class UserDataForm(forms.ModelForm):
    
    
    class Meta:
        model = User
        # fields = '__all__'   
        exclude=('username',)
	



















# path = 'management/test.json'


# class ContactForm(forms.Form): 

# 	with open(path,'r+') as json_file:
# 	    json_data = json_file.read()
	    
# 	    json_dict = json.loads(json_data)
	    
# 	    date = json_dict[0]['fields']['last_login']
# 	    name = json_dict[0]['fields']['username']
# 	    first_name = name
	    
	
    
	# def load_fixture(request):
	# 	data = {
	#     	'first_name':first_name
	#     }
	    
	#     # context={
	#     #   	'name':name
	#     # }
	    
 #        template = 'create.html'
	# 	form = ContactForm(data)        

	# return render (request ,template, form)
