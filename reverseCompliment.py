DNA = "AAGCT"
index = 0

repG = "C"
repC = "G"
repA = "T"
repT = "A"


for y in DNA:
    if y == "G":
      DNA = DNA[:index] + repG + DNA[index +1:]
    if y == "A":
      DNA = DNA[:index] + repA + DNA[index +1:]
    if y == "C":
      DNA = DNA[:index] + repC + DNA[index +1:]
    if y == "T":
      DNA = DNA[:index] + repT + DNA[index +1:]
    index = index +1

DNA = DNA[::-1]
print DNA
