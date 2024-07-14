from django.contrib import admin
from .models import Task, StatusChangeRequest, TaskGroup
from .forms import TaskGroupForm

class TaskGroupAdmin(admin.ModelAdmin):
    form = TaskGroupForm
    list_display = ('name', 'get_director', 'get_staff_members')

    def get_director(self, obj):
        return obj.director
    get_director.short_description = 'Director'

    def get_staff_members(self, obj):
        return ", ".join([user.username for user in obj.staff_members.all()])
    get_staff_members.short_description = 'Staff Members'

admin.site.register(TaskGroup, TaskGroupAdmin)

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'status', 'get_assigned_to', 'assigned_group', 'created_by', 'created_at', 'updated_at')
    search_fields = ('title', 'description', 'assigned_to__username', 'assigned_group__name', 'created_by__username')
    list_filter = ('status', 'assigned_to', 'assigned_group', 'created_by')
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'status', 'assigned_to', 'assigned_group', 'created_by')
        }),
    )

    def get_assigned_to(self, obj):
        return ", ".join([user.username for user in obj.assigned_to.all()])
    get_assigned_to.short_description = 'Assigned To'

admin.site.register(Task, TaskAdmin)

@admin.register(StatusChangeRequest)
class StatusChangeRequestAdmin(admin.ModelAdmin):
    list_display = ('task', 'requested_by', 'current_status', 'requested_status', 'is_approved')
    search_fields = ('task__title', 'requested_by__username', 'current_status', 'requested_status')
    list_filter = ('is_approved', 'current_status', 'requested_status')
