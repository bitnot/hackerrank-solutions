object Solution extends App {
    import scala.io.StdIn.{readInt, readLine}
    import scala.annotation.tailrec
    import scala.collection.{SortedSet, mutable}
    
    implicit val roadOrdering = Ordering.by[(Int, Int, Int), (Int, Int, Int)](x => (-x._3, x._1, x._2))

    // Read and solve
    val nk = readLine().split(" ").map(_.toInt)
    val (n, k) = (nk(0), nk(1))
    
    val roads = mutable.SortedSet.empty[(Int,Int,Int)]  
    for(_ <- 1 until n){
        val rl = readLine().split(" ").map(_.toInt)
        val road = ( rl(0), rl(1), rl(2) )   
        roads += road 
    }
                    
    val machines = (0 until k).map(mk => readInt()).toSeq
    
    println(solve(n, k, roads, machines))
    
    // Solution below

    // Simplifies copy-paste from IDE
    def debug(message: String, thing: Any) = Unit

    def solve(n: Int,
               k: Int,
               roads: SortedSet[(Int, Int, Int)],
               machines: Seq[Int]): Int = {
      val machineSets = mutable.Map[Int, Int]() ++ machines.map(m => m -> m)
      val allSets = mutable.Map[Int, Int]() ++ (0 until n).map(m => m -> m)
      val ranks = mutable.Map[Int, Int]() ++ (0 until n).map(m => m -> 1)

      @tailrec
      def findSet(x: Int): Int = {
        val y = allSets(x)
        if (y == x) y
        else findSet(y)
      }

      def mergeSet(x: Int, y: Int): Int = {
        val rankX = ranks(x)
        val rankY = ranks(y)
        if (rankX > rankY) {
          allSets += y -> x
          x
        }
        else if (rankX < rankY) {
          allSets += x -> y
          y
        }
        else {
          allSets += x -> y
          ranks += y -> (rankY + 1)
          y
        }
      } 

      var sum = 0
      for ((x, y, weight) <- roads) {
        val setX = findSet(x)
        val setY = findSet(y)
        if (setX != setY) {
          if (machineSets.contains(setX) && machineSets.contains(setY)) {
            // exclude road
            sum += weight
            debug("discarded:", (x, y, weight, setX, setY, machineSets, allSets))
          } else {
            //connect road
            val merged = mergeSet(setX, setY)
            debug(s"merged:$merged", (x, y, weight, setX, setY, machineSets, allSets))
            if (machineSets.contains(setX)) {
              val m = machineSets(setX)
              machineSets -= setX
              machineSets += merged -> m
            }
            else if (machineSets.contains(setY)) {
              val m = machineSets(setY)
              machineSets -= setY
              machineSets += merged -> m
            }
          }
        }
      }
      sum
    }

}
