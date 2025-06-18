from django.shortcuts import render

from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {"posts": posts})

def venus(request):
    return render(request, 'venus/venus.html')
