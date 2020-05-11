import fits.fit_formula as fit_formula

def g_coeff_for_mchirp_degr_median(x_in, y_in):
    value = 0.
    # coefficients
    coeff = [-4.5665393412012115E+01,
            -3.0355761550341639E-04,
            -4.3387039954587885E-03,
            2.1567149256430032E-04,
            1.0594528187896908E-03,
            -1.0087265701210423E-05
            ]

    value = fit_formula.formula_for_single_coeff_degr(coeff, x_in, y_in)
    return value

def g_coeff_for_mchirp_degr_68lower(x_in, y_in):
    value = 0.

    coeff = [2.9410274532176395E+01,
            -1.7235836661537573E-04,
            -4.9486057131789395E-03,
            3.5409334225687316E-04,
            1.4831335845725874E-03,
            -9.5738355526089414E-05
            ]

    value = fit_formula.formula_for_single_coeff_degr(coeff, x_in, y_in)
    return value

def g_coeff_for_mchirp_degr_68upper(x_in, y_in):
    value = 0.

    coeff = [-1.4713868824728985E+02,
            -6.0806298927742390E-04,
            -5.5971499410283499E-03,
            4.9881286489466756E-04,
            4.6053646600479844E-04,
            6.3218981624986784E-05
            ]

    value = fit_formula.formula_for_single_coeff_degr(coeff, x_in, y_in)
    return value

def g_coeff_for_mchirp_degr_95lower(x_in, y_in):
    value = 0.

    coeff = [8.5167896394206628E+02,
            3.9297811168918274E-04,
            1.2599662602632456E-03,
            -8.3875243304764040E-04,
            2.2938091204756299E-04,
            1.4048387098943184E-04
            ]

    value = fit_formula.formula_for_single_coeff_degr(coeff, x_in, y_in)
    return value

def g_coeff_for_mchirp_degr_95upper(x_in, y_in):
    value = 0.

    coeff = [-2.0206168253181784E+02,
            -1.0773601431434184E-03,
            -7.0606643290558047E-03,
            8.7893720389087184E-04,
            5.0547043170458099E-04,
            2.7359187488140268E-05
            ]

    value = fit_formula.formula_for_single_coeff_degr(coeff, x_in, y_in)
    return value

def median(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [-2.0750761608577693E+02,
            1.5861081896955889E+02,
            -3.6919876082811854E+01,
            2.6648442969478729E+00,
            1.8301621903164712E+01,
            g_coeff_for_mchirp_degr_median(z, y_in),
            1.4407092232126228E+01,
            -1.1993976979890366E+00,
            6.4866587580750004E+00,
            4.4128240621014347E+00,
            -2.1525099898846936E+00,
            2.0269239106144354E-01,
            -5.8157111154880470E-01,
            -2.3161911642217925E-01,
            1.3457904372290841E-01,
            -1.3051264134048779E-02
            ]

    z_c = 0.35060618803120297
    value = fit_formula.formula_for_uncertainty_degr(coeff, z_c, x_in, y_in, z)
    return value

def quantile_68lower(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [5.2978518208808651E+01,
            3.5381997097271729E+01,
            -1.7814273749894234E+01,
            1.6930538140408400E+00,
            -1.3995232030031266E+02,
            g_coeff_for_mchirp_degr_68lower(z, y_in),
            2.7098874357917797E+00,
            -6.0082549942397456E-01,
            3.7699014146353036E+01,
            -1.0461480521082313E+01,
            1.7881891585445819E-01,
            8.2514838286962267E-02,
            -2.5687116616731340E+00,
            7.1959942634471452E-01,
            -1.5416449578439462E-02,
            -5.2602258193132911E-03
            ]

    z_c = 0.3542061792890977
    value = fit_formula.formula_for_uncertainty_degr(coeff, z_c, x_in, y_in, z)
    return value

def quantile_68upper(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [-5.4555388067796264E+02,
            3.1808090875470560E+02,
            -6.1721618049077570E+01,
            3.9375937259508649E+00,
            2.3332513376019543E+02,
            g_coeff_for_mchirp_degr_68upper(z, y_in),
            3.0214569394800513E+01,
            -2.0123195562972356E+00,
            -3.7580740070400658E+01,
            2.5249811915193099E+01,
            -5.4063001193342561E+00,
            3.7050196080064524E-01,
            2.3509719659283626E+00,
            -1.6206618718594701E+00,
            3.5196408969452619E-01,
            -2.4292875687592641E-02
            ]

    z_c = 0.34467532294774433
    value = fit_formula.formula_for_uncertainty_degr(coeff, z_c, x_in, y_in, z)
    return value

def quantile_95lower(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [2.6785029941521548E+03,
            -1.2618588361220379E+03,
            1.9315870111028732E+02,
            -9.5982148478495741E+00,
            -1.7994059638836768E+03,
            g_coeff_for_mchirp_degr_95lower(z, y_in),
            -1.3144651776987618E+02,
            6.6030779337020533E+00,
            3.7832096287001139E+02,
            -1.7969650735421376E+02,
            2.7872087356015818E+01,
            -1.4092234799173582E+00,
            -2.5249278928753750E+01,
            1.2015602135415349E+01,
            -1.8688648020703340E+00,
            9.4866689107902857E-02
            ]

    z_c = 0.3536044677233083
    value = fit_formula.formula_for_uncertainty_degr(coeff, z_c, x_in, y_in, z)
    return value

def quantile_95upper(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [-7.4940405168837333E+02,
            4.1416320400132372E+02,
            -7.6589013134561313E+01,
            4.6950046078692509E+00,
            3.5144771234370751E+02,
            g_coeff_for_mchirp_degr_95upper(z, y_in),
            3.8607902421475437E+01,
            -2.4346233912502679E+00,
            -5.9325172502605525E+01,
            3.5240111878740393E+01,
            -6.9137307427265480E+00,
            4.4533582759153489E-01,
            3.6781340555308777E+00,
            -2.2221261181924277E+00,
            4.4137155485960733E-01,   
            -2.8658571007099454E-02
            ]

    z_c = 0.3336238385300752
    value = fit_formula.formula_for_uncertainty_degr(coeff, z_c, x_in, y_in, z)
    return value
