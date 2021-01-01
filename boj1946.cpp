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
		cin>>N; //지원자의 숫자
		struct Stu a[N];
		for(int j=0; j<N; j++){
			cin >> a[j].s1 >> a[j].s2;
		} //점수 배정한 상태 
		
		int sum = 0;
		
		for(int i=0; i<N; i++){
			
			
			for(int j=0; j<N; j++){
				if(j == i){
					continue;
				}
				
				else{
					if( a[i].s1>a[j].s1 && a[i].s2>a[j].s2   ){
						//result[i] =  뭘 대입해야 되는거지???;
						sum+=1;
					} 
					else{
						continue;
					}
					
					
					/*a[i] 의 1차점수와 a[j] 의 1차 점수를 비교한다 ->
					a[i] 의 2차점수와 a[j] 의 2차 점수를 비교한다
					
					a[i] 의 순위가 모두 a[j] 의 순위보다 크다면 a[i] 는 탈락한다 <- array가 하나 더 만들어서 1 또는 0을 넣고  나중에 1의 갯수를 출력한다 
					*/
				}
			
			}
			
		} 
		cout << sum << endl;
	
	}
	
	
	
	return 0;
}
