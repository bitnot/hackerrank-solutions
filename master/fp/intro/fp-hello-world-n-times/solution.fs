open System

let rec helloWorlds n =
    if n > 0 then
        printfn "Hello World"
        helloWorlds (n-1)
        
[<EntryPoint>]
let main argv = 
    let n = Console.ReadLine() |> int
    helloWorlds n
    0 // return an integer exit code
