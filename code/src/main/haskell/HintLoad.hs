{-# LANGUAGE LambdaCase, ScopedTypeVariables #-}

module HintLoad where
import Control.Monad.IO.Class (liftIO)
import Control.Monad.Trans.Class (lift)
import Control.Monad.Trans.Writer (execWriterT, tell)
import Data.List (intercalate)
import Data.Foldable (for_)
import Data.Semigroup ((<>))
import Options.Applicative
import System.FilePath (pathSeparator)
import qualified Language.Haskell.Interpreter as Hint


data ArgOptions = ArgOptions {
  mode      :: String,
  modle    :: String,
  functon  :: String
}

argParser :: Parser ArgOptions
argParser = ArgOptions
  <$> strOption (long "mode" <> short 'o')
  <*> strOption (long "module" <> short 'm' <> value "")
  <*> strOption (long "function" <> short 'f' <> value "")

outputPrefix = "OUTPUT --> "

main :: IO ()
-- main = do
--   r <- Hint.runInterpreter $ getFunc "Tutorial.Example" "nub"
--   -- r <- Hint.runInterpreter $ browse "Tutorial.Example"
--   case r of
--     Left err -> putStrLn $ errorString err
--     Right () -> return ()
-- main = getFunc "Tutorial.Example" "nub"
-- main = browse "Tutorial.Example"
main = runner =<< execParser opts
  where
    opts = info (argParser <**> helper)
      (fullDesc
      <> progDesc "Parsing a haskell file"
      <> header "HintLoad - Load haskell files using HINT")

runner :: ArgOptions -> IO()
runner (ArgOptions "getFunc" "" "") = putStrLn $ "Not a valid option "
runner (ArgOptions "getFunc" _ "") = putStrLn $ "Not a valid option "
runner (ArgOptions "getFunc" m f) = getFunc m f
runner (ArgOptions "browse" "" _) = putStrLn $ "Not a valid option "
runner (ArgOptions "browse" m _) = browse m

runner _ = putStrLn $ "Not a valid option "


say :: String -> Hint.Interpreter ()
say = liftIO . putStrLn

errorString :: Hint.InterpreterError -> String
errorString (Hint.WontCompile es) = intercalate "\n" (header : map unbox es)
  where
    header = "ERROR: Won't compile:"
    unbox (Hint.GhcError e) = e
errorString e = intercalate "\n" ("ERROR: " : (show e) : [])

-- getFunc :: String -> String -> Hint.Interpreter ()
-- getFunc m f = do
--   Hint.loadModules ["Tutorial/Example.hs"]
--   -- Hint.setImports ["Data.Typeable"]
--   Hint.setTopLevelModules [m]
--   r <- Hint.typeOf f
--   say $ r

getFunc :: String -> String -> IO()
getFunc m f = do
  r <- Hint.runInterpreter $ do
    Hint.loadModules [toFilePath m]
    -- Hint.setImports ["Data.Typeable"]
    Hint.setTopLevelModules [m]
    r <- Hint.typeOf f
    say $ outputPrefix ++ r
  case r of
    Left err -> putStrLn $ errorString err
    Right () -> return ()

browse :: Hint.ModuleName -> IO ()
browse moduleName = do
  r <- Hint.runInterpreter $ do
    Hint.loadModules [toFilePath moduleName]
    Hint.setImports ["Prelude", "Data.Typeable", moduleName]
    exports <- Hint.getModuleExports moduleName
    execWriterT $ do
      for_ exports $ \case
        Hint.Fun identifier -> do
          tp <- lift $ Hint.typeOf identifier
          tell [(identifier, tp)]
        _ -> pure ()
  case r of
    Left err -> putStrLn $ errorString err
    Right x -> putStrLn $ outputPrefix ++ (intercalate "@@" $ map (\xa -> (fst xa) ++ ":$$:" ++ (snd xa)) x)

toFilePath :: String -> String
toFilePath m = map (\xm -> if xm == '.' then pathSeparator; else xm) m  ++ ".hs"


-- browse :: Hint.ModuleName -> Hint.Interpreter ()
-- browse moduleName = do
--   Hint.setImports ["Prelude", "Data.Typeable", moduleName]
--   exports <- Hint.getModuleExports moduleName
--   x <- for_ exports $ \case
--       Hint.Fun identifier -> do
--         tp <- lift $ Hint.typeOf identifier
--         [(identifier, tp)]
--       _ -> lift $ ("XXX", "XXX")  -- skip datatypes and typeclasses
--   say $ "Coming Soon ... "
