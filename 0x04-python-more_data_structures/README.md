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


#### Example in code:

```
	sample = {'Ndiawo':142, 'Abuko':136, 'Atieno':157}  // creates a dictionary `sample`

	sample['Ombima'] = 412     // Add `Ombima` records to the dictionary

	`del` sample['Atieno']    //Removes `Atieno` pair of key:value from the dictionary.

	list(sample)     //Lists all the records in the sample dictionary excluding the values.

	sorted(sample)  //Returns a sorted list of keys in the sample dictionary.

	Ndiawo `in` sample    // Evaluates to `true` since Ndiawo is a key in the `sample` dictionary.

	Atieno `not in` sample  // Also evaluates to `true` since Atieno was deleted from the dictionary.

```

- The `dict()` constructor builds dictionaries directly from the sequences of key-value pairs:

Example:

```
	sample([('Ndiawo', 142), ('Abuko', 146), ('Atieno', 156)])

```

- Dictionary comprehensions can also be used to create dictionaries from arbitrary key and value expressions:

```
	{x: x**2 for x in (2, 4, 6)}  // This creats a dictionary with key-value pairs as below:

	{2: 4, 4: 16, 6: 36}

```

## Looping Techniques in sequences and dictinaries

- Looping through sequences and or dictionaries can be done in  a number of ways, depending on the need. Below are some of the techniques used in looping through them:

1. **.items()** method -> `Applies to dictionaries`, whereby the key and corresponding value can be retrieved at the same time.

Example: 

```
	knights = {'gallahad': 'the pure', 'robin': 'the brave'}

	for k, v in knights.`items()`:
		print(k, v)


	gallahad the pure          //Results
	robin the brave           //Results
	
```

2. **enumerate()** function -> Works with sequences, retrieves the `position index` and the corresponding `value` at the same time.

Example:

```
	for i, v in `enumerate(['Tic', 'Tac', 'Toe'])`:
		print(i, v)


	0 Tic		//Results
	1 Tac
	2 Toe

```

3. **zip()** function -> Pairs through looping, entries in two or more sequences at the same time.

Example:

```
	questions = ['name','quest', 'favorite-color']

	answers = ['Lancelot', 'the holy grail', 'blue']


	for q, a in `zip(questions, answers)`:
		print('What is your {0}? It is {1}.'.format(q, a))



	What is your name? It is Lancelot.            //Results
	What is your quest? It is the holy grail.
	What is your favorite-color? It is blue.

```

4. **reversed()** function -> Allows looping over a sequence in reverse by specifying the sequence in a forward direction.

Example:

```
	for i in `reversed(range(1, 10, 2))`:
		print(i)


	
	9	//Results
	7
	5
	3
	1

```

5. **sorted()** function -> Loops over a sequence in a sorted order,and returns a new sorted sequence while leaving the source unaltered.

Example:

```
	basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

	for i in `sorted(basket)`:
		print(i)


	apple	//Results
	apple
	banana
	orange
	orange
	pear

```

6. **set()** -> When used on a sequence elliminates duplicate elements. When used with **sorted()**, over a sequence loops over unique elements of the sequence in a sorted order.

Example:

```
	basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

	for f in `sorted(set(basket))`:

	
	apple	//Results
	banana
	orange
	pear
```

***NB*** -> It is generally considered better practice and its also simpler and safer to create a new list instead of attempting to change a list while looping over it.

	 -> The operators `in` and `not in` are membership tests and can determine whether a value is in or not in a container.

	 -> The operators `is` and `is not` compare whether two objects are really the same object.

	 -> Sequence objects may be compared to other objects with the smae sequence type. The comparison uses `lexographical ordering` whereby the first two items are compared and if they differ this determines the comparison result, otherwise the next two are compared and so on.

	 - If the sequence is exhausted, and all items are equal, it is considered equal

	- Otherwise if one sequence defers to the other, they are considered not equal.

	- If one sequence is `a sub-sequence` to the other, it is considered the `lesser one`, even if all its items equally compare to some items in the other sequence.


## Lambda, filter(), map() and reduce()

### Lambda fuctions

- Known as the lambda operator or function.
- Is a way to creat small anonymous functions (throw-away functions), just needed where they have been create
  and discarded thereafter.
- Are mainly used in conjuction with the functions `filter()`, `map()` and `reduce()`.

- General syntax is of the form:

	```
		lambda argument_list: expression

		Example:

			sum = lambda x, y: x + y
			sum(3, 4)

	```

  Whereby the argument list consists of a comma separaed list of arguments and the expression is an arithmetic expression using these arguments.

- This function can be asigned to a variable to give it a name.


### The map() function

- Takes two arguments:

	```
		r = map(func, seq)
	```

	Whereby the first argument, `func` is the name of a function and the second argument, `seq` is a sequence whose elements are to be subjected to the function in the first argument.

- Example:

	```
		C = [39.2, 36.5, 37.3, 38, 37.8]
		F = list(map(lambda x: (float(9)/5)*x + 32, C))

	```

- map() can be applied to more than one list. These lists do not need to be of the same length.

- Example:

	```
		a = [1, 2, 3, 4]
		b = [17, 12, 11, 10]
		c = [-1, -4, 5, 9]

		list(map(lambda x, y, z : x+y+z, a, b, c))


		[17, 10, 19, 23] // Results
	```

- When a list has fewer values than the other, map() stops when the shortest list has been consumed.

#### Mapping a list of functions

- It is also very possible to map a bunch of functions to a single python object. These functions may be supplied in the form of an iterable such as a list or tuple.

- The example below illustrates this:

	```
		from math import sin, cos, tan, pi

		def map_functions(x, functions):  // Here x = object, functions = bunch of functions

			res = []

			for func in funcions:
				res.append(func(x))
			return res

		family_of_functions = (sin, cos, tan)
		
		print(map_functions(pi, family_of_functions)

	```

### Filtering

- Through the function, `filter(function, sequence)` offers a way to filter out all the elements of a sequence for which the function `function` returns True.

- An item is produced by the iterator result of `filter(function, sequence)` if item is included in the sequence `sequence` and if the `function(item)` returns `True` 

- The function `filter(f, I)` needss a function as the first argument, `f` has to return a `Boolean` value and this function is applied to every element of the list I. Only if f returns `True` will the element in `I` be returned by the iterator, which is the return value of filter.

- Exampl:

	```
		fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
		odd_numbers = list(filter(lambda x: x % 2, fibonacci))
		
		print(odd_numbers)
	```

## Reducing a list

- The function, `reduce(func, seq)` continually applies the function `func()` to the sequence `seq`. It returns a single value.

- Here's an illustration of how the reduce() works.
	
	if the seq = [s1, s2, s3, s4,...sn], calling reduce(func, seq) works like this:

	At first the first two elements of seq will be applied to func, i.e func(s1, s2) and the list on which
	the function func now works on looks like this, [func(s1, s2), s3, s4,...sn].

	In the next step, func is applied to the previous result and the third element of the list, i.e 
		func(func(s1, s2), s3)

	This goes on cummulatively until just one element is left and returns this element as the result
	of reduce().

- In order to use reduce(), you have to import `functools`.
