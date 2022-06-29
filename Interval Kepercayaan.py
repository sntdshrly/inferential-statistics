import math
import statistics
from scipy.stats import norm
import numpy as np
import scipy

'''
catatan untuk proporsi
jika ada survey sebelumnya = p topi
jika tidak ada survey sebelumnya = p topi= 0.50 dan q topi = 0.50
'''


def cariZc():  # Critical Value
    c = float(input("c="))
    Zc = norm.ppf(((1-c)/2)+c)
    print(f"Zc={Zc}")


def cariZcDiketahuiAlfa():  # Critical Value
    alfa = float(input("alfa=")) # Input lgsg kalo bukan two-tailed test
    Zc = norm.ppf(alfa)
    print(f"Zc={Zc}")


def cariTc():  # Critical Value
    c = float(input("c="))
    n = float(input("n="))
    df = n - 1
    tc = scipy.stats.t.ppf(((1-c)/2), df)
    print(f"tc={tc*-1}")


def cariChiSquare():  # Critical Value
    c = float(input("c="))
    n = float(input("n="))
    df = n - 1
    chiKanan = (1-c)/2
    chiKiri = (1+c)/2
    print("X2L=", scipy.stats.chi2.ppf(chiKanan, df))
    print("X2R=", scipy.stats.chi2.ppf(chiKiri, df))


def cariX():
    '''
    x - E = 1
    x + E = 2
    -----------+
    2x = 3
    x = ?
    '''
    marginErrorKiri = float(input("margin error kiri="))
    marginErrorKanan = float(input("margin error kanan="))
    x = (marginErrorKiri + marginErrorKanan) / 2
    print(f"x bar={x}")


def cariNSigmaKnown():
    c = float(input("c="))
    Zc = norm.ppf(((1-c)/2)+c)
    sigma = float(input("sigma="))
    E = float(input("error="))
    n = (Zc * sigma / E)**2
    print("n=", n)


def cariNProporsi():
    p = float(input("p="))
    q = 1-p
    c = float(input("c="))
    Zc = norm.ppf(((1-c)/2)+c)
    E = float(input("error="))
    n = p * q * (Zc/E)**2
    print("n=", n)


def peluangMarginErrorSigmaKnown():
    x = float(input("x="))
    c = float(input("c="))
    sigma = float(input("sigma="))
    n = int(input("n="))
    Zc = norm.ppf(((1-c)/2)+c)
    marginErrorKiri = x - Zc * sigma / math.sqrt(n)
    marginErrorKanan = x + Zc * sigma / math.sqrt(n)
    print(f"p.margin error kiri {marginErrorKiri}")
    print(f"p.margin error kanan {marginErrorKanan}")


def peluangMarginErrorSigmaUnknown():
    x = float(input("x="))
    c = float(input("c="))
    s = float(input("s="))
    n = int(input("n="))
    df = n - 1
    tc = scipy.stats.t.ppf(((1-c)/2), df)
    tc = tc * -1
    marginErrorKiri = x - tc * s / math.sqrt(n)
    marginErrorKanan = x + tc * s / math.sqrt(n)
    print(f"p.margin error kiri {marginErrorKiri}")
    print(f"p.margin error kanan {marginErrorKanan}")


def peluangChiSquare():
    n = int(input("n="))
    s = float(input("s="))
    c = float(input("c="))
    df = n-1
    chiKanan = (1-c)/2
    chiKiri = (1+c)/2
    X2L = scipy.stats.chi2.ppf(chiKiri, df)
    X2R = scipy.stats.chi2.ppf(chiKanan, df)
    tipe = str(input("var/sb="))
    if(tipe == 'var'):
        print("X2R=", (n-1)*(s**2)/X2R)
        print("X2L=", (n-1)*(s**2)/X2L)
    elif(tipe == 'sb'):
        print("X2R=", math.sqrt((n-1)*(s**2)/X2R))
        print("X2L=", math.sqrt((n-1)*(s**2)/X2L))


def peluangProporsi():
    n = int(input("n="))
    x = float(input("x="))
    c = float(input("c="))
    p = x/n
    q = 1 - p
    Zc = norm.ppf(((1-c)/2)+c)
    peluangKanan = p + Zc * math.sqrt((p*q)/n)
    peluangKiri = p - Zc * math.sqrt((p*q)/n)
    print("peluang kiri", peluangKiri)
    print("peluang kanan", peluangKanan)


def marginError():
    distribusi = str(input("n/t/chi/proporsi="))
    if (distribusi == 'n'):
        c = float(input("c="))
        n = int(input("n="))
        sigma = float(input("sigma="))
        Zc = norm.ppf(((1-c)/2)+c)
        marginError = Zc * sigma / math.sqrt(n)
        print(f"margin error {marginError}")
    elif (distribusi == 't'):
        c = float(input("c="))
        n = int(input("n="))
        s = float(input("s="))
        df = n - 1
        tc = scipy.stats.t.ppf(((1-c)/2), df)
        marginError = tc*-1 * s / math.sqrt(n)
        print(f"margin error {marginError}")
    elif (distribusi == 'proporsi'):
        c = float(input("c="))
        p_topi = float(input("p topi="))
        q_topi = float(input("q topi="))
        n = float(input("n="))
        Zc = norm.ppf(((1-c)/2)+c)
        marginError = Zc * math.sqrt(p_topi*q_topi/n)
        print(f"margin error {marginError}")


def hitungMeanDanStd():
    a = [590,450,490,680,380,500,570,620,640,530,780,720]
    mean = np.sum(a)/len(a)
    std = (statistics.stdev(a))
    print(f"n={len(a)}")
    print(f"mean={mean}")
    print(f"std={std}")


def main():
    cariTc()



if __name__ == '__main__':
    main()
