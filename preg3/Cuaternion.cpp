/**
 * CI3825 - Lenguajes de Programación I
 * Pregunta 4
 * 
 * Implementación de la clase Cuaternion.
 * 
 * @author Christopher Gómez (c) 2022
 */

#include <iostream>
using namespace std;

class Cuaternion {
private:
    double a, b, c, d;
public:
    Cuaternion(double a, double b, double c, double d);
    Cuaternion(double a, double b, double c);
    Cuaternion(double a, double b);
    Cuaternion(double a);
    Cuaternion();
    Cuaternion operator+(Cuaternion& q);
};

Cuaternion::Cuaternion(double a, double b, double c, double d) {
    this->a = a;
    this->b = b;
    this->c = c;
    this->d = d;
}

Cuaternion::Cuaternion(double a, double b, double c) {
    this->a = a;
    this->b = b;
    this->c = c;
    this->d = 0;
}

Cuaternion::Cuaternion(double a, double b) {
    this->a = a;
    this->b = b;
    this->c = 0;
    this->d = 0;
}

Cuaternion::Cuaternion(double a) {
    this->a = a;
    this->b = 0;
    this->c = 0;
    this->d = 0;
}

Cuaternion::Cuaternion() {
    this->a = 0;
    this->b = 0;
    this->c = 0;
    this->d = 0;
}

// ostream& operator<<(ostream& os, const Date& dt)
// {
//     os << dt.mo << '/' << dt.da << '/' << dt.yr;
//     return os;
// }

int main() {
    // Crea cuaternión
    Cuaternion a(1, 2, 3, 4);

    // calculate and display the area and volume of the room
    cout << "a =  " << endl;

    return 0;
}