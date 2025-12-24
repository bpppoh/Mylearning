#include <iostream>

using namespace std ;

class employee {
    public :
        string name ;
        int age ;
        float salary ;
        bool employed ;

        employee() {
            
        }
        employee(string name, int age, float salary, bool employed) {
            this->name = name ;
            this->age = age ;
            this->salary = salary ;
            this->employed = employed ;
        }
};

string getType(string) {return "string";} 
string getType(int) {return "int";}
string getType(float) {return "float";}
string getType(bool) {return "bool";}

int main() {
    employee employees[] = {
        employee("Alice",30,55000.75,true),
        employee("Bob",25,48000.00,false)
    };
    
    cout << boolalpha ;
    for(int i = 0 ; i < sizeof(employees)/sizeof(employees[0]) ; i++) {
        cout << "Employee " << i+1 << endl ;
        cout << "   Name: " << employees[i].name << " ,Type: " << getType(employees[i].name) << endl ;
        cout << "   Age: " << employees[i].age << " ,Type: " << getType(employees[i].name) << endl ;
        cout << "   Salary: " << employees[i].salary << " ,Type: " << getType(employees[i].name) << endl ;
        cout << "   Employed: " << employees[i].employed << " ,Type: " << getType(employees[i].name) << endl ;
    }
    
}