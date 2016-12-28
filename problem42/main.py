
"""init from here"""
score = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10, "K":11, "L":12, "M":13,
         "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19, "T":20, "U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26, '"':0}

for line in open("words.txt", 'r'):
    words = line[:-1].split(',')

"""max_sum = 192 < 200"""
maximum = 0

for word in words:
    alphabets = list(word)
    temp_sum = sum(map(lambda alphabet: score[alphabet], alphabets ))
    maximum = max(maximum, temp_sum)

count = 0

triangles = [n*(n+1)/2 for n in xrange(maximum) if n*(n+1)/2 < maximum]


for word in words:
    alphabets = list(word)
    temp_sum = sum(map(lambda alphabet: score[alphabet], alphabets ))
    if temp_sum in triangles:
        count += 1

print count
