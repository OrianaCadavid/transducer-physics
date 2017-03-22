import numpy as np
import matplotlib.pyplot as plt
from glob import glob
import subprocess
import os
k = 8.6173303E-5
Ef = 0.55


def fermi_dirac(E, T):
    if T == 0:
        return np.piecewise(E, [E < Ef, E == Ef, E > Ef], [1, 0.5, 0])
    return 1 / (1 + np.exp((E - Ef) / k / T))


def clean():
    for f in glob(r"[0-9][0-9]*.pdf"):
        os.remove(f)


def combinePdf():
    files = glob(r"[0-9][0-9]*.pdf")
    files.sort()
    subprocess.call(
        ['pdftk'] +
        files +
        ['cat', 'output', 'fermi-dirac.pdf']
    )


def main():
    E = np.linspace(0, 1, 10000)
    for i, T in enumerate(np.arange(0, 5001, 100)):
        f = fermi_dirac(E, T)
        plt.plot(E, f)
        if i % 10 == 0 and i > 0:
            plt.title(
                r'Fermi-Dirac distribution, ${}K \leq T \leq {}K$'.format(
                    (i - 10) * 100, i * 100
                )
            )
            plt.xlabel('$E$ (eV)')
            plt.ylabel('$f(E)$')
            plt.savefig('{}.pdf'.format(i))
            plt.clf()
    combinePdf()
    clean()


if __name__ == '__main__':
    main()
