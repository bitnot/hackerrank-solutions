object Solution extends App{
    def miniMaxSum(arr: Array[Int]): (Long, Long) = {
        var min = Long.MaxValue
        var max = Long.MinValue
        var sum = 0L
        for (i <- arr){
            min = min.min(i)
            max = max.max(i)
            sum += i
        }
        (sum - max, sum - min)
    }
    
    val arr = scala.io.StdIn.readLine.split(" ").map(_.trim.toInt)
    val result = miniMaxSum(arr)
    println(s"${result._1} ${result._2}")
}
