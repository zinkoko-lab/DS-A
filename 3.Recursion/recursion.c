#include <stdio.h>

int sqSum(int num) {
    int sum = num * num;
    if (num-1) {
        sum += sqSum(num-1);
    }
    return sum;
}

int main() {
    int result = sqSum(100);
    printf("%d\n", result);
    return 0;
}