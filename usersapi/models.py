from django.db import models

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.core.validators import MaxValueValidator, MinValueValidator 

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Workout(models.Model):

    name = models.CharField(max_length=50)
    muscle = models.CharField(max_length=50)
    intesityLevel = models.PositiveIntegerField(default=5, 
                                                validators=[MinValueValidator(1), 
                                                MaxValueValidator(5)])
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.name

        #find location of specific -- reverse
    def get_absolute_url(self):
        return reverse('workout-detail', kwargs={'pk': self.pk})