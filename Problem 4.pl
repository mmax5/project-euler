#!/usr/bin/perl -w

use strict;
use warnings;

$num = 0;

for($i = 999; $i > 100; $i--){
	for($j = 999; $j > 100; $j--){
		$temp = $i * $j;
		$string = sprintf "%d", $temp;
		if(($temp > $num) and is_palindrome($string)){
			$num = $temp;
			}
		}
	
	}

print "$num";

sub is_palindrome {
	$string = $_[0];
	if((length($string) == 0) or (length($string) == 1)){
		return 1;
		}
	if(substr($string, 0, 1) == substr($string,-1,1)){
			return is_palindrome(substr($string, 1, length($string)-2));
		}
		return 0;

	}
