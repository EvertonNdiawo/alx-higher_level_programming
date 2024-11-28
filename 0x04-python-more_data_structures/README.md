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
