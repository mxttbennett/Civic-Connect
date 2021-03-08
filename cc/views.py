from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm, IssueForm, AddBookmarkForm, RemoveBookmarkForm, TemplateForm
from .models import SiteUser, Issue, UserIssue, UserTemplate
from django.views import generic
from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404

def indexView(request):
    id_list = list(element.user_id for element in SiteUser.objects.all())
    user_list = SiteUser.objects.all()
    user_issues = UserIssue.objects.all()
    issues = Issue.objects.all()
    user_issue_names = list(element.issue_name for element in UserIssue.objects.filter(user_id = request.user))

    if request.method == 'GET':
        form = ContactForm()
    
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            # from_email = form.cleaned_data['from_email']
            to_email = form.cleaned_data['to_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, 'justincai1990@gmail.com', [to_email])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('/')
    return render(request, "index.html", {'form': form, 'id_list': id_list, 'user_list': user_list, 'user_issues': user_issues, 'issues': issues, 'user_issue_names': user_issue_names})

def templateBuilderView(request):
    id_list = list(element.user_id for element in SiteUser.objects.all())
    user_list = SiteUser.objects.all()
    user_issues = UserIssue.objects.all()
    issues = Issue.objects.all()

    if request.method == 'GET':
        form = TemplateForm()
        
    else:
        form = TemplateForm(request.POST)
        if form.is_valid():
            # issue_name = form.cleaned_data['issue_name']
            # issue_text = form.cleaned_data['issue_text']
            try:
                if not issues.filter(issue_name = request.POST['issue_name']):
                    Issue.objects.create(user_id=request.POST['user_id'],
                    issue_name=form.cleaned_data['issue_name'],
                    issue_text=form.cleaned_data['issue_text'],
                    is_approved = False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            # return render(request, "template_builder.html", {'form': form, 'id_list': id_list, 'user_list': user_list, 'user_issues': user_issues, 'issues': issues})
            return redirect("/")
    return render(request, "template_builder.html", {'form': form, 'id_list': id_list, 'user_list': user_list, 'user_issues': user_issues, 'issues': issues})

def userinfo(request):
    # print(request.POST['user_id'])
    # print(SiteUser.objects.all()[1].user_id)
    # print(request.POST['user_id'] == SiteUser.objects.all()[1].user_id)
    try:
        if not SiteUser.objects.filter(user_id = request.POST['user_id']):
            SiteUser.objects.create(user_id=request.POST['user_id'],
                               user_first_name=request.POST['first_name'],
                               user_last_name=request.POST['last_name'],
                               user_street_add=request.POST['street'],
                               user_city_add=request.POST['city'],
                               user_state_add=request.POST['state'],
                               user_zip=request.POST['zip'],
                               user_email=request.POST['email'],
                               user_phone=request.POST['phone'])
            User.objects.filter(id=request.user.id).update(username=request.POST['user_id'])
        return HttpResponseRedirect(reverse('cc:index'))
      
    except (KeyError, SiteUser.DoesNotExist):
       print("This failed")
       return HttpResponseNotFound('<h1>Page not found</h1>')
       print(KeyError)
       return render(request, 'email.html', {
           'error_message': "You didn't write a comment",
       })


def updateinfo(request):
    # print(request.POST['user_id'])
    # print(SiteUser.objects.all()[1].user_id)
    # print(request.POST['user_id'] == SiteUser.objects.all()[1].user_id)
    try:
        
        if not SiteUser.objects.filter(user_id = request.POST['user_id']):
            SiteUser.objects.create(user_id=request.POST['user_id'],
                               user_first_name=request.POST['first_name'],
                               user_last_name=request.POST['last_name'],
                               user_street_add=request.POST['street'],
                               user_city_add=request.POST['city'],
                               user_state_add=request.POST['state'],
                               user_zip=request.POST['zip'],
                               user_email=request.POST['email'],
                               user_phone=request.POST['phone'])
            User.objects.filter(id=request.user.id).update(username=request.POST['user_id'])
        else:
            if request.POST['first_name'] != "":
               SiteUser.objects.filter(user_id = request.POST['user_id']).update(user_first_name=request.POST['first_name'])
            if request.POST['last_name'] != "":
               SiteUser.objects.filter(user_id = request.POST['user_id']).update(user_last_name=request.POST['last_name'])
            if request.POST['street'] != "":
               SiteUser.objects.filter(user_id = request.POST['user_id']).update(user_street_add=request.POST['street'])
            if request.POST['city'] != "":
               SiteUser.objects.filter(user_id = request.POST['user_id']).update(user_city_add=request.POST['city'])
            if request.POST['state'] != "":
               SiteUser.objects.filter(user_id = request.POST['user_id']).update(user_state_add=request.POST['state'])
            if request.POST['zip'] != "":
               SiteUser.objects.filter(user_id = request.POST['user_id']).update(user_zip=request.POST['zip'])
            if request.POST['email'] != "":
               SiteUser.objects.filter(user_id = request.POST['user_id']).update(user_email=request.POST['email'])
            if request.POST['phone'] != "":
               SiteUser.objects.filter(user_id = request.POST['user_id']).update(user_phone=request.POST['phone'])
            User.objects.filter(id=request.user.id).update(username=request.POST['user_id'])
            
        return HttpResponseRedirect(reverse('cc:profile'))
      
    except (KeyError, SiteUser.DoesNotExist):
       print("This failed")
       return HttpResponseNotFound('<h1>Page not found</h1>')
       print(KeyError)
       return render(request, 'email.html', {
           'error_message': "You didn't write a comment",
       })

def idinfo(request):
    id_list = list(element.user_id for element in SiteUser.objects.all())

    print(id_list)
    # id_list = True
    return render(request, 'cc/index.html', {'id_list': id_list})

def displayinfo(request):
  id = request.POST['user_id']
  info = get_object_or_404(SiteUser, user_id=id)
  name_info = " ".join(list([info.user_first_name, info.user_last_name]))
  mail_info = ", ".join(list([info.user_street_add, info.user_city_add, info.user_state_add, info.user_zip]))
  email_info = info.user_email
  phone_info = info.user_phone
  dict = {'name_info': name_info, 'mail_info': mail_info, 'email_info': email_info, 'phone_info': phone_info}
  return render(request, 'cc/index.html', dict)

def loadtemplate(request):
  name = request.POST['issue_name_input']
  issue_obj = get_object_or_404(Issue, issue_name=name)
  template_title = issue_obj.issue_name
  template_text = issue_obj.issue_text
  user_issue_names = list(element.issue_name for element in UserIssue.objects.filter(user_id = request.user))

  form = ContactForm(initial={'subject': template_title, 'message': template_text})
  id_list = list(element.user_id for element in SiteUser.objects.all())
  user_list = SiteUser.objects.all()
  user_issues = UserIssue.objects.all()
  issues = Issue.objects.all()
  return render(request, 'cc/index.html', {'user_issue_names': user_issue_names, 'template_title': template_title, 'template_text': template_text, 'form': form, 'id_list': id_list, 'user_list': user_list, 'user_issues': user_issues, 'issues': issues})

def redirect_view(request):
    response = redirect('/')
    return response
    
def profileView(request):
    id_list = list(element.user_id for element in SiteUser.objects.all())
    user_list = SiteUser.objects.all()
    issues = Issue.objects.all()
    user_issues = UserIssue.objects.all()
    approved_issues = list(element.issue_name for element in Issue.objects.all() if element.is_approved)
    
    # add_bookmark_form = AddBookmarkForm()
    # remove_bookmark_form = RemoveBookmarkForm()
    
    if request.method == 'GET':

        add_bookmark_form = AddBookmarkForm()
        remove_bookmark_form = RemoveBookmarkForm()

    elif request.method == 'POST':
        
        add_bookmark_form = AddBookmarkForm(request.POST or None)
        remove_bookmark_form = RemoveBookmarkForm(request.POST or None)
    
        
        if request.POST.get('formPurpose') == 'ADD' and add_bookmark_form.is_valid():
            issue_name = add_bookmark_form.cleaned_data['issue_name']
            form_user_id = request.POST.get('formUser')
            add_bookmark_form = AddBookmarkForm(None)
            remove_bookmark_form = RemoveBookmarkForm(None)
            try:
                for issue in issues:
                    if issue_name.upper() == issue.issue_name.upper():
                        UserIssue.objects.filter(user_id=form_user_id, issue_name=issue.issue_name).delete()
                        UserIssue.objects.create(user_id=form_user_id, issue_name=issue.issue_name)
                return render(request, "profile.html", {'add_bookmark_form': add_bookmark_form, 'remove_bookmark_form': remove_bookmark_form, 'id_list': id_list, 'user_list': user_list, 'user_issues': user_issues, 'issues': issues, 'approved_issues': approved_issues})
            except:
                return print('ADD BOOKMARK ERROR')
            return render(request, 'cc/profile.html', {})

        elif request.POST.get('formPurpose') == 'REMOVE' and remove_bookmark_form.is_valid():
            issue_name = remove_bookmark_form.cleaned_data['issue_name']
            form_user_id = request.POST.get('formUser')
            add_bookmark_form = AddBookmarkForm(None)
            remove_bookmark_form = RemoveBookmarkForm(None)
            try:
                for issue in issues:
                    if issue_name.upper() == issue.issue_name.upper():
                        UserIssue.objects.filter(user_id=form_user_id, issue_name=issue.issue_name).delete()
                return render(request, "profile.html", {'add_bookmark_form': add_bookmark_form, 'remove_bookmark_form': remove_bookmark_form, 'id_list': id_list, 'user_list': user_list, 'user_issues': user_issues, 'issues': issues, 'approved_issues': approved_issues})
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, 'cc/profile.html', {})

    return render(request, "profile.html", {'add_bookmark_form': add_bookmark_form, 'remove_bookmark_form': remove_bookmark_form, 'id_list': id_list, 'user_list': user_list, 'user_issues': user_issues, 'issues': issues, 'approved_issues': approved_issues})
 

def templateView(request):
    id_list = list(element.user_id for element in SiteUser.objects.all())
    user_list = SiteUser.objects.all()
    issues = Issue.objects.all()
    user_issues = UserIssue.objects.all()
    
    # add_bookmark_form = AddBookmarkForm()
    # remove_bookmark_form = RemoveBookmarkForm()
    
    if request.method == 'GET':

        add_bookmark_form = AddBookmarkForm()
        remove_bookmark_form = RemoveBookmarkForm()

    elif request.method == 'POST':
        
        add_bookmark_form = AddBookmarkForm(request.POST or None)
        remove_bookmark_form = RemoveBookmarkForm(request.POST or None)
        
        print(request.user)
        
        if request.POST.get('formPurpose') == 'ADD' and add_bookmark_form.is_valid():
            issue_name = add_bookmark_form.cleaned_data['issue_name']
            form_user_id = request.POST.get('formUser')
            remove_bookmark_form = RemoveBookmarkForm(None)
            try:
                for issue in issues:
                    if issue_name == issue.issue_name:
                        UserIssue.objects.filter(user_id=form_user_id, issue_name=issue_name).delete()
                        UserIssue.objects.create(user_id=form_user_id, issue_name=issue_name)
                return render(request, "profile.html", {'add_bookmark_form': add_bookmark_form, 'remove_bookmark_form': remove_bookmark_form, 'id_list': id_list, 'user_list': user_list, 'user_issues': user_issues, 'issues': issues})
            except:
                return print('ADD BOOKMARK ERROR')
            return render(request, 'cc/profile.html', {})

        elif request.POST.get('formPurpose') == 'REMOVE' and remove_bookmark_form.is_valid():
            issue_name = remove_bookmark_form.cleaned_data['issue_name']
            form_user_id = request.POST.get('formUser')
            add_bookmark_form = AddBookmarkForm(None)
            try:
                UserIssue.objects.filter(user_id=form_user_id, issue_name=issue_name).delete()
                return render(request, "profile.html", {'add_bookmark_form': add_bookmark_form, 'remove_bookmark_form': remove_bookmark_form, 'id_list': id_list, 'user_list': user_list, 'user_issues': user_issues, 'issues': issues})
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, 'cc/profile.html', {})

    return render(request, "profile.html", {'add_bookmark_form': add_bookmark_form, 'remove_bookmark_form': remove_bookmark_form, 'id_list': id_list, 'user_list': user_list, 'user_issues': user_issues, 'issues': issues})
  