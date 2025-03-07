from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.get_duration import get_duration, format_duration, is_visit_long


def storage_information_view(request):
    # Программируем здесь
    for visit in Visit.objects.filter(leaved_at=None):  # перебрали тех кто не вышел
        non_closed_visits = [
            {
                "who_entered": visit.passcard.owner_name,  # получили имя
                "entered_at": visit.entered_at,  # получили время входа
                "duration": format_duration(
                    get_duration(visit)
                ),  # получили время нахождения в хранилище
            }
        ]
    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }
    return render(request, "storage_information.html", context)
