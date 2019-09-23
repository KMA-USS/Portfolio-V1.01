from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import FormMixin
from django.shortcuts import render, redirect
from .models import Project, Toolset, Skill
from django.core.mail import send_mail
from .forms import Contactme
# Create your views here.

class HomeView(FormMixin, TemplateView):
    form_class = Contactme
    template_name = 'app/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['projectlist'] = Project.objects.all().order_by('status')
        context['toolset'] = Toolset.objects.all()
        context['form'] = self.get_form()
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            subject = form.cleaned_data.get('subject', '')
            content = form.cleaned_data.get('message', '')
            from_email = form.cleaned_data.get('email', '')
                
            message = "New message from: %s \nContent: %s" % (from_email, content)

            send_mail(subject, message, from_email, ['kelvinmayoayeni@gmail.com'])
            return redirect('/#contact')
        # return render(request, self.template_name, {'form': form})
        context = self.get_context_data(*args, **kwargs)
        context['form'] = form
        return render(request, self.template_name, context)


class ProjectDetail(DetailView):
    model = Project
    context_object_name = 'projectdetail'
    template_name = 'app/projectdetail.html'


