from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'tasks', views.TaskViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'status_change_requests', views.StatusChangeRequestViewSet)

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('tasks/<int:pk>/', views.task_detail, name='task_detail'),
    path('tasks/new/', views.task_form, name='task_form'),
    path('tasks/<int:pk>/request_status_change/', views.request_status_change, name='request_status_change'),
    path('status_change_requests/<int:pk>/approve/', views.approve_status_change, name='approve_status_change'),
    path('login/', views.custom_login, name='custom_login'),
    path('api/', include(router.urls)),
]
