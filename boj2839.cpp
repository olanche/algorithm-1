#include<iostream>
using namespace std;

int main(void){
	int N;
	int temp = 10000;
	scanf("%d", &N);
	
	if(N%5 == 0){
		cout << N/5 ;
	}
	else{
		temp = N/5; //11의 경우를 생각하자 
	    
		while( temp>=0  ){
		    
			if(  ( N - (temp*5) ) %3  == 0 ){
			    cout <<  ( ( N - (temp*5) ) /3) + temp;
			    break;
		    }
		    temp --;
		
	    }
		
		
		
		
	}
	if(temp == -1){
		cout << -1;
	}
	
	
	return 0;
}
