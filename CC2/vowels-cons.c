#include <stdio.h>
#include <stdlib.h>
#include<string.h>
struct node{
    char data;
    struct node *next;
};
struct node *head1,*head2,*temp1,*temp2;
void arrange(char ch){
    struct node *ptr=(struct node*)malloc(sizeof(struct node*));
    ptr->data=ch;
    ptr->next=NULL;
    if(ch=='a'|| ch=='e' || ch=='i' || ch=='o' || ch=='u'){
        if (head1==NULL){
            head1=ptr;
            temp1=ptr;
        }
        else{
            temp1->next=ptr;
            temp1=temp1->next;
        }
    }
    else{
        if (head2==NULL){
            head2=ptr;
            temp2=ptr;
        }
        else{
             temp2->next=ptr;
            temp2=temp2->next;
        }
    }
}
void display(struct node* head){
    struct node *temp=head;
    while(temp->next!=NULL){
        printf("%c ",temp->data);
        temp=temp->next;
    }
    printf("%c ",temp->data);
}
int main() {
	char ch;
	int n,t,i,j;
	printf("Enter no of testcases : ");
	scanf("%d",&t);
	for(i=0;i<t;i++){
	    printf("Enter the value of n : ");
	    scanf("%d",&n);
	    for(j=0;j<n;j++){
	        scanf(" %c",&ch);
	        arrange(tolower(ch));
	    }
	    if (head1!=NULL){
	    temp1->next=head2;
	    display(head1);
	    }
	    else{
	         display(head2);
	    }
	    printf("\n");
	    head1=NULL;
	    head2=NULL;
	    temp1=NULL;
	    temp2=NULL;
	}
}

