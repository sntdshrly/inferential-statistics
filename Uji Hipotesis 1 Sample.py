import math
import statistics
from scipy.stats import norm
import numpy as np

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

def ujiStatistik():

    alfa = float(input("alfa="))
    H0 = str(input("H0 (boleh kosong)="))
    Ha = str(input("Ha (boleh kosong)="))
    klaim = str(input("klaim (boleh kosong)="))
    tail = str(input("tail(left/right/two)="))
    z_diketahui = str(input("z diketahui/tidak="))

    if z_diketahui == 'diketahui':
        z = float(input("z="))
    elif z_diketahui == 'tidak':
        x_bar = float(input("x_bar="))
        mu = float(input("mu="))
        sigma = float(input("sigma="))
        n = int(input("n="))
        z = ( x_bar - mu ) / ( sigma / math.sqrt(n))
   
    if tail == 'left' or tail == 'right':
        z0 = norm.ppf(alfa) # Daerah Penolakan / Z-Score
    elif tail == 'two':
        z0 = norm.ppf(alfa/2) # Daerah Penolakan / Z-Score

    if z >= 0:
        A = 1-norm.cdf(z,0,1) # Peluang Kumulatif
    elif z < 0:
        A = norm.cdf(z,0,1) # Peluang Kumulatif

    if tail == 'two':
        p = 2 * A
        if p <= alfa :
            statement = "reject H0"
        elif p > alfa :
            statement = "failed to reject H0"
        print(f"z0={z0} z={z} p={p}")
        print(f"statement={statement}")
    elif tail == 'left' or tail == 'right':
        p = A
        if p <= alfa :
            statement = "reject H0"
        elif p > alfa :
            statement = "failed to reject H0"
        print(f"z0={z0} z={z} p={p}")
        print(f"statement={statement}")

def cariZcDiketahuiAlfa(): # Critical Value
    alfa = float(input("alfa=")) # Input lgsg kalo bukan two-tailed test
    Zc = norm.ppf(alfa)
    print(f"Zc={Zc}")

def main():
    ujiStatistik()
 
if __name__ == '__main__':
    main()