from django.contrib.auth.models import User
from django.db import models

class TaskGroup(models.Model):
    name = models.CharField(max_length=255)
    director = models.ForeignKey(User, on_delete=models.CASCADE, related_name='directed_task_groups', null=True, blank=True)
    staff_members = models.ManyToManyField(User, related_name='task_groups', blank=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    assigned_to = models.ManyToManyField(User, related_name='tasks', blank=True)  # Changed to ManyToManyField
    assigned_group = models.ForeignKey(TaskGroup, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tasks')
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed')], default='pending')

    def __str__(self):
        return self.title

class StatusChangeRequest(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='status_change_requests')
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='status_change_requests')
    current_status = models.CharField(max_length=20)
    requested_status = models.CharField(max_length=20)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.task.title} - {self.requested_status}"
