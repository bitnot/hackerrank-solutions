#!/usr/bin/perl

my $millionseven =(10**9 + 7);

$nrTests = <STDIN>;
chomp $nrTests;

for ($i = $nrTests; $i > 0 && $nrTests <=20; $i--){
    $mnTmp = <STDIN>;
    chomp $mnTmp;
    ($m,$n) = split / /, $mnTmp;
    
    $cyTmp = <STDIN>;
    chomp $cyTmp;
    @cy = split / /, $cyTmp;
        
    $cxTmp = <STDIN>;
    chomp $cxTmp;
    @cx = split / /, $cxTmp;
    
    
    if( !( $n >= 2 && $n <= 1000000
        && $m >= 2 && $m <= 1000000 
        && $n == scalar(@cx)+1
        && $m == scalar(@cy)+1
        )
       ){  
        break;
    }
	
    my $cost = 0; 
	@cy = sort {$b <=> $a} @cy;
	@cx = sort {$b <=> $a} @cx;
    
    while( (scalar(@cy) + scalar(@cx)) > 0 ){		        
        # pick the costliest edge, and cut it
        if(scalar(@cx) > 0 && (scalar(@cy) == 0 || $cx[0] >= $cy[0] ) ){  
            $cost += shift(@cx) * ($m - scalar(@cy)) % $millionseven;			
        }
        if(scalar(@cy) > 0 && (scalar(@cx) == 0 || $cy[0] >= $cx[0] ) ){ 
            $cost += shift(@cy) * ($n - scalar(@cx)) % $millionseven;                               
        } 
        else { break; }
    }
    
    $cost = $cost % $millionseven;
    print "$cost\n";    
} 