from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'list/member_list.html', {})
# Create your views here.
