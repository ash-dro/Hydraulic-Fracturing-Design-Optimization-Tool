import numpy as np

def calculate_net_pressure(rate_bpm, viscosity_cp, height_m):
    """
    Calculates net fracturing pressure (MPa)
    """
    rate_m3s = rate_bpm * 0.00265 / 60  # bpm → m3/s
    mu = viscosity_cp / 1000  # cp → Pa.s

    p_net = (mu * rate_m3s / height_m**3)**0.25
    return p_net * 10  # scaled to MPa


def calculate_fracture_width(p_net, height_m, youngs_modulus_gpa):
    E = youngs_modulus_gpa * 1e9  # GPa → Pa
    width = (p_net * 1e6 * height_m) / E
    return width * 1000  # meters → mm


def calculate_fracture_length(rate_bpm, width_mm):
    return (rate_bpm / width_mm) * 5  # scaled (meters)