from django.shortcuts import render
from django.http import HttpResponse
from .models import Member
from .forms import MemberForm
from .forms import SearchForm

def index(request):
    members = Member.objects.all().order_by('Lname')
    form = SearchForm()
    return render(request, 'list/member_list.html', {'members': members, 'form': form})

def member_new(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MemberForm()
    return render(request, 'list/member_edit.html', {'form': form})
            
# Create your views here.
