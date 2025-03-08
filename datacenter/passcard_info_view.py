from datacenter.models import Passcard, Visit
from django.shortcuts import render, get_object_or_404
from datacenter.get_duration import get_duration, format_duration, is_visit_long


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    this_passcard_visits = Visit.objects.filter(passcard=passcard)
    for visit in Visit.objects.filter(passcard=passcard):
        this_passcard_visits = [
            {
                "entered_at": visit.entered_at,
                "duration": format_duration(get_duration(visit)),
                "is_strange": is_visit_long(visit),
            },
        ]
    context = {"passcard": passcard, "this_passcard_visits": this_passcard_visits}
    return render(request, "passcard_info.html", context)
