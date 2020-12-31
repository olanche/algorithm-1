#include<iostream>

using namespace std;
int arr[15];  
int sum=0; 



int main(void){
	int N,k;
	scanf("%d", &N);
	scanf("%d", &k);
	
	for(int i=0; i<N; i++){
		scanf("%d", &arr[i]);
	}
	
	
	while(true ){
		int temp;
		int j=0;
		while(   arr[j] < k      ){
			temp = arr[j];
			j++;
			
		}
		
		sum += k/temp;
		
		k = k%temp;  
		
		if(k==0){
			break;
		}
		
		
		
	}
	
	
	
	printf("%d", sum);
	return 0;
}
