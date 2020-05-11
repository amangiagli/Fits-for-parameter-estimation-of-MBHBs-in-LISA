import fits.fit_formula as fit_formula

def g_coeff_for_massratio_degr_median(x_in, y_in):
    value = 0.
    # coefficients
    coeff = [-1.0236437813566958E+02,
            -1.5468190118352154E-05,
            -3.6991219718467516E-03,
            -1.3188145829750534E-05,
            7.1978459694893430E-04,
            6.1766555285030513E-05
            ]

    value = fit_formula.formula_for_single_coeff_degr(coeff, x_in, y_in)
    return value

def h_coeff_for_massratio_degr_68lower(x_in, y_in):
    value = 0.

    coeff = [1.3255942507904699E+01,
            -4.0748712654456772E-05,
            -9.1325992759582288E-04,
            7.7441928237329306E-05,
            2.7819425200293301E-04,
            -2.3624067675064862E-05
            ]

    value = fit_formula.formula_for_single_coeff_degr(coeff, x_in, y_in)
    return value

def g_coeff_for_massratio_degr_68upper(x_in, y_in):
    value = 0.

    coeff = [-1.9675465747321402E+02,
            -5.1323494518426007E-04,
            -4.4461999734676204E-03,
            3.9320333057659860E-04,
            3.0250511471078016E-04,
            6.4338102008186233E-05
            ]

    value = fit_formula.formula_for_single_coeff_degr(coeff, x_in, y_in)
    return value

def h_coeff_for_massratio_degr_95lower(x_in, y_in):
    value = 0.

    coeff = [-1.1047091785769783E+02,
            7.0302405662810993E-05,
            4.3494092117796051E-05,
            -1.0163021368379791E-04,
            1.5822557592116057E-04,
            -6.7065458254060182E-07
            ]

    value = fit_formula.formula_for_single_coeff_degr(coeff, x_in, y_in)
    return value

def h_coeff_for_massratio_degr_95upper(x_in, y_in):
    value = 0.

    coeff = [4.3971846644760674E+01,
            -2.9252419579997157E-04,
            -2.3512447750447876E-03,
            3.4020182369953462E-04,
            3.5180551395222161E-04,
            -4.2898439172132127E-05
            ]

    value = fit_formula.formula_for_single_coeff_degr(coeff, x_in, y_in)
    return value

def median(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [-3.7757817992650030E+02,
            2.4591068045645105E+02,
            -5.1696162898553304E+01,
            3.4915073025982597E+00,
            1.2889369373230198E+02,
            g_coeff_for_massratio_degr_median(z, y_in),
            2.4019387654367968E+01,
            -1.7381871421690605E+00,
            -1.6275114415939562E+01,
            1.6092818864769374E+01,
            -4.1347430418741320E+00,
            3.1393459758453446E-01,
            9.2635479705335921E-01,
            -1.0058780295676080E+00,
            2.6607178179250468E-01,
            -2.0436547601718758E-02
            ]

    z_c = 0.3612267063992481
    value = fit_formula.formula_for_uncertainty_degr(coeff, z_c, x_in, y_in, z)
    return value

def quantile_68lower(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [-1.3345301786377374E+02,
            1.3088418536752886E+02,
            -3.3953513083215789E+01,
            2.5947694107776176E+00,
            -1.8309060213370934E+01,
            -3.2866925890160353E+01,
            h_coeff_for_massratio_degr_68lower(z, y_in),
            -1.1913852271741385E+00,
            1.2570903112305297E+01,
            2.4171701192360846E+00,
            -2.0048597878981700E+00,
            2.0498247169654249E-01,
            -8.9864517589466786E-01,
            -1.3699375805686786E-01,
            1.2995308692929797E-01,
            -1.3421154802529145E-02
            ]

    z_c = 0.3535346468954887
    value = fit_formula.formula_for_uncertainty_degr(coeff, z_c, x_in, y_in, z)
    return value

def quantile_68upper(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [-6.9359700997068308E+02,
            3.9411174715068643E+02,
            -7.4590140556169743E+01,
            4.6575117044023031E+00,
            3.3012442343317576E+02,
            g_coeff_for_massratio_degr_68upper(z, y_in),
            3.8623111044116328E+01,
            -2.4834720982310738E+00,
            -5.7547247144940691E+01,
            3.5490233646177060E+01,
            -7.1431552266075098E+00,
            4.6791643350330503E-01,
            3.6746087728280221E+00,
            -2.2997788029950375E+00,
            4.6720200983692450E-01,
            -3.0760109154414295E-02
            ]

    z_c = 0.3442742143067669
    value = fit_formula.formula_for_uncertainty_degr(coeff, z_c, x_in, y_in, z)
    return value

def quantile_95lower(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [2.2912742300556333E+03,
            -1.0636052150470962E+03,
            1.5963001353543299E+02,
            -7.7233077824021201E+00,
            -1.5580518746314297E+03,
            7.2797010980585503E+02,
            h_coeff_for_massratio_degr_95lower(z, y_in),
            5.4268050219803001E+00,
            3.3013514807283394E+02,
            -1.5495528729579982E+02,
            2.3668905207833269E+01,
            -1.1730145405658163E+00,
            -2.2133760416320285E+01,
            1.0413645826849525E+01,
            -1.5962850201934202E+00,
            7.9522067003381380E-02
            ]

    z_c = 0.35296969958909774
    value = fit_formula.formula_for_uncertainty_degr(coeff, z_c, x_in, y_in, z)
    return value

def quantile_95upper(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [-8.4437424557915210E+02,
            4.6296205419751499E+02,
            -8.4837369921004580E+01,
            5.1555866092458453E+00,
            4.1334224276122143E+02,
            -2.3375040113495123E+02,
            h_coeff_for_massratio_degr_95upper(z, y_in),
            -2.7345485375017198E+00,
            -7.2037697182364369E+01,
            4.1749661868701999E+01,
            -8.0162417543974094E+00,
            5.0707109977412301E-01,
            4.5191974863700475E+00,
            -2.6528166859160240E+00,
            5.1433851165711530E-01,  
            -3.2746694526110787E-02
            ]

    z_c = 0.3351163261973684
    value = fit_formula.formula_for_uncertainty_degr(coeff, z_c, x_in, y_in, z)
    return value
