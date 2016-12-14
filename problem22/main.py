
score = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10, "K":11, "L":12, "M":13,
         "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19, "T":20, "U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26, '"':0}

for line in open("names.txt", 'r'):
    names = line[:-1].split(',')

names.sort()
count = 1
total_sum = 0
# print names
for name in names:
    alphabets = list(name)
    temp_sum = sum(map(lambda alphabet: score[alphabet], alphabets ))
    total_sum = total_sum + temp_sum*count
    count += 1
print total_sum
