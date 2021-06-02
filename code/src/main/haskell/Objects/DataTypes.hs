module Objects.DataTypes where

{-# LANGUAGE OverloadedStrings, ExtendedDefaultRules #-}

import Database.MongoDB as Mongo
import Data.Text as T

data DataType = PrimitiveType {
  pName :: String
} | ArrayType {
  baseType :: DataType
} | TupleType {
  types :: [DataType]
} deriving (Show)

slaccType :: DataType -> String
slaccType (PrimitiveType _) = "PrimitiveType"
slaccType (ArrayType _) = "ArrayType"
slaccType (TupleType _) = "TupleType"

dtName :: DataType -> String
dtName (PrimitiveType pName) = pName
dtName (ArrayType _) = "array"
dtName (TupleType _) = "tuple"

dType :: DataType -> DataType
dType (ArrayType baseType) = baseType
dType _ = error "Unsupported error!"

dataTypeFromDocument :: Mongo.Value -> DataType
dataTypeFromDocument (Mongo.Doc doc) =
  case (Mongo.at (T.pack "slacc_type") doc) of
    "PrimitiveType" -> PrimitiveType {pName = Mongo.at (T.pack "name") doc}
    "ArrayType" -> ArrayType {baseType = dataTypeFromDocument $ Mongo.at (T.pack "type") doc}
    "TupleType" -> TupleType {types = Prelude.map dataTypeFromDocument $ Mongo.at (T.pack "types") doc}
dataTypeFromDocument _ = error "Unsupported WTF!!"



-- class BaseType a where
--   slaccType :: a -> String
--   name :: a -> String
--
-- data PrimitiveType = PrimitiveType {
--   pName :: String
-- } deriving (Show)
--
-- data ArrayType = ArrayType {
--   baseType :: BaseType a
-- } deriving (Show)
--
-- instance BaseType PrimitiveType  where
--   slaccType a = "PrimitiveType"
--   name = pName
--
-- instance BaseType ArrayType where
--   slaccType a = "ArrayType"
--   name a = "array"
