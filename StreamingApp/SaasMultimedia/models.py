from django.conf import settings
from django.db import models
from django.core.validators import FileExtensionValidator

class Multimedia(models.Model):
    image = models.ImageField(upload_to='images/Saas_Multimedia/', validators=[FileExtensionValidator(allowed_extensions=['jpg','png','jpeg'])])
    alt = models.CharField(max_length=64, null=True, default='no alt')
    title = models.CharField(max_length=64, null=True, default='no alt')
    section_multimedia_type = models.CharField(max_length=15, choices=settings.SAAS_SECTIONS)  # choices(Logo|Caroussel|Favicon)
