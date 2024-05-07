#include<stdio.h>
int main(){
int day;
printf("Enter the day(1-7):");
scanf("%d",&day);

 switch(day){
 case 1:printf("monday:\n");
 break;
 case 2:printf("tuesday\n");
 break;
 case 3:printf("wednesday\n");
 break;
 case 4:printf("thursday\n");
 break;
 case 5:printf("friday\n");
 break;
 case 6:printf("saturday\n");
 break;
 case 7:printf("sunday\n");
 break;
 default:printf("Not a valid day!\n");
 }
return 0;
}
