from django.db import models

import PIL

from PIL import Image
from imagekit.models.fields import ImageSpecField
from imagekit.processors import ResizeToFit, Adjust,ResizeToFill

class Analys(models.Model):
	text_analys = models.TextField('текст для анализа')

	def __str__(self):
		return self.text_analys
	class Meta :
		verbose_name = 'анализ'
		verbose_name_plural = 'анализа'