from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
	parent = models.ForeignKey('self', verbose_name=_('parent'), blank=True, on_delete=models.CASCADE, null=True)
	title = models.CharField(verbose_name=_('title'), blank=True, max_length=50)
	description = models.TextField(verbose_name=_('description'), blank=True)
	avatar = models.ImageField(_('avatar'), blank=True, upload_to='categories')
	is_enable = models.BooleanField(_('is enable'), default=True)
	created_time = models.DateTimeField(_('created time'), auto_now_add=True)
	updated_time = models.DateTimeField(_('updated time'), auto_now=True)

	class Meta:
		db_table = 'categories'
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.title


class Product(models.Model):
	title = models.CharField(verbose_name=_('title'), blank=True, max_length=50)
	description = models.TextField(verbose_name=_('description'), blank=True)
	avatar = models.ImageField(_('avatar'), blank=True, upload_to='categories')
	is_enable = models.BooleanField(_('is enable'), default=True)
	category = models.ManyToManyField('Category', verbose_name=_('categories'), blank=True)
	created_time = models.DateTimeField(_('created time'), auto_now_add=True)
	updated_time = models.DateTimeField(_('updated time'), auto_now=True)

	class Meta:
		db_table = 'products'
		verbose_name = 'Product'
		verbose_name_plural = 'Products'

	def __str__(self):
		return self.title


class File(models.Model):
	FILE_AUDIO = 1
	FILE_VIDEO = 2
	FILE_PDF = 3
	FILE_TYPES = (
		(FILE_AUDIO, _('audio')),
		(FILE_VIDEO, _('video')),
		(FILE_PDF, _('pdf'))
	)

	product = models.ForeignKey('Product', verbose_name=_('product'), on_delete=models.CASCADE, related_name='files')
	title = models.CharField(verbose_name=_('title'), blank=True, max_length=50)
	file_type = models.PositiveSmallIntegerField(_('file type'), choices=FILE_TYPES)
	file = models.FileField(_('file'), upload_to='files/%Y/%m/%d')
	is_enable = models.BooleanField(_('is enable'), default=True)
	created_time = models.DateTimeField(_('created time'), auto_now_add=True)
	updated_time = models.DateTimeField(_('updated time'), auto_now=True)

	class Meta:
		db_table = 'files'
		verbose_name = 'File'
		verbose_name_plural = 'Files'

	def __str__(self):
		return self.title
