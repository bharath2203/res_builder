from django import forms
from .models import Personal, Education, Skill, Project, Experience
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class LoginForm(forms.Form):
  username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User Name'}))
  password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class PersonalForm(forms.ModelForm):
  class Meta:
    model = Personal
    exclude = ('user',)


class EducationForm(forms.ModelForm):
  class Meta:
    model = Education
    exclude = ('user',)

class SkillForm(forms.ModelForm):
  class Meta:
    model = Skill
    exclude = ('user', )
    widgets = (
      {'skill': forms.TextInput(attrs={'placeholder': 'Enter Skill'})},
      {'level': forms.NumberInput(attrs={'placeholder': 'Enter value between 1 and 10'})}
    )
      
class ProjectForm(forms.ModelForm):
  class Meta:
    model = Project
    exclude = ('user',)


class ExperienceForm(forms.ModelForm):
  class Meta:
    model = Experience
    exclude = ('user',)
