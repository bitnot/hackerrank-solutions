#!/usr/bin/perl
use Data::Dumper;

$t = <STDIN>;
chomp $t;

for my $a0 (0..$t-1){
    my $n = <STDIN>;
    chomp $n;
    
    my $a_temp = <STDIN>;
    chomp $a_temp;
    my @a = split / /,$a_temp; 
    
    my $sum_left =0;
    my @search = map { {
            val => $_, 
            sum_left=> $sum_left += $_,
            sum_right=> 0
            }
        } @a;
              
    my $sum_right=0;  
    my $sum_match=0;
    my $s0 = scalar(@search);
    while ($s0--){
        $sum_right += $search[$s0]{val};
        $search[$s0]->{sum_right} = $sum_right;
        if($search[$s0]->{sum_right} == $search[$s0]->{sum_left}){
            $sum_match = 1;
            last;
        }
    }
        
    print $sum_match==1 ? "YES\n" : "NO\n";
}