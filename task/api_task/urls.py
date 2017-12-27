from django.conf.urls import url, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'tasks', views.NewTaskViewSet)
router.register(r'projects', views.ProjectViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]