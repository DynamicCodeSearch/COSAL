
{-# LANGUAGE ForeignFunctionInterface #-}
{-# LANGUAGE TemplateHaskell #-}

module Tutorial.ExampleSLACCExport where

import           Data.ByteString (ByteString)
import qualified Data.ByteString as BS
import qualified Data.ByteString.Lazy as BSL
import qualified Data.MessagePack as MSG
import Foreign.C
import FFI.Anything.TypeUncurry.Msgpack

import Tutorial.Example as BasePack



foreign export ccall hasPath_slacc_export :: CString -> IO CString
hasPath_slacc_export = export BasePack.hasPath



foreign export ccall fac_slacc_export :: CString -> IO CString
fac_slacc_export = export BasePack.fac



foreign export ccall doubleList_slacc_export :: CString -> IO CString
doubleList_slacc_export = export BasePack.doubleList



foreign export ccall asc_slacc_export :: CString -> IO CString
asc_slacc_export = export BasePack.asc



foreign export ccall add_slacc_export :: CString -> IO CString
add_slacc_export = export BasePack.add



foreign export ccall lagrange_slacc_export :: CString -> IO CString
lagrange_slacc_export = export BasePack.lagrange



foreign export ccall fibTail_slacc_export :: CString -> IO CString
fibTail_slacc_export = export BasePack.fibTail



foreign export ccall isAsc_slacc_export :: CString -> IO CString
isAsc_slacc_export = export BasePack.isAsc



foreign export ccall facTail_slacc_export :: CString -> IO CString
facTail_slacc_export = export BasePack.facTail

-- foreign export ccall foldTrie_slacc_export :: CString -> IO CString
-- foldTrie_slacc_export = export BasePack.foldTrie
