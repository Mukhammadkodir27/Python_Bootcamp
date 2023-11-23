#include <iostream>
#include <cmath>

int main() {
    int persons;

    // Input the number of persons (n should be greater than or equal to 1)
    do {
        std::cout << "Enter the number of persons (must be at least 1): ";
        std::cin >>persons;
    } while (persons < 1);

    for (int i = 1; i <= persons; ++i) {
        double weight, height, bmi;

        // Input weight and height for each person
        std::cout << "\nEnter weight (in kilograms) for person " << i << ": ";
        std::cin >> weight;

        std::cout << "Enter height (in meters) for person " << i << ": ";
        std::cin >> height;

        // Calculate BMI
        bmi = weight / std::pow(height, 2);

        // Print BMI
        std::cout << "BMI for person " << i << ": " << bmi << " - ";

        // Categorize based on BMI
        if (bmi < 18.5) {
            std::cout << "Underweight\n";
        } else if (bmi < 25) {
            std::cout << "Ideal\n";
        } else if (bmi < 30) {
            std::cout << "Overweight\n";
        } else {
            std::cout << "Obese\n";
        }
    }

    return 0;
}