from django.urls import path
from. import views

urlpatterns = [
    path('teachers/', views.teachers,name='teachers'),
    path('teachers/videos/', views.teachers_videos,name='teachers_videos'),
    path('teachers/videos/upload' , views.teachers_videos_upload,name="teachers_videos_upload"),
    path ('' , views.home , name ="home"),
]