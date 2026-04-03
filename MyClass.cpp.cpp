/**
Baptiste BR 3 Avril 2026
*/

#include <iostream>
#include "MyClass.hpp"

MyClass::MyClass(){

    std::cout << "MyClass start" << std::endl;


}

MyClass::~MyClass() {
    std::cout << "MyClass end" << std::endl;
    this->_id = 0;
}

int MyClass::init() {
    
    return 0;

}

void MyClass::setId(int newId) {
    this->_id = newId;
}

int MyClass::print() {
    std::cout << "identifiant : " << this->_id << std::endl;
    return 0;
}