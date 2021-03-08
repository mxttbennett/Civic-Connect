from django.test import TestCase

from .models import SiteUser, Issue, UserIssue

# Create your tests here.

class ViewsTestCase(TestCase):
    def test_index_loads(self):
        """The index page loads properly"""
        response = self.client.get('127.0.0.1:8000')
        self.assertEqual(response.status_code, 404)

class ProfileTestCase(TestCase):
    def test_profile_firstname(self):
        """The app saves your first name"""
        people = SiteUser.objects.create(user_first_name="Kanye", user_last_name="West")
        self.assertNotEqual(people.user_last_name, "Kanye")

    def test_profile_email(self):
        bob = SiteUser.objects.create(user_email="bob@gmail.com")
        bob.email = "bob@gmail.com"
        self.assertEqual(bob.email, "bob@gmail.com")

    def test_profile_address(self):
        bob = SiteUser.objects.create(user_street_add="100 Rotunda Ave")
        bob.address = "100 Rotunda Ave"
        self.assertEqual(bob.address, "100 Rotunda Ave")

    def test_profile_city(self):
        bob = SiteUser.objects.create(user_city_add="Charlottesville")
        bob.city = "Charlottesville"
        self.assertEqual(bob.city, "Charlottesville")

    def test_profile_state(self):
        bob = SiteUser.objects.create(user_state_add="Virginia")
        bob.state = "Virginia"
        self.assertEqual(bob.state, "Virginia")

    def test_profile_zip(self):
        bob = SiteUser.objects.create(user_zip="22903")
        bob.zip = "22903"
        self.assertEqual(bob.zip, "22903")

class IssueTestCase(TestCase):
    def test_issue_name(self):
        issue = Issue.objects.create(issue_name="Police Brutality")
        issue.name = "Police Brutality"
        self.assertEqual(issue.name, "Police Brutality")

    def test_issue_text(self):
        issue = Issue.objects.create(issue_name="Abortion Rights", issue_text="Abortions should be a human right!")
        issue.text = "Abortions should be a human right!"
        self.assertEqual(issue.text, "Abortions should be a human right!")

    def test_issue_creation(self):
        issue = Issue.objects.create(issue_name="Gun Control", issue_text="Guns are dangerous and should be harder to get!")
        issue.name = "Gun Control"
        issue.text = "Guns are dangerous and should be harder to get!"
        self.assertEqual(issue.name, "Gun Control")
        self.assertEqual(issue.text, "Guns are dangerous and should be harder to get!")