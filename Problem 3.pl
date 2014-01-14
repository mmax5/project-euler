#!/usr/bin/perl -w

use strict;
use warnings;
use Math::Complex;


=pod
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
=cut

my $num = 600851475143;
my $largest = 2;

for(my $i = int(sqrt($num)); $i > 2; $i--){
	if(($num % $i ==0) and (is_prime($i))){
		$largest = $i;
		last;
	}
	}

print "$largest";

sub is_prime{
	my $n = $_[0];
	for(my $j = 2; $j < $n/2; $j++){
		if ($n % $j == 0){
			return 0;
			}
		}
		return 1; 
	}
