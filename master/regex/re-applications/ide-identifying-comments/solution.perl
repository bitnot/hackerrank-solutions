#!/usr/bin/perl
use strict;
use warnings;

my $code;

foreach my $line ( <STDIN> ) {
    $code = $code . $line;
}

my @comments = ($code =~ /(\/\*.*?(?:\*\/)+?)|(\/\/.*?)(?:\n)/sg );


foreach my $line ( @comments ) {
    if($line){
        $line =~ s/^\s+//;
        $line =~ s/\n\s+/\n/g;
        print $line . "\n";
    }
}