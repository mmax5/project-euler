use strict;
use warnings;
use Math::Complex;

my $i = 0;
my $num = 0;
my $tri = 0;

while(!$tri){
        $num += $i++;
	my $factor = 2 * factors($num);
	print $num, " ", $factor, "\n";
	if($factor >= 500){
	        last;
	        }

        }

print $num;
	
sub factors
{
        my($n) = @_;
        my $str = grep { $n % $_ == 0 }(1 .. int(sqrt($n))+1);
        return $str
}
