# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt


def cm2inch(value):
    return value/2.54

data = {
    0: (3.00, 10.85, 30.00),
    1: (3.69, 10.85, 28.31),
    2: (4.32, 10.85, 26.77),
    3: (4.90, 10.85, 25.37),
    4: (5.42, 10.85, 24.09),
    5: (5.90, 10.85, 22.93),
    6: (6.33, 10.85, 21.86),
    7: (6.73, 10.85, 20.89),
    8: (7.09, 10.85, 20.01),
    9: (7.42, 10.85, 19.20),
    10: (7.73, 10.85, 18.46),
    11: (8.00, 10.85, 17.79),
    12: (8.25, 10.85, 17.18),
    13: (8.48, 10.85, 16.62),
    14: (8.69, 10.85, 16.11),
    15: (8.88, 10.85, 15.65),
    16: (9.05, 10.85, 15.23),
    17: (9.21, 10.85, 14.84),
    18: (9.35, 10.85, 14.49),
    19: (9.49, 10.85, 14.17),
    20: (9.60, 10.85, 13.88),
    21: (9.71, 10.85, 13.61),
    22: (9.81, 10.85, 13.37),
    23: (9.90, 10.85, 13.14),
    24: (9.99, 10.85, 12.94),
    25: (10.06, 10.85, 12.76),
    26: (10.13, 10.85, 12.59),
    27: (10.20, 10.85, 12.43),
    28: (10.25, 10.85, 12.30),
    29: (10.30, 10.85, 12.17),
    30: (10.35, 10.85, 12.05),
    31: (10.40, 10.85, 11.94),
    32: (10.44, 10.85, 11.85),
    33: (10.47, 10.85, 11.76),
    34: (10.50, 10.85, 11.68),
    35: (10.53, 10.85, 11.61),
    36: (10.56, 10.85, 11.54),
    37: (10.59, 10.85, 11.48),
    38: (10.61, 10.85, 11.42),
    39: (10.63, 10.85, 11.37),
    40: (10.65, 10.85, 11.33),
    41: (10.67, 10.85, 11.28),
    42: (10.68, 10.85, 11.24),
    43: (10.70, 10.85, 11.21),
    44: (10.71, 10.85, 11.18),
    45: (10.72, 10.85, 11.15),
    46: (10.73, 10.85, 11.12),
    47: (10.74, 10.85, 11.10),
    48: (10.75, 10.85, 11.08),
    49: (10.76, 10.85, 11.06),
    50: (10.77, 10.85, 11.04),
    51: (10.77, 10.85, 11.02),
    52: (10.78, 10.85, 11.00),
    53: (10.79, 10.85, 10.99),
    54: (10.79, 10.85, 10.98),
    55: (10.80, 10.85, 10.97),
    56: (10.80, 10.85, 10.96),
    57: (10.81, 10.85, 10.95),
    58: (10.81, 10.85, 10.94),
    59: (10.81, 10.85, 10.93),
    60: (10.81, 10.85, 10.92),
    61: (10.82, 10.85, 10.92),
    62: (10.82, 10.85, 10.91),
    63: (10.82, 10.85, 10.90),
    64: (10.82, 10.85, 10.90),
    65: (10.83, 10.85, 10.89),
    66: (10.83, 10.85, 10.89),
    67: (10.83, 10.85, 10.89),
    68: (10.83, 10.85, 10.88),
    69: (10.83, 10.85, 10.88),
    70: (10.83, 10.85, 10.88),
    71: (10.83, 10.85, 10.87),
    72: (10.84, 10.85, 10.87),
    73: (10.84, 10.85, 10.87),
    74: (10.84, 10.85, 10.87),
    75: (10.84, 10.85, 10.87),
    76: (10.84, 10.85, 10.86),
    77: (10.84, 10.85, 10.86),
    78: (10.84, 10.85, 10.86),
    79: (10.84, 10.85, 10.86),
    80: (10.84, 10.85, 10.86)
}

# image size in cm, and dpi
fig = plt.figure(figsize=(cm2inch(15), cm2inch(7)), dpi=200)
# position of axes in fraction of image (l,b,w,h)
ax = fig.add_axes([0.1, 0.2, .85, .75])
line1, = ax.plot(data.keys(), [y[0] for y in data.values()], '--')
line2, = ax.plot(data.keys(), [y[1] for y in data.values()])
line3, = ax.plot(data.keys(), [y[2] for y in data.values()], '-.')
ax.set_xlim(0, 80)
ax.grid(False)
plt.xlabel(u"Année")
plt.ylabel(u"$R_s(t-t_{0})$")
plt.legend([line1, line2, line3], [
    u"$R1_s(t=t_{0})<\\frac{1}{c}$",
    u"$R2_s(t=t_{0})=\\frac{1}{c}$",
    u"$R3_s(t=t_{0})>\\frac{1}{c}$"
], loc=1)
plt.show()
