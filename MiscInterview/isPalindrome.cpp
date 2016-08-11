#include<stdio.h>
#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

//returns boolean if something is palindrome 

bool isPalindrome (string str);

int main (void){
	int a, b;

	if (isPalindrome("abba"))
		cout << "nice";

	if (isPalindrome("hey there"))
		cout << "nice2";

	return 0;
}

bool isPalindrome (string str){
	string secondStr = str;

	std::reverse(str.begin(), str.end());

	if (str.compare(secondStr) != 0){
		return false;
	}

	return true;
}

//python
// def IsPalindromeString(n):
//     myLen = len(n)
//     i = 0
//     while i <= myLen/2:
//         if n[i] != n[myLen-1-i]:
//             return False
//         i += 1
//     return True