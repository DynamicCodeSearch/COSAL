module Tutorial.Example where
import Data.Char

in_range min max x = x >= min && x <= max

add :: Int -> Int -> Int
-- add a b = a + b
-- add a = (\b -> a + b)
add = (\a -> (\b -> a + b))


fac :: Int -> Int
fac n
  | n <= 1 = 1
  | otherwise = n * fac(n - 1)


facTail :: Int -> Int
facTail n = aux n 1
  where
    aux n acc
      | n <= 1 = acc
      | otherwise = aux (n - 1) (n * acc)


fibTail :: Int -> Int
fibTail n
  | n <= 1 = 1
  | otherwise = fibAux n 1 0
    where
      fibAux n result previous
        | n == 0 = result
        | otherwise = fibAux (n - 1) (result + previous) result


fib :: Int -> Int
fib n
  | n <= 1 = 1
  | otherwise = fib (n - 1) + fib (n - 2)


asc :: Int -> Int -> [Int]
asc m n
  | m > n = []
  | m == n = [m]
  | m < n = m : asc (m + 1) n

el :: (Eq a) => a -> [a] -> Bool
el _ [] = False
el e (x:xs) = (e == x) || (el e xs)

nub :: (Eq a) => [a] -> [a]
nub [] = []
nub (x:xs) = x : nub (remDup x xs)
  where
    remDup v lst
      | lst == [] = []
      | otherwise = [l | l <- lst, v /= l]
--
-- nub (x:xs)
--   | x `el` xs = nub xs
--   | otherwise = x : nub xs

isAsc :: [Int] -> Bool
isAsc [] = True
isAsc [x] = True
isAsc (x:xs) = (x <= head xs) && isAsc xs

hasPath :: [(Int, Int)] -> Int -> Int -> Bool
hasPath [] x y = x == y
hasPath xs x y
  | x == y = True
  | otherwise =
    let xs' = [(m, n) | (m, n) <- xs, m /= x ] in
    or [hasPath xs' n y| (m, n) <- xs, m == x]


doubleList :: [Int] -> [Int]
doubleList = map (\x -> 2*x)

rev :: [a] -> [a]
rev = foldl (\acc x-> x:acc) []

prefixes :: [a] -> [[a]]
prefixes = foldr (\x acc -> [x] : (map ((:) x) acc)) []


lagrange :: [(Float, Float)] -> Float -> Float
lagrange xs x = foldl (\acc (xj,y) -> acc + (y * l xj)) 0 xs
  where
    l xj = foldl (
      \acc (xk, _) ->
        if xj==xk then
          acc
        else
          acc * ((x-xk/(xj-xk)))
      ) 1 xs


data Trie a = Leaf a | Node a [Trie a]
foldTrie :: (b -> a -> b) -> b -> Trie a -> b
foldTrie f acc (Leaf x) = f acc x
foldTrie f acc (Node x xs) = foldl (foldTrie f) (f acc x) xs
  where
    f' acc t = foldTrie f acc t
-- foldTrie f acc (Node x xs) = foldl f' (f acc x) xs
--   where
--     f' acc t = foldTrie f acc t


greet :: IO()
greet = do
  putStrLn "What is your name?"
  name <- getLine
  let uName = map toUpper name
  putStrLn $ "Hello " ++ uName

tempFunc :: (Num a, Ord b) => a -> (a, b) -> Int
tempFunc i j = 0
