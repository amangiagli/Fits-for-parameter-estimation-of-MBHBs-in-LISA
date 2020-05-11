import fits.fit_formula as fit_formula

def a_coeff_dl_merger_below3e6_degr_median(x_in):
    value = 0.
    # coefficients
    coeff = [2.0565893085297295E-05,
            -2.0103510632092567E-02,
            3.1603402340107413E-04,
            -1.4998862667408815E-04,
            2.0653792864527295E-05
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in)
    return value

def a_coeff_dl_merger_above3e6_degr_median(x_in):
    value = 0.
    # coefficients
    coeff = [3.9198890734081695E-07,
            -2.6406994055505287E-03,
            6.2097033771302346E-06,
            -2.8737293225166973E-06,
            3.9793387817990948E-07
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in)
    return value

def a_coeff_for_dl_below3e6_degr_68lower(x_in, y_in):
    value = 0.

    coeff = [1.3006015984239257E-05,
            -1.6224362947077520E-02,
            1.9687228522712134E-04,
            -9.6635202682769628E-05,
            1.3582721255461227E-05
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value

def a_coeff_for_dl_above3e6_degr_68lower(x_in, y_in):
    value = 0.

    coeff = [6.1125742677768214E-07,
            -3.4429446832741962E-03,
            9.4137687661069387E-06,
            -4.3002293026199846E-06,
            5.9115245678317552E-07
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value


def a_coeff_for_dl_below3e6_degr_68upper(x_in, y_in):
    value = 0.

    coeff = [2.5044154256384934E-05,
            -2.2329431723857630E-02,
            3.6331618413733063E-04,
            -1.7146314851977681E-04,
            2.3598892703328804E-05
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value

def a_coeff_for_dl_above3e6_degr_68upper(x_in, y_in):
    value = 0.

    coeff = [1.0467195233171159E-06,
            -4.1876168164473836E-03,
            1.6811482330124820E-05,
            -7.8208892543142646E-06,
            1.0799493325435875E-06
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value


def a_coeff_for_dl_below3e6_degr_95lower(x_in, y_in):
    value = 0.

    coeff = [1.2399281167995918E-05,
            -1.5882916345597527E-02,
            1.7163007864702003E-04,
            -7.8053856571063936E-05,
            1.0348824248954710E-05
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value

def a_coeff_for_dl_above3e6_degr_95lower(x_in, y_in):
    value = 0.

    coeff = [4.6608976282368152E-06,
            -9.2471917750553689E-03,
            7.2494495194513745E-05,
            -3.3879073522040193E-05,
            4.6090482783751579E-06
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value

def a_coeff_for_dl_below3e6_degr_95upper(x_in, y_in):
    value = 0.

    coeff = [1.7587362420354699E-05,
            -1.7672749376770453E-02,
            2.7183857235303053E-04,
            -1.3095327477532224E-04,
            1.8545154534450604E-05
            ]

    value = fit_formula.formula_for_single_coeff_merger(coeff, x_in, y_in)
    return value

def a_coeff_for_dl_above3e6_degr_95upper(x_in, y_in):
    value = 0.

    coeff = [7.5425721904062693E-07,
            -3.5027577924608257E-03,
            1.2558106736397633E-05,
            -5.5136221369396991E-06,
            7.3106306477508918E-07
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
