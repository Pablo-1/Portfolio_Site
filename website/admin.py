from django.contrib import admin
from .models import Feedback
from .forms import FeedbackForm
# Register your models here.
class FeedbackAdmin(admin.ModelAdmin):
    form = FeedbackForm
admin.site.register(Feedback, FeedbackAdmin)