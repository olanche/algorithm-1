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
	sort(  a, a+N     ); //�ε����� �տ� �ִ� ������ ���� ����� �����Ѵ� 
	//���� ����
	int j,k, sum = 0;
	for(j=0; j<N; j++){
		for(k=0; k<=j; k++){
			sum += a[k];
			
			
			 
		}
	} 
	printf("%d", sum);
	
	
}
