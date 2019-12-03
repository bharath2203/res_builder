from django import forms
from .models import Personal, Education, Skill, Project, Experience
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django.core.exceptions import ValidationError
import datetime

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

    widgets = {
        'graduation_date': forms.NumberInput(attrs={'onchange': 'yearValidation(this.value)'})
      }


  def clean_graduation_date(self):
    date = self.cleaned_data['graduation_date']
    now = datetime.datetime.now()
    year = now.year
    if date > year:
      raise ValidationError("Greater value than today")
      return year
    return date


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
