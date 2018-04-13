object Solution extends App {
    import scala.io.StdIn
    
    def cost(b: Array[Int]): Int =  {
        import scala.math.{abs, max}
        val n = b.length
        var high = 0 // sum of sequence ending with 1
        var low  = 0 // sum of sequence ending with Bi
        for(i <- 1 to n-1){
            val highToLow  = abs(b(i-1) - 1)    // ...Bk.1
            val lowToHigh  = abs(1 - b(i))      // ...1.Bk+1
            val highToHigh = abs(b(i) - b(i-1)) // ...Bk.Bk+i
            val nextLow = max(low, high + highToLow)
            val nextHigh = max(high + highToHigh, low + lowToHigh)
            low = nextLow
            high = nextHigh
        }
        max (high, low)
    }

    val t = StdIn.readInt();
    for( _ <- 1 to t){
        val n = StdIn.readInt();
        val b = StdIn.readLine().split(' ').map(_.toInt).toArray
        val result = cost(b);
        println(result)
    }
}
