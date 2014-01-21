package projecteuler;

import java.util.Arrays;

import static java.lang.Math.sqrt;

/**
 * Created by mmax on 1/21/14.
 */
public class Problem37 {
    private static int SIZE = 1000000;

    public static void main(String[] args){
        boolean[] primes = new boolean[SIZE];
        Arrays.fill(primes, true);

        int truncatedPrimesSum = 0;
        primes[1] = false;
        primes[2] = true;
        for(int i = 3; i < SIZE; i++){
            if(primes[i] == true){
                if(isPrime(i)){
                    primes[i] = true;
                }else{
                    for(int j = i; j < SIZE; j+=i){
                        primes[j] = false;
                    }
                }
            }
        }
        for(int i = 10; i < SIZE; i++){
            if(primes[i] == true){

                String n = String.valueOf(i);
                boolean truncated = true;

                while(truncated && !n.equals("")){
                    n = n.substring(1);
                    if(!n.equals("") && !primes[Integer.parseInt(n)]){
                        truncated = false;
                    }
                }
                n = String.valueOf(i);
                while(truncated && !n.equals("")){
                    n = n.substring(0, n.length()-1);
                    if(!n.equals("") && !primes[Integer.parseInt(n)]) truncated = false;
                }
                if(truncated){
                    System.out.println(i);
                    truncatedPrimesSum += i;
                }

            }
        }

        System.out.println(truncatedPrimesSum);
    }

    private static boolean isPrime(int n){
        for(int i = 2; i < sqrt(n) +1; i++){
            if (n % i == 0) return false;
        }
        return true;
    }
}
