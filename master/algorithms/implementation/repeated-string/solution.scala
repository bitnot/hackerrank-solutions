object Solution {
    def repeatedString(s: String, n: Long): Long = {
        val total = s.filter(_ == 'a').length
        val last = s.take((n % s.length).toInt).filter(_ == 'a').length
        total * (n / s.length) + last
    }

    def main(args: Array[String]) {
        import scala.io.StdIn._

        val s = readLine
        val n = readLine.trim.toLong
        val result = repeatedString(s, n)

        val printWriter = new java.io.PrintWriter(sys.env("OUTPUT_PATH"))
        printWriter.println(result)
        printWriter.close()
    }
}