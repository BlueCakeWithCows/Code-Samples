/***
An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.
*/

#include <malloc.h>
#include <stdint.h>

  typedef struct XOR_node_bt_ {
    int element;
    void * xor_pointer;
  }
XOR_node_bt;

typedef struct XOR_linked_list_bt_ {
  int length;
  XOR_node_bt * XOR_NODE;
}
XOR_linked_list_bt;

int add(XOR_linked_list_bt * , int element);
int get(XOR_linked_list_bt * , int index);

int add(XOR_linked_list_bt * linked_list, int element) {
  if (linked_list == NULL) {
    return 1;
  }
  XOR_node_bt * new_node = malloc(sizeof(XOR_node_bt));
  new_node -> element = element;

  linked_list -> length++;

  if (linked_list -> XOR_NODE == 0) {
    new_node -> xor_pointer = (void * ) linked_list;
    linked_list -> XOR_NODE = new_node;
    return 0;
  }

  XOR_node_bt * current_node = linked_list -> XOR_NODE;
  void * last_node = (void * ) linked_list;
  while (current_node != 0) {
    if (current_node -> xor_pointer == last_node) {
      current_node -> xor_pointer = (XOR_node_bt * )((uintptr_t) last_node ^ (uintptr_t) new_node);
      new_node -> xor_pointer = current_node;
      break;
    }
    XOR_node_bt * tmp = current_node;
    current_node = (XOR_node_bt * )((uintptr_t) current_node -> xor_pointer ^ (uintptr_t) last_node);
    last_node = (void * ) tmp;
  }
  return 0;
}

int get(XOR_linked_list_bt * linked_list, int index) {
  if (linked_list == NULL) {
    return 0;
  }

  if (index < 0) {
    return 0;
  }
  if (index >= linked_list -> length) {
    return 0;
  }

  XOR_node_bt * current_node = linked_list -> XOR_NODE;
  void * last_node = linked_list;
  while (index > 0 && current_node != 0) {
    XOR_node_bt * tmp = current_node;
    current_node = (XOR_node_bt * )((uintptr_t) current_node -> xor_pointer ^ (uintptr_t) last_node);
    last_node = (void * ) tmp;
    index--;
  }
  return current_node -> element;
}