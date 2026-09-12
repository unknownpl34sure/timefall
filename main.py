from datetime import datetime
from core import get_remaining_time_to_new_year
from formatting import format_remaining_time


def main():
    local_time = datetime.now().astimezone()
    remaining = get_remaining_time_to_new_year(local_time)
    print(format_remaining_time(remaining))


if __name__ == '__main__':
    main()