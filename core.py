from datetime import datetime, timedelta


def get_next_new_year(local_time: datetime) -> datetime:
    next_new_year = local_time.replace(year=local_time.year + 1, month=1, day=1,
                                  hour=0, minute=0, second=0, microsecond=0)
    return next_new_year


def get_remaining_time_to_new_year(local_time: datetime) -> timedelta:
    next_new_year = get_next_new_year(local_time)
    return next_new_year - local_time
