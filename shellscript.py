import django
django.setup()

from life.models import Question, Answer, User
from django.utils import timezone

print("Question Objects: {}".format(Question.objects.all()))
print("Answer Objects: {}".format(Answer.objects.all()))
print("User Objects: {}".format(User.objects.all()))


