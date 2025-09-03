from django.db import models
from django.utils.translation import pgettext_lazy as _


class Category(models.Model):
	parent = models.ForeignKey('self', verbose_name=_('parent'), blank=True, on_delete=models.CASCADE)
	title = models.CharField(verbose_name=_('title'), blank=True)
	description = models.TextField(verbose_name=_('description'), blank=True)
	avatar = models.ImageField(_('avatar'), blank=True, upload_to='categories')
	is_enable = models.BooleanField(_('is enable'), default=True)
	created_time = models.DateTimeField(_('created time'), auto_now_add=True)
	updated_time = models.DateTimeField(_('updated time'), auto_now=True)

	class Meta:
		db_table = 'categories'
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'


class Product(models.Model):
	title = models.CharField(verbose_name=_('title'), blank=True)
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


class File(models.Model):
	product = models.ForeignKey('Product', verbose_name=_('product'), on_delete=models.CASCADE)
	title = models.CharField(verbose_name=_('title'), blank=True)
	file = models.FileField(_('file'), upload_to='files/%Y/%m/%d')
	is_enable = models.BooleanField(_('is enable'), default=True)
	created_time = models.DateTimeField(_('created time'), auto_now_add=True)
	updated_time = models.DateTimeField(_('updated time'), auto_now=True)

	class Meta:
		db_table = 'files'
		verbose_name = 'File'
		verbose_name_plural = 'Files'




























