from django import forms
from .models import Notice
from django.utils import timezone

class NoticeForm(forms.ModelForm):
    publish_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        initial=timezone.now
    )

    class Meta:
        model = Notice
        fields = ['title', 'description', 'publish_date', 'attachment']
