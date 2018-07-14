object Solution {

    // Complete the averageOfTopEmployees function below.
    def averageOfTopEmployees(rating: Seq[Int]) : Double = {
        val topPerformers = rating.filter(_ >= 90.0)   
        val sum =  topPerformers.fold(0)(_ + _).toDouble
        val count = topPerformers.size
        if(count > 0) sum / count
        else 0
    }

    def main(args: Array[String]) {
        val stdin = scala.io.StdIn

        val n = stdin.readLine.trim.toInt

        val rating = Array.ofDim[Int](n)

        for (ratingItr <- 0 until n) {
            val ratingItem = stdin.readLine.trim.toInt
            rating(ratingItr) = ratingItem}

        println("%2.2f".format(averageOfTopEmployees(rating)))
    }
}
