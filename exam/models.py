from django.db import models

# Create your models here.
from datetime import datetime, timedelta

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
	def create_user(self, email, password, **kwargs):

		if not email or not password:
			raise ValueError("User must have email and password")

		user = self.model(
            email=UserManager.normalize_email(email),
            **kwargs
        )

		user.set_password(password)
		user.save()

		return user

	def create_superuser(self, email, password, **kwargs):
		user = self.create_user(email, password, **kwargs)
		user.is_superuser = True
		user.is_staff = True
		user.role = 1
		user.save()

		return user


class User(AbstractBaseUser, PermissionsMixin):
	SUPER_ADMIN = 1
	STUDENT = 2
	TEACHER = 3
	ROLE_CHOICES = (
        (STUDENT, 'Student'),
        (SUPER_ADMIN, 'Super Admin'),
        (TEACHER , 'Teacher'),
    )
	first_name = models.CharField(max_length = 100, null = False)
	last_name = models.CharField(max_length = 100, null = False)
	email = models.EmailField(null=False, unique=True)
	is_active = models.BooleanField(default=True)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
	is_staff = models.BooleanField(default=False)
	role = models.SmallIntegerField(choices = ROLE_CHOICES, null = True)
	objects = UserManager()
	USERNAME_FIELD = 'email'
	def get_full_name(self):
		return self.first_name + " " + self.last_name
	def get_short_name(self):
		return self.first_name

class Section(models.Model):
	section = models.CharField(max_length = 100)

	def __str__(self):
		return str(self.section)

class Question(models.Model):
	section = models.ForeignKey(Section, on_delete = models.CASCADE, null = True)
	question = models.CharField(max_length = 200)

	def __str__(self):
		return str(self.question)

class Choice(models.Model):
	question = models.ForeignKey(Question,max_length = 200, on_delete = models.CASCADE)
	choice = models.CharField(max_length = 200)

	def __str__(self):
		return str(self.choice) 

class Exam(models.Model):
	name = models.CharField(max_length = 200)
	start_date = models.DateTimeField()
	duration = models.IntegerField()
	section = models.ManyToManyField(Section)

	def __str__(self):
		return str(self.name)


