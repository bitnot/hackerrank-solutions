object Solution {
    import scala.collection.Searching._
    
    def subSum(runningSum:Array[Long], maxSum:Long):Long = {
        val n = runningSum.length
        runningSum.search(maxSum) match {
            case InsertionPoint(x) if x < n => x + 1L
            case Found(x) => x + 1L
            case _ => -1L
        }
    }
    
    def main(args: Array[String]) {
        val n = readLong()
        val a = readLine().trim().split(" ").map(x=>x.toLong)
        val decresing = a.sortWith(_ > _)
        val runningSum = decresing
            .scanLeft(0L)(_ + _)
            .drop(1)
            .toArray
        val t = readLong()
        1L to t foreach {_ => 
            val maxSum = readLong()
            val ss = subSum(runningSum, maxSum)
            println(ss)
        }
    }
}