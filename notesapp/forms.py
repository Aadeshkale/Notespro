from django import forms
from notesapp.models import NotesInfo 
class LoginForm(forms.Form):
    email=forms.EmailField(max_length=100,
    label="Enter Your email",
    widget=forms.EmailInput(attrs={
        'class':'text-left form-control',
    })
    )
    password=forms.CharField(max_length=20,
    label="Enter Your Password",
    widget=forms.PasswordInput(attrs={
        'class':'form-control',
    })
    )
class InsertForm(forms.ModelForm):
    class Meta():
        model=NotesInfo
        fields=['subject','discription']
    subject=forms.CharField(max_length=255,
    label="Enter Your Subject for note",
    widget=forms.TextInput(attrs={
        'class':'text-left form-control',
    })
    )
    discription=forms.CharField(max_length=500,
    label="Enter Your note here",
    widget=forms.Textarea(attrs={
        'class':'text-left form-control',
    })
    )

class DeleteForm(forms.Form):
    ids=forms.IntegerField(
        label="Enter Id of Note for deletion",
        widget=forms.NumberInput(attrs={
            'class':'form-control',
        })
    )

class UpdateForm(forms.Form):
    ids=forms.IntegerField(
        label="Enter Id of Note for Updation",
        widget=forms.NumberInput(attrs={
            'class':'form-control',
        })
    )
    subject=forms.CharField(max_length=255,
    label="Enter Your Subject for note",
    widget=forms.TextInput(attrs={
        'class':'text-left form-control',
    })
    )
    discription=forms.CharField(max_length=500,
    label="Enter Your note here",
    widget=forms.Textarea(attrs={
        'class':'text-left form-control',
    })
    )