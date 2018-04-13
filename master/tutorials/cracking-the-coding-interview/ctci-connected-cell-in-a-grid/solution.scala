object Solution {
    import scala.collection.mutable
    
    type Node = Tuple2[Int, Int]
    type Graph = Tuple3[Array[Array[Int]], Int, Int]

    def main(args: Array[String]) {
        println(sizeOfBiggestRegion(readGraphFromStdin()))
    }
    
    def sizeOfBiggestRegion(implicit graph: Graph):Int = {
        implicit val visited = mutable.Set.empty[Node]
        getNodes(graph)
            .map(getRegionSizeDfs)
            .max
    }
    
    def getRegionSizeDfs(node:Node)(implicit graph:Graph, visited:mutable.Set[Node]):Int = 
        if(visited.contains(node)) 
            0
        else {
            visited += node
            if(isEmpty(node)) 
                0
            else 
                1 +
                getChildren(node)
                    .map(getRegionSizeDfs)
                    .sum
        }
    
    
    def isEmpty(node:Node)(implicit graph: Graph):Boolean = {
        val (grid, _, _) = graph
        val (i,j) = node
        grid(i)(j) == 0
    }
    
    def getNodes(graph:Graph): Seq[Node] = {
        val(_, n, m) = graph
        for {
            i <- 0 until n
            j <- 0 until m
        } yield i -> j
    }   
    
    def getChildren(node:Node)(implicit graph:Graph): Seq[Node] = {
        val (_, n, m) = graph
        val (i,j) = node
        for {
            ci <- i - 1 to i + 1 if 0 <= ci && ci < n
            cj <- j - 1 to j + 1 if 0 <= cj && cj < m 
            if ci != i || cj != j
        } yield ci -> cj 
    }
    
    def readGraphFromStdin():Graph = {
        val sc = new java.util.Scanner (System.in);
        val n = sc.nextInt();
        val m = sc.nextInt();
        val grid = Array.ofDim[Int](n,m);
        for(i <- 0 until n) {
           for(j <- 0 until m){
              grid(i)(j) = sc.nextInt();
           }
        }
        (grid, n, m)
    }
}
