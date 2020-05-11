import fits.fit_formula as fit_formula

def h_coeff_for_skyloc_median(x_in, y_in):
    value = 0.
    # coefficients
    coeff = [-1.2998569358666512E+02,
            -2.5407666734371414E-04,
            -2.2575081789341788E-03,
            4.8233028991520360E-04
            ]

    value = fit_formula.formula_for_single_coeff(coeff, x_in, y_in)
    return value

def h_coeff_for_skyloc_68lower(x_in, y_in):
    value = 0.

    coeff = [-1.6455304689229274E+02,
            -2.1558079036731862E-04,
            -2.1047119580990988E-03,
            4.4831576725083271E-04
            ]

    value = fit_formula.formula_for_single_coeff(coeff, x_in, y_in)
    return value

def h_coeff_for_skyloc_68upper(x_in, y_in):
    value = 0.

    coeff = [-7.7372880766603473E+01,
            -5.0404870799591818E-04,
            -1.6330226187266648E-03,
            4.2637194717641530E-04
            ]

    value = fit_formula.formula_for_single_coeff(coeff, x_in, y_in)
    return value

def h_coeff_for_skyloc_95lower(x_in, y_in):
    value = 0.

    coeff = [-1.8387702050020783E+02,
            -4.3383947238852775E-04,
            -3.0634804127408124E-03,
            5.9519360784229651E-04
            ]

    value = fit_formula.formula_for_single_coeff(coeff, x_in, y_in)
    return value

def h_coeff_for_skyloc_95upper(x_in, y_in):
    value = 0.

    coeff = [-2.5305792594533123E+01,
            -6.6028067061252218E-04,
            -2.0242686392157152E-03,  
            4.6797257314495704E-04
            ]

    value = fit_formula.formula_for_single_coeff(coeff, x_in, y_in)
    return value

def median(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [2.5682794698562793E+03,
            -1.2088867458262862E+03,
            1.8441276102638886E+02,
            -9.1358588450798983E+00,
            -1.7966725729005454E+03,
            8.4684724050324257E+02,
            h_coeff_for_skyloc_median(z, y_in),
            6.4995221230976465E+00,
            3.8967032205367116E+02,
            -1.8379560920858785E+02,
            2.8282010689190667E+01,
            -1.4198129953538099E+00,
            -2.6699734405440108E+01,
            1.2592899734271874E+01,
            -1.9396274786117975E+00,
            9.7576939343500868E-02
            ]

    z_c = 0.753336858154
    value = fit_formula.formula_for_uncertainty(coeff, z_c, x_in, y_in, z)
    return value

def quantile_68lower(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [3.5127180632786244E+03,
            -1.6260377884336460E+03,
            2.4543186500104008E+02,
            -1.2081778549458440E+01,
            -2.3444842968404409E+03,
            1.0859195836516317E+03,
            h_coeff_for_skyloc_68lower(z, y_in),
            8.1482265319464986E+00,
            4.9104598404312981E+02,
            -2.2731428602521220E+02,
            3.4461695876504905E+01,
            -1.7088466384278149E+00,
            -3.2744043469738600E+01,
            1.5135220328177340E+01,
            -2.2921364003566680E+00,
            1.1362260623309339E-01,
            ]

    z_c = 0.744398474179
    value = fit_formula.formula_for_uncertainty(coeff, z_c, x_in, y_in, z)
    return value

def quantile_68upper(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [1.5775769285035890E+03,
            -7.3127530118471304E+02,
            1.0931029452773879E+02,
            -5.2971435299831624E+00,
            -1.1082983482596171E+03,
            5.1370292692164276E+02,
            h_coeff_for_skyloc_68upper(z, y_in),
            3.7997753747143825E+00,
            2.4522223883340030E+02,
            -1.1386720374795571E+02,
            1.7238101098629254E+01,
            -8.5326653984364498E-01,
            -1.7239197760462620E+01,
            8.0199722318598887E+00,
            -1.2189237701759765E+00,
            6.0702890555717204E-02,
            ]

    z_c = 0.757431626681
    value = fit_formula.formula_for_uncertainty(coeff, z_c, x_in, y_in, z)
    return value

def quantile_95lower(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [3.8741083764096511E+03,
            -1.7970393784813259E+03,
            2.7221144086706954E+02,
            -1.3475152060792460E+01,
            -2.6029953747213290E+03,
            1.2087319005253571E+03,
            h_coeff_for_skyloc_95lower(z, y_in),
            9.1581119863286631E+00,
            5.4871842191002747E+02,
            -2.5480018655181109E+02,
            3.8797776002176334E+01,
            -1.9359222221073082E+00,
            -3.6799313006832733E+01,
            1.7072758299717123E+01,
            -2.5983306041991341E+00,
            1.2968059503032237E-01,
            ]

    z_c = 0.744398474179
    value = fit_formula.formula_for_uncertainty(coeff, z_c, x_in, y_in, z)
    return value

def quantile_95upper(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [2.9713141934541613E+02,
            -1.6819762659514268E+02,
            2.8855798927140341E+01,
            -1.5699380191075194E+00,
            -2.8900747293616320E+02,
            1.5182645049148269E+02,
            h_coeff_for_skyloc_95upper(z, y_in),
            1.3667791382659343E+00,
            7.9197529450118637E+01,
            -4.0380800240963929E+01,
            6.6287904623957745E+00,
            -3.5538272899979617E-01,
            -6.4425618496952959E+00,
            3.2388459100054625E+00,
            -5.2786764481177428E-01,
            2.8226874185207862E-02,
            ]

    z_c =  0.77847203374
    value = fit_formula.formula_for_uncertainty(coeff, z_c, x_in, y_in, z)
    return value
