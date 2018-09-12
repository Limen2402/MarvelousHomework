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
