/**
 * CI3825 - Lenguajes de Programación I
 * Pregunta 3
 * 
 * Suite de tests unitarios para la clase de cuaternión.
 * 
 * @author Christopher Gómez (c) 2022
 */
#include "../src/Cuaternion.hpp"

#define CATCH_CONFIG_MAIN
#include "catch.hpp"
using namespace Catch::literals;

TEST_CASE( "constructores", "[cuaterniones]" ) {
    // Usa todos los contructores disponibles para
    // los cuaterniones, con combinaciones de enteros
    // y doubles, debería hacer typecasting implícito.
    Cuaternion a = Cuaternion(1, 2.7, 3, 4);
    Cuaternion b = Cuaternion(1, 2, 3.4);
    Cuaternion c = Cuaternion(1.0, 2);
    Cuaternion d = Cuaternion(1);
    Cuaternion e = Cuaternion();

    // Chequea que los cuaterniones creado sean correctos
    // y que la igualdad sirva como se desea (sin importar
    // el si se compara entre enteros y double).
    REQUIRE( a == Cuaternion(1.0, 2.7, 3.0, 4) );
    REQUIRE( b == Cuaternion(1, 2, 3.4, 0.0) );
    REQUIRE( c == Cuaternion(1, 2, 0, 0) );
    REQUIRE( d == Cuaternion(1, 0, 0, 0) );
    REQUIRE( e == Cuaternion(0, 0.0, 0.0, 0) );
}

TEST_CASE( "operaciones", "[cuaterniones]" ) {
    // Usa todas las operaciones disponibles para
    // los cuaterniones, con combinaciones de enteros
    // y doubles, debería hacer typecasting implícito.
    Cuaternion a = Cuaternion(1, 2.7, 3, 4);
    Cuaternion b = Cuaternion(2, 2, 3.4);
    Cuaternion c = Cuaternion(-1.0, -2.7, -3, -4);
    Cuaternion d = Cuaternion();
    Cuaternion e = Cuaternion(1, 2, 3, 4);
    Cuaternion ctte = Cuaternion(1);
    Cuaternion i = Cuaternion(0, 1);
    Cuaternion j = Cuaternion(0, 0, 1);
    Cuaternion k = Cuaternion(0, 0, 0, 1);

    SECTION ( "suma" ) {
        // Suma usual de cuaterniones
        CHECK( a+b == Cuaternion(3, 4.7, 6.4, 4) );

        // Suma con el inverso aditivo igual al cuaternion nulo
        CHECK( a+c == Cuaternion() );

        // Suma con el neutro aditivo igual al mismo cuaternion
        CHECK( a+d == a );

        // Conmutatividad
        CHECK( a+b == b+a );

        // Asociatividad
        CHECK( a+b+e == (a+b)+e );
        CHECK( a+b+e == a+(b+e) );
        CHECK( (a+b)+e == a+(b+e) );
    }

    SECTION ( "conjugacion" ) {
        // Conjugación usual de cuaterniones
        CHECK( ~a == Cuaternion(1, -2.7, -3, -4) );
        CHECK( ~c == Cuaternion(-1, 2.7, 3, 4) );

        // Conjugada de la conjugada es el mismo cuaternión
        CHECK( ~~c == c );
        
        // Conjugada del cuaternión nulo es sí mista
        CHECK( ~d == d );
    }

    SECTION ( "multiplicación" ) {
        // Multiplicación usual de cuaterniones
        CHECK( b*a == Cuaternion(-13.6, 21, 1.4, 4.82) );
        CHECK( e*e == Cuaternion(-28, 4, 6, 8) );

        // Multiplicar por el cuaternión nulo da el cuaternión nulo
        CHECK( a* d == Cuaternion() );

        // No es conmutativa
        CHECK_FALSE( a*b == b*a );

        // Mantiene las propiedades
        CHECK( i*i == Cuaternion(-1) );
        CHECK( j*j == Cuaternion(-1) );
        CHECK( k*k == Cuaternion(-1) );
        CHECK( i*j*k == Cuaternion(-1) );
    }

    SECTION( "norma" ) {
        // Norma usual de cuaterniones
        CHECK( &a == Approx(5.76974869) );
        CHECK( &i == 1 );
        CHECK( &j == 1 );
        CHECK( &k == 1 );

        // Norma del vector nulo es 0
        CHECK( &d == 0 );
    }

    SECTION( "operaciones con escalares" ) {
        SECTION( "suma con entero o double a derecha" ) {
            // Suma con escalares
            CHECK( a + 0 == a );
            CHECK( a + 0.0 == a );
            CHECK( d+1 == ctte );
            CHECK( e+2 == Cuaternion(3, 2, 3, 4) );
        }

        SECTION( "multiplicacion con entero o double a izquierda" ) {
            // Multiplicacion con escalares
            CHECK( a * 1 == a );
            CHECK( a * 0 == d );
            CHECK( e * 2 == Cuaternion(2, 4, 6, 8) );
        }
    }
}

TEST_CASE( "operaciones combinadas" ) {
    Cuaternion a = Cuaternion(1, 2.7, 3, 4);
    Cuaternion b = Cuaternion(2, 2, 3.4);
    Cuaternion c = Cuaternion(-1.0, -2.7, -3, -4);
    Cuaternion i = Cuaternion(0, 1);
    Cuaternion j = Cuaternion(0, 0, 1);
    Cuaternion k = Cuaternion(0, 0, 0, 1);

    SECTION( "expresiones son válidas" ) {
        REQUIRE_NOTHROW( a*b+c );
        REQUIRE_NOTHROW( (b+b) * (c+~a) );
        REQUIRE_NOTHROW( &(c+b) );
        REQUIRE_NOTHROW( a*3.0 + 7.0 );
        REQUIRE_NOTHROW( (b+b)*&c );
    }

    SECTION( "expresiones son correctas" ) {
        // Se usa la norma para testear igualdad por aritmética
        // de punto flotante. |resultado - esperado| < eps
        Cuaternion res1 = a*b+c;
        Cuaternion expected1 = Cuaternion(-14.6, -8.9, 14.4, 7.18);
        double dist1 = &(res1 + expected1*-1);
        CHECK( dist1 <= 0.000001 );

        Cuaternion res2 = (b+b) * (c + ~a);
        Cuaternion expected2 = Cuaternion(62.4, -76, 8, -19.28);
        double dist2 = &(res2 + expected2*-1);
        CHECK( dist2 <= 0.000001 );

        double res3 = &(c * b);
        CHECK( res3 == Approx(25.517687983) );
    }

    SECTION( "resultados/propiedades" ) {
        // Replicar un cuaternion como combinación lineal de los
        // cuaterniones de la base
        CHECK( a == i*2.7 + j*3 + k*4 + 1);

        // Cuaternión por su conjugada solo tiene parte entera
        CHECK( a*~a == Cuaternion(33.29) );

        // Norma de la conjugada es igual la norma del cuaternion
        CHECK( &~a == &a );
    }
}
