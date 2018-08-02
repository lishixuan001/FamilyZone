from django.shortcuts import render
from django.core import serializers
from django.utils import timezone
from django.http import HttpResponseRedirect
from life.models import *

# question_text = ""
# question_description = ""
# userList = User.objects.all()
# user_self = None
# if len(userList) > 0:
#     user_self = userList[0]

# Default User -> Anonymous (id=5)
guestUser = User.objects.get(id=5)
currentUser = guestUser

def index(request):
    global currentUser
    global guestUser
    if request.method == 'POST':
        currentUser = guestUser
        return HttpResponseRedirect('/life/')
    else:
        pass
    context = {
        'user': currentUser,
    }
    return render(request, 'life/index.html', context)
  
def forum(request):
    global currentUser
    question_list = Question.objects.all()
    context = {
        'question_list': question_list
    }
    return render(request, 'life/forum.html', context)

def forum_create(request):
    global currentUser
    if request.method == 'POST':
        question_text = request.POST['question'].strip()
        question_description = request.POST['description'].strip()
        currentUser.question_set.create(question=question_text, description=question_description)
#         Question.objects.create(user=currentUser, question=question_text, description=question_description)
        return HttpResponseRedirect('/life/forum/')
    else:
        pass
    return render(request, 'life/forum_create.html')

def reminder(request):
    global currentUser
    return render(request, 'life/reminder.html')

def tracker(request):
    global currentUser
    return render(request, 'life/tracker.html')

def case(request):
    global currentUser
    return render(request, 'life/case.html')

def case_create(request):
    global currentUser
    return render(request, 'life/case_create.html')

def tracker(request):
    global currentUser
    return render(request, 'life/tracker.html')

def question(request, question_id):
    global currentUser
    question = Question.objects.get(id=question_id)
    
    if request.method == 'POST':
        answer = request.POST['answer'].strip()
        currentUser.answer_set.create(question=question, answer=answer)
        question.save()
        return HttpResponseRedirect('/life/forum/question/' + str(question_id))
    else:
        pass

    context = {
        'question': question,
    }
    return render(request, 'life/question.html', context)

def registration(request):
    global currentUser
    if request.method == 'POST':
        username = request.POST['username'].strip()
        password = request.POST['password'].strip()
        User.objects.create(username=username, password=password)
        return HttpResponseRedirect('/life/')
    else:
        pass
    return render(request, 'life/registration.html')

def login(request):
    global currentUser
    context = {
        'user_not_found': False,
        'password_mismatch': False,
    }
    if request.method == 'POST':
        username = request.POST['username'].strip()
        password = request.POST['password'].strip()
        
        search_result = User.objects.filter(username=username)
        if len(search_result) == 0:
            context['user_not_found'] = True
        else:
            user = search_result[0]
            if user.check_password(password):
                currentUser = user
                context['user_not_found'] = False
                context['password_mismatch'] = False
                return HttpResponseRedirect('/life/')
            else:
              context['password_mismatch'] = True
                
    else:
        pass
            
    return render(request, 'life/login.html', context)




































# END