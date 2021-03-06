from django.shortcuts import render
from . import models , forms
from django.http import HttpResponse

# Create your views here.
def home (request):
    contex ={}

    return render (request , 'sitebp/home.html' , contex)

def teachers (request):
    contex ={}

    return render (request , 'sitebp/teachers.html' , contex)


def teachers_exercise (request):
    exercise = models.Exercise.objects.all()
    contex ={'exercise' : exercise}

    return render (request , 'sitebp/teachers_exercis.html' , contex)

def teachers_exercise_answers (request,answer_id):
    #answer = models.Answers.objects.filter(id = answer_id)
    #contex ={'answers' : answer}
    answers=models.Answers.objects.filter(exercise=models.Exercise.objects.get(id=answer_id))
    contex={'answers':answers}
    return render (request , 'sitebp/teachers_exercise_answers.html' , contex)


def teachers_videos (request):
    videos = models.Videos.objects.all()
    contex ={'videos' : videos}

    return render (request , 'sitebp/teachers_videos.html' , contex)


def teachers_exercise_upload (request):
    form = forms.Teachers_exercise_upload
    if request.method == 'POST':
        form = forms.Teachers_exercise_upload(request.POST , request.FILES)
        if form.is_valid ():
            form.save()
            return HttpResponse ("OK")

    contex ={'form' : form}


    return render (request , 'sitebp/teachers_exercise_upload.html' , contex)



def teachers_videos_upload (request):
    form = forms.Teachers_videos_upload
    if request.method == 'POST':
        form = forms.Teachers_videos_upload(request.POST , request.FILES)
        if form.is_valid ():
            form.save()
            return HttpResponse ("OK")

    contex ={'form' : form}


    return render (request , 'sitebp/teachers_videos_upload.html' , contex)


def teachers_videos_seen (reauest , videoid):
    return render(reauest, 'sitebp/teachers_videos_seen.html',{'video':models.Videos.objects.get(id=videoid)})
