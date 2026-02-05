#include<iostream>
#include<vector>
using namespce std;

vector<int> getAlternates(vector<int> &arr)
{
    vector<int> res;
    for(int i =0; i<arr.size(); i++){
        if(i%2 == 0){
            res.push_back(arr[i]);
        }
    }
    return res;
}

int main()
{
    vector<int> arr = {10,20,30,40,50,60,70};
    vector<int> alternates = getAlternates(arr);    
    for(int x: alternates){
        cout<<x<<" ";
    }
}

// Recursive approach
#include<iostream>
#include<vector>
using namespace std;
