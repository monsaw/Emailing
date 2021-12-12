from django.shortcuts import render
from django.views.generic import ListView,UpdateView,DeleteView,CreateView
from .models import Email
from django.urls import reverse_lazy
from django.core.mail import send_mail
# Create your views here.


class EmailList(ListView):
    template_name = 'mail/Emaillist.html'
    context_object_name = 'emails'
    model = Email

class EmailCreate(CreateView):
    template_name = 'mail/Emailcreate.html'
    model = Email
    fields = ('email',)

class EmailUpdate(UpdateView):
    template_name = 'mail/Emailupdate.html'
    model = Email
    fields = ('email',)

class EmailDelete(DeleteView):
    template_name = 'mail/Emaildelete.html'
    model = Email
    success_url = reverse_lazy('mail:emails')

def send_email(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']

        send_mail(
                subject,
                message,
                'lawalmonsuru1995@gmail.com',
                list(Email.objects.all().values_list('email',flat=True)),fail_silently=False
        )
    emails = Email.objects.all()
    return render(request,'mail/send.html',{'emails':emails})


def base(request):
    return render(request,'mail/home.html',{})

def about(request):
    return render(request,'mail/about.html',{})




