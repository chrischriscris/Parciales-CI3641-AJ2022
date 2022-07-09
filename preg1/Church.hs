module Church (
    Church(..),
    suma, multiplicacion,
    comoNatural, comoNumeral,
    (+:), (*:),
) where

-- | Representación de los numerales de Church.
data Church = Cero | Suc Church
    deriving (Eq, Show)

-- | Suma dos numerales de Church.
-- Usa que suc(m) + n = m + suc(n)
suma :: Church -> Church -> Church
suma Cero    n    = n
suma m       Cero = m
suma (Suc m) n    = suma m (Suc n)

-- | Multiplica dos numerales de Church.
-- Usa que suc(m) * n = (m * n) + n
multiplicacion :: Church -> Church -> Church
multiplicacion Cero    n    = Cero
multiplicacion m       Cero = Cero
multiplicacion (Suc m) n    = suma n $ multiplicacion m n

-- | Operador de suma de numerales de Church.
infixl 6 +:
(+:) :: Church -> Church -> Church
(+:) = suma

-- | Operador de multiplicación de numerales de Church.
infixl 7 *:
(*:) :: Church -> Church -> Church
(*:) = multiplicacion

-- | Convierte un numeral de Church a un número natural.
comoNatural :: Church -> Integer
comoNatural m = comoNatural' m 0

-- | Función auxiliar para la conversion de Church a natural.
comoNatural' :: Church -> Integer -> Integer
comoNatural' Cero    acc = acc
comoNatural' (Suc n) acc = comoNatural' n (acc + 1)

-- | Convierte un número natural a un numeral de Church.
-- Usa que n = suc(n-1)
comoNumeral :: Integer -> Church
comoNumeral 0 = Cero
comoNumeral n = Suc $ comoNumeral (n - 1)