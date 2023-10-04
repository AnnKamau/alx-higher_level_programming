#include "lists.h"

/**
 * insert_node - inserts a number in a sorted linked list
 * @head: a pointer the head of the list
 * @number: the number insterted
 * Return: NULL if function fails otherwise pointer to new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *knew;

	knew = malloc(sizeof(listint_t));
	if (knew == NULL)
		return (NULL);
	knew->n = number;

	if (node == NULL || node->n >= number)
	{
		knew->next = node;
		*head = knew;
		return (knew);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	knew->next = node->next;
	node->next = knew;

	return (knew);
}
