package projecteuler;

import java.math.BigInteger;

/**
 * Created by mmax on 1/21/14.
 */
public class Problem33 {
    public static int gcd(int a, int b) {
        if (b==0) return a;
        return gcd(b,a%b);
    }



    public static void main(String[] args){
        int dProd = 1;
        int nProd = 1;

        for (int i = 1; i < 10; i++) {
            for (int d = 1; d < i; d++) {
                for (int n = 1; n < d; n++) {
                    if ((n * 10 + i) * d == n * (i * 10 + d)) {
                        dProd *= d;
                        nProd *= n;
                    }
                }
            }
        }
        dProd /= gcd(nProd, dProd);
        System.out.print(dProd);
    }

}
