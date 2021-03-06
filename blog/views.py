from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, HttpResponse, HttpResponseRedirect, RequestContext, Http404
from django.conf import settings
from django.views import generic
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from . import models
from .forms import ContactForm
from .models import Profile, Entry

from .forms import EntrySearchForm, AddArticleForm, BashOnButtonForm

from haystack.generic_views import SearchView
from django.contrib import messages

class BlogIndex(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "home.html"
    paginate_by = 2


class BlogDetail(generic.DetailView):
    model = models.Entry
    template_name = "post.html"
    
def contactUs(request):
    title = 'Contact Us'
    form = ContactForm(request.POST or None)
    confirm_message =None
    
    if request.method == 'POST' and form.is_valid():
        comment = form.cleaned_data['comment']
        name = form.cleaned_data['last_name']
        subject = "thank you fo your preorder"
        messages = '%s%s' %(comment, name)
        from_email = form.cleaned_data['email']
        to_us = [settings.EMAIL_HOST_USER]
        print subject, messages, from_email, to_us
        send_mail(subject, messages, from_email, to_us, fail_silently = True)
        title = "thank you"
        confirm_message = '''
        Thanks for your message. We will answer as soon as possible.
        '''
        form = None
    context = {
            'title': title,
            'form':form,
            'confirm_message':confirm_message
        }
        
    # context = locals()
    template = 'contact.html'
    return render(request, template, context)

@login_required
def user_profile(request):
	if request.user.is_authenticated():
		user = request.user
	else:
		user = None
	context = {'user': user}
	template = 'profile.html'
	return render(request, template, context)

@login_required
def like_article(request):

    article_id = None
    if request.method == 'GET' and 'id' in request.GET:
        article_id = request.GET['id']
    
    likes = 0
    
    if article_id:
        article = Entry.objects.get(id=int(article_id))
        
        if article:
            likes = article.likes + 1
            article.likes = likes
            article.save()

    return HttpResponse(likes)

def track_url(request):

    article_slug = None
    url = '.'
    if request.method == 'GET':
        if 'slug' in request.GET:
            article_slug = request.GET['slug']
            import ipdb; ipdb.set_trace()
            try:
                page = Entry.objects.get(slug=article_slug)
                page.views = page.views + 1
                page.save()
                url = page.url
            except:
                pass

    return redirect(url)


def ent_search(request):
    form = EntrySearchForm(request.GET)
    ent_search = form.search()
    return render_to_response('search/search.html', {'ent_search': ent_search})

@login_required
def add_article(request):

    
    form = AddArticleForm(request.POST)
    context={
        'form':form
        }
    
    if request.POST:
        if form.is_valid():
            form.save()

            message = messages.info(request, "You successfully added new article!")
    form = AddArticleForm        
            
           


    return render(request, 'add.html', context )

import os
import subprocess
from subprocess import Popen, PIPE
import pexpect
import sh
from sh import tail
def cc_gen(request):
    name = "AAAAAAA"
    
    form = BashOnButtonForm
    path = '/volumes/storage/_codework/blogsample1/qblog/qblog/blog/openvpn.sh'
    # path1 = '/volumes/storage/_codework/blogsample1/qblog/qblog/blog/openvpn.sh'
    # os.chmod(path1, 755)
    # subprocess.check_output(['bash', '-c', '/volumes/storage/_codework/blogsample1/qblog/qblog/blog/openvpn_install.sh && testerSSLTSL'])
    # bashCommand = "cwm --rdf test.rdf --ntriples > test.nt"
    
    # process = subprocess.Popen(bashCommand.split())
    # output = process.communicate()[0]

    proc = Popen(
    "bash /volumes/storage/_codework/blogsample1/qblog/qblog/blog/openvpn.sh",

    shell=True,
    stdout=PIPE, stderr=PIPE
    )
    proc1 = Popen(
    "openvpn --genkey --secret key",
    
    shell=True,
    stdout=PIPE, stderr=PIPE
    )
    proc1.wait()    # wait for end process
    res = proc.communicate()  # get tuple('stdout res', 'stderr res')
    # result = proc.stdout.readlines()
    # text = proc.stdout.read()
    res1 = proc1.communicate()
    
    # os.chmod(path, 755) # give permissions
    
    # p = subprocess.Popen(['openvpn.sh' ,'1'], shell=True, stdout=subprocess.PIPE)
    # c = subprocess.call(["df","-h",path])
    # line = p.stdout.readline()
    # line1 = p.stderr.readlines()
    # run = sh.Command('openvpn.sh') # Absolute path
    # run()
    # lscmd = sh.Command("ls")  # Absolute path not needed
    # lscmd()
    # for line in tail("-f", path, _iter=True):
    #     d = line
    #     print d
    return render_to_response('contact.html', locals(), RequestContext(request))

# from subprocess import Popen, PIPE
# proc = Popen(
#     "python D:/axe/python/easygui/easygui.pyw",
#     shell=True,
#     stdout=PIPE, stderr=PIPE
# )
# proc.wait()   
# res = proc.communicate()  
# if proc.returncode:
#     print res[1]
# print 'result:', res[0]


# def post_like(request):
   
#     form = LikesForm(request.POST or None)
#     confirm_message =None
    
#     if request.method == 'POST' and form.is_valid():
#         likes = form.cleaned_data['likes']
        
#         subject = "thank you fo your feadback"
#         messages = '%s' %(subject)

        
        # confirm_message = '''
        # Thanks for your message. We will answer as soon as possible.
        # '''
        
    #     form.save()
    #     context = {
                
    #             'form':form,
    #             'confirm_message':confirm_message
    #         }
    # return render(request,'home.html', comtext)













     # def search(request):
    #     return render(request,'students/students_list.html',{})
    #   if 'q' in request.GET:
    #       return u'%s?status_message = You searched for: %r' % request.GET['q']
    #   else:
    #       return u'%s?status_message = You submitted an empty form.'% request.GET['q']
    #

# from .students.search_indexes import StudentIndex

# def last_name_search(request, last_name):  
#     context = dict(last_name = last_name)
#     context['students'] = StudentIndex.objects.filter(last_name=last_name)[:5]
#     return render(request, 'base.html', context)


# 
# class CustomSearchView(SearchView):
#     template_name='students/students_list.html'




