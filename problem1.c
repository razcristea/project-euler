#include <stdio.h>  
#include <time.h>  

void multiples(int num)
{
    double time_spent = 0.0;
    clock_t begin = clock();
    int sum = 0;
    for (int i = 0; i < num; i++)
    {
        if ( i % 3 == 0 || i % 5 == 0)
        {
            sum = sum + i;
        }
    }
    printf("[ Result of problem#1]: %d \n",sum); 
    clock_t end = clock();
    time_spent += (double)(end - begin) / CLOCKS_PER_SEC;
    printf("\nResult generated in %f milliseconds.\n", time_spent*1000);
}

int main()
{    
    int number;
    printf("[   Euler   problem#1] Enter number: ");    
    scanf("%d",&number);
    multiples(number);   
    return 0;  
}  


