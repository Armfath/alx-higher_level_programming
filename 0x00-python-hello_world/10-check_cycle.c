#include "lists.h"
/**
 * check_cycle - checck if linked list has cycle
 *
 * @list: pointer to the list
 *
 * Return: 0 if list has not cycle 1 else
 */
int check_cycle(listint_t *list)
{
	listint_t *current;
	listint_t *temp;

	temp = list;
	while (list)
	{
		current = list->next;
		list = list->next;
		if (temp == current)
			return (1);
	}
	return (0);
}
