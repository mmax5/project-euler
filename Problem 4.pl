#!/usr/bin/perl -w

use strict;
use warnings;

=pod
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
=cut



my $num = 0;

for(my $i = 999; $i > 100; $i--){
	for(my $j = 999; $j > 100; $j--){
		my $temp = $i * $j;
		my $string = sprintf "%d", $temp;
		if(($temp > $num) and is_palindrome($string)){
			$num = $temp;
			}
		}
	
	}

print "$num";

sub is_palindrome {
	my $string = $_[0];
	if((length($string) == 0) or (length($string) == 1)){
		return 1;
		}
	if(substr($string, 0, 1) == substr($string,-1,1)){
			return is_palindrome(substr($string, 1, length($string)-2));
		}
		return 0;

	}
