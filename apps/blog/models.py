from django.db import models
import datetime
from config.settings import MEDIA_URL, STATIC_URL

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    #image le digo donde subirlo, si le pongo los /, entiende que son carpetas y lo pondra en la ultima carpeta que le digo, en este caso, images que esta dentro de blog, la cual las creara dentro de la carpeta media del proyecto interno o servidor
    image = models.ImageField(upload_to=f'{MEDIA_URL}blog/images')
    #con el datetime.date.today, al ponerlo en el default, le digo que si no le paso nada, por defecto le ponga la fecha en la que se subio
    date = models.DateField(default=datetime.date.today)

    def get_image(self):
        if self.image:
            return self.image.url
        return f'{STATIC_URL}images/empty.png'
