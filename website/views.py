from django.shortcuts import render
from .forms import FeedbackForm
from django.shortcuts import redirect

# Create your views here.
# def home(request):
#     form = FeedbackForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = FeedbackForm()

#     context = {
#         'form': form
#     }
#     return render(request, 'home.html', context)

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

# def send_form(request):
#     form = FeedbackForm()
#     if request.method == "POST":
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             form.save()
#         else:
#             form = FeedbackForm()
    
#     return render(request, 'sucess.html', {'form':form})