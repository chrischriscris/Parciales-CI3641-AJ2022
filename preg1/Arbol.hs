module Arbol (
    Arbol (..),
) where

-- | Representación de árbol binario.
data Arbol a = Hoja a | Rama a (Arbol a) (Arbol a)
    deriving (Eq, Show)

-- | Retorna un booleano que indica si el arbol es un Max Heap simétrico.
esMaxHeapSimetrico :: Ord a => Arbol a -> Bool
esMaxHeapSimetrico a = esMaxHeap a && esSimetrico a

-- | Retorna un booleano que indica si el arbol es un Max Heap.
esMaxHeap :: Ord a => Arbol a -> Bool
esMaxHeap (Hoja _) = True
esMaxHeap (Rama val izq der) =
    esMaxHeap izq && esMaxHeap der && val >= max (valor izq) (valor der)
    where
        valor (Hoja val)     = val
        valor (Rama val _ _) = val

-- | Retorna un booleano que indica si el arbol es simétrico.
esSimetrico :: Eq a => Arbol a -> Bool
esSimetrico a = preOrder a  == postOrder a
    where
        preOrder :: Arbol a -> [a]
        preOrder (Hoja val) = [val]
        preOrder (Rama val izq der) = val : preOrder izq ++ preOrder der

        postOrder :: Arbol a -> [a]
        postOrder (Hoja val) = [val]
        postOrder (Rama val izq der) = postOrder izq ++ postOrder der ++ [val]