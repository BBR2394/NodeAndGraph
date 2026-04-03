/**
Baptiste BR 3 Avril 2026
*/

#include <iostream>
#include "MyClass.hpp"

int main(int ac, char **av) {
    MyClass monobjet;
    std::cout << "bonjour" << std::endl;
    monobjet.print();
    monobjet.setId(42);
    monobjet.print();
    return 0;
}