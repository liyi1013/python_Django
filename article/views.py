from django.shortcuts import render

from django.http import HttpResponse

from article.models import Article
from datetime import datetime
from django.http import Http404

# Create your views here.
def home(request):
    # s = "Hello World, Django \n this is my first django app"
    # return HttpResponse(s)
    post_list = Article.objects.all()
    return render(request, 'home.html', {'post_list' : post_list})


# def detail0(request, my_args):
#     post = Article.objects.all()[int(my_args)]
#     str = ("title = %s, category = %s, date_time = %s, content = %s"
#            %(post.title, post.category, post.date_time, post.content))
#     return HttpResponse(str)
#     #1 return HttpResponse("You're looking at my_args %s." % my_args)

def detail(request, id=0):
    try:
        post = Article.objects.get(id=str(id))
        print post
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post' : post})

def test(request):
    return render(request, 'test.html', {'current_time': datetime.now()})

def base(request):
    return render(request, 'base.html')

def add(request,a,b):
    mysum =int(a)+int(b)
    s = ("%s + %s = %s"
           %(a, b, str(mysum)))
    return HttpResponse(s)