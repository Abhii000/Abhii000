#include <iostream>
using namespace std;
int main(){
    int a,b,c;
    int arr[3][3];
    for(int i=0;i<3;i++){
        cout<<"type"<<endl;
        for(int j=0;j<3;j++){
            cin>>arr[i][j];
        }

    }
    int set=15;
    int cost=0;
     while(true){
        int col1=arr[0][0]+arr[0][1]+arr[0][2];
        int col2=arr[1][0]+arr[1][1]+arr[1][2];
        int col3=arr[2][0]+arr[2][1]+arr[2][2];

        int row1=arr[0][0]+arr[1][0]+arr[2][0];
        int row2=arr[0][1]+arr[1][1]+arr[2][1];
        int row3=arr[0][2]+arr[1][2]+arr[2][2];

        int dia1=arr[0][0]+arr[1][1]+arr[2][2];
        int dia2=arr[0][2]+arr[1][1]+arr[2][0];
   
        if(col1==15){
            if(col2==15){
                if(col3==15){
                    if(row1==15){
                        if(row2==15){
                            if(row3==15){
                                if(dia1==15){
                                    if(dia2==15){
                                        break;
                                    }
                                }
                                
                            }
                        }
                    }
                }
            }
            
        }
        else{
            int k=arr[0][0];
            arr[0][0]=15-arr[0][1]+arr[0][2];
        cost=k-arr[0][0];}
    }
    cout<<"perfect sqr";
    
    return 0;
}