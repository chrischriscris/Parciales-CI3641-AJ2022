/**
 * CI3825 - Lenguajes de Programación I
 * Pregunta 4
 * 
 * Cabecera de la implementación de Cuaternion.
 * 
 * @author Christopher Gómez (c) 2022
 */
#ifndef CUATERNION_HPP
#define CUATERNION_HPP
#include <iostream>
using namespace std;

/**
 * Clase que modela el cuaternión.
 * 
 * Soporta las operaciones de suma, multiplicación,
 * conjugada y norma, mediante la sobrecarga de los
 * operadores +, *, ~, &.
 * 
 * Soporta también la suma y multiplicación por la
 * derecha de enteros y double.
 * 
 * @author Christopher Gómez (c) 2022
 */
class Cuaternion {
private:
    double a, b, c, d;
public:
    Cuaternion(double a, double b, double c, double d);
    Cuaternion(double a, double b, double c);
    Cuaternion(double a, double b);
    Cuaternion(double a);
    Cuaternion();
    Cuaternion operator+(const Cuaternion &other);
    Cuaternion operator+(double other);
    Cuaternion operator+(int other);
    Cuaternion operator~();
    Cuaternion operator*(const Cuaternion &other);
    Cuaternion operator*(double other);
    Cuaternion operator*(int other);
    double operator&();
    bool operator==(const Cuaternion &other) const;
    void print();
};

// ostream& operator<<(ostream& os, Cuaternion const& value);

#endif