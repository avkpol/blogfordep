from django.db import models
from django.http import HttpResponseForbidden, HttpResponseRedirect

from management.models.user_model import User
from management.from_json import model_from_json
from .forms import UserDataForm
from django.shortcuts import render, render_to_response, RequestContext, get_object_or_404

from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist

# from jsonview.decorators import json_view

# from dajaxice.utils import deserialize_form
# from dajaxice.decorators import dajaxice_register


def form_save_and_edit(request, id=None, template_name='create.html'):

	""" referring data from "model_from_json()",
	making data visible within another function """
	
	func = model_from_json()

	""" savind and editing form data in the same form """
	
	
	form = UserDataForm(request.POST)
	if request.POST:
	
			

			updated_field = form.save()
			last_name = request.session['last_name'] = updated_field.last_name
			first_name = request.session['first_name'] = updated_field.first_name
			email = request.session['email'] = updated_field.email
			skype = request.session['skype'] = updated_field.skype
			
			form = UserDataForm({
			'last_name': last_name,
			'first_name': first_name,
			'skype':skype,
			'email':email
			})
			
			redirect_url = reverse('create')
			message = messages.info(request, "You successfully updated your profile!")
			
			if form.is_valid():
				form.save()
			
	else:

		form = UserDataForm({
			'last_name': func['last_name'],
			'first_name':func['first_name'],
			'email':func['email'],
			'skype':func['skype'],
			
			})
		
		message = messages.success(request, "You just loaded your profile initial data")
	return render_to_response('create.html', {'form': form,}, context_instance=RequestContext(request))

	# @dajaxice_register
	# def send_form(request, form):
	#     dajax = Dajax()
	#     form = UserDataForm(deserialize_form(form))

	#     if form.is_valid():
	#         dajax.remove_css_class('#my_form input', 'error')
	#         dajax.alert("Form is_valid(), your username is: %s" % form.cleaned_data.get('username'))
	#     else:
	#         dajax.remove_css_class('#my_form input', 'error')
	#         for error in form.errors:
	#             dajax.add_css_class('#id_%s' % error, 'error')

	#     return dajax.json()

	# def dajax_example(request, text):
	#     return simplejson.dumps({'message':'Hello from Python!'})




# def send_form_via_ajax(request):
# 	 if request.is_ajax() and request.POST:
# 	 	form = UserDataForm(request.POST or None)
# 	 	if form.is_valid():
# 	 		form.save()
#         #do some stuff
       
#         new_data = json.dumps("string text")
#         return HttpResponse(new_data, context_type='application/json')
#     else:
#         raise Http404






# @json_view
# def send_form_via_ajax(request):
#     form = UserDataForm(request.POST or None)
#     if form.is_valid():
#         # You could actually save through AJAX and return a success code here
#         form.save()
#         return {'success': True}

#     # RequestContext ensures CSRF token is placed in newly rendered form_html
#     request_context = RequestContext(request)
#     form_html = render_crispy_form(form, context=request_context)
#     return {'success': False, 'form_html': form_html}
	








# def form_edit(request, id=None, template_name='create.html'):

# 	func = model_from_json()
# 	try:
# 	    id = request.session['id']
# 	    new_record=User.objects.get(id=id)
# 	    form=UserDataForm(request.POST,  request.FILES, instance = new_record)

# 	except:
# 	    form = UserDataForm({
# 	    'last_name': func['last_name'],
# 	    'first_name':func['first_name'],
# 	    'email':func['email'],
# 	    'skype':func['skype'],
# 	    })
# 	    if form.is_valid():
# 			form.save()
# 	try:
# 		form=UserDataForm(request.POST, request.FILES, instance = new_record)
# 		if form.is_valid():
# 			form.save()

# 	except Exception, e:
# 	    print e
# 	return render_to_response('create.html', {'form': form,}, context_instance=RequestContext(request))


	# func = model_from_json()
	# try:
	#     id = request.session['id']
	#     new_record=User.objects.get(id=id)
	#     form=UserDataForm(request.POST, instance = new_record)
	# except:
	#     form = UserDataForm({
	#     'last_name': func['last_name'],
	#     'first_name':func['first_name'],
	#     'email':func['email'],
	#     # 'date':func['date']
	#     })
	# try:
	#     form=UserDataForm(request.POST, instance = new_record)
	#     form.save()
	    
	# except Exception, e:
	#     print (e)
	# return render_to_response('create.html', {'form': form,}, context_instance=RequestContext(request))





	# func = model_from_json()
	# try:
	#     id = request.session['id']
	#     new_record=User.objects.get(id=id)
	#     form=UserDataForm(request.POST, instance = new_record)
	# except:
	#     form = UserDataForm({
	#     'last_name': func['last_name'],
	#     'first_name':func['first_name'],
	#     'email':func['email'],
	#     # 'date':func['date']
	#     })
	# try:
	#     form=UserDataForm(request.POST, instance = new_record)
	#     form.save()

	# except Exception, e:
	#     print e
	# return render_to_response('create.html', {'form': form,}, context_instance=RequestContext(request))


	# func = model_from_json()
	# try:
	#     id = request.session['id']
	#     new_record=User.objects.get(id=id)
	#     form=UserDataForm(request.POST, instance = new_record)
	# except:
	#     form = UserDataForm({
	#     'last_name': func['last_name'],
	#     'first_name':func['first_name'],
	#     'email':func['email'],
	#     # 'date':func['date']
	#     })
	# try:
	#     form=UserDataForm(request.POST, instance = new_record)
	#     form.save()

	# except Exception, e:
	#     print e
	# return render_to_response('create.html', {'form': form,}, context_instance=RequestContext(request))






# def form_edit(request, id=None, template_name='create.html'):
# 	func = model_from_json()
	
# 	try:
# 		form = UserDataForm(request.POST or None, instance=id)
# 		user_id = request.session['id']
# 		new_record=User.objects.get(id=user_id)
       
#         if form.is_valid() and request.method=="POST":
#             form = UserDataForm(request.POST or None, instance=id)
#             newform = form.save(commit=False)
#             newform.save()
#         return HttpResponseRedirect('create.html')    
#     except:
#         form = UserDataForm(request.POST or None)
#         if form.is_valid() and request.method=="POST":
#         	form = UserDataForm(request.POST,{
# 	 		'last_name': func['last_name'],
# 	 		'first_name':func['first_name'],
# 	 		'email':func['email'],
# 			})
#             newform = form.save(commit=False)
#             newform.save()
#     return render_to_response('edit.html', {'form': form,}, context_instance=RequestContext(request))







	# func = model_from_json()
	# form = UserDataForm(request.POST)
	
	# if request.POST:
	# 	form = UserDataForm(request.POST,{
	# 		'last_name': func['last_name'],
	# 		'first_name':func['first_name'],
	# 		'email':func['email'],
			
	# 		})
	# 	if form.is_valid():
	# 			form.save()
	# 	message = messages.success(request, "You just loaded your profile initial data")
	# 	message = messages.success(request, "You just loaded your profile initial data")
		
	# 	return HttpResponseRedirect(redirect_url)	
	# else:
	# 	updated_field = form.save()

	# 	last_name = request.session['last_name'] = updated_field.last_name
	# 	first_name = request.session['first_name'] = updated_field.first_name
	# 	# date = request.session['last_name'] = updated_field.date
	# 	email = request.session['first_name'] = updated_field.email
		
	# 	form = UserDataForm(request.POST,{
	# 	'last_name': last_name,
	# 	'first_name': first_name,
	# 	# 'date':date,
	# 	'email':email,
	# 	})
		
	# 	message = messages.success(request, "You successfully updated your profile!")
	# 	redirect_url = reverse('create')
	# 	message = messages.success(request, "You successfully updated your profile!")
		
	# 	if form.is_valid():
	# 		form.save()
						
		
		
	# return render_to_response('edit.html', {'form': form,}, context_instance=RequestContext(request))
	

	# func = model_from_json()
	# form = UserDataForm(request.POST)
	
	# if request.POST:
	# 	if form.is_valid():
	# 		form.save()
	  
	# 		updated_field = form.save()

	# 		last_name = request.session['last_name'] = updated_field.last_name
	# 		first_name = request.session['first_name'] = updated_field.first_name
	# 		# date = request.session['last_name'] = updated_field.date
	# 		email = request.session['first_name'] = updated_field.email
			
	# 		form = UserDataForm({
	# 		'last_name': last_name,
	# 		'first_name': first_name,
	# 		# 'date':date,
	# 		'email':email,
	# 		})
			
	# 		message = messages.success(request, "You successfully updated your profile!")
	# 		redirect_url = reverse('create')
	# 		message = messages.success(request, "You successfully updated your profile!")
			
	# 		# if form.is_valid():
	# 		# 	form.save()
						
	# 		return HttpResponseRedirect(redirect_url)
	# else:

	# 	form = UserDataForm(request.POST,{
	# 		'last_name': func['last_name'],
	# 		'first_name':func['first_name'],
	# 		'email':func['email'],
			
	# 		})
	# 	message = messages.success(request, "You just loaded your profile initial data")
	# 	message = messages.success(request, "You just loaded your profile initial data")
	# return render_to_response('edit.html', {'form': form,}, context_instance=RequestContext(request))
	



	# func = model_from_json()
	
	
	
	# 	user_id = request.session['id']
	# 	new_record=User.objects.get(id=user_id)
		
	# except ObjectDoesNotExist:
	# 	print 'gdgdgfgfgfggf'
	# 	# form = UserDataForm({
	# 	# 	'last_name': func['last_name'],
	# 	# 	'first_name':func['first_name'],
	# 	# 	'email':func['email'],
	# 	# 	# 'date':func['date']
	# 	# 	})

	# 	form = UserDataForm(request.POST, instance = new_record)
	# if form.is_valid():
	# 	form.save(commit=True)
	# 	print form.errors

				
	# return render_to_response('create.html', {'form': form,}, context_instance=RequestContext(request))


	
	
	
		
	# if id:
	#     username = get_object_or_404(User, pk=id)
	#     if User.user != request.user:
	#     	print id
	#         return HttpResponseForbidden()
	# else:
	#     username = User(username=request.user)

	# func = model_from_json()
	
	# form = UserDataForm(request.POST)
	# if request.POST:
	  
	# 	updated_field = form.save()
	# 	request.session['new_rec'] = updated_field.id
	# 	new_record=User.objects.get(id=request.session['new_rec'])
	# 	new_last_name = new_record.last_name
	# 	new_first_name = new_record.first_name
	# 	new_email = new_record.email
	# 	new_date = new_record.date
	# 	form = UserDataForm({
	# 	'last_name': new_last_name,
	# 	'first_name': new_first_name,
	# 	# 'date':new_date,
	# 	'email':new_email,
	# 	})
		
	# 	message = messages.success(request, "You successfully updated your profile!")
	# 	redirect_url = reverse('create')
	# 	message = messages.success(request, "You successfully updated your profile!")
		
	# 	if form.is_valid():
	# 		form.save()
					
	# 		return HttpResponseRedirect(redirect_url)
	# else:

	# 	form = UserDataForm({
	# 		'last_name': func['last_name'],
	# 		'first_name':func['first_name'],
	# 		'email':func['email'],
	# 		'date':func['date']
	# 		})
	# 	message = messages.success(request, "You just loaded your profile initial data")
	# 	message = messages.success(request, "You just loaded your profile initial data")
	# return render_to_response('edit.html', {'form': form,}, context_instance=RequestContext(request))

# from crispy_forms.utils import render_crispy_form
# from jsonview.decorators import json_view
# """need to istall django-jsonview
# 	pip install django-jsonview
#                    """




# new = User.objects.create(date = date, username= username,email=email)
	# new.last_name = str(request.user.last_name)
	# new.save()
	# last_name = str(request.user.last_name)	
	# template = 'create.html'
# def form_edit(request, id=None, template_name='create.html'):

# 	func = model_from_json()

# 	try:
# 		user_id = request.session['id']
# 		new_record=User.objects.get(id=user_id)
		
		
# 		form=UserDataForm(request.POST, instance = new_record)
# 		if form.is_valid():
# 			form.save()
			
		

# 		redirect_url = reverse('create')
# 		message = messages.success(request, "You successfully updated your profile!")
		
# 		message = messages.success(request, "You successfully updated your profile!")
		
				
# 		return HttpResponseRedirect(redirect_url,{'form': form,},)
	


# 	except:
# 		form = UserDataForm({
# 			'last_name': func['last_name'],
# 			'first_name':func['first_name'],
# 			'email':func['email'],
# 			'date':func['date']
# 			})
# 		message = messages.success(request, "You just loaded your profile initial data")
# 		message = messages.success(request, "You just loaded your profile initial data")	
# 	return render_to_response('create.html', {'form': form,}, context_instance=RequestContext(request))


		
	# if id:
	#     username = get_object_or_404(User, pk=id)
	#     if User.user != request.user:
	#     	print id
	#         return HttpResponseForbidden()
	# else:
	#     username = User(username=request.user)

	# form = UserDataForm(request.POST)
	# if request.POST:
	  
	# 	updated_field = form.save()
	# 	request.session['id'] = updated_field.id


		# last_name = request.session['last_name'] = updated_field.last_name
		# first_name = request.session['first_name'] = updated_field.first_name
		# # date = request.session['last_name'] = updated_field.date
		# email = request.session['first_name'] = updated_field.email
		
		# if 'last_name' in request.session['new_rec']:
		# 	last_name = request.session['last_name']
			

		# new_record=User.objects.get(id=request.session['new_rec'])
		# new_last_name = new_record.last_name
		# new_first_name = new_record.first_name
		# new_email = new_record.email
		# new_date = new_record.date
		# form = UserDataForm({
		# 'last_name': last_name,
		# 'first_name': first_name,
		# # 'date':date,
		# 'email':email,
		# })
		
		# message = messages.success(request, "You successfully updated your profile!")
		# redirect_url = reverse('create')
		# message = messages.success(request, "You successfully updated your profile!")
		
		# if form.is_valid():
		# 	form.save()
					
		# 	return HttpResponseRedirect(redirect_url)

# def form_edit(request, id=None, template_name='create.html'):

# 	""" referring data from "model_from_json()",
# 	making data visible within another function """
	
# 	func = model_from_json()
	
# 	form = UserDataForm(request.POST)
# 	if request.POST:
	  
# 		updated_field = form.save()
# 		request.session['new_rec'] = updated_field.id
# 		new_record=User.objects.get(id=request.session['new_rec'])
# 		last_name = request.session['last_name'] = updated_field.last_name
# 		first_name = request.session['first_name'] = updated_field.first_name
# 		skype = request.session['skype'] = updated_field.email
# 		email = request.session['email'] = updated_field.email

# 		form = UserDataForm({
# 		'last_name': last_name,
# 		'first_name': first_name,
# 		'skype': skype,
# 		'email':email
# 		})
		
# 		# message = messages.success(request, "You successfully updated your profile!")
# 		redirect_url = reverse('create')
# 		message = messages.success(request, "You successfully updated your profile!")
	
# 		if form.is_valid():
# 			form.save()
					
# 			return HttpResponseRedirect(redirect_url)
# 	else:

# 		form = UserDataForm({
# 			'last_name': func['last_name'],
# 			'first_name':func['first_name'],
# 			'email':func['email'],
# 			'skype':func['skype']
# 			})
# 		message = messages.success(request, "You just loaded your profile initial data")
# 		# message = messages.success(request, "You just loaded your profile initial data")
# 	return render_to_response('create.html', {'form': form,}, context_instance=RequestContext(request))












	
		
	

