import fits.fit_formula as fit_formula

def a_coeff_dl_merger_below3e6_median(x_in):
    value = 0.
    # coefficients
    coeff = [1.9147454482918484E-05,
            -2.0082922342517996E-02,
            2.8455779390319205E-04,
            -1.3818538872270879E-04,
            1.9466950970646528E-05
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in)
    return value

def a_coeff_dl_merger_above3e6_median(x_in):
    value = 0.
    # coefficients
    coeff = [1.3969415365922027E-06,
            -4.9447211248042165E-03,
            2.0873094040065287E-05,
            -9.8464892636526637E-06,
            1.3461724163140343E-06
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in)
    return value

def a_coeff_for_dl_below3e6_68lower(x_in, y_in):
    value = 0.

    coeff = [1.3148283865171910E-05,
            -1.6227060938199728E-02,
            2.0203253979051669E-04,
            -9.8520752516164398E-05,
            1.3884473165756440E-05
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value

def a_coeff_for_dl_above3e6_68lower(x_in, y_in):
    value = 0.

    coeff = [1.3852762292521566E-06,
            -5.0945807664646153E-03,
            2.1944387986613031E-05,
            -1.0411244776682639E-05,
            1.4407856124930354E-06
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value


def a_coeff_for_dl_below3e6_68upper(x_in, y_in):
    value = 0.

    coeff = [2.6960341930421476E-05,
            -2.2341029660214957E-02,
            3.8892175294325768E-04,
            -1.8271576936420861E-04,
            2.5192329187856057E-05
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value

def a_coeff_for_dl_above3e6_68upper(x_in, y_in):
    value = 0.

    coeff = [1.3990768653911720E-06,
            -5.0351127989659815E-03,
            2.1245473721604422E-05,
            -1.0272056309160323E-05,
            1.4240036465783068E-06
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value


def a_coeff_for_dl_below3e6_95lower(x_in, y_in):
    value = 0.

    coeff = [1.3126571116312916E-05,
            -1.5893545792551353E-02,
            1.9817772972651561E-04,
            -9.3729930085532622E-05,
            1.2859590635301845E-05
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value

def a_coeff_for_dl_above3e6_95lower(x_in, y_in):
    value = 0.

    coeff = [4.6128460455476095E-06,
            -9.2447152324990588E-03,
            6.8999016656315847E-05,
            -3.2555204548518398E-05,
            4.4694655714690859E-06
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value

def a_coeff_for_dl_below3e6_95upper(x_in, y_in):
    value = 0.

    coeff = [1.2981486649549587E-05,
            -1.5404131481153072E-02,
            2.0572291267783173E-04,
            -9.8089981494373882E-05,
            1.3702530318009015E-05
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value

def a_coeff_for_dl_above3e6_95upper(x_in, y_in):
    value = 0.

    coeff = [7.1983950063687095E-07,
            -3.5031054974054981E-03,
            1.0988244507292560E-05,
            -5.1206881943507378E-06,
            6.9176952849074536E-07
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value

def median_below3e6(x_in, y_in):
    value = 0.0
    # coefficients
    coeff = [a_coeff_dl_merger_below3e6_median(x_in),
            6.0883584347940598E+00,
            2.6990188112591529E+01,
            -3.8543642883892582E-01,
            -5.0583577679440968E+00,
            7.9450656242018636E-02,
            3.0698635097331284E-01,
            -1.8889554661700818E+00,
            -4.2879409927718548E-02,
            1.9481779733233484E-01
            ]

    value = fit_formula.formula_for_uncertainty_merger(coeff, x_in, y_in)
    return value

def median_above3e6(x_in, y_in):
    value = 0.0
    # coefficients
    coeff = [a_coeff_dl_merger_above3e6_median(x_in),
            3.0014543240922844E+01,
            7.7090859293570858E+01,
            -1.1700743460021761E+00,
            -9.9143103614152928E+00,
            9.1512878102704587E-02,
            4.2341782990045473E-01,
            -7.7822287270172747E+00,
            6.2015185729194844E-02,
            5.4011639798891942E-01
            ]

    value = fit_formula.formula_for_uncertainty_merger(coeff, x_in, y_in)
    return value

def quantile_below3e6_68lower(x_in, y_in):
    value = 0.0
    # coefficients
    coeff = [a_coeff_for_dl_below3e6_68lower(z, y_in),
            6.5691625245704861E+00,
            3.2902204461285343E+01,
            -3.9844503225840799E-01,
            -6.0465218010685371E+00,
            7.7153361156579781E-02,
            3.6112540124042614E-01,
            -2.0440630176155814E+00,
            -3.7953159429360395E-02,
            2.0607108369141258E-01
            ]

    value = fit_formula.formula_for_uncertainty_merger(coeff, x_in, y_in)
    return value

def quantile_above3e6_68lower(x_in, y_in):
    value = 0.0
    # coefficients
    coeff = [a_coeff_for_dl_above3e6_68lower(z, y_in),
            3.1886765465300929E+01,
            7.4578545814651918E+01,
            -1.1274142861581655E+00,
            -9.5723225214644376E+00,
            9.1047941603978000E-02,
            4.0747455370211938E-01,
            -8.3617635892803648E+00,
            5.6534543095522416E-02,
            5.8435991490551231E-01
            ]

    value = fit_formula.formula_for_uncertainty_merger(coeff, x_in, y_in)
    return value

def quantile_below3e6_68upper(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [a_coeff_for_dl_below3e6_68upper(z, y_in),
            5.9339407982024248E+00,
            2.4703192970334747E+01,
            -3.8577118272640537E-01,
            -4.6994854685850340E+00,
            8.0334968535042073E-02,
            2.8916206943542111E-01,
            -1.8422160094777602E+00,
            -4.3722549893413620E-02,
            1.9201534068839821E-01
            ]

    value = fit_formula.formula_for_uncertainty_merger(coeff, z_c, x_in, y_in, z)
    return value

def quantile_above3e6_68upper(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [a_coeff_for_dl_above3e6_68upper(z, y_in),
            3.1649671732493463E+01,
            7.4520572515247679E+01,
            -1.2357546070035830E+00,
            -9.3884526489778217E+00,
            9.3014166128206233E-02,
            3.9138389657712480E-01,
            -8.1875641979630291E+00,
            6.9925511517817007E-02,
            5.6499674636067887E-01
            ]

    value = fit_formula.formula_for_uncertainty_merger(coeff, z_c, x_in, y_in, z)
    return value

def quantile_below3e6_95lower(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [a_coeff_for_dl_below3e6_95lower(z, y_in),
            7.1343524709442425E+00,
            3.3239644401416101E+01,
            -4.0753289902485634E-01,
            -6.0585299676135325E+00,
            7.4617284772507508E-02,
            3.5891230636368565E-01,
            -2.2350129904974247E+00,
            -3.3728883924160180E-02,
            2.2131598663993723E-01
            ]

    value = fit_formula.formula_for_uncertainty_merger(coeff, z_c, x_in, y_in, z)
    return value

def quantile_above3e6_95lower(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [a_coeff_for_dl_above3e6_95lower(z, y_in),
            3.1075422472291670E+01,
            3.6196123054279091E+01,
            -1.1102599929459649E+00,
            -4.0334738949529951E+00,
            8.9416345365559646E-02,
            1.4191028210452217E-01,
            -8.1229419751942231E+00,
            5.5368346329004670E-02,
            5.6676921587453322E-01
            ]

    value = fit_formula.formula_for_uncertainty_merger(coeff, z_c, x_in, y_in, z)
    return value

def quantile_below3e6_95upper(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [a_coeff_for_dl_below3e6_95upper(z, y_in),
            5.5113114607002123E+00,
            3.6262757794532142E+01,
            -3.9276877734581467E-01,
            -6.8440297029232227E+00,
            8.1789669310811219E-02,
            4.2054785220783497E-01,
            -1.6968096327420032E+00,
            -4.4164152088848052E-02,
            1.8024389045218947E-01
            ]

    value = fit_formula.formula_for_uncertainty_merger(coeff, z_c, x_in, y_in, z)
    return value

def quantile_above3e6_95upper(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [a_coeff_for_dl_above3e6_95upper(z, y_in),
            3.3468857883325398E+01,
            1.1227099496418226E+02,
            -1.3161856749786589E+00,
            -1.4813508350572153E+01,
            9.3557211259584161E-02,
            6.5054235559041729E-01,
            -8.6685736639037678E+00,
            8.0763489069628935E-02,
            5.9664306201476069E-01
            ]

    value = fit_formula.formula_for_uncertainty_merger(coeff, z_c, x_in, y_in, z)
    return value
