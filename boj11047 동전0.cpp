#include<iostream>

using namespace std;
int arr[15]; //�迭�� ���� ������ �����ؾ��� 
int sum=0; //�̰��� ������ش� �������� 
void function(int start){
	int i=0; int temp;
	int a,b;
	while(   arr[i]  <start  ){
		temp = arr[i]; /*�� �������� �߿��� �κ��ε� ..... start���ٴ� ���� �׼��� �� ���� ū���� temp�� �ְ� �װɷ� ����Ѵ�*/
		i++;
	}
	a = start % temp;
	b = start/temp;
	sum += b;
	if(a == 0) return;   
	
	function(a);  //��� �Լ��� ����ϴ� �����̴� 
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
