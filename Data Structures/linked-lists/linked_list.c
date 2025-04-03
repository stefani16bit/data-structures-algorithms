#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    char data;
    struct node *link;
} *ptr;

void addNextNode(ptr list, char data) {
    ptr currentNode = list;
    while (currentNode->link != NULL) {
        currentNode = currentNode->link;
    }
    
    currentNode->data = data;
    currentNode->link = malloc(sizeof(struct node));
}

void printList(ptr list) {
    ptr currentNode = list;
    do {
        printf("%c", currentNode->data);
        currentNode = currentNode->link;
    } while (currentNode->link != NULL);
}

int main()
{
    ptr list = malloc(sizeof(struct node));
    addNextNode(list, 'S');
    addNextNode(list, 'T');
    addNextNode(list, 'E');
    addNextNode(list, 'F');
    addNextNode(list, 'A');
    addNextNode(list, 'N');
    addNextNode(list, 'I');
    printList(list);
    return 0;
}
