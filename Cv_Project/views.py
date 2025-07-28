from django.shortcuts import render

from contactUs_app.models import Footer, Info
from projects_app.models import Project


def home(request):

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        info_object = Info(name=name, email=email, subject=subject, message=message)
        info_object.save()

    projects = Project.objects.all()
    footer = Footer.objects.all().last()

    return render(request, 'index.html', context={'projects': projects, 'footer': footer})