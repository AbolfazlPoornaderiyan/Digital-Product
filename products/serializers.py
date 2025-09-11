from rest_framework import serializers

from .models import Category, Product, File


class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ["id", "title", "description", "avatar"]


class FileSerializer(serializers.ModelSerializer):
	class Meta:
		model = File
		fields = ['id', 'title', 'file_type', 'file']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
	category = CategorySerializer(many=True)
	files = FileSerializer(many=True)

	class Meta:
		model = Product
		fields = ['id', 'title', 'description', 'avatar', 'category', 'files', 'url']
