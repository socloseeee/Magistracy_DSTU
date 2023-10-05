#include <iostream>
#include <omp.h>

int main() {
    #pragma omp parallel
    {
        int thread_id = omp_get_thread_num();
        #pragma omp critical
        std::cout << "Thread " << thread_id << " started." << std::endl;
    }

    return 0;
}
