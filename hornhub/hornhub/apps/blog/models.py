from django.db import models

import PIL

from PIL import Image
from imagekit.models.fields import ImageSpecField
from imagekit.processors import ResizeToFit, Adjust,ResizeToFill

class Stat(models.Model):
	stat_nam = models.CharField('название статьи', max_length = 200)
	stat_text = models.TextField('текст статьи')
	pub_date = models.DateTimeField('дата')
	img_stat = models.ImageField( upload_to='img', blank=False, null=True)

	def __str__(self):
		return self.stat_nam

	class Meta :
		verbose_name = 'Статья'
		verbose_name_plural = 'Статьи'


class Coment(models.Model):
	kay = models.ForeignKey(Stat, on_delete = models.CASCADE)
	coment_auther = models.CharField('имя автора', max_length =  50)
	coment_text = models.CharField('текст автора', max_length = 200)
	
	def __str__(self):
		return self.coment_auther

	class Meta:
		verbose_name = 'Комментарий'
		verbose_name_plural = 'Комменты'
