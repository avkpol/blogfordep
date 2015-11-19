from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def checkout(request):
	if request.method=='POST':
		
		stripe_token = request.POST['stripeToken']
		print stripe_token
	
	context = {}
	template = 'checkout.html'
	return render(request, template, context)

