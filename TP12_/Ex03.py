import re

date = "Réunion prévue le 15 Juin 2026"
re_date=re.compile(r"(?P<jour>\d{1,2}?) (?P<mois>\w+?) (?P<année>\d{4}?)")
dateRe=re_date.search(date)
print(dateRe.group('mois'),dateRe.group('jour'),dateRe.group('année'))
