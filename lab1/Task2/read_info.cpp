#include <iostream>
#include <fstream>
#include <vector>
#include <thread>

void printLines(const std::vector<std::string>& lines, int start, int end) {
    for (int i = start; i < end; ++i) {
        std::cout << lines[i] << std::endl;
    }
}

int main() {
    // Считываем информацию из файла и выводим ее в консоль
    std::ifstream inFile("comp_system.txt");
    if (inFile.is_open()) {
        std::vector<std::string> lines;
        std::string line;

        // Чтение строк из файла в вектор
        while (std::getline(inFile, line)) {
            lines.push_back(line);
        }
        inFile.close();

        std::cout << "Технические характеристики вычислительной системы:" << std::endl;

        // Создаем потоки для параллельного вывода строк из вектора
        int numThreads = std::thread::hardware_concurrency(); // Получаем количество доступных ядер
        std::vector<std::thread> threads;
        int chunkSize = lines.size() / numThreads;

        for (int i = 0; i < numThreads; ++i) {
            int start = i * chunkSize;
            int end = (i == numThreads - 1) ? lines.size() : (i + 1) * chunkSize;
            threads.emplace_back(printLines, std::ref(lines), start, end);
        }

        for (std::thread& t : threads) {
            t.join();
        }
    } else {
        std::cerr << "Не удалось открыть файл для чтения" << std::endl;
        return 1;
    }

    return 0;
}
