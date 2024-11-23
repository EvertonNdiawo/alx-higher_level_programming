#include "lists.h"
#include <stdio.h>

/**
 * print_python_list_info - Prints basic info about python lists.
 * @p: A PyObject pointer representing a Python list.
 *
 * Description: Prints the size of the list, the memory allocated, and the
 *              type of each element in the list.
 *
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, allocated, i;
	PyObject *item;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "Error: Object is not a Python list.\n");
		return;
	}

	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;


	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
