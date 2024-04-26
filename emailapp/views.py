from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
class Home(View):
    def get(self, request):
        return render(request,'input.html')
class Send(View):
    def get(self, request):
        subject='Thankyou for contacting us'
        email_message='we get in few moments'
        from_email=settings.EMAIL_HOST_USER
        email=request.GET["t1"]
        to_list=[email]
        send_mail(subject,email_message,from_email,to_list,fail_silently=False)
        return HttpResponse("mail sent successfully")