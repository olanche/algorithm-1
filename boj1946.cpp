#include<iostream>

using namespace std;

struct Stu{
	int s1;
	int s2;
};

int main(void){
	
	int T;
	cin>>T;
	for(int i=0; i<T; i++){
		int N;
		cin>>N; //�������� ����
		struct Stu a[N];
		for(int j=0; j<N; j++){
			cin >> a[j].s1 >> a[j].s2;
		} //���� ������ ���� 
		
		int sum = 0;
		
		for(int i=0; i<N; i++){
			
			
			for(int j=0; j<N; j++){
				if(j == i){
					continue;
				}
				
				else{
					if( a[i].s1>a[j].s1 && a[i].s2>a[j].s2   ){
						//result[i] =  �� �����ؾ� �Ǵ°���???;
						sum+=1;
					} 
					else{
						continue;
					}
					
					
					/*a[i] �� 1�������� a[j] �� 1�� ������ ���Ѵ� ->
					a[i] �� 2�������� a[j] �� 2�� ������ ���Ѵ�
					
					a[i] �� ������ ��� a[j] �� �������� ũ�ٸ� a[i] �� Ż���Ѵ� <- array�� �ϳ� �� ���� 1 �Ǵ� 0�� �ְ�  ���߿� 1�� ������ ����Ѵ� 
					*/
				}
			
			}
			
		} 
		cout << sum << endl;
	
	}
	
	
	
	return 0;
}
