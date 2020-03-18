import fits.fit_formula as fit_formula

def a_coeff_dl_merger_below3e6_median(x_in):
    value = 0.
    # coefficients
    coeff = [1.9581265544714911E-05,
            -2.0110584514536130E-02,
            2.8279461534581239E-04,
            -1.3599915516964789E-04,
            1.9030595522340092E-05
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in)
    return value

def a_coeff_dl_merger_above3e6_median(x_in):
    value = 0.
    # coefficients
    coeff = [1.2038396087691276E-06,
            -4.9449950936695693E-03,
            1.8619895111897702E-05,
            -8.7130120817819007E-06,
            1.1815963708583502E-06
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in)
    return value

def a_coeff_for_dl_below3e6_68lower(x_in, y_in):
    value = 0.

    coeff = [1.2572903425167386E-05,
            -1.6239261913710203E-02,
            1.9807488371879436E-04,
            -9.4810605044260633E-05,
            1.3080634860449378E-05
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value

def a_coeff_for_dl_above3e6_68lower(x_in, y_in):
    value = 0.

    coeff = [1.3356240046733745E-06,
            -5.0954087822570170E-03,
            2.1969343620152812E-05,
            -1.0492800522535053E-05,
            1.4485779005890338E-06
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value


def a_coeff_for_dl_below3e6_68upper(x_in, y_in):
    value = 0.

    coeff = [2.7113695868779926E-05,
            -2.2383085188973889E-02,
            3.9968595771495714E-04,
            -1.8728987892176028E-04,
            2.5631851224350754E-05
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value

def a_coeff_for_dl_above3e6_68upper(x_in, y_in):
    value = 0.

    coeff = [1.4635759919549340E-06,
            -5.0384477825184404E-03,
            2.2827907987243488E-05,
            -1.0808022566871513E-05,
            1.4798313623122579E-06
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value


def a_coeff_for_dl_below3e6_95lower(x_in, y_in):
    value = 0.

    coeff = [1.3056113690177544E-05,
            -1.5910706421302483E-02,
            2.0487836309913613E-04,
            -9.7553566594138990E-05,
            1.3505998479235331E-05
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value

def a_coeff_for_dl_above3e6_95lower(x_in, y_in):
    value = 0.

    coeff = [4.8976192739275615E-06,
            -9.2543564179901443E-03,
            7.7716968122175132E-05,
            -3.6444159457347715E-05,
            4.9934736694135425E-06
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value

def a_coeff_for_dl_below3e6_95upper(x_in, y_in):
    value = 0.

    coeff = [1.3689033581651044E-05,
            -1.5424761427772413E-02,
            2.1454588055064120E-04,
            -1.0258462099971413E-04,
            1.4267731381563152E-05
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value

def a_coeff_for_dl_above3e6_95upper(x_in, y_in):
    value = 0.

    coeff = [6.6966303841735863E-07,
            -3.5036930962991236E-03,
            1.0800141220712155E-05,
            -5.0629371935289001E-06,
            6.8715251733703672E-07
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
