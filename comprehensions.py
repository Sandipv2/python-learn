# List Comprehensions
arr = [x for x in range(1,6)]
# [1, 2, 3, 4, 5]

# Dictionary Comprehension
no_sqr = {x: x**2 for x in range(1,6)} 
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

list_compre = [{"num": x, "sqr": x**2} for x in range(1,3)]
# [{'num': 1, 'sqr': 1}, {'num': 2, 'sqr': 4}]


print(arr)
print(list_compre)
print()

    
