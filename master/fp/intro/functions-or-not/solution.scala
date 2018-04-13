import scala.io.StdIn.{readInt,readBoolean}

object Solution {
    def main(args: Array[String]) {
        def couldBeFunction={
            val lines = readInt()
            val maxOccurences =(1 to lines)
                .map(_=> readLine().split(" "))
                .groupBy(_(0))
                .values
                .map(_.size)
                .reduceLeft(_ max _)
            maxOccurences == 1
        }
        val times = readInt()
        (1 to times).foreach {_=>{
            println( if(couldBeFunction) "YES" else "NO")
        }}
    }
}