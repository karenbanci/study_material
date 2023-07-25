from enum import Enum

class DayOfWeek(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

def day_response(day:DayOfWeek):
    if day == DayOfWeek.MONDAY:
        return "Monday =D uhulllll "
    elif day == DayOfWeek.TUESDAY:
        return "TUESDAY =D bleeeeeee"
    elif day == DayOfWeek.WEDNESDAY:
        return "WEDNESDAY =D hihihihihi"
    elif day == DayOfWeek.THURSDAY:
        return "THURSDAY =D omgggggggg"
    elif day == DayOfWeek.FRIDAY:
        return "FRIDAY =D I love it"
    elif day == DayOfWeek.SATURDAY:
        return "SATURDAY =D ihullllll"
    elif day == DayOfWeek.SUNDAY:
        return "SUNDAY =D nooooooo"
    else:
        return "It's wrong =("

for day in DayOfWeek:
    print(f"Today is {day.name} is {day_response(day)}")