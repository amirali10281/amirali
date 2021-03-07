from django import forms
from django.forms import ModelForm
from . import models


class Teachers_videos_upload (ModelForm):
    class Meta:
        model = models.Videos
        fields = '__all__'


class Teachers_exercise_upload (ModelForm):
    class Meta:
        model = models.Exercise
        fields = '__all__'


class Student_exercise_upload (ModelForm):
    class Meta:
        model = models.Answers
        fields = ['exercise','number','file']

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
   # passw = forms.CharField(label='pass', max_length=100)


class login (ModelForm):
    class Meta:
        model=models.Login
        fields= '__all__'
        widgets = {'password':forms.PasswordInput()}
''''
class login (ModelForm):
    number=forms.CharField()
    password=forms.CharField(widgets=forms.PasswordInput)

'''

class vote(ModelForm):
    class Meta:
        model=models.vote
        fields=['number']