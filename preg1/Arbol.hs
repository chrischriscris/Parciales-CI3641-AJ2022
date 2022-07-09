module Arbol (
    Arbol (..),
) where

-- | Representación de árbol binario.
data Arbol a = Hoja a | Rama a (Arbol a) (Arbol a)
    deriving (Eq, Show)

esMaxHeapSimetrico :: Ord a => Arbol a -> Bool
esMaxHeapSimetrico (Hoja _) = True
esMaxHeapSimetrico (Rama a izq der) =
    esMaxHeapSimetrico izq && esMaxHeapSimetrico der