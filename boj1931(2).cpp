#include<iostream>
#include<algorithm>
using namespace std;
struct Time{
		long long s;
		long long f;
	};

bool compare( Time &t1, Time&t2){
	if(t1.f==t2.f){
		return t1.s < t2.s;
	}
	else{
		return t1.f < t2.f;
	}
}

int main(void){
	
	
	int N;
	cin>>N;
	struct Time a[N];
	for(int i=0; i<N; i++){
		cin >> a[i].s >> a[i].f;
	}
	sort(a, a+N, compare);
	long long start = a[0].f;
	int sum = 1;
	for(int i=1; i<N; i++){
		if(start <= a[i].s){
			sum++;
			start = a[i].f;
		}
	}
	printf("%d", sum);
	return 0;
}
