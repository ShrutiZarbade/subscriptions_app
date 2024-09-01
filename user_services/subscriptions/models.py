from django.db import models

# Create your models here.

class UserDetails(models.Model):
    
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255, unique=True)
    is_subscribed = models.BooleanField(default=False)

    def __str__(self):
        return self.email
