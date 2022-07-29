from django.views.generic import TemplateView, \
    FormView, CreateView, ListView, DetailView, UpdateView
from django.urls import reverse_lazy
from classroom.models import Teacher, Reviews
from .forms import ContactForm


# Create your views here.
class HomeView(TemplateView):
    template_name = 'classroom/home.html'


class ThanksView(TemplateView):
    template_name = 'classroom/thanks.html'


class TeacherCreateView(CreateView):
    # CreateView auto looking for model_form.html
    model = Teacher
    fields = '__all__'
    success_url = reverse_lazy('classroom:teacher-list')


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'

    # success_url = '/classroom/thanks'
    success_url = reverse_lazy('classroom:thanks')

    def form_valid(self, form):
        return super().form_valid(form)


class TeacherListView(ListView):
    model = Teacher
    context_object_name = 'teachers'


class TeacherDetailView(DetailView):
    model = Teacher


class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = "__all__"
    success_url = reverse_lazy('classroom:teacher-list')
