import java.io.PrintWriter

object Solution {
  import scala.collection.mutable
    
  type Tree = (Int, mutable.Map[Int, (Int, Int)])

  def swapNodes(indexes: Array[Array[Int]],
                queries: Array[Int]): Array[Array[Int]] = {
    val tree = makeTree(indexes)
    queries.map { level =>
      walk(swap(tree, level)).toArray
    }
  }

  def makeTree(indexes: Array[Array[Int]]): Tree = {
    val n = indexes.length
    val nodes = mutable.Map.empty[Int, (Int, Int)]
    val nonRoot = mutable.Set.empty[Int]
    for (i <- 1 to n) {
      val Array(left, right) = indexes(i - 1)
      nodes(i) = (left, right)
      nonRoot += left
      nonRoot += right
    }
    val root = ((1 to n).toSet -- nonRoot).head
    (root, nodes)
  }

  def swap(tree: Tree, level: Int): Tree = {
    val (root, nodes) = tree

    def mustSwap(currentLevel: Int) = currentLevel % level == 0

    def dfSwap(currentNode: Int, currentLevel: Int): Unit = {
      if (currentNode > 0) {
        val (left, right) = nodes(currentNode)
        if (mustSwap(currentLevel)) {
          nodes(currentNode) = (right, left)
        }

        dfSwap(left, currentLevel + 1)
        dfSwap(right, currentLevel + 1)
      }
    }

    dfSwap(root, 1)
    tree
  }

  def walk(tree: Tree): Seq[Int] = {
    val (root, nodes) = tree

    def walkLNR(currentNode: Int): Seq[Int] = {
      if (currentNode <= 0) Seq.empty
      else {
        val (left, right) = nodes(currentNode)
        walkLNR(left) ++ Seq(currentNode) ++ walkLNR(right)
      }
    }

    walkLNR(root)
  }
    
    def main(args: Array[String]) {
        val stdin = scala.io.StdIn

        val printWriter = new PrintWriter(sys.env("OUTPUT_PATH"))

        val n = stdin.readLine.trim.toInt

        val indexes = Array.ofDim[Int](n, 2)

        for (indexesRowItr <- 0 until n) {
            indexes(indexesRowItr) = stdin.readLine.split(" ").map(_.trim.toInt)
        }

        val queriesCount = stdin.readLine.trim.toInt

        val queries = Array.ofDim[Int](queriesCount)

        for (queriesItr <- 0 until queriesCount) {
            val queriesItem = stdin.readLine.trim.toInt
            queries(queriesItr) = queriesItem}

        val result = swapNodes(indexes, queries)

        printWriter.println(result.map(_.mkString(" ")).mkString("\n"))

        printWriter.close()
    }
}
