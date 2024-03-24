"""
FILE:		list_comp.py
TITLE:		List Comprehension Demo
AUTHOR:		Daniel R. South

PROGRAM OUTPUT:

Create a list of the powers of 2
[1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

Create a list of tuples = (n, 2**n)
[(0, 1), (1, 2), (2, 4), (3, 8), (4, 16), (5, 32), (6, 64), (7, 128), (8, 256), (9, 512), (10, 1024)]

Create a range of positive integers with a gap
[1, 2, 3, 4, 5, 6, 14, 15, 16, 17, 18, 19]

Creare a list of names that contain lower case 'a'
['Carole', 'Fiona', 'Gina', 'Hanah', 'Jasmine', 'Laura', 'Naomi', 'Oksana', 'Raven', 'Sara', 'Tina', 'Zara']

Creare a list of names that DO NOT contain lower case 'a'
['Anne', 'Beverly', 'Dierdre', 'Emily', 'Irene', 'Michelle', 'Penelope', 'Wendy', 'Yvonne']

Create two lists: powers of 2, and powers of 2 multiplied by the square root of two
[1, 2, 4, 8, 16, 32, 64, 128]
[1.4, 2.8, 5.7, 11.3, 22.6, 45.3, 90.5]

Combine and sort the lists. This result is the range of full stops on a camera lens.
[1, 1.4, 2, 2.8, 4, 5.7, 8, 11.3, 16, 22.6, 32, 45.3, 64, 90.5, 128]

"""

print("\nCreate a list of the powers of 2")
list1 = [2**x for x in range(11)]
print(list1)

print("\nCreate a list of tuples = (n, 2**n)")
list2 = [(x, 2**x) for x in range(11)]
print(list2)

print("\nCreate a range of positive integers with a gap")
list3 = [x for x in range(20) if x > 0 and (x < 7 or x > 13)]
print(list3)

names = ["Anne", "Beverly", "Carole", "Dierdre", "Emily", "Fiona", "Gina", "Hanah", "Irene", "Jasmine", "Laura", "Michelle", "Naomi", "Oksana", "Penelope", "Raven", "Sara", "Tina", "Wendy", "Yvonne", "Zara"]

print("\nCreare a list of names that contain lower case 'a'")
list4 = [x for x in names if "a" in x]
print(list4)

print("\nCreare a list of names that DO NOT contain lower case 'a'")
list5 = [x for x in names if "a" not in x]
print(list5)


print("\nCreate two lists: powers of 2, and powers of 2 multiplied by the square root of two")

from math import sqrt
sqrt2 = sqrt(2)

stops1 = [2**x for x in range(8)]
stops2 = [round((2**x) * sqrt2, 1) for x in range(7)]
print(stops1)
print(stops2)

print("\nCombine and sort the lists. This result is the range of full stops on a camera lens.")
stops1.extend(stops2)
stops1.sort()
print(stops1)
