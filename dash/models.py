from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserTracker(models.Model):
    tourist = models.OneToOneField(User, on_delete=models.CASCADE)
    place_1 =  models.BooleanField(max_length=100, null=True, blank=True)
    place_2 =  models.BooleanField(max_length=100, null=True, blank=True)
    place_3 =  models.BooleanField(max_length=100, null=True, blank=True)
    place_4 =  models.BooleanField(max_length=100, null=True, blank=True)
    place_5 =  models.BooleanField(max_length=100, null=True, blank=True)
    place_6 =  models.BooleanField(max_length=100, null=True, blank=True)
    place_7 =  models.BooleanField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.tourist)
    class Meta:
        verbose_name_plural = 'UserTracker'





class AdminTracker(models.Model):
	place_1 =  models.CharField(max_length=100, null=True, blank=True)
	place_2 =  models.CharField(max_length=100, null=True, blank=True)
	place_3 =  models.CharField(max_length=100, null=True, blank=True)
	place_4 =  models.CharField(max_length=100, null=True, blank=True)
	place_5 =  models.CharField(max_length=100, null=True, blank=True)
	place_6 =  models.CharField(max_length=100, null=True, blank=True)
	place_7 =  models.CharField(max_length=100, null=True, blank=True)
	tourist = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.tourist)

class Meta:
	verbose_name_plural = 'AdminTracker'

