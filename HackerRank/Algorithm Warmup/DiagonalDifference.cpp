#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int num = 0;
    int temp;
    int sum1 =0; 
    int sum2 = 0;
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    cin >> num;
    
    for (int i = 0; i < num; i ++){
        for (int j = 0; j < num; j++) {
            cin >> temp;
            if  (i == j) {
                sum1 = sum1 + temp; 
            }//if 
            
            if (i == (num - 1 - j)){
                sum2 = sum2 + temp;
            }
        }//inner for
    }//outter for
    
    cout << abs(sum1-sum2) << endl; 
    return 0;
}