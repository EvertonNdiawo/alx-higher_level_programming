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

		squares[-3:] #Slicing -> Returns a new list containing the last 3 items.

	```

2. Lists support concatenation operations:

	```
		Example:

		squares + [36, 49, 64, 81, 100]

		This would returns a result containing all items contained in the `squares` list and the new items. 

		i.e [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

	```

3. listname***.append(item)*** -> Adds a new item at the end of the specified list.
	
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
