from django.conf import settings
from django.db import models
#from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    #created_date = models.DateTimeField(default=timezone.now)
    #published_date = models.DateTimeField(blank=True, null=True)

    """
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    """

    def __str__(self):
        return self.title

class User(models.Model):

	gender= models.CharField(max_length=10)
	name = models.CharField(max_length=40)

class Title(models.Model):

		title = models.TextField()

class meaow(models.Model):
	figaro = models.CharField(max_length=33)


		 
	
	
		
		


