from rest_framework import generics
from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .serializers import PostSerializer
from .models import Post
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrReadonly
from rest_framework.filters import SearchFilter,OrderingFilter
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

# FBV
@api_view(['GET'])
def public_post_list(request):
    qs = Post.objects.filter(is_public = True)
    serializer = PostSerializer(qs,many=-True)
    return Response(serializer.data)

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated,IsAuthorOrReadonly]

    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['message']


    def perform_create(self, serializer):
        author = self.request.user
        ip = self.request.META['REMOTE_ADDR']
        serializer.save(author = author,ip=ip)

    @action(detail=False,methods=['GET'])
    def public(self,request):
        qs = self.get_queryset().filter(is_public=True)
        serializer = self.get_serializer(qs,many = True)
        return Response(serializer.data)

    @action(detail=True,methods=['PATCH'])
    def set_public(self,request,pk):
        instance = self.get_object()
        instance.is_public = True
        instance.save(update_fields=['is_public'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
        
    
    # def dispatch(self,request,*args,**kwargs):

    #     return super().dispatch(request,*args,**kwargs)
# def post_list(request):
#     pass

# def post_detail(request):
#     pass

