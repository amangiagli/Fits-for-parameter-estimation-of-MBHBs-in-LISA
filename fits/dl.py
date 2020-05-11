import fits.fit_formula as fit_formula

def h_coeff_for_dl_median(x_in, y_in):
    value = 0.
    # coefficients
    coeff = [-4.8845056441915276E+01,
            -1.0938551223067465E-04,
            -8.1071305662013384E-04,
            1.8399310536946912E-04
            ]

    value = fit_formula.formula_for_single_coeff(coeff, x_in, y_in)
    return value

def h_coeff_for_dl_68lower(x_in, y_in):
    value = 0.

    coeff = [-6.9433922137158262E+01,
            -4.9368806581662536E-05,
            -5.1271876008367678E-04,
            1.3350613088496401E-04
            ]

    value = fit_formula.formula_for_single_coeff(coeff, x_in, y_in)
    return value

def h_coeff_for_dl_68upper(x_in, y_in):
    value = 0.

    coeff = [-3.7055075662374890E+01,
            -1.8049195265178815E-04,
            -6.0040308207535357E-04,
            1.6121933615096285E-04
            ]

    value = fit_formula.formula_for_single_coeff(coeff, x_in, y_in)
    return value

def h_coeff_for_dl_95lower(x_in, y_in):
    value = 0.

    coeff = [-9.0143953446931647E+01,
            -5.0351642922722730E-05,
            -4.8349766812840519E-04,
            1.3033861633190118E-04
            ]

    value = fit_formula.formula_for_single_coeff(coeff, x_in, y_in)
    return value

def c_coeff_for_dl_95upper(x_in, y_in):
    value = 0.

    coeff = [-2.5169988890711966E+01,
            -9.3891303428774277E-04,
            -4.1277788652912218E-03,  
            9.9912507438210682E-04
            ]

    value = fit_formula.formula_for_single_coeff(coeff, x_in, y_in)
    return value

def median(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [1.0057917317448487E+03,
            -4.5818576861152718E+02,
            6.7239660496558315E+01,
            -3.1844807301742639E+00,
            -7.1834142298801578E+02,
            3.2878696067250110E+02,
            h_coeff_for_dl_median(z, y_in),
            2.3557355917786058E+00,
            1.5820548279871630E+02,
            -7.2626824828993989E+01,
            1.0851539915743034E+01,
            -5.2782193780604869E-01,
            -1.0962379443152951E+01,
            5.0395502790162592E+00,
            -7.5515065245869328E-01,
            3.6906902496985236E-02
            ]

    z_c = 0.37956925304
    value = fit_formula.formula_for_uncertainty(coeff, z_c, x_in, y_in, z)
    return value

def quantile_68lower(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [1.5595829881344866E+03,
            -7.1106979083954172E+02,
            1.0518661269036690E+02,
            -5.0493961958289484E+00,
            -1.0245267187697998E+03,
            4.6731778504658951E+02,
            h_coeff_for_dl_68lower(z, y_in),
            3.3558277496666093E+00,
            2.1211316858149445E+02,
            -9.6741953563015841E+01,
            1.4389649784378197E+01,
            -6.9694751955358925E-01,
            -1.4018132549375236E+01,
            6.3882114506209042E+00,
            -9.4986576978219261E-01,
            4.6021686447716093E-02
            ]

    z_c = 0.380781280538
    value = fit_formula.formula_for_uncertainty(coeff, z_c, x_in, y_in, z)
    return value

def quantile_68upper(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [7.5697110447184843E+02,
            -3.4862848998468229E+02,
            5.1563862290366309E+01,
            -2.4593811863423753E+00,
            -5.3700536609489734E+02,
            2.4785231084077259E+02,
            h_coeff_for_dl_68upper(z, y_in),
            1.7983759230797585E+00,
            1.1812050420392515E+02,
            -5.4633397345299358E+01,
            8.2114040873891572E+00,
            -4.0187517750793234E-01,
            -8.1936855001345723E+00,
            3.7947059373361522E+00,
            -5.7207762690784136E-01,
            2.8145533137490020E-02
            ]

    z_c = 0.380781280538
    value = fit_formula.formula_for_uncertainty(coeff, z_c, x_in, y_in, z)
    return value

def quantile_95lower(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [1.9888416241269651E+03,
            -9.2141892917234691E+02,
            1.3911437229942968E+02,
            -6.8473417214736818E+00,
            -1.2856562403246389E+03,
            5.9544384421174709E+02,
            h_coeff_for_dl_95lower(z, y_in),
            4.4559490183320918E+00,
            2.6314755763326713E+02,
            -1.2182421992023200E+02,
            1.8451933848110457E+01,
            -9.1320347073613561E-01,
            -1.7245579748609714E+01,
            7.9770499940890893E+00,
            -1.2076919006570961E+00,
            5.9775529154421747E-02
            ]

    z_c = 0.380781280538
    value = fit_formula.formula_for_uncertainty(coeff, z_c, x_in, y_in, z)
    return value

def quantile_95upper(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [-2.6783174926735035E+02,
            1.4136198848292008E+02,
            c_coeff_for_dl_95upper(z, y_in),
            1.4809266799334615E+00,
            1.2911667656731572E+02,
            -7.0771158435387008E+01,
            1.2929737022157907E+01,
            -7.7395197783312142E-01,
            -1.9986563949760324E+01,
            1.1480894074380167E+01,
            -2.1781736076371496E+00,
            1.3393458697325045E-01,
            1.0153578542816051E+00,
            -6.1793684854471831E-01,
            1.2249641448323345E-01,
            -7.7482954494598744E-03
            ]

    z_c = 0.374955353836
    value = fit_formula.formula_for_uncertainty(coeff, z_c, x_in, y_in, z)
    return value
