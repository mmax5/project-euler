package projecteuler;

import java.util.Arrays;

import static java.lang.Math.sqrt;

/**
 * Created by mmax on 1/21/14.
 */
public class Problem35 {
    private static int SIZE = 1000000;


    public static void main(String[] args){

        boolean[] primes = new boolean[SIZE];
        Arrays.fill(primes, true);

        int circularPrimes = 13;
        for(int i = 100; i < SIZE; i++){
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

        for(int i = 100; i < SIZE; i++){
            if(primes[i]){
                //  197, 971, 719
                boolean circular = true;
                String n = String.valueOf(i);
                do{
                    n = String.valueOf(n).substring(1) + String.valueOf(n).charAt(0);
                    if(!primes[Integer.parseInt(n)]) circular = false;
                }while(!String.valueOf(i).equals(n));
                if(circular) circularPrimes +=1;
            }

        }
        System.out.println(circularPrimes);

    }

    public static boolean isPrime(int n){
        for(int i =2; i < sqrt(n)+ 1; i++){
            if(n % i == 0){
                return false;
            }
        }
        return true;

    }

}
