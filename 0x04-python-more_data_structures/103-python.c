#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <Python.h>

/**
* print_python_list - prints info about python lists.
* @p: address of PyObject struct.
*/
void print_python_list(PyObject *p)
{
	int index;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %lu\n", ((PyVarObject *)p)->ob_size);
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	index = 0;
	while (index < ((PyVarObject *)p)->ob_size)
	{
		printf("Element %d: %s\n", index,
			((PyListObject *)p)->ob_item[index]->ob_type->tp_name);
		if (!strcmp(((PyListObject *)p)->ob_item[index]->ob_type->tp_name, "bytes"))
			print_python_bytes(((PyListObject *)p)->ob_item[index]);
	index++;
	}
}

/**
* print_python_bytes - prints info about python lists.
* @p: address of pyobject struct.
*/
void print_python_bytes(PyObject *p)
{
	size_t index, len, size;
	char *str;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes"))
	{
		printf(" [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = ((PyVarObject *)p)->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;
	len = size + 1 > 10 ? 10 : size + 1;
	printf(" size: %lu\n", size);
	printf(" trying string: %s\n", str);
	printf(" first %lu bytes: ", len);
	index = 0;
	while (index < len)
	{
		printf("%02hhx%s", str[index], index + 1 < len ? " " : "");
		index++;
	}
	printf("\n");
}
