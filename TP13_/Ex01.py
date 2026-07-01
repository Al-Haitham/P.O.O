import re

logs = """
2026-01-10;Ali;SUCCESS
2026-01-10;Ali;FAILED
2026-01-10;Ali;FAILED
2026-01-10;Ali;FAILED
2026-01-10;Sara;SUCCESS
2026-01-10;Omar;FAILED
2026-01-10;Omar;FAILED
"""

usrSt=re.sub(";"," ",logs)
print(usrSt)

users=re.findall(r"\b(?P<utilisateur>[A-Z][a-z]+?) (?P<status>[A-Z]+\b)",usrSt)
print(users)