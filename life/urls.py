from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('forum/',views.forum, name='forum'),
    path('forum_create/',views.forum_create, name='forum_create'),
    path('reminder/',views.reminder, name='reminder'),
    path('tracker/',views.tracker, name='tracker'),
    path('case/',views.case, name='case'),
    path('case_create/',views.case_create, name='case_create'),
    path('tracker/',views.tracker, name='tracker'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    path('forum/question/<int:question_id>/',views.question, name='question'),
]



