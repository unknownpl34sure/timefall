from datetime import timedelta


TIME_UNIT_FORMS = {
    "day": {
        "one": "день",
        "few": "дня",
        "many": "дней",
    },
    "hour": {
        "one": "час",
        "few": "часа",
        "many": "часов",
    },
    "minute": {
        "one": "минута",
        "few": "минуты",
        "many": "минут",
    },
    "second": {
        "one": "секунда",
        "few": "секунды",
        "many": "секунд",
    },
}


def get_time_unit_word(number: int, unit: str) -> str:
    if 11 <= number % 100 <= 14:
        form = "many"

    elif number % 10 == 1:
        form = "one"

    elif number % 10 in (2, 3, 4):
        form = "few"

    else:
        form = "many"

    return TIME_UNIT_FORMS[unit][form]


def format_remaining_time(remaining_time: timedelta) -> str:
    remaining_days = remaining_time.days
    remaining_hours = remaining_time.seconds // 3600
    remaining_minutes = (remaining_time.seconds % 3600) // 60
    remaining_seconds = remaining_time.seconds % 60

    return (f"До Нового года осталось: {remaining_days} {get_time_unit_word(remaining_days, 'day')}, "
            f"{remaining_hours} {get_time_unit_word(remaining_hours, 'hour')}, "
            f"{remaining_minutes} {get_time_unit_word(remaining_minutes, 'minute')}, "
            f"{remaining_seconds} {get_time_unit_word(remaining_seconds, 'second')}")
