#include <stdio.h>
void update(int *a,int *b){
    printf("%d\n",*a+*b);
    if (*a>*b) printf("%d",*a-*b);
    else printf("%d",*b-*a);
}
int main()
{
    int a,b;
    scanf("%d",&a);
    scanf("%d",&b);
    printf("\n")
    update(&a,&b);
    return 0;
}
