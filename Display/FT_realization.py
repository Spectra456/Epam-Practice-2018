import Display.FT as ft
import Display.dataReader as r
import matplotlib.pyplot as plt

array = r.bin2float("php.dat", 1000)


def fourier(array):
    deltaT = 0.002
    N = len(array)

    FT_res = ft.fourier_transform(array, deltaT)

    x_array = [i * FT_res.deltaF for i in range(N)]

    return x_array, FT_res.frequencies
