## PYTHON-MORE_DATA-STRUCTURES

## Sets

- Is an unordered collection with no duplicate elements.
- Basic usage is to `test for membership` and `eliminate duplicate entries`.
- Objects support mathematical operations like union, intersection, difference and symmetric difference.
- Can be created using `curly braces` or even using the `set()` function. Preference for an empty set is to declare it using the `set()` function and not the curly braces, which creates an empty dictionary.

- example using `{}`:
	```
		basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
		
		print(basket)

		{'orange', 'banana', 'pear', 'banana'} //Result


		'orange' `in` basket

		True //Result

		'crabgrass' `in` basket

		False //result
	```

- Example using `set()`:

	```
		a = set('abracadabra')
		b = set('alacazam')


		>>> a

		{'a', 'r', 'b', 'c', 'd'} //Result of unique letters in a

		>>> a `-` b

		{'r', 'd', 'b'} //Result of letters in a but not in b

		>>> a `|` b

		{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'} //Result of letters in a or b or both

		>>> a `&` b

		{'a', 'c'} //Result of letters in both a and b

		>>> a `^` b

		{'r', 'd', 'b', 'm', 'z', 'l'} //Result of letters in a or b but not both

	```

- Similar to lists, `set comprehensions` are also supported:

	```
		a = {X for X in 'abracadabra' if X `not in` 'abc'}

		>>> a

		{'r', 'd'} //Result of all letters found in `abracadabra` where the letters are not in contained in `a, b or c`.
```

## Dictionaries

- Are indexed by keys, unlike in python's sequences `lists, strings, tuples e.t.c` that are indexed by a range of numbers.

- These keys can be any `immutable` types eg strings and numbers.

- A tuple can be used as a key if it only contains strings, or numbers or another tuple. If it contains any mutable object either directly or indirectly, it cannot be used as a key.

- Lists cannot be used as keys since they can be modified in place using index assignments, slice operations or methods such as append().

- An empty dictionary is created using a pair of empty braces `{}`.

- The body of a dictionary generally consists of a comma-seperated list of `key:value` pairs. This is also how a dictionary is written on output.

- Main operations on a dictionary are storing values with some key and extracting this given value using the given key. 

- Deletion of a `key:value` pair is also possible using the `del` keyword.

- Storing with a key that is already in use replaces the old value associated with that key with the newly supplied value. 

- Extracting a value using a  non-existent key results in an error. 

- The operation `list(d)` on a dictionary returns a list of all the keys used in the dictionary.
- To check whether a single key is found within a dictionary, the keyword `in` suffices. 
- `sorted(d)` returns a sorted list of keys in the dictionary. 
