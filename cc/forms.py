from django import forms

class ContactForm(forms.Form):
    # from_email = forms.EmailField(required=True)
    to_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    
class IssueForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea, required=True)
    
class AddBookmarkForm(forms.Form):
    issue_name = forms.CharField(required=True)
    
class RemoveBookmarkForm(forms.Form):
    issue_name = forms.CharField(required=True)

class TemplateForm(forms.Form):
    # from_email = forms.EmailField(required=True)
    issue_name = forms.CharField(required=True)
    issue_text = forms.CharField(widget=forms.Textarea, required=True)