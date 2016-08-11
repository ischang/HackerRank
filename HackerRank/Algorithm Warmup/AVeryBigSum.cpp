#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    long long int num, num1;
    long long int sum = 0;
    cin >> num; 
    long long int array[num] = {};
    
    for (int i = 0; i < num; i++){
        cin >> num1;
        array[i] = num1;
    }//for
    
    for (int j = 0; j < num; j++){
        sum = array[j] + sum;
    }//for
    
    cout << sum;
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}