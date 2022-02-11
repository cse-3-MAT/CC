#include <stdio.h>
#include<stdlib.h>
struct node{
    int data;
    struct node *next;
    int val;
};
struct node *head=NULL;
struct node *temp;
struct node *temp1;
void insert(int item){
    struct node *ptr=(struct node*)malloc(sizeof(struct node *));
    ptr->data =item;
    ptr->next=NULL;
    ptr->val=0;
    if (head==NULL){
        head=ptr;
    }
    else{
        temp->next=ptr;
    }
    temp=ptr;
    if(item==2){
        temp1=ptr;
    }
    if(item==10){
        ptr->next=temp1;
    }
    
}
/*void display(){
    struct node *dip=head;
    while(dip!=NULL){
        printf("%d ",dip->data);
        dip=dip->next;
        if(dip->data==10){
            break;
        }
        
    }
    printf("%d ",dip->data);
 
}*/
void find(){
    struct node *t=head;
    while(t!=NULL){
        if (t->val==1) {
            printf("Loop exists");
            return ;
        }
        t->val=1;
        t=t->next;
    }
    printf("loop doesn't exist ");
    return;
}
int main()
{
    insert(1);
    insert(2);
    insert(5);
    insert(8);
    insert(10);
    find();
    return 0; 
}