(fn[n]
   (if (< 0 n) 
        (do
        (println "Hello World")
        (recur (dec n))
   ))
)
