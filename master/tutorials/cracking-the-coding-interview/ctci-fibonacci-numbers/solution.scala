object Solution extends App {
    def fibonacci(x:Int):Int = {
        @scala.annotation.tailrec
        def fib(a:Int, b:Int, n:Int):Int = 
            if(n > 0)
                fib(b, a+b, n-1)
            else
                a
        fib(0, 1, x)
    }
    
    println(fibonacci(readInt()))
}
