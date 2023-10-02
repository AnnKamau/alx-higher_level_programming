#incude "lists.h"

/**
 * check_cycle - checks if linked list has a cycle
 * @list: linked list for checking
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *low = list;
	listint_t *flow = list;

	if (!list)
		return (0);

	while (low && flow && flow->next)
	{
		low = low->next;
		flow = flow->next->next;

		if (low == flow)
			return (1);
	}
	return (0);
}
