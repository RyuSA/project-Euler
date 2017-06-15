
problem = []

for row in open('problem.txt', 'r').readlines():
    problem.append([int(x) for x in row[:-1].split(' ')])

for index in range(1,len(problem)):
    for i in range(len(problem[index])):
        if(i == 0):
            problem[index][i] = problem[index][i] + problem[index-1][i]
        elif(i == len(problem[index])-1):
            problem[index][i] = problem[index][i] + problem[index-1][i-1]
        else:
            problem[index][i] = problem[index][i] + max(problem[index-1][i],problem[index-1][i-1])
        print(problem[index])

print("////////////////////////////")
print(problem[len(problem[index])])
