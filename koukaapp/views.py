from django.shortcuts import render
from django.views.generic import ListView,DetailView,FormView
from .models import BlogContent

from django.urls import reverse_lazy
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import EmailMessage
# Create your views here.
class MainView(FormView):
    template_name="main.html"
    form_class = ContactForm
    success_url = reverse_lazy("koukaapp:main")
    def form_valid(self, form):
        name = form.cleaned_data["name"]
        email = form.cleaned_data["email"]
        phone = form.cleaned_data["phone"]
        message = form.cleaned_data["message"]
        
        subject = "問い合わせ:{}".format(name)
        message = "FROM:{0}\nEMAIL:{1}\nPHONE:{2}\nMESSAGE:{3}".format(name,email,phone,message)
        from_email = "django4tester@gmail.com"
        to_list = ["django4tester@gmail.com"]
        
        message = EmailMessage(subject=subject,body=message,from_email=from_email,to=to_list)
        message.send()
        messages.success(self.request, "Send Message is Collect!")
        return super().form_valid(form)
    
class ContentView(ListView):
    template_name="content.html"
    context_object_name = "orderby_records"
    queryset = BlogContent.objects.order_by("-posted_at")

class ChildDetailView(DetailView):
    template_name="detail.html"
    model = BlogContent