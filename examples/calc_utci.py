from pythermalcomfort.models import utci
import numpy as np
import time

# Docs -
# https://pythermalcomfort.readthedocs.io/en/latest/reference/pythermalcomfort.html#universal-thermal-climate-index-utci

# input variables
tdb = 27  # dry bulb air temperature, [$^{\circ}$C]
tr = 30  # mean radiant temperature, [$^{\circ}$C]
v = 1  # average air speed, [m/s]
rh = 50  # relative humidity, [%]
utci_val = utci(tdb, tr, v, rh)
print(f'UTCI Value Run 1: {utci_val}')

utci_val = utci(tdb=60, tr=30, v=1, rh=60)
print(f'UTCI Value Run 2: {utci_val}')
print(f'UTCI Value Run 3: {utci(tdb=60, tr=30, v=1, rh=60, limit_inputs=False)}')

utci_val = utci(tdb=77, tr=77, v=6.56168, rh=60, units="IP")
print(f'UTCI Value Run 4: {utci_val}')

# numpy examples
utci_val = utci(
    tdb=[29, 29, 25],
    tr=[30, 30, 25],
    v=[1, 2, 1],
    rh=[60, 60, 50],
)
print(f'UTCI Numpy Run 1: {utci_val}')

utci_val = utci(
    tdb=[29, 29, 25],
    tr=[30, 30, 25],
    v=[1, 2, 1],
    rh=[60, 60, 50],
    return_stress_category=True,
)
print(f'UTCI Numpy Run 2: {utci_val}')
print(f'UTCI Numpy Run 2 UTCI Value: {utci_val["utci"]}')
print(f'UTCI Numpy Run 2 Stress Category: {utci_val["stress_category"]}')

iterations = 100000
tdb = np.empty(iterations)
tdb.fill(25)
start = time.time()
utci_val = utci(tdb=tdb, tr=30, v=1, rh=60)
end = time.time()
print(f'Run Time of Numpy Run 3: {end - start}')
