#include <iostream>
#include <fstream>
#include <thread>
#include <vector>
#include <mutex>

std::mutex consoleMutex;

int* createAndFillArray(int size) {
    int* arr = new int[size];
    std::vector<std::thread> threads;

    for (int i = 0; i < size; ++i) {
        threads.emplace_back([i, &arr]() {
            arr[i] = i;
        });
    }

    for (std::thread& t : threads) {
        t.join();
    }

    return arr;
}

void printArrayRange(const int* arr, int start, int end) {
    std::lock_guard<std::mutex> lock(consoleMutex);
    for (int i = start; i <= end; ++i) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
}

void saveArrayToBinaryFile(const int* arr, int size, const std::string& filename) {
    std::ofstream file(filename, std::ios::binary);
    if (file.is_open()) {
        file.write(reinterpret_cast<const char*>(arr), size * sizeof(int));
        file.close();
        std::cout << "Массив успешно сохранен в файл: " << filename << std::endl;
    } else {
        std::cerr << "Ошибка при открытии файла для записи." << std::endl;
    }
}

void readArrayFromBinaryFile(const std::string& filename) {
    std::ifstream file(filename, std::ios::binary);
    if (file.is_open()) {
        file.seekg(0, std::ios::end);
        int size = file.tellg() / sizeof(int);
        file.seekg(0, std::ios::beg);

        int* arr = new int[size];
        file.read(reinterpret_cast<char*>(arr), size * sizeof(int));

        std::cout << "Содержимое массива из файла " << filename << ":" << std::endl;
        for (int i = 0; i < size; ++i) {
            std::cout << arr[i] << " ";
        }
        std::cout << std::endl;

        delete[] arr;
        file.close();
    } else {
        std::cerr << "Ошибка при открытии файла для чтения." << std::endl;
    }
}

int main() {
    int size, start, end;
    std::string filename;

    // Ввод размера массива с консоли
    std::cout << "Введите размер массива: ";
    std::cin >> size;

    // Создание и заполнение массива индексами
    int* myArray = createAndFillArray(size);

    // Вывод содержимого массива в заданном диапазоне
    std::cout << "Введите начальный и конечный индексы для вывода массива: ";
    std::cin >> start >> end;
    printArrayRange(myArray, start, end);

    // Сохранение массива в двоичный файл
    std::cout << "Введите имя файла для сохранения массива: ";
    std::cin >> filename;
    saveArrayToBinaryFile(myArray, size, filename);

    // Считывание и вывод массива из двоичного файла
    std::cout << "Введите имя файла для считывания массива: ";
    std::cin >> filename;
    readArrayFromBinaryFile(filename);

    // Освобождение памяти, выделенной под массив
    delete[] myArray;

    return 0;
}
