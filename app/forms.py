from django import forms
from app.models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model=Feedback
        fields="__all__"