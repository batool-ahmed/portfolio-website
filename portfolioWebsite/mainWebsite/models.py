from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from PIL import Image

class Portfolio(models.Model):
    portfolio_id = models.AutoField(primary_key=True, db_column='id')
    title = models.CharField(max_length=20, null=False, blank=False)
    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    content = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to='pictures', null=False)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 1000 or img.width > 1000:
            output_size = (1000, 1000)
            img.thumbnail(output_size)
            img.save(self.image.path)






