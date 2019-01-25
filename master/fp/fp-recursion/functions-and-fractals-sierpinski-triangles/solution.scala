object Solution {
  def nextRow(prevRow: Long, shouldBreak: Boolean): Long =
    if (shouldBreak)
      ((prevRow << 1) ^ prevRow ^ (prevRow >> 1)) & ((prevRow << 1) ^ (prevRow >> 1))
    else
      prevRow | prevRow << 1 | prevRow >> 1

  def makeRows(fractalization: Int, nrRows: Int, nrCols: Int): Seq[Long] = {
    val breakRowNr = nrRows / (1L << fractalization)
    (1 until nrRows)
      .foldLeft(Seq(1L << (nrCols / 2))) {
        case (rows, rowIndex) =>
          nextRow(rows.head, rowIndex % breakRowNr == 0) +: rows
      }
      .reverse
    }

  def showRow(rowBits: Long, nrCols: Int): String = {
    (0 until nrCols).reverse.map { i =>
      if (((1L << i) & rowBits) > 0) "1" else "_"
    }.mkString
  }

  def drawTriangles(n: Int) {
    makeRows(n, 32, 63).foreach { row =>
      println(showRow(row, 63))
    }
  }

  def main(args: Array[String]) {
    drawTriangles(readInt())
  }
}