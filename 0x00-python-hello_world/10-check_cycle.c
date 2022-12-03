#include "lists.h"

/**
 * check_cycle - check if linked list has cycle or not
 * @list: linked list of integers
 * Return: 1 if linked list has cycle, 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *current = list;

	if (list == NULL || list->next == NULL)
		return (0);

	while (current != NULL)
	{
		listint_t *next = current->next;
		while (next != NULL)
		{
			if (next == current)
				return (1);
			next = next->next;
		}
		current = current->next;
	}

	return (0);
}

//  5         35          15       20       25        30       35

//  5         35          15       20       25        30       35

// next 	= 35
// current  = 5

// next = 15
// current  = 5

// next = 20
// current  = 5

// next = 25
// current  = 5

// next = 30
// current  = 5

// next = 35
// current  = 5