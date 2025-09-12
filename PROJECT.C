#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_STACK 100
#define MAX_URL_LEN 255   /* smaller buffer for Turbo C++ safety */

typedef struct {
    char *items[MAX_STACK];
    int top;
} Stack;

void init_stack(Stack *s) {
    s->top = -1;
}

int is_empty(Stack *s) {
    return (s->top == -1);
}

int is_full(Stack *s) {
    return (s->top == MAX_STACK - 1);
}

char *my_strdup(const char *s) {
    char *p;
    int len;
    len = strlen(s);
    p = (char *) malloc(len + 1);
    if (p == NULL) {
        return NULL;
    }
    strcpy(p, s);
    return p;
}

void push(Stack *s, const char *str) {
    char *copy;
    if (is_full(s)) {
        printf("Stack overflow, can't push '%s'\n", str);
        return;
    }
    copy = my_strdup(str);
    if (copy == NULL) {
        printf("Memory allocation failed in push()\n");
        return;
    }
    s->top = s->top + 1;
    s->items[s->top] = copy;
}

char *pop(Stack *s) {
    char *res;
    if (is_empty(s)) {
        return NULL;
    }
    res = s->items[s->top];
    s->items[s->top] = NULL;
    s->top = s->top - 1;
    return res;
}

void clear_stack(Stack *s) {
    char *p;
    while (!is_empty(s)) {
        p = pop(s);
        free(p);
    }
}

void print_stack(Stack *s) {
    int i;
    if (is_empty(s)) {
        printf("[]\n");
        return;
    }
    printf("[");
    for (i = 0; i <= s->top; i = i + 1) {
        printf("%s", s->items[i]);
        if (i < s->top) {
            printf(", ");
        }
    }
    printf("]\n");
}

int valid_url(const char *url) {
    const char *p;
    if (strncmp(url, "http://", 7) == 0) {
        p = url + 7;
    }
    else if (strncmp(url, "https://", 8) == 0) {
        p = url + 8;
    }
    else {
        return 0;
    }
    while (*p != '\0') {
        if (*p == '.') {
            return 1;
        }
        p = p + 1;
    }
    return 0;
}

int main(void) {
    Stack back, forward;
    char current[MAX_URL_LEN + 1];
    char input[MAX_URL_LEN + 1];
    int choice;
    char *tmp;

    init_stack(&back);
    init_stack(&forward);

    strcpy(current, "Home");

    while (1) {
        printf("\nCurrent Page: %s\n", current);
        printf("Back History: ");
        print_stack(&back);
        printf("Forward History: ");
        print_stack(&forward);

        printf("\nMenu:\n");
        printf("1. Visit Page\n");
        printf("2. Go Back\n");
        printf("3. Go Forward\n");
        printf("4. Exit\n");
        printf("Enter choice: ");
        
        if (scanf("%d", &choice) != 1) {
            /* clear input buffer */
            while (getchar() != '\n');
            printf("Invalid input. Please enter a number.\n");
            continue;
        }
        /* consume leftover newline */
        while (getchar() != '\n');

        if (choice == 1) {
            int len_input;
            printf("Enter URL (include http:// or https://): ");
            if (fgets(input, sizeof(input), stdin) == NULL) {
                continue;
            }
            /* strip newline at end if present */
            len_input = strlen(input);
            if (len_input > 0 && input[len_input - 1] == '\n') {
                input[len_input - 1] = '\0';
            }
            if (strlen(input) == 0) {
                printf("Please enter a URL.\n");
                continue;
            }
            if (!valid_url(input)) {
                printf("Invalid URL format. Try again.\n");
                continue;
            }
            push(&back, current);
            clear_stack(&forward);
            /* copy input into current */
            strncpy(current, input, MAX_URL_LEN);
            current[MAX_URL_LEN] = '\0';
        }
        else if (choice == 2) {
            char *prev;
            if (is_empty(&back)) {
                printf("No pages in back history.\n");
            } else {
                push(&forward, current);
                prev = pop(&back);
                if (prev != NULL) {
                    strncpy(current, prev, MAX_URL_LEN);
                    current[MAX_URL_LEN] = '\0';
                    free(prev);
                }
            }
        }
        else if (choice == 3) {
            char *next;
            if (is_empty(&forward)) {
                printf("No pages in forward history.\n");
            } else {
                push(&back, current);
                next = pop(&forward);
                if (next != NULL) {
                    strncpy(current, next, MAX_URL_LEN);
                    current[MAX_URL_LEN] = '\0';
                    free(next);
                }
            }
        }
        else if (choice == 4) {
            printf("Exiting...\n");
            break;
        }
        else {
            printf("Invalid choice, try again.\n");
        }
    }

    clear_stack(&back);
    clear_stack(&forward);
    return 0;
}
