#include "lists.h"
/**
 * traverse_check - traverses a list and checks if it's a cycle list
 * @head : headnode
 * Return: 0 if no cycle 1 if cycle
 */
int traverse_check(listint_t *head)
{
	listint_t *current = head;

	while (current != NULL)
	{
		current = current->next;
		if (current == head)
		{
			return (1);/*cycle*/
		}
	}
	return (0);
}
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list : the linked list starting point to check
 * Return: 0 IF NO CYCLE 1 IF CYCLE
 */
int check_cycle(listint_t *list)
{
	if (!list)
	{
		return (0);
	}
	return (traverse_check(list));
}
