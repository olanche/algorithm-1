#include<iostream>
#include<algorithm>
using namespace std;

bool compare(int x, int y){
	return x>y;
}

int main(void){
	int N;
	cin >> N;
	int a[N];
	for(int i=0; i<N; i++){
		cin >> a[i];
	}
	//a를 내림차순으로 정렬한다
	//제일 큰 중량을 들 수 있는 로프는 무조건 사용한다  는 개념에서 착안한다 
	sort(a,a+N, compare);
	
	int w[N];
	
	for(int i=0; i<N; i++){
		w[i] = (i+1)  *   a[i] ;
	}
	
	int max =0 ;
	for(int i=0; i<N; i++ ){
		if( w[i] > max   ){
			max = w[i];
		}
	}
	printf("%d", max);
	return 0;
}
