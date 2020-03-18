def formula_for_single_coeff(coeff, x_in, y_in):
    temp = 0.

    temp += coeff[0]
    temp += coeff[1] * y_in
    temp += coeff[2] * x_in
    temp += coeff[3] * x_in * y_in

    return temp

def formula_for_single_coeff_merger(coeff, x_in):
    temp = 0.

    x_in_sqd = x_in*x_in

    temp += coeff[0] + coeff[1] * x_in + coeff[2] * x_in_sqd + coeff[3] * x_in_sqd*x_in + coeff[4] * x_in_sqd * x_in_sqd
    temp = x_in / temp

    return temp

def formula_for_single_coeff_degr(coeff, x_in, y_in):
    temp = 0.

    temp += coeff[0]
    temp += coeff[1] * y_in
    temp += coeff[2] * x_in
    temp += coeff[3] * x_in * y_in
    temp += coeff[4] * x_in * x_in
    temp += coeff[5] * x_in * x_in * y_in

    return temp

def formula_for_uncertainty(coeff, z_c, x_in, y_in, z):
    temp = 0.

    x_in_sqd = x_in*x_in
    x_in_trd = x_in_sqd * x_in
    y_in_sqd = y_in*y_in
    y_in_trd = y_in_sqd * y_in

    temp += coeff[0]
    temp += coeff[1] * y_in
    temp += coeff[2] * y_in_sqd
    temp += coeff[3] * y_in_trd
    temp += coeff[4] * x_in
    temp += coeff[5] * x_in * y_in
    temp += coeff[6] * x_in * y_in_sqd
    temp += coeff[7] * x_in * y_in_trd
    temp += coeff[8] * x_in_sqd
    temp += coeff[9] * x_in_sqd * y_in
    temp += coeff[10] * x_in_sqd * y_in_sqd
    temp += coeff[11] * x_in_sqd * y_in_trd
    temp += coeff[12] * x_in_trd
    temp += coeff[13] * x_in_trd * y_in
    temp += coeff[14] * x_in_trd * y_in_sqd
    temp += coeff[15] * x_in_trd *y_in_trd
    return temp + z_c*(z-0.5)*( 1./(0.25*z + 0.25))


def formula_for_uncertainty_merger(coeff, x_in, y_in):
    temp = 0.

    x_in_sqd = x_in*x_in
    x_in_trd = x_in_sqd * x_in
    y_in_sqd = y_in*y_in
    y_in_trd = y_in_sqd * y_in

    temp = coeff[0]
    temp += coeff[1] * x_in
    temp += coeff[2] * y_in
    temp += coeff[3] * x_in_sqd
    temp += coeff[4] * y_in_sqd
    temp += coeff[5] * x_in_trd
    temp += coeff[6] * y_in_trd
    temp += coeff[7] * x_in * y_in
    temp += coeff[8] * x_in_sqd * y_in
    temp += coeff[9] * x_in * y_in_sqd

    return temp

def formula_for_uncertainty_degr(coeff, z_c, x_in, y_in, z):
    temp = 0.

    x_in_sqd = x_in*x_in
    x_in_trd = x_in_sqd * x_in
    y_in_sqd = y_in*y_in
    y_in_trd = y_in_sqd * y_in

    temp += coeff[0]
    temp += coeff[1] * y_in
    temp += coeff[2] * y_in_sqd
    temp += coeff[3] * y_in_trd
    temp += coeff[4] * x_in
    temp += coeff[5] * x_in * y_in
    temp += coeff[6] * x_in * y_in_sqd
    temp += coeff[7] * x_in * y_in_trd
    temp += coeff[8] * x_in_sqd
    temp += coeff[9] * x_in_sqd * y_in
    temp += coeff[10] * x_in_sqd * y_in_sqd
    temp += coeff[11] * x_in_sqd * y_in_trd
    temp += coeff[12] * x_in_trd
    temp += coeff[13] * x_in_trd * y_in
    temp += coeff[14] * x_in_trd * y_in_sqd
    temp += coeff[15] * x_in_trd *y_in_trd
    return temp + z_c*(z-1.)*( 1./(0.25*z + 0.25))
