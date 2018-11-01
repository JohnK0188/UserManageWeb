from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .forms import PostForm

def index(request):
    return render(request, 'MainApp/index.html', {})

def join(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            dbdbMem = form.save(commit=False)
            dbdbMem.join_date = timezone.now()
            dbdbMem.save()
    else:
        form = PostForm()
    return render(request, 'MainApp/join.html', {'form': form})