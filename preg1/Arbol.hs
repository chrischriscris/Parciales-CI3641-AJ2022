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
esSimetrico a = preorder a  == postorder a
    where
        preorder :: Arbol a -> [a]
        preorder (Hoja val) = [val]
        preorder (Rama val izq der) = val : preorder izq ++ preorder der

        postorder :: Arbol a -> [a]
        postorder (Hoja val) = [val]
        postorder (Rama val izq der) = postorder izq ++ postorder der ++ [val]