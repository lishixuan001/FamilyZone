from django.db import models
from django.utils import timezone

class Group(models.Model):
	established = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=50)

class User(models.Model):
    def __str__(self):
        return self.username
    username = models.CharField(max_length=20)
    password = models.CharField(default="", max_length=30)
    job_title = models.CharField(default="Anonymous", max_length=30)
    workplace = models.CharField(default="Anonymous", max_length=40)
    identified = models.BooleanField(default=False)
    
    def check_password(self, psw):
        return psw == self.password
    
class Question(models.Model):
    def __str__(self):
        if len(self.question) > 20:
            return self.question[:20]
        return self.question
    question = models.CharField(max_length=50)
    description = models.CharField(default="", max_length=500)
    
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    prof_answered = models.BooleanField(default=False)
    
    # >>> q.creation_date.strftime("%x") 
    # '07/23/18'
    # >>> q.creation_date.strftime("%X")
    # '06:30:39'
    # Many other directives to explore
    creation_date = models.DateTimeField(editable=False, blank=True, null=True)
    last_modified = models.DateTimeField(editable=False, blank=True, null=True)
    
    # Every time question's answers change, remember to q.save() to update q.prof_answered value
    def hasIdentifiedAnswer(self, *args, **kwargs):
        for answer in self.answer_set.all():
            if answer.user.identified:
                return True
        return False

    def save(self, *args, **kwargs):
        if not self.id:
            self.creation_date = timezone.now()
        self.last_modified = timezone.now()
        self.prof_answered = self.hasIdentifiedAnswer()
        return super(Question, self).save(*args, **kwargs)
    
class Answer(models.Model):
    def __str__(self):
        if len(self.answer) > 20:
            return self.answer[:20]
        return self.answer
    
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    
    answer = models.CharField(max_length=500)
    
    # Show how many likes got from users
    likes = models.IntegerField(default=0)
    
    creation_date = models.DateTimeField(editable=False, blank=True, null=True)
    last_modified = models.DateTimeField(editable=False, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.creation_date = timezone.now()

        self.last_modified = timezone.now()
        return super(Answer, self).save(*args, **kwargs)


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# When using shell first type in following    
# >>> exec(open('shellscript.py').read())
    
# END