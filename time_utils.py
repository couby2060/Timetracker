def round_up_to_nearest_quarter(time_minutes: int) -> int:
    """Round up time to the nearest quarter hour."""
    return ((time_minutes + 14) // 15) * 15

def minutes_to_hhmm(time_minutes: int) -> str:
    """Convert time in minutes to a string in the format HH:MM."""
    return f"{time_minutes // 60:02}:{time_minutes % 60:02}"
