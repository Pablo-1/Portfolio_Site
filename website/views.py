from django.shortcuts import render
from .forms import FeedbackForm
from django.shortcuts import redirect


def home(request):
    form = FeedbackForm()
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            form = FeedbackForm()
            return redirect('home')
        else:
            form = FeedbackForm()
    return render(request, 'home.html', {'form':form})