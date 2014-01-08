#!/usr/bin/perl -w

use strict;
use warnings;

$sum = 0

for($i = 0; $i < 100; $i++){
	if ($i % 5 == 0 || $i %3 == 0)
		$sum += $i
	
	}
	
	print "$sum";
