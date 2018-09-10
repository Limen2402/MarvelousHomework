# for i in range(1, 100):
#    if i % 15 == 0: 
#        print("fizzbuzz")
#    elif i % 5 == 0: 
#        print("buzz")
#    elif i % 3 == 0: 
#        print("fizz")
#    else: 
#        print(i)
# 
#
#steps = [(1,0),(-1,0),(0,1),(0,-1)]
#
#def generate_walk(path, L):
#    if L == 0:
#        print(path)
#    else: 
#        for dx, dy in steps:
#            x, y = path[-1]
#            pp = path.copy()
#            pp.append((x+dx,y+dy))
#            generate_walk(pp, L-1)
#
#generate_walk([(0,0)], 1)
#

av_phys = 0
av_math = 0
av_rus = 0
n = 0

with open('dataset_3363_3.txt') as input:
    for line in input:
        n += 1
        x = line.split(';')
        av_math += int(x[1])
        av_phys += int(x[2])
        av_rus += int(x[3])
        print((int(x[1]) + int(x[2]) + int(x[3])) / 3)
print(av_math / n, av_phys / n, av_rus / n)

