from management.models.user_model import User, UserDataForm
from django.core import serializers
from django.template import RequestContext
from django.shortcuts import render_to_response
# from management.views.create import model_from_json



        
   

# def create_model(request):
#     """Create a new User form """
    
#     if request.method == 'POST':
#         form = UserDataForm(request.POST)

#         if form.is_valid():

#             # Create a new Server object.
#             form.save()
#     else:
#         form = UserDataForm(username)
        
#     context = RequestContext(request, {
#         'form': form 

            
#     })
#     return render_to_response('create.html', context)



