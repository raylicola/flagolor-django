from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, 'post_outfit/index.html')

def register(request):
    return render(request, 'post_outfit/register.html')