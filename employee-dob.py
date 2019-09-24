import sys

d = {}
a = []
with open("employees.txt", "r" ) as f_src:
   lines = f_src.readlines()

i = 0
while i < len(lines):
   employee_number = lines[i].split()[0]
   if employee_number not in d:
      a = lines[i].split()
      d[employee_number] = {
        "id": a[0],
        "name": " ".join(a[2:]),
        "dob": a[1],
      }
      i = i + 1

details = sys.stdin.read().split()

for key in details:
   print(d[key]["dob"])







