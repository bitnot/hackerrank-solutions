#!/usr/bin/perl

my $n = <STDIN>;
chomp $n;

for (my $i = 1; $i <= $n; $i++) {
    $nrSpaces = $n - $i;
    $nrHashes = $i;
    $step = (' ' x $nrSpaces) . ('#' x $nrHashes);
    print "$step\n";
    
}

