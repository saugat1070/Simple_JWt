from django.urls import path
from Token.views import StudentView
urlpatterns = [
    path('student_record/',StudentView.as_view(),name='student_record'),
    
]