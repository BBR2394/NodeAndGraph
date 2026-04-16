/**
Baptiste BR 3 Avril 2026
*/

#include <list>
#include "MyClass.hpp"

MyClass::MyClass(){

    std::cout << "MyClass start" << std::endl;


}

MyClass::~MyClass() {
    std::cout << "MyClass end" << std::endl;
    this->_id = 0;
}

int MyClass::print(std::string tt) {
    std::cout << "identifiant : " << this->_id << std::endl;
    return 0;
}

int MyClass::init() {
    
    //this->_cmdavailable.emplace(0, &print(std::string ));
    //this->_cmdavailable['display'] = &print(std::string)
//     mymap['a']="an element";
//     mymap['b']="another element";
//     mymap['c']=mymap['b'];
//      mymap.emplace('x',100);
//   mymap.emplace('y',200);
//   mymap.emplace('z',100);
    return 0;

}

void MyClass::setId(int newId) {
    this->_id = newId;
}

int MyClass::computePrompt(std::string &line) {
    std::list<std::string> lstStr;

    std::cout << "la ligne : " << line << std::endl;

    

    return 0;
}

int MyClass::prompt() {
    char line[256];

    //std::cin.getline(line,256);
    std::string stringline;
    std::cout << "$>" ;
    std::cin >> stringline;

    this->computePrompt(stringline);
    //std::cout << "Ligne : " << stringline << std::endl;

    std::cout << "fin" << std::endl;
    return 0;
}