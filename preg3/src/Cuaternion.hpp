/**
 * CI3825 - Lenguajes de Programación I
 * Pregunta 4
 * 
 * Implementación de la clase Cuaternion.
 * 
 * @author Christopher Gómez (c) 2022
 */
#ifndef CUATERNION_HPP
#define CUATERNION_HPP

class Cuaternion {
private:
    double a, b, c, d;
public:
    Cuaternion(double a, double b, double c, double d);
    Cuaternion(double a, double b, double c);
    Cuaternion(double a, double b);
    Cuaternion(double a);
    Cuaternion();
    Cuaternion operator+(Cuaternion &other);
    Cuaternion operator+(double other);
    Cuaternion operator+(int other);
    Cuaternion operator~();
    Cuaternion operator*(Cuaternion &other);
    Cuaternion operator*(double other);
    Cuaternion operator*(int other);
    double operator&();
    bool operator==(Cuaternion other) const;
    void print();
};

#endif