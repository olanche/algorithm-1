#include <iostream>
#include<string>
using namespace std;

int main(void){
	string s;
	cin >> s;
	string tmp;
	int answer = 0;
	bool firstMinus = false;

	for(int i=0; i<=s.length(); i++){
		if(s[i] == '+' || s[i] == '-' || s[i] == '\0'){
			if(firstMinus){
				answer -= stoi(tmp);
			}else{
				answer += stoi(tmp);
			}

			if(s[i] == '-'){
				firstMinus = true;
			}
				

			tmp.clear();
			continue;
		}

		tmp += s[i];
	}

	cout << answer << "\n";
	return 0;
}
