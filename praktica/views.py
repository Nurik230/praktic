from django.shortcuts import render

def index(request):
    a = ('Hello')
    return render(request, 'praktica/index.html', {'a'})