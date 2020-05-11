import fits.fit_formula as fit_formula

def g_coeff_for_massratio_median(x_in, y_in):
    value = 0.
    # coefficients
    coeff = [6.7760600911746053E+01,
            8.0095393231883766E-05,
            8.7799287507532679E-03,
            -8.3094231933430215E-04
            ]

    value = fit_formula.formula_for_single_coeff(coeff, x_in, y_in)
    return value

def g_coeff_for_massratio_68lower(x_in, y_in):
    value = 0.

    coeff = [1.5314881606912172E+02,
            1.0094163016958356E-03,
            9.2153190824952325E-03,
            -9.3933552814110519E-04
            ]

    value = fit_formula.formula_for_single_coeff(coeff, x_in, y_in)
    return value

def h_coeff_for_massratio_68upper(x_in, y_in):
    value = 0.

    coeff = [5.2722073109081853E+00,
            1.8214301124367492E-04,
            1.7111971528211371E-03,
            -1.9146255493615862E-04
            ]

    value = fit_formula.formula_for_single_coeff(coeff, x_in, y_in)
    return value

def g_coeff_for_massratio_95lower(x_in, y_in):
    value = 0.

    coeff = [8.5021387079558497E+02,
            1.3229835907117282E-03,
            9.8383387936712783E-03,
            -1.0797718232918386E-03
            ]

    value = fit_formula.formula_for_single_coeff(coeff, x_in, y_in)
    return value

def g_coeff_for_massratio_95upper(x_in, y_in):
    value = 0.

    coeff = [-7.9836201862996560E+01,
            -3.2167518242546801E-04,
            1.7909265087543013E-03,
            2.3068359733899473E-04
            ]

    value = fit_formula.formula_for_single_coeff(coeff, x_in, y_in)
    return value

def median(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [1.1122136205510805E+02,
            -1.3237937071695352E+01,
            -6.2391762181895780E+00,
            8.5329856288318595E-01,
            -1.9237105440281439E+02,
            g_coeff_for_massratio_median(z, y_in),
            -5.8134549786472949E+00,
            -7.6827371200429151E-03,
            5.4779230147318650E+01,
            -2.1489938425448898E+01,
            2.4462260072031765E+00,
            -6.7153107415983015E-02,
            -4.2842995636895926E+00,
            1.7446116861367225E+00,
            -2.1440870534554457E-01,
            7.3079134967724002E-03
            ]

    z_c = 0.359816614542
    value = fit_formula.formula_for_uncertainty(coeff, z_c, x_in, y_in, z)
    return value

def quantile_68lower(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [4.0389188178526143E+02,
            -1.5250551310110501E+02,
            1.5512989085050922E+01,
            -2.6179965467387722E-01,
            -3.7144201791474819E+02,
            g_coeff_for_massratio_68lower(z, y_in),
            -1.9195813118287923E+01,
            6.8098753674879298E-01,
            8.9849773318541850E+01,
            -3.8254620683271682E+01,
            5.0816919654471384E+00,
            -2.0328648701310925E-01,
            -6.4682047265150224E+00,
            2.7900751528199881E+00,
            -3.7913001639504884E-01,
            1.5841057467412156E-02
            ]

    z_c = 0.35045568790425
    value = fit_formula.formula_for_uncertainty(coeff, z_c, x_in, y_in, z)
    return value

def quantile_68upper(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [-1.3290837161371786E+02,
            1.0025483084638451E+02,
            -2.3595207016195545E+01,
            1.7276518411712671E+00,
            -3.6698508862303910E+01,
            -4.5963903830578419E+00,
            h_coeff_for_massratio_68upper(z, y_in),
            -5.6772507174265252E-01,
            2.3238141477892437E+01,
            -6.8044080613838638E+00,
            1.9059675575438773E-01,
            4.7122195834390368E-02,
            -2.2388722869425433E+00,
            7.9187538703996596E-01,
            -6.7923795075541804E-02,
            -1.2534228061156227E-04
            ]

    z_c = 0.359816614542
    value = fit_formula.formula_for_uncertainty(coeff, z_c, x_in, y_in, z)
    return value

def quantile_95lower(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [2.6704487996529711E+03,
            -1.2606642961676357E+03,
            1.9357038157728718E+02,
            -9.6592012449824178E+00,
            -1.7934163237584899E+03,
            g_coeff_for_massratio_95lower(z, y_in),
            -1.3153550269515063E+02,
            6.6284302500794041E+00,
            3.7917131301225589E+02,
            -1.8043504049618127E+02,
            2.8059365938876816E+01,
            -1.4233821582621999E+00,
            -2.5566316529023567E+01,
            1.2196111116049000E+01,
            -1.9030583140170165E+00,
            9.6982333713413027E-02
            ]

    z_c = 0.359816614542
    value = fit_formula.formula_for_uncertainty(coeff, z_c, x_in, y_in, z)
    return value

def quantile_95upper(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [-3.9208917643599367E+02,
            2.2579906744746447E+02,
            -4.3612762086350564E+01,
            2.7803381338559907E+00,
            1.1972187522510883E+02,
            g_coeff_for_massratio_95upper(z, y_in),
            1.7206575069822847E+01,
            -1.1923617876521639E+00,
            -6.7690317468235914E+00,
            7.5662950802307130E+00,
            -2.0797038080757799E+00,
            1.6553807594850412E-01,
            -3.6784296392653926E-01,
            -9.8959685637238337E-02,
            7.2042955086622840E-02,
            -7.3867905826148217E-03
            ]

    z_c = 0.34860010661775
    value = fit_formula.formula_for_uncertainty(coeff, z_c, x_in, y_in, z)
    return value
