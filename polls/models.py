from django.db import models


# Create your models here.
class Question(models.Model):
    question_text = models.CharField("질문", max_length=200)
    pub_date = models.DateTimeField("생성일시")

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey("Question", on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
