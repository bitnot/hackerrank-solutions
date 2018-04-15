object Solution extends App {
    def mod(i: Long) = i % 1000000007L
    
    def f1(i:Long, k:Long) : Long = mod((k - 1) * f2(i - 1, k))
    
    def f2(i:Long, k:Long) : Long = {
        @scala.annotation.tailrec
        def f2rec(a:Long, b:Long, j:Long) : Long = {
            if(j <= 1) mod(a)
            else f2rec(
                b, 
                mod((k - 1) * a) + mod((k - 2) * b), 
                j - 1)
        }
        f2rec(0, 1, i)
    }
    
    def countArray(n: Long, k: Long, x: Long) : Long =  {
        if(x == 1) f1(n, k)
        else       f2(n, k)
    }

    scala.io.StdIn.readLine().split(" ").map(_.toLong).toList match {
        case n :: k :: x :: Nil => println(countArray(n, k, x))
        case _                  => println(0)
    }
}
