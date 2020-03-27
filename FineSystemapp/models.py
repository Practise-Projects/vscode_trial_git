from django.db import models
#from datetime import datetime
# Create your models here.

class login(models.Model):
    Username = models.CharField(max_length=100, primary_key=True)
    Password = models.CharField(max_length=100)

    def __str__(self):
        return self.Username


class RULEs(models.Model):
    Username = models.ForeignKey(login, on_delete=models.CASCADE)
    Rule = models.CharField(max_length=500)
    Fine_amount = models.IntegerField()

    def __str__(self):
        return self.Rule


class Apply_Fine(models.Model):
    Username = models.ForeignKey(login, on_delete=models.CASCADE)
    Rule = models.ForeignKey(RULEs, on_delete=models.CASCADE)
    Fine_Amount = models.IntegerField()
    Date = models.DateTimeField()
    reason = models.CharField(max_length=500, unique=False, default=None)

    def __str__(self):
        return  str(self.Username)


