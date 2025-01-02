## JAVASCRIPT - OBJECTS, SCOPES and CLOSURES

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



### Constructors

- Are very useful when creating multiple objects. Saves the time that could have otherwise been spent in creating multiple objects using the `object literal` way, whereby all objects are typed one after the other.

- Sort of provides an automatic way of creating multiple objects from a single definition.

- Also allows for updating multiple objects at once.

- A `constructor` is simply a function that is called using the `new` keyword.

- When called, a constructor;
	1. Creates a new object
	2. Binds `this` keyword to the new object, so its available for use with the objects created
	3. Run the code in the constructor(function that is called using `this` keyword)
	4. Return the new object.

- By convention, constructors start with a capital letter and are named for the type of object. Example:

```
	function person(name) {
	  this.name = name;
	  this.introduceSelf = function () {
	    console.log(`Hi! I'm ${this.name}.`);
	  };
	}


	const salva = new person("Salva");   // Creates a person object with name value of Salva

```


## CLASSES AND CONSTRUCTORS

- A class is a template for creating objects and is declared using the `class` keyword.

- Classes can be defined in two ways:

	1. **Class declaration:** 

```
	class rectangle {
	  constructor(height, width) {
	    this.height = height;
	    this.width = width;
	  }
	}
```

	2. **Class expression:**

```
	const rectangle = class {
	  constructor(height, width) {
	    this.height = height;
	    this.width = width;
	  }
	}
```

- The above code creates a class called `rectangle` with: a `height`and `width` property, a constructor that takes `height` and `width` parameter that is used to initialize the new object's height and width properties.

- Class fields such as height and width are not variables and therefore keywords such as `const` are not used in declaring them.

- It is also possible to initialize properties with a default value so that when an object of the said class is created, the property is initialized with a default value.

- The constructor works just like a constructor defined outside a class definition.[ `See constructor section above` ](#Constructors)

- Given that a class provides a template to create new objects of the same type, creating a new instance of the same object just requires the use of `new` keyword. Example:

```
	const square = new rectangle(10, 10);
```

- **_NOTE_** - If no special initialization is necessary, it is possible to omit the constructor and a default constructor will be generated instead.
- There can only be one method with the identifier `constructor` within a given class.



### Inheritance

- The `extends` keyword is used to indicate that a class inherits from another class. Example:

```
	class professor extends person {
	  teaches;

	  constructor(name, teaches) {
	    super(name);
	    this.teaches = teaches;
	  }

	  introduceSelf() {
	    console.log(`My name is ${this.name} and I will be your ${this.teaches} professor.`);
	  }
```

- In the new class that inherits from the other, only the newly added properties need to be declared.

- In this scenario, the professor class is known as a `subclass` of the `person` class.

- If a subclass has any of its own initializations to do, it must first call the `superclass` constructor using `super()`, passing any parameters that the superclass constructor is expecting.

- The `super` keyword calls the constructor of the super class.




### ENCAPSULATION

- Private data properties must be declared in the class declaration starting with `#`. 

- Private properties have one restriction, in that all property names declared in the same class must be unique. Whereas with public properties, they can exist with the same name and the last one overwrites the others before it.

- Private properties cannot be accessed outside the class and provisions for a way to hide certain properties of an object. Example:

```
	class student extends person {
	  #year         //private member

	  constructor(name, year) {
	    super(name);
	    this.#year = year;
	  }


	// With this code, trying:

		const summert = new student("summers", 2);
	   	summers.#year;    //results into a syntax error since year is private and cannot be accessed outside of the class declaration.

```


#### Private methods

- just like private data properties, their names start with a `#` and they can only be called by the object's own methods. Example:

```
	class example {
	  somePublicMethod() {
		this.#somePrivateMethod();
	  }

	  #somePrivateMethod() {
	    console.log("You called me ?");
	  }
	}
```


### Static methods and fields

- `static` keyword defines a static method or field for a class. These fields or methods are defined on the class itself instead of each instance of the class.

- Static methods are often used to create utility functions for an application

- Static filds are useful for `caches`, `fixed-configuration` or any other data that doesn't need to be replicated across all instances.


## Closures

- a combination of functions bundled together(enclosed) with references to its surrounding state(lexical environment).

- Gives a function access to its outer scope.

- in JS, created everytime a function is created, at creation time.

### Lexical scope

- `lexical` scoping uses the location where a variable is declared within the source code to determine where that variable is available.

- for instance, nested functions have access to variables declared in their outer scope.

- Example:

```
	function init () {
	  var name = 'Mozilla';    //name is local to init()
	  function displayName () {
	    //is an inner function, that forms a closure.
	    console.log(name);  //Uses a variable declared in the parent function.
	  }
	  displayName();
	}
	init();
```

- In this example, the inner function displayName() has no local variables of its own, but is able to access the variables(name) of the outer scope within the closure.

### Scoping with `let` and `cost`

- `var` can either create a `function-scoped` or a `global-scoped` variable, depending on whether the variable is declared within a function or outside a function(global) within the source code.

- It is imperative however to note that in JS, blocks like the if statement do not create any scoping and therefore using var within such blocks result into a global-scoping and this could result into unintended behaviour.

- In order to create block-scoped variables, in JS, use `let` and `const` declarations.

#### Closure scope chain

- A nested function's access to the outer function's scope includes the enclosing scope of the outer function - effectively creating a chain of function scopes.
