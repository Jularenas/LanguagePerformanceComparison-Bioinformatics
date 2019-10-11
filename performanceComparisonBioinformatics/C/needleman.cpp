#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;

const int gap=2;
const int mut=1;
int needleman(string,string);
int minF(int,int);

int main (int argc, char** argv) {
	

	string preFile1="fastaFiles/";
	preFile1+=argv[1];
	const char *f1 = preFile1.c_str();
    
	std::stringstream ss;
	string line;
	ifstream myfile (f1);
	if (myfile.is_open())
	{
		int i=0;
		while ( getline (myfile,line) )
		{
		  if(i==0){
		  		i++;	
			}
			else{
				ss << line ;
			}
		}
		myfile.close();
	}
	else cout << "Unable to open file"; 
	std::string s1 = ss.str();
	//cout<<s1<<"\n";
	
	
	string preFile2="fastaFiles/";
	preFile2+=argv[2];
	const char *f2 = preFile2.c_str();
	
	std::stringstream ss2;
	string line2;
	ifstream myfile2 (f2);
	if (myfile2.is_open())
	{
		int i=0;
		while ( getline (myfile2,line2) )
		{
			if(i==0){
		  		i++;	
			}
			else{
				ss2 << line2 ;
			}
		}
		myfile2.close();
	}
	else cout << "Unable to open file"; 
	
	int m=minF(1,2);
	std::string s2 = ss2.str();
	//cout<<s2<<"\n";
	int score=needleman(s1,s2);
	cout<<score;
	int val=std::min(1,2);
	//cout<<val;
	return score;
}

int needleman(string s1,string s2){
	int len1=s1.length()+1;
	int len2=s2.length()+1;
	int matrizDinamica[len1][len2];
	
	for(int i=0;i<s1.length()+1;i++){
		for(int j=0;j<s2.length()+1;j++){
			matrizDinamica[i][j]=0;
		}
	}	
	
	for(int i=0;i<len1;i++){
		matrizDinamica[i][0]=i*gap;
		
	}
	
	for(int i=0;i<len2;i++){
		matrizDinamica[0][i]=i*gap;
	
	}
	
	for (int i=0;i<len1;i++){
		for (int j=0;j<len2;j++){
			int upVal=matrizDinamica[i-1][j];
			int leftVal=matrizDinamica[i][j-1];
			int diagVal=matrizDinamica[i-1][j-1];
			
			int costUp=upVal+2;
			int costLeft=leftVal+2;
			int costDiag=diagVal;
			if(s1[i-1]!=s2[j-1]){
				costDiag=costDiag+1;
			}
			int min1=std::min(costDiag,costUp);
			int min2=std::min(min1,costLeft);
			if(min2>0){
				matrizDinamica[i][j]=min2;
			}
		}
	}
	return matrizDinamica[len1-1][len2-1];
}

int minF(int a, int b){
	int val=a;
	if(a<b){
		val=a;
	}
	else{
		val=b;
	}
	return val;
}


