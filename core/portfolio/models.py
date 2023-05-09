from django.db import models
from django.db.models.fields import CharField,URLField
from django.db.models.fields.files import ImageField
from config.settings import MEDIA_URL, STATIC_URL

class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    image = ImageField(upload_to=f'{MEDIA_URL}postfolio/images/')
    url = URLField(blank=True)

    def __str__(self):
        return self.title
    

    def get_image(self):
        if self.image:
            return self.image
        return f'{STATIC_URL}images/empty.png'