from django.utils.timezone import localtime

SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60
LONG_VISIT_THRESHOLD_SECONDS = 600


def get_duration(visit):
    time_now = localtime()
    if visit.leaved_at:
        time_in_storage = visit.leaved_at - visit.entered_at
        return time_in_storage
    else:
        time_in_storage = time_now - visit.entered_at
        return time_in_storage


def format_duration(duration):
    total_seconds = int(duration.total_seconds())
    hours = total_seconds // SECONDS_PER_HOUR
    minutes = (total_seconds % SECONDS_PER_HOUR) // SECONDS_PER_MINUTE
    seconds = total_seconds % SECONDS_PER_MINUTE
    return f"{hours:02}:hours  {minutes:02}:minutes {seconds}:seconds"


def is_visit_long(visit):
    return not get_duration(visit).total_seconds() > LONG_VISIT_THRESHOLD_SECONDS