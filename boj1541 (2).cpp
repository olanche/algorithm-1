#include<iostream>
#include<string>

using namespace std;

int main(void){
	string s;
	cin >> s;
	bool firstMinus = false;
	int answer =0; 
	string temp;
	for(int i=0; i<=s.length(); i++){
		if(  s[i] == '-' || s[i]=='+' || s[i] == '\0'      )
		{
			if(firstMinus== true){
				answer -= stoi(temp );
			}
			else{
				answer +=stoi(temp);
			}
			if(s[i] == '-'){
				firstMinus = true;
			}
			temp.clear();
			
		}
		else{
			temp = temp+s[i];
		}
		
		
	}
	
	cout<<answer;
	
	return 0;
}
