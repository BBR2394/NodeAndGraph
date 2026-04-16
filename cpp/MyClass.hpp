/**
Baptiste BR 3 Avril 2026
*/

#include <iostream>
#include <string>
#include <map>

typedef void (*ptrFunction)(void);


class MyClass {

enum eCOMMAND { 
    DISPLAY = 0, 
    ADD, 
    OTHER 
};

public:
    MyClass();
    ~MyClass();

private:
    int _id;
    std::map<std::string, ptrFunction> _cmdavailable;

public:
    int init();
    void setId(int);
    int print(std::string);

    int computePrompt(std::string &);
    int prompt();

};