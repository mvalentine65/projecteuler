from __future__ import annotations
from enum import Enum


class Days(Enum):
    """
    1 indexed enum for the days of the week.
    """
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

    def to_zeller_num(self) -> int:
        return (self.value + 1) % 7

    @staticmethod
    def from_zeller_num(day: int) -> Days:
        num = (day + 6) % 7
        if num == 0:
            return Days.SUNDAY
        return Days(num)

class Months(Enum):
    """
    1 indexed enum for the month of the year.
    """
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12


DAYS_IN_WEEK = 7

MONTHS_IN_YEAR = 12


def zeller_congruence(day: int, month: int, year: int) -> Days:
    of_century = year % 100
    century = year // 100
    zellner_num = (day + ((13 * (month+1)) // 5) + of_century + 
        (of_century // 4) + (century // 4) + 5 * century) % 7
    return Days.from_zeller_num(zellner_num)
