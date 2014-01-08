#!/usr/bin/perl -w

$sum = 0;
$last = 1;

for($i = 1; $i < 4000000;){
	$i = $i + $last;
	$last = $i - $last;
	if($i % 2 == 0){
		$sum += $i;
		}
	}
	
print "$sum";