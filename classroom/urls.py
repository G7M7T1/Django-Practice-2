from django.urls import path
from .views import HomeView, ThanksView, ContactFormView, \
    TeacherCreateView, TeacherListView, TeacherDetailView

app_name = 'classroom'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('thanks/', ThanksView.as_view(), name='thanks'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('addteacher/', TeacherCreateView.as_view(), name='add-teacher'),
    path('teachers/', TeacherListView.as_view(), name='teacher-list'),
    path('teachers/<int:pk>', TeacherDetailView.as_view(), name='teacher-detail')
]