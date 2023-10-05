#include <iostream>
#include <omp.h>
#include <vector>

int main() {
    int num_threads = 4;
    int vector_size = 5;

    std::vector<int> vector1 = {1, 2, 3, 4, 5};
    std::vector<int> vector2 = {6, 7, 8, 9, 10};

    int result = 0;

    #pragma omp parallel num_threads(num_threads)
    {
        int thread_id = omp_get_thread_num();
        int local_result = 0;

        #pragma omp for
        for (int i = 0; i < vector_size; ++i) {
            local_result += vector1[i] * vector2[i];
        }

        #pragma omp critical
        result += local_result;
    }

    std::cout << "Scalar product: " << result << std::endl;

    return 0;
}
