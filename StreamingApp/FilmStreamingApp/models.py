from django.db import models

# Create your models here.
#from ..Users.models import CustomUser
from django.db import models

# Create your models here.
class FilmsApplication(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    director = models.CharField(max_length=64)
    image = models.ImageField(upload_to='images/film_cover_image/')
    liked_yes_or_no = models.BooleanField(default=False)
    seen_yes_or_no = models.BooleanField(default=False)
    #user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'description', 'director')

    def __str__(self):
        return self.name
