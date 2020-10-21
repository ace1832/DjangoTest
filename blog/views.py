from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#List of dictionary
#Part 03 Min 17:10 for summary of passing posts to
#the html view.
posts= [
    {

        'author': 'rafi',
        'title': 'test post',
        'content': 'first post content',
        'date_posted': 'Sep 28'

    },
    {

        'author': 'reaz',
        'title': 'test post 2',
        'content': 'second post content',
        'date_posted': 'Sep 28'

    }


]


#render takes a request as the first argument
#in the 2nd argument it takes the html template 
#within the template subfolder
def home(request):
    context={
        'posts':posts 
#'posts' is the key and posts dictionary above is the
# passed value 
    }
#This context is passed to the render parameter
    return render(request,'blog/home.html',context)
    

def about(request):
    #return HttpResponse('<h1>About</h1>')
    return render(request,'blog/about.html',{'title':'About'})
    

