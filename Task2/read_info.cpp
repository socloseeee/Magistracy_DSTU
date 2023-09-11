#include <iostream>
#include <fstream>
#include <string>

int main() {
    // Считываем информацию из файла и выводим ее в консоль
    std::ifstream inFile("comp_system.txt");
    if (inFile.is_open()) {
        std::string line;
        std::cout << "Технические характеристики вычислительной системы:" << std::endl;
        while (std::getline(inFile, line)) {
            std::cout << line << std::endl;
        }
        inFile.close();
    } else {
        std::cerr << "Не удалось открыть файл для чтения" << std::endl;
        return 1;
    }

    return 0;
}