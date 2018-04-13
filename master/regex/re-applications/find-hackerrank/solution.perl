#!/usr/bin/perl

use warnings;

my $n = <STDIN>;
chomp $n;

while($n--){
    my $line = <STDIN>;
    chomp $line;
    if($line =~ /^(hackerrank)(.*\1){0,1}$/){
        print "0\n";
    }
    elsif($line =~ /^(hackerrank).*$/){
        print "1\n";
    }
    elsif($line =~ /^.*(hackerrank)$/){
        print "2\n";
    }
    else{
        print "-1\n";
    }

}