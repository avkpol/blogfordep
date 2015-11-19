'''
django-split-json-widget (autofill django forms with json data)

https://github.com/abbasovalex/django-SplitJSONWidget-form

Installation

pip install django-split-json-widget 
or pip install git+https://github.com/abbasovalex/django-SplitJSONWidget-form.git
'''

from django import forms
from splitjson.widgets import SplitJSONWidget


class Form(forms.Form):
    attrs = {'class': 'special', 'size': '40'}
    data = forms.CharField(widget=SplitJSONWidget(attrs=attrs, debug=True))