from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'David',
        'content': 'My test blog',
        'message': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        'date_posted': 'June 18 2019'
    },
    {
        'author': 'DLP',
        'content': 'My #2 test blog',
        'message': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        'date_posted': 'June 19 2019'
    }
]
def home(request):
    post_dict = {
        'posts': posts,
        'title': 'Blog-Home'
    }
    return render(request,'blog/home.html',post_dict)

def about(request):
    return render(request,'blog/about.html',{'title': 'About!'})