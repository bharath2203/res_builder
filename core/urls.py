from django.contrib import admin
from django.urls import path, include
from core.views import ( 
  res_login, res_logout, dashboard, personal, resume,
  education, skill, education_add, skill_delete,
  education_edit, education_delete, nothing,
  project, project_add, project_edit, project_delete,
  experience, experience_add, experience_edit, experience_delete
  )

urlpatterns = [
  path('', nothing, name = "direct"),
  path('login', res_login, name = "login"),
  path('logout', res_logout, name = "logout"),
  path('dashboard', dashboard, name = "dashboard"),
  path('resume/<str:id>', resume, name = "resume"),
  path('personal', personal, name = "personal"),
  path('education', education, name = "education"),
  path('education/add', education_add, name = "education_add"),
  path('education/edit/<int:id>', education_edit, name = "education_edit"),
  path('education/delete/<int:id>', education_delete, name = "education_delete"),
  path('skill', skill, name = "skill"),
  path('skill/delete/<int:id>', skill_delete, name = "skill_delete"),
  path('project', project, name = "project"),
  path('project/add', project_add, name = "project_add"),
  path('project/edit/<int:id>', project_edit, name = "project_edit"),
  path('project/delete/<int:id>', project_delete, name = "project_delete"),
  path('experience', experience, name = "experience"),
  path('experience/add', experience_add, name = "experience_add"),
  path('experience/edit/<int:id>', experience_edit, name = "experience_edit"),
  path('experience/delete/<int:id>', experience_delete, name = "experience_delete"),
]