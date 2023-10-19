#include <iostream>
#include <vector>
#include <thread>
#include <mutex>

int main() {
    int num_threads = 4;
    int vector_size = 5;

    std::vector<int> vector1 = {1, 2, 3, 4, 5};
    std::vector<int> vector2 = {6, 7, 8, 9, 10};

    int result = 0;
    std::mutex resultMutex;

    std::vector<std::thread> threads;

    for (int t = 0; t < num_threads; ++t) {
        threads.emplace_back([&, t]() {
            int local_result = 0;

            for (int i = t; i < vector_size; i += num_threads) {
                local_result += vector1[i] * vector2[i];
            }

            std::lock_guard<std::mutex> lock(resultMutex);
            result += local_result;
        });
    }

    for (std::thread& thread : threads) {
        thread.join();
    }

    std::cout << "Scalar product: " << result << std::endl;

    return 0;
}
