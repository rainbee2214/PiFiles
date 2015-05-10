/*  
    This program implements the BBP algorithm to generate a few hexadecimal
    digits beginning immediately after a given position id, or in other words
    beginning at position id + 1.  On most systems using IEEE 64-bit floating-
    point arithmetic, this code works correctly so long as d is less than
    approximately 1.18 x 10^7.  If 80-bit arithmetic can be employed, this limit
    is significantly higher.  Whatever arithmetic is used, results for a given
    position id can be checked by repeating with id-1 or id+1, and verifying 
    that the hex digits perfectly overlap with an offset of one, except possibly
    for a few trailing digits.  The resulting fractions are typically accurate 
    to at least 11 decimal digits, and to at least 9 hex digits.  
*/

/*  David H. Bailey     2006-09-08 */

// Formatting and modifications
// Joel Kuntz 2015-05-09

#include <math.h>

#define NHX 16
#define ntp 25
#define eps 1e-17

void ihex (double x, int m, char c[]);
double series (int m, int n);
double expm (double x, double y);

/*  index is the digit position.  Digits generated follow immediately after. */
char* getPiHex(int index)
{
    double pid, s1, s2, s3, s4;
    char chx[NHX];

    s1 = series (1, index);
    s2 = series (4, index);
    s3 = series (5, index);
    s4 = series (6, index);
    pid = 4. * s1 - 2. * s2 - s3 - s4;
    pid = pid - (int) pid + 1.;
    ihex (pid, NHX, chx);

    return chx;
}

/*  This returns, in chx, the first nhx hex digits of the fraction of x. */
void ihex (double x, int nhx, char chx[])
{
    int i;
    double y;
    char hx[] = "0123456789ABCDEF";

    y = fabs (x);

    for (i = 0; i < nhx; i++)
    {
        y = 16. * (y - floor (y));
        chx[i] = hx[(int) y];
    }
}

/*  This routine evaluates the series  sum_k 16^(id-k)/(8*k+m) 
    using the modular exponentiation technique. */
double series (int m, int id)
{
    int k;
    double ak;
    double p;
    double s;
    double t;

    s = 0.;

    /*  Sum the series up to id. */
    for (k = 0; k < id; k++)
    {
        ak = 8 * k + m;
        p = id - k;
        t = expm (p, ak);
        s = s + t / ak;
        s = s - (int) s;
    }

    /*  Compute a few terms where k >= id. */
    for (k = id; k <= id + 100; k++){
        ak = 8 * k + m;
        t = pow (16., (double) (id - k)) / ak;
        if (t < eps) break;
        s = s + t;
        s = s - (int) s;
    }
    
    return s;
}

/*  expm = 16^p mod ak.  This routine uses the left-to-right binary 
    exponentiation scheme. */
double expm (double p, double ak)
{
    int i, j;
    double p1, pt, r;
    static double tp[ntp];
    static int tp1 = 0;

    /*  If this is the first call to expm, fill the power of two table tp. */
    if (tp1 == 0) 
    {
        tp1 = 1;
        tp[0] = 1.;

        for (i = 1; i < ntp; i++) tp[i] = 2. * tp[i-1];
    }

    if (ak == 1.) return 0.;

    /*  Find the greatest power of two less than or equal to p. */
    for (i = 0; i < ntp; i++) if (tp[i] > p) break;

    pt = tp[i-1];
    p1 = p;
    r = 1.;

    /*  Perform binary exponentiation algorithm modulo ak. */
    for (j = 1; j <= i; j++)
    {
        if (p1 >= pt)
        {
            r = 16. * r;
            r = r - (int) (r / ak) * ak;
            p1 = p1 - pt;
        }
        pt = 0.5 * pt;
        if (pt >= 1.)
        {
            r = r * r;
            r = r - (int) (r / ak) * ak;
        }
    }

    return r;
}