from django.shortcuts import render
from . import models , forms
from django.http import HttpResponse
from datetime import datetime 
from django.views import generic

# Create your views here.
def home (request):
    
    form = forms.login()
    if request.method == 'POST':
        form = forms.login(request.POST)
        if form.is_valid ():
            if (models.users.objects.filter(number=request.POST['number'])):
            #if (models.users.objects.filter(number=request.POST['number'])) or (models.users.objects.get(number=request.POST['number']).pnumber == request.POST['password']):
                #if models.users.objects.filter(number=request.POST['number'])[0].pnumber==request.POST['number']:
                print(models.users.objects.get(number=request.POST['number']).pnumber,request.POST['password'])
                print (models.users.objects.get(number=request.POST['number']).mode)
                if (models.users.objects.get(number=request.POST['number']).pnumber == request.POST['password']):
                
                    #return render (request , 'sitebp/teachers.html' )
                    if models.users.objects.get(number=request.POST['number']).mode=='t':
                        return render (request , 'sitebp/teachers.html' )
                    else: return render (request , 'sitebp/students.html' )

    contex ={'form' : form}

    return render (request , 'sitebp/home.html' , contex)

def teachers (request):
    contex ={}

    return render (request , 'sitebp/teachers.html' , contex)


def students (request):
    contex ={}

    return render (request , 'sitebp/students.html' , contex)


def students_exercise (request):
    exercise = models.Exercise.objects.all()
    contex ={'exercise' : exercise}

    return render (request , 'sitebp/students_exercis.html' , contex)

def students_videos (request):
    videos = models.Videos.objects.all()
    contex ={'videos' : videos}

    return render (request , 'sitebp/students_videos.html' , contex)

def teachers_exercise (request):
    exercise = models.Exercise.objects.all()
    contex ={'exercise' : exercise}

    return render (request , 'sitebp/teachers_exercis.html' , contex)



def teachers_exercise_answers (request,answer_id):
    #answer = models.Answers.objects.filter(id = answer_id)
    #contex ={'answers' : answer}
    answers=models.Answers.objects.filter(exercise=models.Exercise.objects.get(id=answer_id))
    #answers=models.Exercise.objects.get(id =answer_id)
    #answers = models.Answers.objects.filter(id=answer_id)
    contex={'answers':answers}
    return render (request , 'sitebp/teachers_exercise_answers.html' , contex)


def teachers_videos (request):
    videos = models.Videos.objects.all()
    contex ={'videos' : videos}

    return render (request , 'sitebp/teachers_videos.html' , contex)


def student_exercise_upload (request):
    form = forms.Student_exercise_upload
    if request.method == 'POST':
        form = forms.Student_exercise_upload(request.POST , request.FILES)
        if form.deadline >= datetime.now() :
            if form.is_valid ():
                form.save()
                return HttpResponse ("OK")
        else : return HttpResponse('its late khi khi khi khi')

    contex ={'form' : form}


    return render (request , 'sitebp/student_exercise_upload.html' , contex)


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


def teachers_videos_seen (request , videoid):
    return render(request, 'sitebp/teachers_videos_seen.html',{'video':models.Videos.objects.get(id=videoid)})

class login(generic.TemplateView):
    
    template_name='sitebp/login.html'

def vote (request,idd):
    form = forms.vote()
    if request.method == 'POST':
        form = forms.vote(request.POST)
        if form.is_valid ():
            q=models.Answers.objects.get(id=idd)
            q.vote=request.POST['number']
            print ('hellllllll')
            
            
            print (q.vote,request.POST['number'])
            q.save()
            return HttpResponse ("OK")

    contex ={'form' : form}
    return render(request, 'sitebp/vote.html',contex)