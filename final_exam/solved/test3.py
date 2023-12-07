def is_valid_time(hour, minute):
    return 0 <= hour < 24 and 0 <= minute < 60


def find_time_in_string(s):
    n = len(s)
    for i in range(n - 1):
        if s[i].isdigit() and s[i + 1].isdigit():
            hour = int(s[i:i + 2])
            minute = 0

            if i + 2 < n and (s[i + 2] == ':' or (s[i + 2].isdigit() and s[i + 3].isdigit())):
                minute_start = i + 3 if s[i + 2] == ':' else i + 2
                if minute_start + 1 < n and s[minute_start].isdigit() and s[minute_start + 1].isdigit():
                    minute = int(s[minute_start:minute_start + 2])

            if is_valid_time(hour, minute):
                return f"{hour:02d}:{minute:02d}"

    return "시간 없음"


str = input()
print(find_time_in_string(str))
