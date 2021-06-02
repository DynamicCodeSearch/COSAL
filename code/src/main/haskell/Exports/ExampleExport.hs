{-# LANGUAGE ForeignFunctionInterface #-}
{-# LANGUAGE TemplateHaskell #-}

module Exports.ExampleExport where

-- import           Data.ByteString (ByteString)
-- import qualified Data.ByteString as BS
-- import qualified Data.ByteString.Lazy as BSL
-- import qualified Data.MessagePack as MSG
import Foreign.C

import FFI.Anything.TypeUncurry.Msgpack

import Tutorial.Example as Eg


foreign export ccall fib_export :: CString -> IO CString
fib_export = export Eg.fib
