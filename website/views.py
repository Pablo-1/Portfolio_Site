from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FeedbackForm

# Create your views here.
def home(request):
    return render(request, 'home.html', context)

