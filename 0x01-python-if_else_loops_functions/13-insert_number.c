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

	if (node == NULL || node->n > number)
	{
		curr->n = number;
		curr->next = NULL;
		*head = curr;
	}

	while (node != NULL)
	{
		if (node->n > number)
		{
			curr->n = number;
			old->next = curr;
			curr->next = node;
			break;
		}
		else
			old = node;
		node = node->next;
	}

	if (!curr->n)
	{
		curr->n = number;
		curr->next = NULL;
		old->next = curr;
	}

	return (*head);
}
