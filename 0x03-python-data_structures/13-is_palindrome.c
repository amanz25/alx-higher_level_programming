#include <stddef.h>
#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - check if a linked list is a palindrome
 * @head: pointer to the first node
 *
 * Return: 1 (success) or 0 (failure)
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	int data[2048], count = 0, i, limit;

	if (head == NULL || *head == NULL)
		return (1);

	while (tmp != NULL)
	{
		data[count] = tmp->n;
		count++;
		tmp = tmp->next;
	}

	limit = (count % 2 == 0) ? count / 2 : (count + 1) / 2;
	i = 0;
	while (i < limit)
	{
		if (data[i] != data[count - 1 - i])
			return (0);
		i++;
	}
	return (1);
}
