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
	//a�� ������������ �����Ѵ�
	//���� ū �߷��� �� �� �ִ� ������ ������ ����Ѵ�  �� ���信�� �����Ѵ� 
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
