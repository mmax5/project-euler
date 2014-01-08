use strict;
use warnings;
use Math::Complex;

my $num = 2 ** 1000;
my $str = sprintf "%.0f", $num;
#print $str;
my $sum = 0;

foreach(split //, $str){
		$sum = $sum + int($_);
	}
	
print $sum;