
from django.urls import include,path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('post',views.PostViewSet) # 2개 URL를 만듬

urlpatterns = [
    path("public/", views.PublicPostListAPIView.as_view()),
    path('',include(router.urls)),
]