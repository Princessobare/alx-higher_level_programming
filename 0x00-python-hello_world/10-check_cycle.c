#include "lists.h"

/**
 * check_cycle - check for cycle in linked list
 * @list: the linked list to be checked
 *
 * Return:returns 1 if list has cycle, else 0
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
