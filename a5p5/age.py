# JTSK-350112
# a5 5.py
# Wossen Hailemariam
# w.hailemariam@jacobs-university.de



import datetime

d_string = input("Day of Birth: ")
while '.' not in d_string and '-' not in d_string:
    d_string = input("Day of Birth: ")


if '.' in d_string:
    isoDate = datetime.datetime.strptime(d_string, "%d.%m.%Y")
    isoDate = isoDate.strftime("%Y-%m-%d")
    date = datetime.date.fromisoformat(isoDate)
else:
    date = datetime.date.fromisoformat(d_string)

diff = datetime.date.today() - date

print((diff.days/365.25)//1)
#done