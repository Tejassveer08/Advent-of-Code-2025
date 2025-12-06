import re

with open("D5Input.txt", "r") as f:
    lines = [line.strip() for line in f if line.strip()]

range_lines = []
ingredient_lines = []

range_pattern = re.compile(r"^\d+-\d+$")   # matches: 123-456

# Split lines automatically
for line in lines:
    if range_pattern.match(line):
        range_lines.append(line)
    else:
        ingredient_lines.append(line)

# Now parse ranges
R = []
for r in range_lines:
    st, ed = map(int, r.split('-'))
    R.append((st, ed))

# ---------- PART 2 ----------
p2 = 0
R = sorted(R)
current = -1

for (s, e) in R:
    if current >= s:
        s = current + 1
    if s <= e:
        p2 += e - s + 1
    current = max(current, e)

# ---------- PART 1 ----------
p1 = 0
for x in ingredient_lines:
    x = int(x)
    for (s, e) in R:
        if s <= x <= e:
            p1 += 1
            break

print(p1)
print(p2)
