//----------------------------------------- Training -------------------------------------------------------------------------
// loading training .csv file in a list  
// extracting examples of (d x 1) 
// initalizing two weight W1 and W2 matrix, randomly of size (n1 x d) and (n2 x n1) dimension  
// Applying (W1^T)*X on input matrix and Hidden layer respectively to form hidden layer H and (W2^T)*H to form output matrix. 
// Backpropagation method in order to adjust the weight of weight matrix
//----------------------------------------------------------------------------------------------------------------------------

//----------------------------------------- Testing ------------------------------------------------------------------------
// 
//
//--------------------------------------------------------------------------------------------------------------------------

#include <iomanip>
#include <iostream>
#include <cstdio>
#include <string.h>
#include <string>
#include <fstream>
#include <stdlib.h>
#include <sstream>

using namespace std;

float data[1000][1000];
int size[2];

void transpose(int a[]){
	int trans[]
	for(int i = 0; i < r; ++i)
		for(int j = 0; j < c; ++j){
			trans[j][i]=a[i][j];
		}
}
void readFile(){

	int i=0,j=0;
	string lineA;
	float in, num;
	string x;
	ifstream fileIN;
	fileIN.open("train.csv");

	//Error check
	if(fileIN.fail()){
		cerr << "Error: File Open" <<endl;
		exit(1);
	}
	cout << '\n';
	while(fileIN.good()){
		while(getline(fileIN, lineA, '\n')){
			istringstream streamA (lineA);
			j=0;
			while(getline(streamA, x, ',')){
				istringstream streamB(x);
				streamB >> num;
				data[i][j]=num;
				j++;
				// cout << num << ",";
			}
			cout <<endl;
			i++;
		}
	}
	size[0] = i;
	size[1] = j;
}

void Training(int exmp[]){
	int d=size[1]-1
	int X1[d][0]; // example array
	int n1, n2 = 3;
	printf("Enter the number of neurons to be in the hidden layer: ");
	scanf("%d", &n1);
	
	int W1[n1][d]; // weight matrix of n1 x d applied on input matrix
	int h1[n1][0]; // set of neurons of hidden layer
	int W2[n2][n1]; // Weight matrix n2 x n1 apllied on hidden layer
	int O[n1][0];

	// Making exmp array of d x 1;
	for (int i=0; i < d; i++){
		X1[i][0]=exmp[i];
	}
	for(int i=0; i<n1; i++){
		for(int j=0; j < d; j++){
			W1[i][j] = rand()%20;
		}
	}

	// calculating the summation of weightage matrix --> Wi*Xi
	for(int i = 0; i < n1; i++){
        for(int j = 0; j < d; j++){
                h1[i][0] += W1[i][j] * X1[j][0];
        }
    }
    for (int i=0; i < n2; i++){
    	for (int j=0; j < n1; j++){
    		O[i][0]+=W2[i][j]*h1[j][0];
    	}
    }

}



int main(){

	readFile();
	int exmp[size[0]-1]={0};

	for(int i=0; i < size[0]; i++){
		for (int j=0; j < size[1]-1; j++){
			exmp[j] = data[i][j];
		}
		Training(exmp);
	}
	

	return 0;
}