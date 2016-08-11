#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int size;
    cin >> size;
    int fract [size];
    float negative;
    float zero;
    
    for (int i = 0; i < size; i++){
        cin >> fract [i];
        if (fract[i] < 0){
            negative++;
        }//if
        else if (fract [i] == 0){
            zero++;
        }//zero
    }//for
    
    cout << (size-(negative+zero))/size << endl << (negative/size) << endl << (zero/size) << endl;
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}
