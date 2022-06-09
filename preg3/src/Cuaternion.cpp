/**
 * CI3825 - Lenguajes de Programación I
 * Pregunta 4
 * 
 * Implementación de la clase Cuaternion.
 * 
 * @author Christopher Gómez (c) 2022
 */
#include <iostream>
#include <cmath>
#include "Cuaternion.hpp"
using namespace std;

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

Cuaternion Cuaternion::operator+(const Cuaternion &other) {
    return Cuaternion(a + other.a, b + other.b, c + other.c, d + other.d);
}

Cuaternion Cuaternion::operator+(double other) {
    return Cuaternion(a + other, b, c, d);
}

Cuaternion Cuaternion::operator+(int other) {
    return Cuaternion(a + other, b, c, d);
}

Cuaternion Cuaternion::operator~() {
    return Cuaternion(a, -b, -c, -d);
}

Cuaternion Cuaternion::operator*(const Cuaternion &other) {
    return Cuaternion(
        a*other.a - b*other.b - c*other.c - d*other.d,
        a*other.b + b*other.a + c*other.d - d*other.c,
        a*other.c - b*other.d + c*other.a + d*other.b,
        a*other.d + b*other.c - c*other.b + d*other.a
    );
}

Cuaternion Cuaternion::operator*(double other) {
    return Cuaternion(a*other, b*other, c*other, d*other);
}

Cuaternion Cuaternion::operator*(int other) {
    return Cuaternion(a*other, b*other, c*other, d*other);
}

double Cuaternion::operator&() {
    return sqrt(a*a + b*b + c*c + d*d);
}

bool Cuaternion::operator==(const Cuaternion &other) const {
    return a == other.a && b == other.b && c == other.c && d == other.d;
}

// ostream& operator<<(ostream& os, Cuaternion const& value) {
//     os << a << " + " << b << "i + " << c << "j +" << d << "k";
//     return os;
// }

void Cuaternion::print() {
    cout << a << " + " << b << "i + " << c << "j + " << d << "k" << endl;
}