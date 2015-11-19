from django.db import models

#from django.db import models
from django.forms import ModelForm
from management.views import load_fixture

class User(models.Model):
    """This class represents a physical server."""
    last_name = models.CharField('name', 
        max_length = 50
    )
    
    def __unicode__(self):
        """Make the model human readable."""
        return self.last_name

class UserDataForm(ModelForm):
    """Auto generated form to create Server models."""
    class Meta:
    	model = User
    	# fields = '__all__'
