from .models import Visit
import localtime


def get_duration(visit):
    time_now = localtime()
    if not visit.leaved_at:
        time_in_storage = time_now - visit.entered_at
        return time_in_storage


def format_duration(duration):
    hours = duration.seconds // 3600
    minutes = (duration.seconds % 3600) // 60
    seconds = duration.seconds % 60
    return f"{hours:02}:hours  {minutes:02}:minutes {seconds}:seconds"


def is_visit_long(visit):
    if get_duration(visit).total_seconds() > 600:
        return True
    else:
        return False
