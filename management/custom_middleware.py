from datetime import datetime

from management.models.requestdb_model import RequestLog


class SaveRequestDb(object):

    def process_request(self, request):
        try:
          if request:
            request_path = request.path
            req = RequestLog(requested_url=request.build_absolute_uri(request_path),
                              datetime=datetime.now(),
                              request_type=request.method,
                              request_ip=request.META['REMOTE_ADDR'],
                              )
            req.save()
        except:
          pass
             
# show last 10 requests
class RequestLogMw(object):
    def process_response(self, request, response):
        if request.path.strip().endswith("requests/"):
            last_req = RequestLog.objects.filter().order_by('-datetime')[: 10]
            return render_to_response("url_log.html",
                                      {'req': last_req, },
                                      context_instance=RequestContext(request))
        return response