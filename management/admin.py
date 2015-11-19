from django.contrib import admin

from models.requestdb_model import RequestLog 
from models.user_model import User



admin.site.register(RequestLog)
admin.site.register(User)
