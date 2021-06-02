{-# LANGUAGE TemplateHaskell #-}
{-# LANGUAGE OverloadedStrings #-}
{-# LANGUAGE LambdaCase, TupleSections #-}

module Parsers.HaskellParser where

-- import Shelly
-- import qualified Data.Text as T
-- import Utils.Cache
-- import Language.Haskell.Exts.Parser
-- import Language.Haskell.Exts.Syntax

-- getAST :: String -> Module
-- getAST fp = do
--   contents <- readFile fp
--   ast <-  parseModule contents
--   -- Check validity of parseResult
--   modu <- fromParseResult ast
--   return modu
--



-- main :: IO ()
-- main = shelly $ silently $ do
--     out <- run "ghc-mod" ["browse", "-d", "Data.List"]
--     -- lns will containes a list of lines with the function names and their types
--     let lns = T.lines out
--     -- Here we print out the number of functions and the first 5 functions
--     liftIO $ putStrLn $ show $ Prelude.length lns
--     liftIO $ mapM_ (putStrLn .T.unpack) $ take 5 lns


-- import qualified System.IO as S
-- import Language.Haskell.TH
-- import qualified Data.Attoparsec.Text as AP
-- import qualified Data.Text.IO as Text
-- import qualified Data.Text as Text
-- import qualified Data.Char as Char
-- import Data.Maybe
-- import Data.List
-- import Control.Applicative
-- import Data.Traversable
-- import Prelude hiding (mapM)

import Language.Haskell.TH
import qualified System.IO as S
import qualified Data.Text as T
import Data.Char
import Data.List
import Control.Monad
import System.IO.Unsafe
import Test.QuickCheck.All
import Test.QuickCheck.Test
import Test.QuickCheck.Property hiding (Result)

-- reifyLocalFunctions :: Q [(Name, Type)]
-- reifyLocalFunctions =
--   listTopLevelFunctionLikeNames >>=
--   mapM (\name -> reifyFunction name >>= mapM (return . (name, ))) >>=
--   return . catMaybes
--   where
--     listTopLevelFunctionLikeNames = do
--       loc <- location
--       text <- runIO $ Text.readFile $ loc_filename loc
--       return $ map (mkName . Text.unpack) $ nub $ parse text
--       where
--         parse text =
--           either (error . ("Local function name parsing failure: " ++)) id $
--           AP.parseOnly parser text
--           where
--             parser =
--               AP.sepBy (optional topLevelFunctionP <* AP.skipWhile (not . AP.isEndOfLine))
--                        AP.endOfLine >>=
--               return . catMaybes
--               where
--                 topLevelFunctionP = do
--                   head <- AP.satisfy Char.isLower
--                   tail <- many (AP.satisfy (\c -> Char.isAlphaNum c || c `elem` ['_', '\'']))
--                   return $ Text.pack $ head : tail
-- 
-- reifyFunction :: Name -> Q (Maybe Type)
-- reifyFunction name = do
--   tryToReify name >>= \case
--     Just (VarI _ t _) -> return $ Just $ t
--     _ -> return Nothing
-- 
-- tryToReify :: Name -> Q (Maybe Info)
-- tryToReify n = recover (return Nothing) (fmap Just $ reify n)

readUTF8File name = S.openFile name S.ReadMode >>=
                    set_utf8_io_enc >>=
                    S.hGetContents

set_utf8_io_enc :: S.Handle -> IO S.Handle
set_utf8_io_enc h = do S.hSetEncoding h S.utf8; return h

generators :: Q Exp --[(Integer, String)]
generators = do
  let filename = "Tutorial/Example.hs"
  ls <- runIO (fmap lines (readUTF8File filename))
  let prefixes = map (takeWhile (\c -> isAlphaNum c || c == '_' || c == '\'') . dropWhile (\c -> isSpace c || c == '>')) ls
      idents = nubBy (\x y -> snd x == snd y) (filter (("has" `isPrefixOf`) . snd) (zip [1..] prefixes))
      warning x = reportWarning ("Name " ++ x ++ " found in source file but was not in scope")
      genOne :: (Int, String) -> Q [Exp]
      genOne (l, x) = do 
        exists <- (warning x >> return False) `recover` (reify (mkName x) >> return True)
        if exists then sequence [ [| ($(stringE $ x ++ " from " ++ filename ++ ":" ++ show l),
                                      (expName $ mkName x)) |] ] 
        else return []
  [| $(fmap (ListE . concat) (mapM genOne idents)) |]

allGens :: Q Exp
allGens = [| $generators |] 
