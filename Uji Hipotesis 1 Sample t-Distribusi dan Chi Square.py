import math
import statistics
from scipy.stats import norm
import numpy as np
from scipy import stats
import scipy
# https://www.statology.org/p-value-from-t-score-python/

'''
catatan untuk menentukan tail
H0 >= dan Ha < left
H0 <= dan Ha > right
H0  = dan Ha != two
'''

'''
p <= alfa atau z <= z0 reject h0
p > alfa atau z > z0  failed to reject h0
'''

def ujiStatistikT():

    alfa = float(input("alfa="))
    H0 = str(input("H0 (boleh kosong)="))
    Ha = str(input("Ha (boleh kosong)="))
    n = int(input("n="))
    df = n-1
    klaim = str(input("klaim (boleh kosong)="))
    tail = str(input("tail(left/right/two)="))
    t_diketahui = str(input("t diketahui/tidak="))

    if t_diketahui == 'diketahui':
        t = float(input("t="))
    elif t_diketahui == 'tidak':
        x_bar = float(input("x_bar="))
        mu = float(input("mu="))
        s = float(input("s="))
        n = int(input("n="))
        t = ( x_bar - mu ) / ( s / math.sqrt(n))
   
    if tail == 'left':
        t0 = stats.t.ppf(alfa,df) # Daerah Penolakan / t-Score
    elif tail == 'right':
        t0 = (stats.t.ppf((1-alfa),df)) # Daerah Penolakan / t-Score
    elif tail == 'two':
        t0_kiri = stats.t.ppf((alfa/2),df) # Daerah Penolakan / t-Score
        t0_kanan = (stats.t.ppf((1-(alfa/2)),df)) # Daerah Penolakan / t-Score

    if tail == 'two':
        if t >= t0_kiri and t <= t0_kanan :
            statement = "failed to reject H0"
        else:
            statement = "reject H0"
        print(f"t0 kiri={t0_kiri} t0 kanan={t0_kanan} t={t}")
        print(f"statement={statement}")
    elif tail == 'left':
        if t >= t0 :
            statement = "failed to reject H0"
        else:
            statement = "reject H0"
        print(f"t0={t0} t={t}")
        print(f"statement={statement}")
    elif tail == 'right':
        if t <= t0 :
            statement = "failed to reject H0"
        else:
            statement = "reject H0"
        print(f"t0={t0} t={t}")
        print(f"statement={statement}")

def ujiStatistikProporsi():
    
    alfa = float(input("alfa="))
    H0 = str(input("H0 (boleh kosong)="))
    Ha = str(input("Ha (boleh kosong)="))
    n = int(input("n="))
    klaim = str(input("klaim (boleh kosong)="))
    tail = str(input("tail(left/right/two)="))
    z_diketahui = str(input("z diketahui/tidak="))

    if z_diketahui == 'diketahui':
        z = float(input("z="))
    elif z_diketahui == 'tidak':
        p_topi_dik = str(input("p topi diketahui/tidak="))
        if p_topi_dik == 'diketahui':
            p_topi = float(input("p_topi="))
            p = float(input("p="))
            n = int(input("n="))
            z = ( p_topi - p ) / math.sqrt(p * (1-p) / n)
        elif p_topi_dik == 'tidak':
            x = float(input("x="))
            n = int(input("n="))
            p_topi = x/n
            p = float(input("p="))
            z = ( p_topi - p ) / math.sqrt(p * (1-p) / n)
    
    if tail == 'left':
        z0 = norm.ppf(alfa) # Daerah Penolakan / t-Score
    elif tail == 'right':
        z0 = norm.ppf(1-alfa) # Daerah Penolakan / t-Score
    elif tail == 'two':
        z0_kiri = norm.ppf((alfa/2)) # Daerah Penolakan / t-Score
        z0_kanan = norm.ppf((1-(alfa/2))) # Daerah Penolakan / t-Score

    if tail == 'two':
        if z >= z0_kiri and z <= z0_kanan :
            statement = "failed to reject H0"
        else:
            statement = "reject H0"
        print(f"z0 kiri={z0_kiri} z0 kanan={z0_kanan} z={z}")
        print(f"statement={statement}")
    elif tail == 'left':
        if z >= z0 :
            statement = "failed to reject H0"
        else:
            statement = "reject H0"
        print(f"z0={z0} z={z}")
        print(f"statement={statement}")
    elif tail == 'right':
        if z <= z0 :
            statement = "failed to reject H0"
        else:
            statement = "reject H0"
        print(f"z0={z0} z={z}")
        print(f"statement={statement}")

def ujiStatistikChi():
    
    alfa = float(input("alfa="))
    H0 = str(input("H0 (boleh kosong)="))
    Ha = str(input("Ha (boleh kosong)="))
    n = int(input("n="))
    klaim = str(input("klaim (boleh kosong)="))
    tail = str(input("tail(left/right/two)="))
    chi_diketahui = str(input("chi diketahui/tidak="))

    if chi_diketahui == 'diketahui':
        chi = float(input("chi="))
    elif chi_diketahui == 'tidak':
        n = int(input("n="))
        df = n-1
        s = float(input("s="))
        var_or_std = str(input("var atau std="))
        if (var_or_std=='var'):
            var = float(input("variansi="))
            chi = ( n - 1 ) * s / var
        elif (var_or_std=='std'):
            std = float(input("std="))
            chi = ( n - 1 ) * s**2 / std**2
    
    if tail == 'left':
        chi0 = scipy.stats.chi2.ppf(alfa, df) # Daerah Penolakan / t-Score
    elif tail == 'right':
        chi0 = scipy.stats.chi2.ppf(1-alfa, df) # Daerah Penolakan / t-Score
    elif tail == 'two':
        chi0_kiri = scipy.stats.chi2.ppf(alfa/2, df) # Daerah Penolakan / t-Score
        chi0_kanan = scipy.stats.chi2.ppf(1-(alfa/2), df) # Daerah Penolakan / t-Score

    if tail == 'two':
        if chi >= chi0_kiri and chi <= chi0_kanan :
            statement = "failed to reject H0"
        else:
            statement = "reject H0"
        print(f"chi0 kiri={chi0_kiri} chi0 kanan={chi0_kanan} chi={chi}")
        print(f"statement={statement}")
    elif tail == 'left':
        if chi >= chi0 :
            statement = "failed to reject H0"
        else:
            statement = "reject H0"
        print(f"chi0={chi0} chi={chi}")
        print(f"statement={statement}")
    elif tail == 'right':
        if chi <= chi0 :
            statement = "failed to reject H0"
        else:
            statement = "reject H0"
        print(f"chi0={chi0} chi={chi}")
        print(f"statement={statement}")


def cariTcDiketahuiAlfa(): # Critical Value
    alfa = float(input("alfa=")) # Input lgsg kalo bukan two-tailed test
    n = float(input("n="))
    df = n-1
    tc = stats.t.ppf(alfa,df)
    print(f"Tc={tc}")

def cariTcDiketahuiAlfaTwo():
    alfa = float(input("alfa=")) # Input lgsg kalo bukan two-tailed test
    n = float(input("n="))
    df = n-1
    t_kiri = stats.t.ppf((alfa/2),df) # Daerah Penolakan / t-Score
    t_kanan = stats.t.ppf((1-(alfa/2)),df)
    print(f"Tc kiri={t_kiri}")
    print(f"Tc kanan={t_kanan}")

def main():
    ujiStatistikProporsi()
 
if __name__ == '__main__':
    main()