from django.shortcuts import render
from .models import Post

# Create your views here.

# posts = [
#     {
#         'author': 'David',
#         'title': 'This is My First BLOG',
#         'content': "Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
#         'date_posted': 'June 18 2019'
#     },
#     {
#         'author': 'DLP',
#         'title': 'This is My Second BLOG',
#         'content': "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters",
#         'date_posted': 'June 19 2019'
#     }
# ]


def home(request):
    post_dict = {
        'posts': Post.objects.all(),
        'title': 'Blog-Home'
    }
    return render(request,'blog/home.html',post_dict)

def about(request):
    return render(request,'blog/about.html',{'title': 'About!'})

def about2(request):
    return render(request,'blog/about2.html',{'title': 'About2!'})