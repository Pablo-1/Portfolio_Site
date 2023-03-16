from django.shortcuts import render
from .forms import FeedbackForm

# Create your views here.
def home(request):
    form = FeedbackForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, 'home.html', context)
