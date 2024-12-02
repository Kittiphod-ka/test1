
# Create your views here.
from django.shortcuts import render
from django.views.generic import UpdateView , DeleteView
from django.urls import reverse_lazy
from .models import *

# Create your views here.

def course_list(request):
    courses = course.objects.all()  # ดึงรายการรายวิชาทั้งหมด
    return render(request, 'course_list.html', {'courses': courses})

def course_search(request):
    search = request.GET.get('id', '')
    courses = course.objects.filter(course_id__icontains=search)
    return render(request, 'course_search.html', {'courses': courses})


class CourseUpdateView(UpdateView):
    model = course
    fields = ['course_name', 'course_teacher'] # form
    template_name = 'course_update.html'
    success_url = reverse_lazy('course_search')

class CourseDeleteView(DeleteView):
    model = course
    template_name = 'course_delete.html'
    success_url = reverse_lazy('course_search')