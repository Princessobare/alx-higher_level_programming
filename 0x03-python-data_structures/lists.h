#ifndef LISTS_H
#define LISTS_H

#include <stdio.h>
#include <stdlib.h>

/**
 * struct listint_s - this is the singly linked list
 * @n: represents an integer
 * @next: this points to the succeeding node
 * Description: this is for the singly linked list node structure
 */

typedef struct listint_s
{
	int n;
	struct listint_s *next;
}

listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);
int is_palindrome(listint_t **head);

#endif
