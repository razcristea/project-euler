#include <stdio.h>
#include <time.h>

void evenfibsum(num)
{
    double time_spent = 0.0;
    clock_t begin = clock();
    int a = 1;
    int b = 2;
    int sum = 0;
    while (a < num || b < num)
    {
        if (a % 2 == 0)
        {
            sum = sum + a;
        } else if (b % 2 == 0)
        {
            sum = sum + b;
        }

        a = a + b;
        b = b + a;
    } 
    printf("[ Result of problem#2]: %d \n",sum);
    clock_t end = clock();
    time_spent += (double)(end - begin) / CLOCKS_PER_SEC;
    printf("\nResult generated in %f milliseconds.\n", time_spent*1000);
}


int main()
{    
    int number;
    printf("[   Euler   problem#2] Enter number: ");    
    scanf("%d", &number);
    evenfibsum(number);   
    return 0;  
}  