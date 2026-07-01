import re

emails = """
ali@gmail.com
sara@yahoo.fr
test.123@ofppt.ma
"""

emailRe=re.compile(r"[a-zA-Z0-9.]+@[a-z]+\.[a-z]+")
print(emailRe.findall(emails))