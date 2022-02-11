#include <stdio.h>
#include <stdlib.h>
#include<string.h>
struct node{
    int data;
    struct node *next;
};





struct node *head,*last,*temp;


void insert(int item){
    struct node *ptr=(struct node*)malloc(sizeof(struct node *));
    ptr->data =item;
    ptr->next=NULL;
    if (head==NULL){
        head=ptr;
    }
    else{
        temp->next=ptr;
    }
    temp=ptr;
}




void rotate(int k){
    
    for(int i=0;i<k;i++){
        last=head;
        while(last->next!=temp){
            last=last->next;
        }
        last->next=NULL;
        temp->next=head;
        head=temp;
        temp=last;
    }
}



void display(){
    struct node *temp1=head;
    while(temp1->next!=NULL){
        printf("%d ",temp1->data);
        temp1=temp1->next;
    }
    printf("%d ",temp1->data);
}



int main(){
    int k;
    insert(1);
    insert(2);
    insert(5);
    insert(8);
    insert(10);
    display();
    printf("\n");
    scanf("%d",&k);
    rotate(k);
    display();
    return 0;
}