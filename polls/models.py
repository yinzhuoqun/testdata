from django.db import models

# Create your models here.

# from django.db import models

class Question(models.Model):
    quesiton_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    
    
class Choice(models.Model):
    quesiton = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)

    votes = models.IntegerField(default=0)
