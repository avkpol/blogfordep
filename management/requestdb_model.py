from django.db import models


class RequestLog (models.Model):
    datetime = models.CharField(max_length=25)
    requested_url = models.CharField(max_length=255)
    request_type = models.CharField(max_length=10)
    request_ip = models.CharField(max_length=20)
    

    def __unicode__(self):
    	return self.requested_url