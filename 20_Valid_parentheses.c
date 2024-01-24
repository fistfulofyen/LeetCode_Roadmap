#include <stdio.h>
#include <math.h>
#include <stdbool.h>
#include <stdlib.h>

struct Node {
    char val;
    struct Node* next;
};

struct Stack {
    struct Node* head;
    size_t len;
};

struct Node* Node(char val, struct Node* next) {
    struct Node* root = (struct Node*)malloc(sizeof(struct Node));
    root -> next = next;
    root -> val = val; 
    return root; 
}

struct Stack* Stack() {
    struct Stack* stack = (struct Stack*)malloc(sizeof(struct Stack));
    stack -> len = 0;
    stack -> head = NULL;
    return stack;
}

void append(struct Stack* stack, char val) {
    struct Node* node = Node(val, stack -> head); 
    stack -> head = node;
    stack -> len += 1;
}

char pop(struct Stack* stack) {
    if (stack -> head == NULL) {
        return NULL;
    }
    char val = stack -> head -> val;
    struct Node* deleteNode = stack -> head;
    stack -> head = stack -> head -> next;
    stack -> len -= 1;
    free(deleteNode);
    return val;
}

void freeStack(struct Stack* stack) {
    while (pop(stack) != NULL) {
        pop(stack);
    }
    free(stack);
}

char opposite_parenthesis(char closing) {
    char opening = NULL;
    if (closing == ')') {
        opening = '(';
    } else if (closing == '}') {
        opening = '{';
    } else if (closing == ']') {
        opening = '[';
    }
    return opening;
}

bool isValid(char * s){
    
    struct Stack* stack = Stack();
    char* chr;
    
    for (chr = s; *chr != '\0'; chr++) {
        if (opposite_parenthesis(*chr) == NULL) {
            append(stack, *chr);
        } else if (stack -> len != 0 && opposite_parenthesis(*chr) == pop(stack)) {
            continue;
        } else {
            return false;
        }
    }
    bool result = stack -> len == 0;
    freeStack(stack);
    return result;
}

int main(){
    // Test 1: Valid string
    char test1[] = "({[]})";
    if (isValid(test1)) {
        printf("Test 1 Passed: %s is a valid string.\n", test1);
    } else {
        printf("Test 1 Failed: %s is not a valid string.\n", test1);
    }

    // Test 2: Invalid string
    char test2[] = "{[}]";
    if (!isValid(test2)) {
        printf("Test 2 Passed: %s is not a valid string.\n", test2);
    } else {
        printf("Test 2 Failed: %s is a valid string.\n", test2);
    }

    // Test 3: Empty string
    char test3[] = "";
    if (isValid(test3)) {
        printf("Test 3 Passed: %s is a valid string.\n", test3);
    } else {
        printf("Test 3 Failed: %s is not a valid string.\n", test3);
    }

    // Test 4: String with other characters
    char test4[] = "a(b{c}d)e";
    if (isValid(test4)) {
        printf("Test 4 Passed: %s is a valid string.\n", test4);
    } else {
        printf("Test 4 Failed: %s is not a valid string.\n", test4);
    }

    return 0;
}
