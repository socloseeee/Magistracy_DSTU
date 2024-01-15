#include <iostream>
#include <future>
#include <vector>

// Функция для вычисления факториала числа
unsigned long long factorial(unsigned int n) {
    if (n <= 1) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

int main() {
    std::vector<unsigned int> numbers = {5, 7, 8, 10};
    std::vector<std::future<unsigned long long>> futures;

    // Создаем асинхронные задачи для вычисления факториала
    for (unsigned int num : numbers) {
        std::future<unsigned long long> fut = std::async(std::launch::async, factorial, num);
        futures.push_back(std::move(fut));
    }

    // Ждем и получаем результаты
    for (size_t i = 0; i < numbers.size(); ++i) {
        unsigned long long result = futures[i].get();
        std::cout << "Factorial of " << numbers[i] << " is " << result << std::endl;
    }

    return 0;
}
