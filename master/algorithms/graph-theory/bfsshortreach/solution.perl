#!/usr/bin/perl
my $numberCases = <STDIN>;
chomp $numberCases;

for(my $caseNr = 1; $caseNr <= $numberCases; $caseNr++ ){
    my $temp = <STDIN>;
    chomp $temp;

    my ($nrNodes,$nrEdges) = split / /, $temp;
    
	my $infinity =  $nrNodes * 10;
    my @nodes = ();
    
    for(my $nodeNr = 1; $nodeNr <= $nrNodes; $nodeNr++){
        $nodes[$nodeNr-1] = {
            number => $nodeNr,
            dist => $infinity,
            nodes => [()],
            #prev => 0,
            visited => 0,
            queued => 0
        };
    }
    
    for(my $edgeNr = 1; $edgeNr <= $nrEdges; $edgeNr++){
        $temp = <STDIN>;
        chomp $temp;
        my ($x,$y) = split / /, $temp;
        push @{ $nodes[$x-1]->{"nodes"} }, $nodes[$y-1];
        push @{ $nodes[$y-1]->{"nodes"} }, $nodes[$x-1];
    }
    
    my $startNr = <STDIN>;
    chomp $startNr;

#traversal
    
    my @queue = ();
    $nodes[$startNr-1]->{"dist"} = 0;
    $nodes[$startNr-1]->{"queued"} = 1;
    push @queue, $nodes[$startNr-1];
   
    while(scalar(@queue) > 0){
		my $current = shift @queue;		
		$current->{"visited"} = 1;
		
        my $newDist =  $current->{"dist"} + 6;
        foreach my $c ( @{ $current->{"nodes"} } )
		{
            if($c->{"dist"} > $newDist){
				$c->{"dist"} = $newDist;
				#$c->{"prev"} = $current;
			}
			
			if(!$c->{"visited"} && !$c->{"queued"}) {
				$c->{queued} =1;
				push @queue, $c;
            }
        }
    }
    
    my @distances = ();
    for (my $pi = 1; $pi <= scalar @nodes; $pi ++){
        if($pi != $startNr){
			my $dist = $nodes[$pi-1]->{"dist"};
			if($dist == $infinity){ $dist = -1 };
            push @distances, $dist;
        }        
    }
    print join(" ", @distances) . "\n";
}