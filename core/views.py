from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import MyUser
from .serializers import BlogSerializer

class BlogViewSet(viewsets.ModelViewSet):

    queryset = MyUser.objects.all()
    serializer_class = BlogSerializer
