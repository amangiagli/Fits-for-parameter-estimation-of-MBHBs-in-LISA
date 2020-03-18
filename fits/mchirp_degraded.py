import fits.fit_formula as fit_formula

def g_coeff_for_mchirp_degr_median(x_in, y_in):
    value = 0.
    # coefficients
    coeff = [4.9356760652761318E+02,
            -1.5458109169748664E-04,
            5.8825316232961258E-05,
            -2.1326315588932892E-04,
            -3.5624545550965814E-04,
            1.6606782659482299E-04
            ]

    value = fit_formula.formula_for_single_coeff_degr(coeff, x_in, y_in)
    return value

def g_coeff_for_mchirp_degr_68lower(x_in, y_in):
    value = 0.

    coeff = [6.6533575499940412E+02,
            -3.6183723175467063E-03,
            -4.3204859295019275E-03,
            4.6824411356245006E-04,
            2.8539980000382185E-04,
            5.7163362407171465E-04
            ]

    value = fit_formula.formula_for_single_coeff_degr(coeff, x_in, y_in)
    return value

def g_coeff_for_mchirp_degr_68upper(x_in, y_in):
    value = 0.

    coeff = [3.9430966287525195E+02,
            -7.8073833211267608E-03,
            -9.1857168232683927E-03,
            4.3554791438106598E-04,
            6.1203057274841245E-04,
            1.2500033972538587E-03
            ]

    value = fit_formula.formula_for_single_coeff_degr(coeff, x_in, y_in)
    return value

def g_coeff_for_mchirp_degr_95lower(x_in, y_in):
    value = 0.

    coeff = [1.0054509431531163E+03,
            1.6941545169226146E-04,
            -1.9853173647871973E-03,
            2.7648698395681202E-04,
            1.1041027124774525E-03,
            -9.3676921018837886E-05
            ]

    value = fit_formula.formula_for_single_coeff_degr(coeff, x_in, y_in)
    return value

def g_coeff_for_mchirp_degr_95upper(x_in, y_in):
    value = 0.

    coeff = [3.9958739777008634E+02,
            -4.1272519158360036E-03,
            -3.6788733672329238E-02,
            6.1197691178649320E-03,
            7.9361378526929087E-03,
            -1.2569919905248638E-03
            ]

    value = fit_formula.formula_for_single_coeff_degr(coeff, x_in, y_in)
    return value

def median(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [1.3739973534401458E+03,
            -6.5787166447424806E+02,
            1.0229466133174714E+02,
            -5.1792379852675312E+00,
            -1.0302817220788777E+03,
            g_coeff_for_mchirp_degr_median(z, y_in),
            -7.7318920720956854E+01,
            3.9629198561064527E+00,
            2.3324726211633418E+02,
            -1.1194706913152207E+02,
            1.7614873556037733E+01,
            -9.0910216984337922E-01,
            -1.6721713971316099E+01,
            8.0411017320048117E+00,
            -1.2698374672475410E+00,
            6.5913468330109026E-02
            ]

    z_c = 0.35060618803120297
    value = fit_formula.formula_for_uncertainty_degr(coeff, z_c, x_in, y_in, z)
    return value

def quantile_68lower(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [2.0495121678635182E+03,
            -9.7235457951099875E+02,
            1.5055926821775913E+02,
            -7.6239665835118791E+00,
            -1.4019122210137225E+03,
            g_coeff_for_mchirp_degr_68lower(z, y_in),
            -1.0351209882871417E+02,
            5.2819368371780158E+00,
            3.0071975949907676E+02,
            -1.4295121219735944E+02,
            2.2317133882958501E+01,
            -1.1446344050592359E+00,
            -2.0731377824460292E+01,
            9.8725242003408304E+00,
            -1.5458916643688099E+00,
            7.9653081808032766E-02
            ]

    z_c = 0.3542061792890977
    value = fit_formula.formula_for_uncertainty_degr(coeff, z_c, x_in, y_in, z)
    return value

def quantile_68upper(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [9.8547460603303375E+02,
            -4.7904060998021731E+02,
            7.5277171195885487E+01,
            -3.8388950580452068E+00,
            -8.1095021155902214E+02,
            g_coeff_for_mchirp_degr_68upper(z, y_in),
            -6.2562641511660232E+01,
            3.2434985287885212E+00,
            1.9271025578146208E+02,
            -9.3875889173207696E+01,
            1.4974141161010492E+01,
            -7.8281448434231038E-01,
            -1.4301074688144546E+01,
            6.9810669827683931E+00,
            -1.1181765852162329E+00,
            5.8845769678157467E-02
            ]

    z_c = 0.34467532294774433
    value = fit_formula.formula_for_uncertainty_degr(coeff, z_c, x_in, y_in, z)
    return value

def quantile_95lower(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [3.2172634229393393E+03,
            -1.5340463952409702E+03,
            2.3974284763416000E+02,
            -1.2298423957909565E+01,
            -2.1078591329608726E+03,
            g_coeff_for_mchirp_degr_95lower(z, y_in),
            -1.5764637800873118E+02,
            8.1272673344967643E+00,
            4.4069382042367317E+02,
            -2.1055116927425527E+02,
            3.3105460062854334E+01,
            -1.7133684526627349E+00,
            -2.9727900896963376E+01,
            1.4225494072740695E+01,
            -2.2420667966426606E+00,
            1.1643842736157239E-01
            ]

    z_c = 0.3536044677233083
    value = fit_formula.formula_for_uncertainty_degr(coeff, z_c, x_in, y_in, z)
    return value

def quantile_95upper(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [9.3081929372525497E+02,
            -4.6274611159148435E+02,
            7.4605862798213167E+01,
            -3.9215727263790194E+00,
            -8.0504952259556615E+02,
            g_coeff_for_mchirp_degr_95upper(z, y_in),
            -6.4875708886281160E+01,
            3.4525373315367673E+00,
            1.9850525540633021E+02,
            -9.8658140291993703E+01,
            1.6087824185573620E+01,
            -8.6196973866745452E-01,
            -1.5187072300988923E+01,
            7.5628322467430511E+00,
            -1.2378984716911248E+00,
            6.6711517979399559E-02
            ]

    z_c = 0.3336238385300752
    value = fit_formula.formula_for_uncertainty_degr(coeff, z_c, x_in, y_in, z)
    return value
