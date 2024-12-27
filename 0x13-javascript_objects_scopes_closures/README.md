## JAVASCRIPT - Objects, Scopes and Closures

### Defining objects

```
	const person = {
		name: ["Bob", "Smith"],
		age: 32;
		bio: function () {
			console.log(`${this.name[0]} ${this.name[1]} is ${this.age} years old.`);
		     },
		introduceSelf: function () {
				 console.log(`Hi I'm ${this.name[0]}.`);
			       },
		};
```

- This code creates an object `person` with properties such as `name`, `age` and methods such as `bio` and `introduceSelf`.

- Properties are variables within an object in js and methods are the functions that act on these variables. Each member (both properties and methods) has a value attached to it, such as `32`, `Bob`, `bio()` etc.

- Each member must be seperated by a comma from the next member.
- A colon seperates every member from its value.

- This object `person` above is known as an `object literal` and is different from the objects instantiated from classes.

### Accessing object members
#### Dot notation

- Our object person above uses dot notation to access properties and methods, whereby the object name(person) acts as the `namespace` and must be entered first to access anything inside the object, followed by a dot and then the item to be accessed inside the object.

- Example:

```
	person.name;
	person.bio();
```

##### Objects as object properties

- Objects can be nested in such a manner that an object contains as property, another object. Example:

```
	const person = {
	  name: {
	    first: "Bob",
	    last: "Smith",
	  },
	  
	  age: 32,
	};
```

- To access this inner property, an extra dot suffices. example: `person.name.first;`

#### Bracket notation

- Provides an alternative way to access object properties.

- Example: 
```
	person["age"];
	person["name"]["first"];
```

- This is almost similar to array way of accessing values, only that instead of the index, you use the property name to access the value.

- For this reason, objects are sometimes called `associative arrays` since they map strings to values in the same way that arrays map numbers to values.

- dot notation is generally preffeered although there are instances where bracket notation is preffered over the dot notation. example scenario is where the object property name is held in a variable.


#### Setting object members

- Updating the value of object members is done by declaring the member to be set using either dot or bracket notation. Example:

```
	person.age = 45;
	person["name"]["last"] = "Cratchit";
```

- It is also possible to create completely new members. Example:

```
	person["eyes"] = "hazel";
	person.farewell = function () {
	  console.log("Bye everyone!");
        };
```

- An advantage of the bracket notation in setting the value is that it can be used to set not only member values dynamically but member names too. Say for instance users are to store values of their choice by obtaining the values from their input, one way to do this would be:

```
	const myDataName = nameInput.value;
	const myDataValue = nameInput.value;

	person[myDataName] = myDataValue;
```

- The above operation would not be possible with the dot notation especially since the dot notation which can only accept a literal member name, not a variable that points to a name.


### **_this_** Keyword

- `this` typically refers to the current object the code is being executed in.
- In the context of an object method, `this` refers to the object that the method was called on.
- the keyword allows the same method definition to work for multiple objects by only refering to the object on which a method is called.
-  Very useful when using `constructors` to create more than one object from a single object definition.
