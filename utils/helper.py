from datetime import UTC, datetime, timedelta


def get_specific_date(date_format="%Y-%m-%d-%H-%M-%S", days=0, hours=0, minutes=0, seconds=0) -> str:
    current_date = datetime.now(tz=UTC)
    specific_date = current_date + timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
    return specific_date.strftime(date_format)
