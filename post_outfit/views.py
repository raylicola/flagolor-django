from django.shortcuts import render

# Create your views here.
def index(request):
    params = {
        'title': 'Hello'
    }
    return render(request, 'post_outfit/index.html', params)