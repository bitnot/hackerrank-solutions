object Solution {
    def countingValleys(s: String): Int = 
        s.foldLeft((0,0)){ case ((h,v),d) => 
            val diff = if(d == 'D') -1 else 1
            val newH = h + diff
            val newV = if(h < 0 && newH == 0) v + 1 else v
            (newH, newV)
        }._2

    def main(args: Array[String]) {
        import scala.io.StdIn._
        val n = readLine.trim.toInt
        val s = readLine
        val result = countingValleys(s)
        val printWriter = new java.io.PrintWriter(sys.env("OUTPUT_PATH"))
        printWriter.println(result)
        printWriter.close()
    }
}