import re
gmail_re = re.compile(".*@gmail\.com$", re.I)
gmail_users = []
for t0 in range(int(input().strip())):
    name, email = input().strip().split(' ')
    if gmail_re.match(email):
        gmail_users.append(name)
print("\n".join(sorted(gmail_users)))