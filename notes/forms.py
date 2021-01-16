from django import forms

from . models import TodoNote


class AddNoteform(forms.ModelForm):
    class Meta:
        model=TodoNote
        fields=('subject','description','deadline')
        widgets = {
            'deadline': forms.DateTimeInput({'type': 'datetime-local'}),
        }
