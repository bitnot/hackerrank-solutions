hello_worlds n = 
    if 0 == n 
    then return () 
    else do
        putStrLn "Hello World"
        hello_worlds (n-1)
        
main = do
   n <- readLn :: IO Int
   hello_worlds n
