from django import forms
from haystack.forms import SearchForm
from .models import Entry

class ContactForm(forms.Form):
	first_name = forms.CharField(max_length=128,required=True, label="first name" )
	last_name = forms.CharField(max_length=128,required=True, label="last name" )
	email= forms.EmailField(required=True, help_text="please provide valid email")
	comment = forms.CharField(required=True, widget=forms.Textarea) 




class EntrySearchForm(SearchForm):

    def no_query_found(self):
        return self.searchqueryset.all()


# class LikeForm(forms.ModelForm):
# 	model = Entry
# 	fields = ('likes',)

class AddArticleForm(forms.ModelForm):
	tags = forms.CharField(max_length=50)
	
	class Meta:
		model = Entry

		exclude = ['publish','modified','views','likes','tags']

class BashOnButtonForm(forms.Form):
	bash_input = forms.CharField(max_length=128,required=True, label="client_key" )

