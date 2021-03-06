"""
Fourier transformation module
"""

import numpy as np
from numba import jit, float64, int64


class FT_result:
    """
    Class that contains result of Fourier transformation over some function at some range

    Attributes:
        frequencies     Values of frequencies
        Re              Values of real part (cosinus basis)
        Im              Values of imaginary part (sinus basis)
        H:              Values of Re + Im parts
        deltaF          Multiplicator for x axis for frequencies
        borderF         Maximum frequency that can be found
    """

    frequencies: list
    Re: list
    Im: list
    H: list
    deltaF: float64
    borderF: float64


@jit
def fourier_transform(arr, deltaT: float) -> FT_result:
    """
    Performs Fourier transformation over some function's values

    :param arr: Array of function's values
    :param deltaT: Step of discretization
    :return: Result of transformation (frequencies, Re values list, Im values list,
    deltaF value for graph scaling and borderF value for max frequency value on graph
    """
    res = FT_result()

    N = len(arr)
    Res = np.array([0] * N, dtype=np.double)
    Ims = np.array([0] * N, dtype=np.double)
    Cs = np.array([0] * N, dtype=np.double)
    t_arr = np.array(arr)

    # Calculate FT
    for n in range(N):
        Res[n], Ims[n], Cs[n] = __FT_step(n, t_arr)

    res.Re = Res.tolist()
    res.Im = Ims.tolist()
    res.H = np.add(res.Re, res.Im)
    res.frequencies = Cs.tolist()
    res.borderF = __calculate_borderF(deltaT)
    res.deltaF = __calculate_deltaF(res.borderF, N)

    return res


def reverse_fourier_transform(arr, deltaT: float) -> list:
    N: int = len(arr)
    res: FT_result = fourier_transform(arr, deltaT)
    answer: np.ndarray = np.multiply(res.H, N)

    return list(answer.tolist())


def __FT_step(n: int, arr: np.ndarray) -> (float, float, float):
    """
    Internal step of Fourier transformation

    :param n: Step number
    :param arr: array of values
    :return: Re value, Im value and C value in terms of Fourier Transformation algo
    """
    N = len(arr)

    idxs = np.array([i for i in range(N)])

    # TODO: change to complex
    # result.Re = result.Re + tempArr[i].Re * Math.Cos((2 * Math.PI * k * i) / N) - tempArr[i].Im * Math.Sin((2 * Math.PI * k * i) / N);
    # result.Im = result.Im + tempArr[i].Re * Math.Sin((2 * Math.PI * k * i) / N) - tempArr[i].Im * Math.Cos((2 * Math.PI * k * i) / N);

    Re = np.divide(
        np.sum(arr * np.cos(2 * np.pi * n * idxs / N)),
        N
    )

    Im = np.divide(
        np.sum(arr * np.sin(2 * np.pi * n * idxs / N)),
        N
    )

    C = np.sqrt(Re ** 2 + Im ** 2)

    return Re, Im, C


@jit(float64(float64, int64))
def __calculate_deltaF(borderF: float, N: int) -> float:
    """
    Calculate \delta F (how long is one step given FT results)

    :param borderF: Max frequency
    :param N: Length of array
    :return: \delta F value
    """
    return borderF / (N / 2)


@jit(float64(float64))
def __calculate_borderF(deltaT: float) -> float:
    """
    Calculate max frequency to be found depend on step of discretization

    :param deltaT: Step of discretization
    :return: Border freq value
    """
    return 1 / (2 * deltaT)
