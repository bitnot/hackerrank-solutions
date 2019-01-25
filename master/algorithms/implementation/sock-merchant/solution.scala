object Solution {
    def sockMerchant(n: Int, ar: Array[Int]): Int = ar.groupBy(identity)
        .values
        .map(_.length / 2)
        .sum

    def main(args: Array[String]) {
        val stdin = scala.io.StdIn
        val n = stdin.readLine.trim.toInt
        val ar = stdin.readLine.split(" ").map(_.trim.toInt)
        val result = sockMerchant(n, ar)
        val printWriter = new java.io.PrintWriter(sys.env("OUTPUT_PATH"))
        printWriter.println(result)
        printWriter.close()
    }
}