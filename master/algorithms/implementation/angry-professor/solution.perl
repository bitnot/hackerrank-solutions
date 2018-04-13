#!/usr/bin/perl

$t = <STDIN>;
chomp $t;

for my $a0 (0..$t-1){
    my $n_temp = <STDIN>;
    chomp $n_temp;
    my ($n, $k) = split / /,$n_temp;
    
    my $a_temp = <STDIN>;
    chomp $a_temp;
    my @a = split / /,$a_temp; 
    
    my @onTime = grep { $_ <= 0 } @a;
	my $shouldCancel = scalar(@onTime) >= $k ? "NO" : "YES";
    print "$shouldCancel\n";
}