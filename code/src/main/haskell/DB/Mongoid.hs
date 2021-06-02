{-# LANGUAGE OverloadedStrings #-}
{-# LANGUAGE ExtendedDefaultRules #-}

module DB.Mongoid where


import Control.Monad.IO.Class (liftIO, MonadIO)
import Database.MongoDB as Mongo
import Data.Text as T
import Data.Typeable

import Objects.HsFunctions (HsFunction, hsFunctionFromDocument, toInt, argsPermutation)

default_ip :: String
default_ip = "127.0.0.1"

hs_func_collection = "hs_functions_metadata"
fuzzed_args_collection = "fuzzed_args"

getConnection :: String -> IO Pipe
getConnection ip = connect (host ip)

dbWrapper :: String -> Action IO a -> IO a
dbWrapper db act = do
  pipe <- connect (host default_ip)
  e <- access pipe master (T.pack db) act
  close pipe
  return e

testCollection :: IO [Document]
testCollection = dbWrapper "Dummy" $ rest =<< Mongo.find (select [] "test_collection") {sort=[]}

-- loadFunction :: String -> Action IO (Maybe Document)
-- loadFunction funcID  =  findOne $ select ["name" =: funcID] hs_func_collection

loadFunction :: String -> String -> IO (Maybe Document)
loadFunction db funcID  =  dbWrapper db $ findOne $ select ["name" =: funcID] hs_func_collection


loadArguments :: String -> String -> IO (Maybe Document)
loadArguments db inputKey = dbWrapper db $ findOne $ select ["key" =: inputKey] fuzzed_args_collection


testFunction :: IO ()
testFunction = do
  e <- loadFunction "Dummy" "func_949e11f31cc8484a81dbceeb95c91442"
  d <- case e of
    Just doc -> print $ hsFunctionFromDocument doc
    Nothing -> error "Maybe the function is deleted. Check DB directly"
  return d

testArgs :: IO ()
testArgs = do
  e <- loadArguments "Dummy" "int##3"
  d <- case e of
    Just arg -> print $ val $ Mongo.valueAt "args" arg
    Nothing -> error "Args not found"
  return d


main :: IO ()
main = testArgs





-- getData = rest =<< find (select [] "test_collection") {sort=[]}
