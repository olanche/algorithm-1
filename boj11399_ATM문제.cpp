#include<iostream>
#include<algorithm>
using namespace std;

int main(void){
	int N;
	scanf( "%d", &N );
	int a[N];
	for(int i =0; i<N; i++){
		scanf("%d", &a[i]);
		
	}
	sort(  a, a+N     ); //인덱스가 앞에 있는 수부터 은행 상담을 시작한다 
	//버블 정렬
	int j,k, sum = 0;
	for(j=0; j<N; j++){
		for(k=0; k<=j; k++){
			sum += a[k];
			
			
			 
		}
	} 
	printf("%d", sum);
	
	
}
