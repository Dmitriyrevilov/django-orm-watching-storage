from datacenter.models import Passcard
from django.shortcuts import render


def active_passcards_view(request):
    posts = Passcard.objects.all()
    activate_passcards = posts.filter(is_active=True)
    context = {
        "active_passcards": activate_passcards, 
    }
    return render(request, "active_passcards.html", context)
