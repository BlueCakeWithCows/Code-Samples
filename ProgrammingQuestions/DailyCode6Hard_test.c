
#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>
#include "DailyCode6Hard.c"
#include <assert.h>

  int list_test() {
    XOR_linked_list_bt * list = calloc(1, sizeof(XOR_linked_list_bt));
    if (list == NULL) {
      return -1;
    }

    add(list, 3);
    add(list, 4);
    add(list, 5);

    assert(get(list, 0) == 3);
    assert(get(list, 1) == 4);
    assert(get(list, 2) == 5);
    assert(get(list, 3) == 0);
  }

int main(int argc, char * argv[]) {
  list_test();
}