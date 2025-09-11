from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Category, Product, File
from .serializers import CategorySerializer, ProductSerializer, FileSerializer


# Category view:
class CategoryListView(APIView):

	def get(self, request):
		categories = Category.objects.all()
		serializers = CategorySerializer(categories, many=True, context={'request': request})
		return Response(serializers.data)


class CategoryDetailView(APIView):

	def get(self, request, pk):
		try:
			category = Category.objects.get(pk=pk)
		except Category.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		serializer = CategorySerializer(category, context={'request': request})
		return Response(serializer.data)


# Product view:
class ProductListView(APIView):

	def get(self, request):
		products = Product.objects.all()
		serializers = ProductSerializer(products, many=True, context={'request': request})
		return Response(serializers.data)


class ProductDetailView(APIView):

	def get(self, request, pk):
		try:
			product = Product.objects.get(pk=pk)
		except Product.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		serializer = ProductSerializer(product, context={'request': request})
		return Response(serializer.data)


# File view:
class FileListView(APIView):

	def get(self, request, product_id):
		files = File.objects.filter(product_id=product_id)
		serializers = FileSerializer(files, many=True, context={'request': request})
		return Response(serializers.data)


class FileDetailView(APIView):

	def get(self, request, pk, product_id):
		try:
			file = File.objects.get(pk=pk, product_id=product_id)
		except File.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		serializer = FileSerializer(file, context={'request': request})
		return Response(serializer.data)
