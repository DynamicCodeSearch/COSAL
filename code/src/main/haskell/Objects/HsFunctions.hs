module Objects.HsFunctions where

{-# LANGUAGE OverloadedStrings, ExtendedDefaultRules #-}

import Data.Map.Strict (Map, fromList)
import Data.Text as T
import Data.Text.Read as R
import Database.MongoDB as Mongo
import Data.Bson (Val)

import Objects.DataTypes as DT

type ParamType = Int

-- Haskell Function

data HsFunction = HsFunction  {
  name :: String,
  isWholeMethod :: Bool,
  sourceCodeFunctionName :: String,
  modle :: Maybe String,
  filePath :: Maybe String,
  defString :: Maybe String,
  parameters :: Maybe (Map Integer DT.DataType),
  returnType :: Maybe DT.DataType,
  inputKey :: Maybe String,
  argsPermutation :: Maybe (Map String [Integer])
  -- argsPermutation :: Maybe [String]
} deriving (Show)

hsFunction = HsFunction { name="", isWholeMethod=True,
  sourceCodeFunctionName="", modle=Nothing, filePath=Nothing,
  defString=Nothing, parameters=Nothing, returnType=Nothing,
  inputKey=Nothing, argsPermutation=Nothing
}

toInt :: T.Text -> Integer
toInt t = case R.decimal t of
    Right (i, _) -> i
    Left err -> error err

toInts :: T.Text -> [Integer]
toInts t = Prelude.map toInt $ T.split (==',') (((T.dropEnd 1).(T.drop 1)) t)

hsFunctionFromDocument :: Mongo.Document -> HsFunction
hsFunctionFromDocument doc = hsFunction {
  name = Mongo.at (T.pack "name") doc
  ,isWholeMethod = Mongo.at (T.pack "isWholeMethod") doc
  ,sourceCodeFunctionName = Mongo.at (T.pack "sourceCodeFunctionName") doc
  ,modle = Mongo.lookup (T.pack "module") doc
  ,filePath = Mongo.lookup (T.pack "filePath") doc
  ,defString = Mongo.lookup (T.pack "defString") doc
  ,parameters = fmap (fromList . toTypeMap) $ Mongo.lookup (T.pack "parameters") doc
  ,returnType = fmap DT.dataTypeFromDocument $ Mongo.lookup (T.pack "returnType") doc
  ,inputKey = Mongo.lookup (T.pack "inputKey") doc
  ,argsPermutation = fmap (fromList . toPermMap) $ Mongo.lookup (T.pack "argsPermutation") doc
} where
    toTypeMap = Prelude.map (\xs -> (toInt (label xs), DT.dataTypeFromDocument (value xs)))
    toPermMap = Prelude.map (\xs -> (T.unpack (label xs), toInts.(T.pack) $ Mongo.fval show $ value xs))
    -- toPermMap arg = (Prelude.map set12) (Mongo.at (T.pack "int") arg)



main :: IO()
main = do
  let func = hsFunction {name="func_default", sourceCodeFunctionName="helloWorld"}
  print func
