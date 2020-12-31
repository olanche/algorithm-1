#include<iostream>

using namespace std;
int arr[15]; //배열을 전역 변수로 설정해야할 
int sum=0; //이값을 출력해준다 마지막에 
void function(int start){
	int i=0; int temp;
	int a,b;
	while(   arr[i]  <start  ){
		temp = arr[i]; /*이 문제에서 중요한 부분인데 ..... start보다는 작은 액수들 중 가장 큰값을 temp에 넣고 그걸로 계산한다*/
		i++;
	}
	a = start % temp;
	b = start/temp;
	sum += b;
	if(a == 0) return;   
	
	function(a);  //재귀 함수를 사용하는 문제이다 
}

int main(void){
	int N,k;
	scanf("%d", &N);
	scanf("%d", &k);
	
	for(int i=0; i<N; i++){
		scanf("%d", &arr[i]);
	}
	
	function(k);
	printf("%d", sum);
	return 0;
}
