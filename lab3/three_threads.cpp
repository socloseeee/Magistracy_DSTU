#include <iostream>
#include <omp.h>

int main() {
    int param_int = 42;
    float param_float = 3.14;
    double param_double = 2.718;

    #pragma omp parallel num_threads(3)
    {
        int thread_id = omp_get_thread_num();
        #pragma omp critical
        std::cout << "Thread " << thread_id << " started." << std::endl;
        
        #pragma omp single
        {
            std::cout << "Parameters: int=" << param_int << ", float=" << param_float << ", double=" << param_double << std::endl;
        }
    }

    return 0;
}
