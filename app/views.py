from django.views.generic import ListView
from django.views.generic.detail import DetailView

from app.models import Student


class StudentList(ListView):
    model = Student

    def get_queryset(self):
        filter_val = self.request.GET.get('faculty', 'All')
        if filter_val == 'All':
            return super().get_queryset()
        print(filter_val)
        return Student.objects.filter(faculty=filter_val)


class StudentDetail(DetailView):
    model = Student
