let replicate (n, list) =
    List.collect (fun e -> List.replicate n e) list

let shiftHead = function
    | h::tail -> (h, tail)
    | [] -> failwith "Unexpected input"

[<EntryPoint>]
let main args = 
    Seq.initInfinite (fun _ -> System.Console.ReadLine())
    |> Seq.takeWhile (fun s -> s <> null)
    |> Seq.map int
    |> List.ofSeq
    |> shiftHead
    |> replicate
    |> List.iter (fun x -> printfn "%i" x)
    0