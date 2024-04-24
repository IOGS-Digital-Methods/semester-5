# Question LIST 1
a=['7', '8', '2', '0']
b=['V', 'P', 'A', 'C']
c=(a*3+b*3)[1:-1]

print(type(c))
print(c)

# Question LIST 2
a=[58]
b=[97, 91]
c=4*a
d=2*b+c

print(d)

# Question LIST 3
'''
On crée une liste contenant les 10 premiers nombres entiers naturels par
liste=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Combien vaut alors liste[2:2] ?
[]
'''

# Question DICT
# Combien vaut la variable c à la fin de ce programme ?
d1={'x': 'w', 'k': 's', 'j': 'k', 'r': 'u'}
d2={'k': 'n', 'u': 'y', 's': 'f', 'w': 'g'}
c=d2[d1['r']]
print(c)


# Question CONDITION
# Si a=49 et b=49 alors la condition logique a!=b est :

# Question CONDITION
a = 7
if a <= 3:
    print(2*a-1)
elif a <= 10:
    print(3*a-2)
else :
    print(4*a-3)

# Question CALCUL
a = 4
c = a // 5
d = a / 5
print(f'C = {c} / {type(c)}')
print(f'D = {d} / {type(d)}')

# Question CALCUL 
a = 21
b = 5
print( (a//b) + (a%b) )

# Question ITERATION
for k in range(3):
    print(k)

for k in range(1 ,10 ,3):
    print(k)


# Question CHAINE CARAC
texte = "Un robot ne peut porter atteinte a un etre humain"
compteur = 0
for lettre in texte :
    if lettre == 'e':
        compteur = compteur + 1
print(compteur)

# Question CHAINE
a="6"
n=4
print(n*a)

# Question PIEGE
a=2
b=7
s=a*b
print("s")

# Question FONCTION
def mystere(a,b):
    return 4*(a+b)
print(mystere (2 ,5))


'''
Antoine doit écrire une fonction qui prend en paramètre un entier n et renvoie True si cet entier est pair, et False si cet entier est impair.

Il écrit le code suivant:


def f(n):
    if n%2 == 0:
        return True
    else:
        return False
Que peut-on reprocher à ce code:

la fonction est mal nommée.
il manque le docstring.
le corps est mal écrit.

(les trois réponses)

--Answer :
def estPair(n):
    """ 
    n -- entier 

    renvoie True si n est pair, False si n est impair.
    >>> estPair(0)
    True
    >>> estPair(1)
    False
    >>> estPair(100)
    True
    >>> estPair(2013)
    False
    """
    return n%2 == 0
'''


'''
def g(x):
    a = a + x
    return a

a = 5
print(g(2))
on obtient:

une erreur
l'affichage de la valeur 7


-- Réponse
une erreur
l'affichage de la valeur 7
La présence d'une affectation a = a+x fait de a une variable locale. De ce fait, on essaie d'augmenter de 2 la valeur de a alors que a n'a pas de valeur affectée. On obtient donc l'erreur local variable 'a' referenced before assignment.
'''

## Python
# How do you insert COMMENTS in Python code?


## NUMPY

# https://www.w3schools.com/quiztest/quiztest.asp?qtest=NUMPY
#   
# What is a correct syntax to print the numbers [3, 4, 5] from the array below:
# arr = np.array([1,2,3,4,5,6,7])

# Which syntax would print the last 4 numbers from the array below:
# arr = np.array([1,2,3,4,5,6,7])

# What is a correct syntax to check the data type of an array? arr.dtype

# What is a correct syntax to create an array of type float?

# In NumPy, what does the SHAPE of an array mean?

# What is a correct syntax to return the shape of an array?

# Which syntax would print the last 4 numbers from the array below:
# arr = np.array([1,2,3,4,5,6,7])
#   print(arr[3:])  


# What is a correct syntax to check the number of dimensions in an array?
# arr.ndim

# What is a correct syntax to return the index of all items that has the value 4 from the array below:
# arr = np.array([1,4,3,4,5,4,4])?

# When using the NumPy random module, how can you return a random number from 0 to 100?
# random.randint(100)

# When using the NumPy random module, how can you return a Normal Data Distrbution with 1000 numbers, concentrated around the number 50, with a standard deviation of 0.2?
# random.normal(size=1000, loc=50, scale=0.2)  

# What is a correct syntax to mathematically add the numbers of arr1 to the numbers of arr2?
# np.add(arr1, arr2)  