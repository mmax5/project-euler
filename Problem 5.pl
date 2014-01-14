#!/usr/bin/perl -w

=pod
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
=cut

use strict;
use warnings;

my $i = 20*20;
my $found = 0;
while(!$found){
	my $j = 20;
	for (; $j > 2; $j--){
		if(!($i % $j == 0)){
			last;
			}
			}
		if($j == 2){
			$found = $i;
			}
	$i += 20;

	}
print "$found";
