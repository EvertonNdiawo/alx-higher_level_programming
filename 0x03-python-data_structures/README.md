# DATA STRUCTURES: - LISTS, TUPLES

## Lists

- Compound data type in python
- List of comma-seperated items enclosed within square brackets.
- Usually items are of same type, but could also contain items of different types.

```
Example:

	squares = [1, 4, 9, 16, 25]
```

### List operations.

1. Lists can be indexed and sliced, just like strings and all other built-in sequence types:

	```
		squares[0] -> returns the item at index 0, that is the square of 1.

		squares[-1] -> returns the last item in the list, i.e 25.

		squares[-3:] #Slicing -> Returns a new list containing the last 3 items.```


2. Lists support concatenation operations:

	```
		Example:

		squares + [36, 49, 64, 81, 100]

		This would returns a result containing all items contained in the `squares` list and the new items. 

		i.e [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

	```

3. listname.append(item) -> Adds a new item at the end of the specified list.
	
	```
		squares.append(121) therefore adds a the square of 11 at the end of our sqaures list.
	```

4. Lists are a ***Mutable*** type (unlike strings which are immutable) and it is therefore possible to change their content: 
	
	```
		example:
			cubes = [1, 8, 27, 65, 125]

			cubes[3] = 64 # modifies the value of the item at index 3.
	```

5. The built-in function ***len()*** also applies to lists and returns the length of a list, i.e the total number of items contained in the said list.

6. It is possible to nest lists:
	```
		a = ['a', 'b', 'c']
		n = [1, 2, 3]
		x = [a, n]

		x is therefore a list that contains two lists within it and its structure may be as follows:

		[['a', 'b', 'c'], [1, 2, 3]]

		with x[0] being list a. and x[1] being list n.

		therefore a reference such as x[0][3] becomes 'c'.

	```

### NOTE: 
	1. Simple assignment in python is by reference (not by value) and therefore when a list is assigned to a variable, any change through the variable is seen through all other variables that refer to the list. 

	2. All slice operations return a new list containing the requested elements. I.e it returns a shallow copy of the list.

	3. Assignment to slices is also possible and can even change the size of the list or clear it entirely.


## More List methods

1. List.__extend(_iterable_)__ -> Extends a list by appending all items from the _iterable_. Same as:
```
 _a[len(a):] = *iterable*_.

```

2. list.__insert(_i_, x)__ -> Insert an item at a given position. First argument is the index of the element before which to insert.

```
   a.insert(0, x) -> Inserts _x_ at the front of the list.
   a.insert(len(a), x) -> Inserts _x_ at the end of the list, so is similar to `a.append(x)`.
```

3. list.__remove(x)__ -> Removes first item from the list, whose value is equal to x. Returns a `ValueError` if there is no such value.

4. list.__pop([_i_]) -> Removes item at the given position in the list and returns it. If no index is specified, `list.pop()` removes and returns the last item in the list. Raises an `IndexError` if list is empty or index is outside the list range.

5. list.__clear()__ -> Removes all items from the list. Similar to `del list[:]`

6. list.__index(x[, start[, end]])__ -> 
	- Returns a zero-based index in the list of the first item whose value is equal to x. Raises a `ValueError` if there is no such item.
	- `start` and `end` arguments are optional, and are only used to limit the search parameters of th list.

7. list.__count(x)__ -> Return number of times _x_ appears in the list.

8. list.__sort(_*_, key=None, reverse=False)__ -> Sorts the items of the list in place. Arguments can be used for better customization.

9. list.__reverse()__ -> Reverse the elements of the list in place.

10. list.__copy()__ -> Return a shallow copy of the list. Similar to `list[:]`


## Using lists as stacks(LIFO).

- Through the list methods above, Lists can be implemented as stackS.
- To add an item, `list.append()` should surfice.
- To remove an item, `list.pop()` surfices. 

## Using lists as Queues(FIFO)

- First, lists are not very effective in implementing queues.
- It is however possible to use lists as queues, albeit with some painful experiences. Lol!
- Appending and poping from the end of the list is fast whereas insertions and pops from the beginning are very slow since all the elements have to be shifted by one.

- __NB:__ To implement a queue, it is advisable to use the `collections.deque` which is designed to have fast appends and pops from both ends of the list.

	```
		example:

			from collections import deque
		
			queue = deque(["Erick", "John", "Michael"])
			queue.append("Add_item")
			queue.append("Add-second_item")
			queue.popleft()
	```

## List comprehensions

- Is a concise way to make lists.
- Some common applications would involve making new lists where each element is the result of some operations applied to each member of another sequence or iterable.
- Another would be to create a subsequence of elements that satisfy a certain condition.

- Example, assuming we are to create a list of squares, we could go about it in three ways as demonstrated below:

```
1. 	squares = []
	for x in range(10):
		squares.append(x**2)

	
	This creates( or overwrites) a variable named x that still exists even after the loop completes.


2. We could also use:
		
	squares = list(map(lambda x: x**2, range(10)))

			equivalent to:
	squares = [x**2 for x in range(10)]  //More readable and concise.


3. List comprehension which consists of `brackets` containing an `expression` followed by a `for clause`, then zero or more for or `if clauses.`

   The result is a new list resulting from evaluating the expression in the context of the for and if clauses which follow it.

	[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y] 

			this creates a list of:

	[(1,3), (1,4), (2,3), (2,1), (2,4), (3,1), (3,4)]



	This is equivalent to:

		combs = []
		for x in [1,2,3]:
			for y in [3,1,4]:
				if x != y:
					combs.append((x, y))
```

## The del statement

- Removes an item from a list given its index instead of its value.
- Different from the pop() method in that it does not return a value.
- Can also be used to clear an entire list completely.


## Tuples and Sequences

- Sequence data types involve types that are arranged in order, support indexing and slicing operations, are either mutable or immutable etc. Examples include, Strings, Lists, range, tuples.

- A tuple consists of a comma seperated list e.g `t = 12345, 54321, 'hello!'`
- Tuples may be nested.
- Tuples are immutable, once created, their values cannot be changed. They can however contain mutable objects within the values, for instance in the case of nesting.
- Tuples are always outputed within brackets to distinguish the nested elements in case they are contained within the tuple. 
- an empty tuple is indicated using empty parenthese e.g `empty = ()`
- a tuple with a single item is indicated by the item followed by a comma. e.g `singleton = 'hello',


## Sets

- Is an unordered collection with no duplicate elements.
- Objects support mathematical operations like union, intersection, difference and symmetric difference.
