from django.db import models
from django import forms
from django.utils import timezone
from django.shortcuts import render_to_response, RequestContext, get_object_or_404

from django.forms import ModelForm
from management import load_fixture

class User(models.Model):
    
    
    last_name = models.CharField(max_length = 50, null = True)
    first_name = models.CharField(max_length = 50)
    # date_of_birth = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now )
    # photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    email = models.EmailField(null = True)
    skype = models.CharField(max_length = 50, null = True)


    def __unicode__(self):
        
        return '%s %s' %( self.last_name, self.email)



# class UserDataForm(forms.Form):
#     """Auto generated form to create User model"""
    
#     class Meta:
#         model = User
#         fields = '__all__'   
    # def populate_form(request, last_name):
    #     last_name = get_object_or_404(User, last_name=last_name)
    #     form = UserDataForm(instance=last_name)
    #     return render_to_response('create.html', {'form': form})
        
    
    	
    # username = forms.ModelChoiceField(queryset=User.objects.none())

    # def populate_form(self, *args, **kwargs):
    #     username = forms.ModelChoiceField(queryset=User.objects.none())
    #     super(UserDataForm, self).__init__(*args, **kwargs)
    #     self.fields['username'] = forms.ModelChoiceField(queryset=User.objects.filter(username=username))
    #     usn = self.fields['username']
    #     form = UserDataForm(usn)

        
    # # def __init__(self, *args, **kwargs):
    # #     super(EditEventForm, self).__init__(*args, **kwargs)
    # #     self.fields['bands'].queryset= \
    # #                   Bands.objects.filter(Q(name='band1')|Q(name='band2'))
    # # class Meta:
    # #     model = Event    

            

    #     return render_to_response('create.html', {'form': form}) 

       
            
    # 