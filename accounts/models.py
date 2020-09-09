from django.db import models
from django.db.models import CASCADE


class Account(models.Model):
    user = models.OneToOneField('auth.User', null=True, blank=True, on_delete=CASCADE)
    dob = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        if self.user:
            user = self.user
            return '{}'.format(user.username)
        return self.pk

