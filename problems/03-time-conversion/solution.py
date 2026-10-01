#!/usr/bin/env python3
"""HackerRank: Time Conversion."""

def timeConversion(s):
    clock_time, period = s[:-2], s[-2:]
    hour, rest = int(clock_time[:2]), clock_time[2:]
    if period == 'AM':
        hour = 0 if hour == 12 else hour
    else:
        hour = 12 if hour == 12 else hour + 12
    return f'{hour:02d}{rest}'

def main():
    import sys
    value = sys.stdin.readline().strip()
    if value:
        print(timeConversion(value))

if __name__ == '__main__':
    assert timeConversion('07:05:45PM') == '19:05:45'
    assert timeConversion('12:00:00AM') == '00:00:00'
    assert timeConversion('12:00:00PM') == '12:00:00'
    main()
