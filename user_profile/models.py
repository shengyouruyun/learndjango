from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):

	username = models.CharField('username', max_length=10, unique=True, db_index=True)
	email = models.EmailField('email address', unique=True)
	joined = models.DateTimeField(auto_now_add=True)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	USERNAME_FIELD = 'username'
	def __unicode__(self):
		return self.username

class UserFollowers(models.Model):
	user = models.OneToOneField(User)
	date = models.DateTimeField(auto_now_add=True)
	count = models.IntegerField(default=1)
	followers = models.ManyToManyField(User, related_name='followers')
	def __str__(self):
		return '%s, %s' % (self.user, self.count)

class Invitation(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	code = models.CharField(max_length=20)
	sender = models.ForeignKey(User)
	def __unicoe__(self):
		return u'%s , %s' % (self.sender.username, self.email)









	







