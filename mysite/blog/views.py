#from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse
from mysite.blog.models import BlogPost   
from mysite.blog.forms import BlogPostForm

def archive(request):
    posts = BlogPost.objects.all()
    t=loader.get_template("archive.html")
    c = Context({'posts':posts})
    return HttpResponse(t.render(c))
    
    
def add_topic(request):
    """
    create a new topic
    """
    if request.method == 'POST':
        form = BlogPostForm(reqeust.POST)
        
        post = form.save()
        message.success(request, _("Topic saved."))
        
        return HttpResponseRedirect(post.get_absolute_url()) #no get_absolute_url() now
        
    else:
        form = BlogPostForm(initial = {'title':'new topic'})
        c = Context({'form':form})
        t=loader.get_template("add_topic.html")
        return HttpResponse(t.render(c))
