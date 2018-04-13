import java.io.PrintWriter

object Solution {
    def birthdayCakeCandles(n: Int, ar: Array[Int]): Int = {
        val max = ar.max
        ar.filter(_ == max).size
    }

    def main(args: Array[String]) {
        val scan = scala.io.StdIn

        val fw = new PrintWriter(sys.env("OUTPUT_PATH"))

        val n = scan.readLine.trim.toInt

        val ar = scan.readLine.split(" ").map(_.trim.toInt)
        val result = birthdayCakeCandles(n, ar)

        fw.println(result)

        fw.close()
    }
}
