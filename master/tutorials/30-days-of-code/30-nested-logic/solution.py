from datetime import date

actual = [int(tmp) for tmp in input().strip().split(' ')]
expected = [int(tmp) for tmp in input().strip().split(' ')]
day,month,year = 0,1,2
actual = date(actual[year], actual[month], actual[day])
expected = date(expected[year], expected[month], expected[day])

fine = 0
if actual <= expected:
    fine = 0
elif  actual.year == expected.year and actual.month == expected.month:
    fine = 15 * (actual.day - expected.day)
elif  actual.year == expected.year:
    fine = 500 * (actual.month - expected.month)
else:
    fine = 10000
              
print(fine)