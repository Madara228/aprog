/*#include <iostream>
#include <conio.h>

using namespace std;

int main()
{
    int i,j,k,n;
    int arr[5];
    n = sizeof(arr)/sizeof(arr[0]);

    for(i=0;i<5;i++){
        cin>>arr[i];
    }
    i = 0;

    for(i=0;i<n-1;i++){
        for(j=0;j<n-1-i;j++){
            if(arr[j]>arr[j+1]){
                k = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = k;
            }
        }
    }

    for(i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
}
*/


#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    const int lenght = 5;
    int arr[lenght] = {21,321,532,234,234};
    int i;

    for(int ifirst = 0; ifirst<lenght - 1; ++ifirst){
        int smallest = ifirst;
        for (i = ifirst + 1; i<lenght;++i){
            if(arr[i]<arr[smallest]){
                smallest = i;
            }

        }
        swap(arr[ifirst],arr[smallest]);

    }

    for(int index = 0 ; index < lenght; ++index){
        cout<<arr[index]<<" ";
    }
}

