object Solution {

    def rotate(str:String):String = {
        val buf = new StringBuilder
        var round = str
        (1 to round.size).foreach(_=>{
            round = round.substring(1) + round(0)
            buf ++= round + " "
        })
        buf.toString
    }
    
    def main(args: Array[String]) {
        val t = readInt()
        (1 to t).foreach(_=>{
            val str = readLine().trim()
            println(rotate(str))
        })
    }
}