#include "lists.h"

/**
 * is_palindrome - check if linked list is palindrome or not
 * @head: first element in the linked list
 */

int is_palindrome(listint_t **head)
{
    listint_t *list = *head;
    listint_t *last = list;
    listint_t *next;

    while (last != NULL)
    {
        last = last->next;
    }

    if (list == NULL)
        return 1;
    else if (list->n != last->n)
        return 0;
    else
    {
        
    }
}

//   5     7     8      9      15      9       8      7      5

//   racecar
//

// raceycar

// kitkat