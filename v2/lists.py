fruits = ["coconut", "banana", "orange"]


# list.append(elem) -- adds a single element to the end of the list. Common error: does not return the new list, just modifies the original.
fruits.append('apple')

# list.insert(index, elem) -- inserts the element at the given index, shifting elements to the right.
fruits.insert(1, 'avocado')

# list.extend(list2) adds the elements in list2 to the end of the list. Using + or += on a list is similar to using extend().
fruits.extend(['kiwi', 'strawberry'])

# list.index(elem) -- searches for the given element from the start of the list and returns its index. Throws a ValueError if the element does not appear (use "in" to check without a ValueError).
index = fruits.index('banana')
# print('apricot' in fruits)
# print('banana' in fruits)
# print(index)

# list.remove(elem) -- searches for the first instance of the given element and removes it (throws ValueError if not present)
fruits.remove('banana')
fruits.remove('orange')

# list.sort() -- sorts the list in place (does not return it). (The sorted() function shown below is preferred.)

# list.reverse() -- reverses the list in place (does not return it)
# print(fruits)
fruits.reverse()
# print(fruits)

# list.pop(index) -- removes and returns the element at the given index. Returns the rightmost element if index is omitted (roughly the opposite of append()).
print(fruits)
elem = fruits.pop()
print(elem)
print(fruits)
