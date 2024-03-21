from django.shortcuts import render
from django.http import HttpResponse
from .models import Member

def index(request):
    members = Member.objects.all().order_by('Lname')
    return render(request, 'list/member_list.html', {'members': members})
# Create your views here.
