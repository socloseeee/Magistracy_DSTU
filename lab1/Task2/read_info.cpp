#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <omp.h>

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
        
        // Используем OpenMP для параллельного вывода строк из вектора
        #pragma omp parallel for
        for (int i = 0; i < lines.size(); ++i) {
            #pragma omp critical
            std::cout << lines[i] << std::endl;
        }
    } else {
        std::cerr << "Не удалось открыть файл для чтения" << std::endl;
        return 1;
    }

    return 0;
}
