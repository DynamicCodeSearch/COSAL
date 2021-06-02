module Examples.Sorts where

-- Bubble Sort
bubbleSort :: [Int] -> [Int]
bubbleSort [] = []
bubbleSort [x] = [x]
bubbleSort (x:y:xs) = if sorted thisSort then thisSort else bubbleSort thisSort
    where thisSort = (min x y) : bubbleSort ((max x y):xs)

sorted :: [Int] -> Bool
sorted [] = True
sorted [x] = True
sorted  (x:y:xs) = if x <= y then sorted (y:xs) else False
