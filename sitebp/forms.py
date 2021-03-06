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


class Answers (ModelForm):
    class Meta:
        model = models.Answers
        fields = ['exercise','number','file']