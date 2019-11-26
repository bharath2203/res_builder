from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.urls import reverse
from .forms import LoginForm, PersonalForm, EducationForm, SkillForm, ProjectForm, ExperienceForm
from django.contrib.auth.models import User
from .models import Education, Skill, Personal, Project, Experience
from django.contrib.auth.decorators import login_required
# Create your views here.



def dashboard(request):
  context = {}
  educations = Education.objects.filter(user = request.user)
  projects = Project.objects.filter(user = request.user)
  personals = Personal.objects.filter(user = request.user)
  if len(personals):
    personal = personals[0]
  skills = Skill.objects.filter(user = request.user)
  experiences = Experience.objects.filter(user = request.user)
  context['educations'] = educations
  context['projects'] = projects
  if len(personals): 
    context['personal'] = personal
  context['skills'] = skills
  context['experiences'] = experiences
  return render(request, 'dashboard.html', context)

def res_login(request):
  if request.user.is_authenticated:
    return redirect(reverse('dashboard'))
  if request.method == 'POST':
    form = LoginForm(data = request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      try:
        user = User.objects.get(username = username)
      except User.DoesNotExist:
        new_user = User.objects.create_user(username = username, password = password)
        new_user.save()
      user = authenticate(username = username, password = password)
      if user is not None:
        login(request, user)
        return redirect(reverse('dashboard'))
      else:
        return HttpResponse('Invalid Credentials')
    else:
      return HttpResponse("Something wrong again")
  else:
    form = LoginForm()
    return render(request, 'login.html', {'form' : form})


def res_logout(request):
  logout(request)
  return redirect(reverse('login'))


def personal(request):
  template = 'personal.html'
  try:
    personal_data = Personal.objects.get(user = request.user)
  except Personal.DoesNotExist:
    personal_data = 0
  print(request.user)
  if request.method == 'POST':
    if personal_data:
      form = PersonalForm(
        data = request.POST,
        instance = personal_data
        )
    else:
      form = PersonalForm(
        data = request.POST,
        )
    if form.is_valid():
      personal = form.save(commit = False)
      personal.user = request.user
      personal.save()
      return redirect(reverse('dashboard'))
    else:
      return render(request, '500.html')
  else:
    if personal_data:
      form = PersonalForm(instance = personal_data)
    else:
      form = PersonalForm()
    return render(request, template, {'form': form})


def education(request):
  template = "education.html"
  educations = Education.objects.filter(user = request.user)
  for education in educations:
    print(education.school_name)
  if request.method == 'POST':
    form = EducationForm(data = request.POST)
    if form.is_valid():
      education = form.save(commit = False)
      education.user = request.user
      education.save()
      return redirect(reverse('education'))
    else:
      return HttpResponse(form.errors)
  else:
    form = EducationForm()
    return render(request, template, {'form': form, 'educations': educations})


def education_add(request):
  template = "education_add.html"
  if request.method == 'POST':
    form = EducationForm(
      data = request.POST
    )
    if form.is_valid():
      education = form.save(commit = False)
      education.user = request.user
      education.save()
      return redirect(reverse('education'))
    else:
      return HttpResponse(form.errors)
  else:
    form = EducationForm()
    return render(request, template, {'form': form})



def education_edit(request, id):
  template = "education_add.html"
  education = Education.objects.get(id = id)
  if request.method == 'POST':
    form = EducationForm(
      data = request.POST,
      instance = education
    )
    if form.is_valid():
      education = form.save(commit = False)
      education.user = request.user
      education.save()
      return redirect(reverse('education'))
    else:
      return HttpResponse(form.errors)
  else:
    form = EducationForm(instance = education)
    return render(request, template, {'form': form})

def education_delete(request, id):
  education = Education.objects.get(id = id)
  education.delete()
  return redirect(reverse('education'))

def skill(request):
  template = "skill.html"
  skills = Skill.objects.filter(user = request.user)
  if request.method == 'POST':
    form = SkillForm(data = request.POST)
    if form.is_valid():
      skill = form.save(commit = False)
      skill.user = request.user
      skill.save()
      return redirect(reverse('skill'))
    else:
      return HttpResponse(form.errors)
  else:
    form = SkillForm()
    return render(request, template, {'form': form, 'skills': skills})

  
def skill_delete(request, id):
  Skill.objects.get(id = id).delete()
  return redirect(reverse('skill'))


def project(request):
  template = "project.html"
  projects = Project.objects.filter(user = request.user)  
  if request.method == 'POST':
    form = ProjectForm(data = request.POST)
    if form.is_valid():
      project = form.save(commit = False)
      project.user = request.user
      project.save()
      return redirect(reverse('project'))
    else:
      return HttpResponse(form.errors)
  else:
    form = ProjectForm()
    return render(request, template, {'form': form, 'projects': projects})


def project_add(request):
  template = "project_add.html"
  if request.method == 'POST':
    form = ProjectForm(
      data = request.POST
    )
    if form.is_valid():
      project = form.save(commit = False)
      project.user = request.user
      project.save()
      return redirect(reverse('project'))
    else:
      return HttpResponse(form.errors)
  else:
    form = ProjectForm()
    return render(request, template, {'form': form})



def project_edit(request, id):
  template = "project_add.html"
  project = Project.objects.get(id = id)
  if request.method == 'POST':
    form = ProjectForm(
      data = request.POST,
      instance = project
    )
    if form.is_valid():
      project = form.save(commit = False)
      project.user = request.user
      project.save()
      return redirect(reverse('project'))
    else:
      return HttpResponse(form.errors)
  else:
    form = ProjectForm(instance = project)
    return render(request, template, {'form': form})

def project_delete(request, id):
  project = Project.objects.get(id = id)
  project.delete()
  return redirect(reverse('project'))

def experience(request):
  template = "experience.html"
  experiences = Experience.objects.filter(user = request.user)  
  if request.method == 'POST':
    form = ExperienceForm(data = request.POST)
    if form.is_valid():
      experience = form.save(commit = False)
      experience.user = request.user
      experience.save()
      return redirect(reverse('experience'))
    else:
      return HttpResponse(form.errors)
  else:
    form = ExperienceForm()
    return render(request, template, {'form': form, 'experiences': experiences})


def experience_add(request):
  template = "experience_add.html"
  if request.method == 'POST':
    form = ExperienceForm(
      data = request.POST
    )
    if form.is_valid():
      experience = form.save(commit = False)
      experience.user = request.user
      experience.save()
      return redirect(reverse('experience'))
    else:
      return HttpResponse(form.errors)
  else:
    form = ExperienceForm()
    return render(request, template, {'form': form})



def experience_edit(request, id):
  template = "experience_add.html"
  experience = Experience.objects.get(id = id)
  if request.method == 'POST':
    form = ExperienceForm(
      data = request.POST,
      instance = experience
    )
    if form.is_valid():
      experience = form.save(commit = False)
      experience.user = request.user
      experience.save()
      return redirect(reverse('experience'))
    else:
      return HttpResponse(form.errors)
  else:
    form = ExperienceForm(instance = experience)
    return render(request, template, {'form': form})

def experience_delete(request, id):
  experience = Experience.objects.get(id = id)
  experience.delete()
  return redirect(reverse('experience'))
