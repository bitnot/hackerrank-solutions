object Solution extends App {   
    def isValid(str:String): Boolean = {
        val freqCounts = str.toSeq
            .groupBy(identity)
            .map { case (_, occurences) => occurences.size }
            .groupBy(identity)
            .map { case (freq, freqInstances) => (freq, freqInstances.size) }
            .toMap
        if(freqCounts.size == 1){
            true
        } else if(freqCounts.size == 2){
            val (commonFreq, _) = freqCounts.maxBy(_._2)
            val (outlierFreq, outlierCount) = freqCounts.minBy(_._2)
            outlierCount == 1 && ((outlierFreq == commonFreq + 1) || outlierFreq == 1 )
        }
        else false
    }
    
    val str = scala.io.StdIn.readLine()
    val result = if(isValid(str)) "YES" else "NO"
    println(result)
}
