from random import randint

#ex1

# l = []

# a = randint(5,10)

# for i in range(a):
#     b = randint(1,100)
#     l.append(b)

# print(l[4])

# l[1] = 17 
# l[3] = l[2] + l[4]
# for loops in range(12):
#     print(l[-1])
    
#ex2
# m = []

# def echange(m):
#     return m[0] + m[-1]

#ex3

# e = []
# produit = 1
# c = randint(5,10)
# a = 0
# d = 0
# moyenne = 0

# for i in range(c):
#     b = randint(0,71)
#     e.append(b)
    
# for i in range(len(e)):
#     print(e[i], end = "\n")
    
#     if e[i]%3 == 0:
#         a += 1

#     if e[i]%2 == 0:
#         d += e[i]
#     moyenne += e[i]
# moyenne = moyenne/len(e)

# print("il y a {} présents sur la liste".format(a))
# print("le résultat des paires est {} ".format(d))

# print("la moyenne est {}".format(moyenne))
# bool =  moyenne >= 10

# for i in range(len(e)):
#     if e[i] >= 50 and e[i] <= 70:
#         produit *= e[i]
        
# print("le produit est de {}".format(produit))

#ex4


# symetrique = []

# def sym(symetrique):
#     a = len(symetrique)
#     for i in range(a//2):
#         if symetrique[i] != symetrique[-i-1]:
#             return 'faux'
#     return 'vrai'

#ex5
# l = [0,1,2,3,4,5]
# a = [i+3 for i in l]
#print(a)

#ex6
# l = [0,1,2,3,4,5]
# a = [i+3 for i in l if i >= 2]
# print(a)

#ex7

# un = "abc"
# deux = "de"

# q = [un[i]+ deux[j] for i in range(3) for j in range(2)]
# print(q)









