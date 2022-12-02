#include "lists.h"

/**
 * insert_node - insert node in sorted order
 * @head: pointer to linked list
 * @number: number to be added to the list
 * Return: the linked list after insertion
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head;
	listint_t *old;
	listint_t *curr;

	curr = malloc(sizeof(listint_t));

	if (node == NULL)
	{
		node->n = number;
		node->next = NULL;
		return node;
	}

	while (node != NULL)
	{
		if (node->n > number)
		{
			curr->n = number;
			printf("curr->n = %d\n", curr->n);
			old->next = curr;
			curr->next = node;
			break;
		}
		else
		{
			old = node;
		}
		node = node->next;
	}
}
