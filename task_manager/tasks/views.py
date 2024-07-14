from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task, StatusChangeRequest, TaskGroup
from .serializers import TaskSerializer, UserSerializer, StatusChangeRequestSerializer
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

# API Views
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class StatusChangeRequestViewSet(viewsets.ModelViewSet):
    queryset = StatusChangeRequest.objects.all()
    serializer_class = StatusChangeRequestSerializer
    permission_classes = [IsAuthenticated]

# Custom Login View
def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('task_list')
        else:
            return HttpResponse('Invalid login credentials')
    return render(request, 'registration/login.html')

# HTML Template Views
@login_required
def task_list(request):
    if request.user.is_superuser:
        tasks = Task.objects.all()
    else:
        tasks = Task.objects.filter(assigned_to=request.user) | Task.objects.filter(assigned_group__in=request.user.task_groups.all())
    status_change_requests = StatusChangeRequest.objects.filter(is_approved=False)
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'status_change_requests': status_change_requests})

@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST' and request.user.is_superuser:
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.status = request.POST.get('status')
        task.save()
        return redirect('task_detail', pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task, 'is_superuser': request.user.is_superuser})

@login_required
def task_form(request):
    if not request.user.is_superuser:
        return redirect('task_list')
    users = User.objects.all()
    groups = TaskGroup.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')
        
        task = Task(title=title, description=description, status=status, created_by=request.user)
        task.save()
        
        if 'assign_to_group' in request.POST:
            assigned_group_id = request.POST.get('assigned_group')
            assigned_group = get_object_or_404(TaskGroup, pk=assigned_group_id) if assigned_group_id else None
            if assigned_group:
                task.assigned_to.add(*assigned_group.staff_members.all())
        elif 'assign_manually' in request.POST:
            assigned_to_ids = request.POST.getlist('assigned_to')
            assigned_to = User.objects.filter(pk__in=assigned_to_ids)
            task.assigned_to.add(*assigned_to)
        
        task.save()
        return redirect('task_list')
    return render(request, 'tasks/task_form.html', {'users': users, 'groups': groups})

@login_required
def request_status_change(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        requested_status = request.POST.get('requested_status')
        StatusChangeRequest.objects.create(
            task=task,
            requested_by=request.user,
            current_status=task.status,
            requested_status=requested_status
        )
        return redirect('task_list')
    return render(request, 'tasks/request_status_change.html', {'task': task})

@login_required
def approve_status_change(request, pk):
    if not request.user.is_superuser:
        return redirect('task_list')
    status_change_request = get_object_or_404(StatusChangeRequest, pk=pk)
    if request.method == 'POST':
        task = status_change_request.task
        task.status = status_change_request.requested_status
        task.save()
        status_change_request.is_approved = True
        status_change_request.save()
        return redirect('task_list')
    return render(request, 'tasks/approve_status_change.html', {'status_change_request': status_change_request})
