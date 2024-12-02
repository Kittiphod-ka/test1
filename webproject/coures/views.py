
# Create your views here.
from django.shortcuts import render
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .models import *

# Create your views here.

def course_search(request):
    search = request.GET.get('id', '')
    courses = course.objects.filter(course_id__icontains=search)
    return render(request, 'course_search.html', {'courses': courses})


class CourseUpdateView(UpdateView):
    model = course
    fields = ['course_name', 'course_teacher'] # form
    template_name = 'course_update.html'
    success_url = reverse_lazy('course_search')

