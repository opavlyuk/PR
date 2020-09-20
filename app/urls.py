from django.urls import path

from app.views import StudentList, StudentDetail

urlpatterns = [
    path('', StudentList.as_view(), name='home'),
    path('<int:pk>/', StudentDetail.as_view(), name='student'),
]
