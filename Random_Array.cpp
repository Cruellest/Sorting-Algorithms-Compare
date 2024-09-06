#include <cstdio>
#include <iostream>
#include <vector>
#include <chrono>
#include <iomanip>
#include <random>
#include <math.h>

using namespace std;
using namespace std::chrono;

void print_vector(const vector<int>& vec) {
    for (int num : vec) {
        cout << num << " ";
    }
    cout << endl;
}

void merge_sort(vector<int> &array){
    if(array.size() > 1){

        size_t mid = array.size()/2;

        vector<int> left_side(array.begin(),array.begin()+mid);
        vector<int> right_side(array.begin()+mid,array.end());

        merge_sort(left_side);
        merge_sort(right_side);

        size_t i = 0;
        size_t j = 0;
        size_t k = 0;

        while (i < left_side.size() && j < right_side.size()){
            if (left_side[i] < right_side[j]){
                array[k] = left_side[i];
                i++;
            }
            else{
                array[k] = right_side[j];
                j++;
            }
            k++;
        }
        while (i<left_side.size())
        {
            array[k] = left_side[i];
            i++;
            k++;
        }
        while (j<right_side.size())
        {
            array[k] = right_side[j];
            j++;
            k++;
        }
        

    }
};


vector<int> quicksort(vector<int> &array){

    if(array.size() <=1){
        return array;
    }

    int pivot = array[array.size()/2];
    vector<int> left,right,middle;

    for (int x : array){
        if (x<pivot){
            left.push_back(x);
        }
        else if (x == pivot)
        {
            middle.push_back(x);
        }
        else{
            right.push_back(x);
        }
    }
    quicksort(left);
    quicksort(right);

    array = left;
    array.insert(array.end(),middle.begin(),middle.end());
    array.insert(array.end(),right.begin(),right.end());

    return array;
}

void gen_random_array(vector<int>& array, int size, int min_value, int max_value){
    //Criando random device e seed usando Mersenne Twister engine
    random_device rd;
    mt19937_64 gen(rd());


    uniform_int_distribution<> distribuition(min_value,max_value);

    array.resize(size);

    for(int& elem : array){
        elem = distribuition(gen);
    }
}


int main(int argc, char const *argv[])
{
    vector<int> arr;
    vector<duration<double>> media_quicksort, media_alg2;

    //Numero de rep
    for (size_t n = 0; n < 100; n= n+10)
    {
        //Step
        for (size_t j = 0; j < 10; j++)
        {
            //Parametros de aleatoriedade do vetor
            gen_random_array(arr,n*1000000,0,pow(n,2));
            vector<int> arr2(arr);
            
            auto start_quicksort = high_resolution_clock::now();
            quicksort(arr);   
            auto end_quicksort = high_resolution_clock::now();

            duration<double> time_quicksort = end_quicksort - start_quicksort;
            
            media_quicksort.push_back(time_quicksort);

        
        }
    cout << fixed << setprecision(10);
    cout <<endl<< n*1000000<< '\t' << (reduce(media_quicksort.begin(),media_quicksort.end())/media_quicksort.size()).count() <<endl;
    media_quicksort.clear();
        
    }
    





    return 0;
}
