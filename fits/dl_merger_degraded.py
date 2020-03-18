import fits.fit_formula as fit_formula

def a_coeff_dl_merger_below3e6_degr_median(x_in):
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

def a_coeff_dl_merger_above3e6_degr_median(x_in):
    value = 0.
    # coefficients
    coeff = [3.7254694751006140E-07,
            -2.6410243686203734E-03,
            5.8415246463056566E-06,
            -2.7106626263182776E-06,
            3.6677080356453210E-07
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in)
    return value

def a_coeff_for_dl_below3e6_degr_68lower(x_in, y_in):
    value = 0.

    coeff = [1.2572903425167386E-05,
            -1.6239261913710203E-02,
            1.9807488371879436E-04,
            -9.4810605044260633E-05,
            1.3080634860449378E-05
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value

def a_coeff_for_dl_above3e6_degr_68lower(x_in, y_in):
    value = 0.

    coeff = [6.1030503770127272E-07,
            -3.4436162716273691E-03,
            9.1445362007870549E-06,
            -4.2128706605604959E-06,
            5.6911998282562995E-07
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value


def a_coeff_for_dl_below3e6_degr_68upper(x_in, y_in):
    value = 0.

    coeff = [2.7113695868779926E-05,
            -2.2383085188973889E-02,
            3.9968595771495714E-04,
            -1.8728987892176028E-04,
            2.5631851224350754E-05
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value

def a_coeff_for_dl_above3e6_degr_68upper(x_in, y_in):
    value = 0.

    coeff = [1.0323688673240304E-06,
            -4.1896451296788064E-03,
            1.5918378807808457E-05,
            -7.5449702457221398E-06,
            1.0355514923159984E-06
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value


def a_coeff_for_dl_below3e6_degr_95lower(x_in, y_in):
    value = 0.

    coeff = [1.3056113690177544E-05,
            -1.5910706421302483E-02,
            2.0487836309913613E-04,
            -9.7553566594138990E-05,
            1.3505998479235331E-05
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value

def a_coeff_for_dl_above3e6_degr_95lower(x_in, y_in):
    value = 0.

    coeff = [4.8976192739275615E-06,
            -9.2543564179901443E-03,
            7.7716968122175132E-05,
            -3.6444159457347715E-05,
            4.9934736694135425E-06
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value

def a_coeff_for_dl_below3e6_degr_95upper(x_in, y_in):
    value = 0.

    coeff = [1.7094201607060706E-05,
            -1.7681472121526792E-02,
            2.5388927718268092E-04,
            -1.1994502402153020E-04,
            1.6618208322727730E-05
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value

def a_coeff_for_dl_above3e6_degr_95upper(x_in, y_in):
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
    coeff = [a_coeff_dl_merger_below3e6_degr_median(x_in),
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
    coeff = [a_coeff_dl_merger_above3e6_degr_median(x_in),
            3.4101844071692867E+01,
            1.5390535125934349E+02,
            -1.2244270913326416E+00,
            -2.1043020885072266E+01,
            9.1850673678172567E-02,
            9.6003122979566058E-01,
            -8.9983956604622559E+00,
            6.9842931421916443E-02,
            6.3079603980496746E-01
            ]

    value = fit_formula.formula_for_uncertainty_merger(coeff, x_in, y_in)
    return value

def quantile_below3e6_68lower(x_in, y_in):
    value = 0.0
    # coefficients
    coeff = [a_coeff_for_dl_below3e6_degr_68lower(z, y_in),
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
    coeff = [a_coeff_for_dl_above3e6_degr_68lower(z, y_in),
            3.1494220548636424E+01,
            1.1611010654704403E+02,
            -1.1805828075392941E+00,
            -1.5675043498192540E+01,
            9.0014096664488452E-02,
            7.0611018539159431E-01,
            -8.2537097868044782E+00,
            6.5408884284824165E-02,
            5.7704622955724982E-01
            ]

    value = fit_formula.formula_for_uncertainty_merger(coeff, x_in, y_in)
    return value

def quantile_below3e6_68upper(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [a_coeff_for_dl_below3e6_degr_68upper(z, y_in),
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
    coeff = [a_coeff_for_dl_above3e6_degr_68upper(z, y_in),
            3.1397092567659008E+01,
            9.2765335252141639E+01,
            -1.2015008730637431E+00,
            -1.2142605750651596E+01,
            9.4212026337055610E-02,
            5.2983020513778456E-01,
            -8.1940014498516547E+00,
            6.3705056016725603E-02,
            5.7223986797232573E-01
            ]

    value = fit_formula.formula_for_uncertainty_merger(coeff, z_c, x_in, y_in, z)
    return value

def quantile_below3e6_95lower(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [a_coeff_for_dl_below3e6_degr_95lower(z, y_in),
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
    coeff = [a_coeff_for_dl_above3e6_degr_95lower(z, y_in),
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
    coeff = [a_coeff_for_dl_below3e6_degr_95upper(z, y_in),
            5.6328829276688293E+00,
            3.1777691078609553E+01,
            -3.7855863156709502E-01,
            -6.0529411240348008E+00,
            8.2092711381870132E-02,
            3.7494146951689178E-01,
            -1.7479900173491720E+00,
            -4.6547086647309555E-02,
            1.8564271704918456E-01
            ]

    value = fit_formula.formula_for_uncertainty_merger(coeff, z_c, x_in, y_in, z)
    return value

def quantile_above3e6_95upper(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [a_coeff_for_dl_above3e6_degr_95upper(z, y_in),
            3.0968212748729449E+01,
            1.1321193108976358E+02,
            -1.2178941289555523E+00,
            -1.5098378542227637E+01,
            9.7888240961620632E-02,
            6.7241078166647483E-01,
            -8.0461721235559462E+00,
            6.2544513290029524E-02,
            5.6088479418023862E-01
            ]

    value = fit_formula.formula_for_uncertainty_merger(coeff, z_c, x_in, y_in, z)
    return value
