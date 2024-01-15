#include <iostream>
#include <thread>
#include <mutex>
#include <vector>

int main() {
    int num_threads = 3;

    int param_int = 42;
    float param_float = 3.14;
    double param_double = 2.718;

    std::mutex printMutex;
    std::vector<std::thread> threads;

    for (int thread_id = 0; thread_id < num_threads; ++thread_id) {
        threads.emplace_back([thread_id, param_int, param_float, param_double, &printMutex]() {
            {
                std::lock_guard<std::mutex> lock(printMutex);
                std::cout << "Thread " << thread_id << " started." << std::endl;
            }

            if (thread_id == 0) {
                std::lock_guard<std::mutex> lock(printMutex);
                std::cout << "Parameters: int=" << param_int << ", float=" << param_float << ", double=" << param_double << std::endl;
            }
        });
    }

    for (std::thread& thread : threads) {
        thread.join();
    }

    return 0;
}
