from django.contrib import admin
from .models import Issue, SiteUser, UserIssue, UserTemplate

# Register your models here.

class IssueAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Issue',               {'fields': ['user_id', 'issue_name', 'issue_text', 'is_approved']})
    ]
    
    list_display = ('issue_name', 'issue_text', 'is_approved')
    
class SiteUserAdmin(admin.ModelAdmin):
    fieldsets = [
        ('User Information',               {'fields': ['user_id', 'user_first_name', 'user_last_name', 'user_street_add', 'user_city_add', 'user_state_add', 'user_zip']})
    ]
    
    list_display = ('user_id', 'user_first_name', 'user_last_name', 'user_street_add', 'user_city_add', 'user_state_add', 'user_zip')
    
class UserIssueAdmin(admin.ModelAdmin):
    fieldsets = [
        ('User Issues',               {'fields': ['user_id', 'issue_name']})
    ]
    
    list_display = ('user_id', 'issue_name')

class UserTemplateAdmin(admin.ModelAdmin):
    fieldsets = [
        ('User Template',               {'fields': ['user_id', 'issue_name', 'issue_text', 'is_approved']})
    ]
    
    list_display = ('user_id', 'issue_name', 'is_approved')

admin.site.register(Issue, IssueAdmin)
admin.site.register(SiteUser, SiteUserAdmin)
admin.site.register(UserIssue, UserIssueAdmin)
admin.site.register(UserTemplate, UserTemplateAdmin)