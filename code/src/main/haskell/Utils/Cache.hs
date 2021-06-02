module Utils.Cache where

import System.IO


readContents :: String -> IO String
readContents fp = do
  contents <- readFile fp
  return contents
