#include <stdio.h>
void updateVar(int *val){
    *val+=10;
}
int main()
{
    int t,n;
    scanf("%d",&t);
    for(int i=0;i<t;i++){
        scanf("%d",&n);
        updateVar(&n);
        printf("%d\n",n);
        n=0;
    }
    return 0;
}
