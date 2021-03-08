from django.db import models

class Issue(models.Model):
    user_id = models.CharField(max_length=200, default="admin")
    issue_name = models.CharField(max_length=200)
    issue_text = models.CharField(max_length=3000)
    is_approved = models.BooleanField(default=True)

class SiteUser(models.Model):
    user_id = models.CharField(max_length=200, unique=True)
    user_first_name = models.CharField(max_length=50)
    user_last_name = models.CharField(max_length=50)
    user_street_add = models.CharField(max_length=150)
    user_city_add = models.CharField(max_length=150)
    user_state_add = models.CharField(max_length=30)
    user_zip = models.CharField(max_length=6)
    user_email = models.CharField(max_length=50)
    user_phone = models.CharField(max_length=50)
    
class UserIssue(models.Model):
    user_id = models.CharField(max_length=200)
    issue_name = models.CharField(max_length=200)
    
    # is_bookmarked = models.BooleanField(default=False)
    def __str__(self):
        return self.issue_name

class UserTemplate(models.Model):
    user_id = models.CharField(max_length=200)
    issue_name = models.CharField(max_length=200)
    issue_text = models.CharField(max_length=3000)
    is_approved = models.BooleanField(default=False)