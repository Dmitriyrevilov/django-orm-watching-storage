from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render

from django.utils.timezone import localtime


from get_duration_and_format_duration import get_duration


def storage_information_view(request):
    # Программируем здесь
    for visit in Visit.objects.filter(leaved_at=None):
        non_closed_visits = [
            {
                "who_entered": visit.passcard.owner_name,  # получили имя
                "entered_at": visit.entered_at,  # получили время входа
                "duration": get_duration(visit),  # получили время входа
            }
        ]
    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }
    return render(request, "storage_information.html", context)
