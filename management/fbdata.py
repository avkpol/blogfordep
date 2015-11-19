# import requests
# import sqlite3
# import os
# from datetime import datetime
# from qblog import settings

from django.shortcuts import render_to_response
from django.template.context import RequestContext

def fb(request):
    context = RequestContext(request,{'request': request,'user': request.user})
    user = request.user
    print user
    return render_to_response('fb.html',context_instance=context)




# GRAPH_API_URL='https://graph.facebook.com/'
# def fb_complete_login(request):
#     resp = requests.get(GRAPH_API_URL + '/avkpol',
#                         params={'access_token': settings.FACEBOOK_USER_ACCESS_TOKEN})
#     # resp.raise_for_status()
#     print resp
#     extra_data = resp.json()
#     login = providers.registry.by_id(FacebookProvider.id).sociallogin_from_response(request, extra_data)
#     return login







# # Fetch Facebook page metrics via Social Graph API into a SQLite DB
# # Grabs the number of likes and "talking about" numbers
 
# import requests
# import sqlite3
# import os
# from datetime import datetime
# from django.shortcuts import render, render_to_response, RequestContext, get_object_or_404
# """
# # # Monkeypatch python not to print "Broken Pipe" errors to stdout.
# # import SocketServer """
# # from wsgiref import handlers
# # SocketServer.BaseServer.handle_error = lambda *args, **kwargs: None
# # handlers.BaseHandler.log_exception = lambda *args, **kwargs: None
 

# base_url = 'https://graph.facebook.com/'

# # These are the accounts for which you will fetch data
# names_list = [
#     'avkpol'
# ]
# # API base URL
# user = requests.django_allauth.filter(
#     provider='facebook',
# ).first()

# for user in names_list:
#         url = base_url + user 
#         print 'Fetching ' + user
#         response = requests.get(url)
#         profile = response.json()
#         # handle = profile['name']
#         print profile
#         # likes = profile['likes']
 
# # Function to add row to accounts table
# def insert_db(request):
#     conn = sqlite3.connect('social_data.db')
#     cur = conn.cursor()
#     cur.execute('''
#         INSERT INTO fbaccounts VALUES (?,?,?,?);
#         ''', (datetime.now(),likes))
#     conn.commit()
#     conn.close()
 
#     # Create the database if it doesn't exist
#     if not os.path.exists('social_data.db'):
#         conn = sqlite3.connect('social_data.db')
#         conn.close()
#     else:
#         pass
     
#     # Create the table if it's not in the db
#     conn = sqlite3.connect('social_data.db')
#     cur = conn.cursor()
#     cur.execute('''CREATE TABLE IF NOT EXISTS fbaccounts 
#         (FetchDate Date, Handle Text, Likes Integer, Talking Integer)
#         ''')
#     conn.commit()
#     conn.close()
     
#     # Iterate over handles and hit the API with each
    
        
#         # talking = profile['talking_about_count']
#         # insert_db(likes)
#     return render(request,'fb.html')



# # When account is created via social, fire django-allauth signal to populate Django User record.
# from allauth.account.signals import user_signed_up
# from django.dispatch import receiver
 
# @receiver(user_signed_up)
# def user_signed_up_(request, user, sociallogin=None, **kwargs):
#     '''
#     When a social account is created successfully and this signal is received,
#     django-allauth passes in the sociallogin param, giving access to metadata on the remote account, e.g.:
 
#     sociallogin.account.provider  # e.g. 'twitter' 
#     sociallogin.account.get_avatar_url()
#     sociallogin.account.get_profile_url()
#     sociallogin.account.extra_data['screen_name']
 
#     See the socialaccount_socialaccount table for more in the 'extra_data' field.
#     '''
 
#     if sociallogin:
#         # Extract first / last names from social nets and store on User record
#         if sociallogin.account.provider == 'twitter':
#             name = sociallogin.account.extra_data['name']
#             user.first_name = name.split()[0]
#             user.last_name = name.split()[1]
 
#         if sociallogin.account.provider == 'facebook':
#             user.first_name = sociallogin.account.extra_data['first_name']
#             user.last_name = sociallogin.account.extra_data['last_name']
 
#         if sociallogin.account.provider == 'google':
#             user.first_name = sociallogin.account.extra_data['given_name']
#             user.last_name = sociallogin.account.extra_data['family_name']
 
#         user.save()
