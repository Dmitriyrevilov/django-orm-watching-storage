from .models import Visit
import localtime


def get_duration(visit):
    time_now = localtime()
    if not visit.leaved_at:
        time_in_storage = time_now - visit.entered_at
        return time_in_storage


def format_duration(duration):
    visit = Visit.objects.all()
    duration = get_duration(visit)
    return duration
