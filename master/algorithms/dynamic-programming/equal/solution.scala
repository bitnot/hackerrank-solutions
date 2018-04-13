object Solution extends App{
    import scala.io.StdIn.{readInt, readLine}
    
    var t = readInt()
    for(_ <- 1 to t){
        val n = readInt()
        val arr = readLine().split(' ').map(_.toInt)
        val result = equal(arr)
        println(result)
    } 

    def equal(arr: Array[Int]): Int =  {
        val min = arr.min
        val diffs = arr.map(_ - min)
        val extra = (0 to 2) //adding extra 1 or 2 chocolates can decrease number of ops
        extra.map{ case ex => 
            diffs.foldLeft(0){ case (total, diff) => total + countOps(diff + ex)}
        }.min
    }
    
    def countOps(diff: Int): Int = { 
        val mod = diff % 5
        (diff / 5) + (mod / 2) + (mod % 2) // it's 2, not 3!
    }
}
