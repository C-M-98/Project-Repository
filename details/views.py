from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from .models import Styles, Skills, Education, EduStyles
from django.views.generic.detail import DetailView

# Create your views here.
class HomePage(TemplateView):
    template_name = "details/home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['styles'] = Styles.objects.all()
        context['skills'] = Skills.objects.all()
        return context
    
    
class Qualifications(ListView):
    model = Education
    template_name = 'details/education.html'
    context_object_name = 'educations'
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        educations = self.get_queryset();
        
        enumerated_educations = list(enumerate(educations, start=1))
        odd_educations = [edu for index, edu in enumerated_educations if index % 2 == 1]
        even_educations = [edu for index, edu in enumerated_educations if index % 2 == 0]
        context['pairs'] = zip(odd_educations, even_educations)
        context['eduStyles'] = EduStyles.objects.all()
        return context
    