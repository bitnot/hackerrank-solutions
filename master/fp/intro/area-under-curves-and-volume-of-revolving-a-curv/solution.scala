def f(coefficients:List[Int],powers:List[Int],x:Double):Double =
    (coefficients,powers)
    .zipped
    .map((a:Int,b:Int) => a * math.pow(x,b))
    .foldLeft(0.0)(_+_)

def area(coefficients:List[Int],powers:List[Int],x:Double):Double = 
    math.Pi * math.pow(f(coefficients,powers,x), 2)

def summation(
    func:(List[Int],List[Int],Double)=>Double,
    upperLimit:Int,
    lowerLimit:Int,
    coefficients:List[Int],
    powers:List[Int]
):Double =
    (lowerLimit.toDouble to upperLimit.toDouble by 0.001)
    .map(x => func(coefficients,powers,x) )
    .foldLeft(0.0)(_+_) / 1000