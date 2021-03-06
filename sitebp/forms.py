from django import forms
from django.forms import ModelForm
from . import models


class Teachers_videos_upload (ModelForm):
    class Meta:
        model = models.Videos
        fields = '__all__'