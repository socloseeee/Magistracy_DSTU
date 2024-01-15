#include <iostream>
#include <thread>
#include <mutex>
#include <vector>

int main() {
    int num_threads = std::thread::hardware_concurrency(); // Получаем количество доступных ядер

    std::vector<std::thread> threads;
    std::mutex printMutex;

    for (int thread_id = 0; thread_id < num_threads; ++thread_id) {
        threads.emplace_back([thread_id, &printMutex]() {
            std::lock_guard<std::mutex> lock(printMutex);
            std::cout << "Thread " << thread_id << " started." << std::endl;
        });
    }

    for (std::thread& thread : threads) {
        thread.join();
    }

    return 0;
}
