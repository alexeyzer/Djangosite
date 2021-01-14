from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Weapon(models.Model):
    title = models.CharField(max_length=50)
    descripiton = models.CharField(max_length=250)
    img = models.URLField()

    def __str__(self):
        return self.title
class Mark(models.Model):
    Markname = models.CharField(max_length=40)
    img = models.ImageField(upload_to='models/')
    def __str__(self):
        return self.Markname
    class Meta:
        verbose_name = "Марка"
        verbose_name_plural = "Марки"

class Model(models.Model):
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE)
    modelname = models.CharField(max_length=40)
    price = models.IntegerField()
    time = models.FloatField()
    volume = models.FloatField()
    num = models.IntegerField()
    power = models.IntegerField()
    deskription = models.TextField()
    img = models.ImageField(upload_to='marks/')
    def __str__(self):
        return self.modelname
    class Meta:
        verbose_name = "Модель"
        verbose_name_plural = "Модели"

