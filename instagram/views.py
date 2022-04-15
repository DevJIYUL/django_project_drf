from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .serializers import PostSerializer
from .models import Post

# class PublicPostListAPIView(generics.ListAPIView):
#     queryset = Post.objects.filter(is_public = True)
#     serializer_class = PostSerializer
# CBV
# class PublicPostListAPIView(APIView):
#     def get(self,request):
#         qs = Post.objects.filter(is_public = True)
#         serializer = PostSerializer(qs,many=-True)
#         return Response(serializer.data)

# public_post_list = PublicPostListAPIView.as_view()

@api_view(['GET'])
def public_post_list(request):
    qs = Post.objects.filter(is_public = True)
    serializer = PostSerializer(qs,many=-True)
    return Response(serializer.data)

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def dispatch(self,request,*args,**kwargs):

        return super().dispatch(request,*args,**kwargs)
# def post_list(request):
#     pass

# def post_detail(request):
#     pass