from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to="profile_pictures")

    def __str__(self) -> str:
        return f'{self.user.username} Profile'


    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300 :
            oriented_size = (300,300)
            img.thumbnail(oriented_size)
            img.save(self.image.path)
    
    


