

from django.shortcuts import render_to_response
from django.template import RequestContext
from management.autofill_form import Form
from management.views import load_fixture
import json

path = 'management/test.json'

def test_dict(request):
    with open(path,'r+') as json_file:
        json_data = json_file.read()
        
        json_dict = json.loads(json_data)

	
    # json = {'a': 1,
    #         'b': 2,
    #         'c': 3,
    #         'd': 4}
    
    form = Form(request.POST or None, initial={'data': json_dict})
    if form.is_valid():
        # validate and save
        pass

    template = 'autofill.html'
    context = RequestContext(request, {'form': form})
    return render_to_response(template, context)