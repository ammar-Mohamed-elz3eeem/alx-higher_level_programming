#include "lists.h"

/**
 * check_cycle - check if linked list has cycle or not
 * @list: linked list of integers
 * Return: 1 if linked list has cycle, 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *current = list;
	listint_t *next;

	if (list == NULL || list->next == NULL)
		return (0);

	while (current != NULL)
	{
		next = current->next;
		while (next->next != NULL)
		{
			if (next == current)
				return (1);
			next = next->next;
			printf("next->n = %d\n", next->n);
			printf("current->n = %d\n", current->n);
		}
		current = current->next;
	}

	return (0);
}
