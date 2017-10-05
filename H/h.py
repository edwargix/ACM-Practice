import math

AI = input().split(' ')
AI = [int(x) for x in AI]
Bribes = math.ceil(AI[0]*(AI[1]-0.99))
print(Bribes)
