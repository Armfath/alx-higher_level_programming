#include "lists.h"
/**
 * insert_node - insert node in a shoerted linked list
 *
 * @head: pointer to the list
 * @number: num to insert
 *
 * Return: pointer to the new list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *temp, *current;
	int end = 0;

	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}
	new->n = number;
	if (number <= current->n)
	{
		new->next = current;
		(*head) = new;
		return (*head);
	}
	while (number > current->n && current->next != NULL)
	{
		temp = current;
		current = current->next;
		if (current->next == NULL)
		{
			end = 1;
			break;
		}
	}
	if (end == 1 && number > current->n)
	{
		add_nodeint_end(head, number);
		return (*head);
	}
	temp->next = new;
	new->next = current;
	return (*head);
}
