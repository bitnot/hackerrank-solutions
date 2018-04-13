#!/usr/bin/perl

my $input = <STDIN>;
my @letters = grep /[a-z]+/i, split //, lc $input;
my %seen = map {  $_=>1 } @letters;
my @unique = keys %seen;
@unique = sort @unique ;
my $abc = join "", @unique;

if($abc eq "abcdefghijklmnopqrstuvwxyz"){
    print "pangram";
} 
else {
    print "not pangram";
}