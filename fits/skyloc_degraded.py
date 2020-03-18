import fits.fit_formula as fit_formula

def h_coeff_for_skyloc_degr_median(x_in, y_in):
    value = 0.
    # coefficients
    coeff = [-1.7505436138962705E+02,
            -1.6871418029009188E-03,
            -1.3455789627105818E-02,
            1.9102751131768515E-03,
            1.9587918596574595E-03,
            -2.5557036488979773E-04
            ]

    value = fit_formula.formula_for_single_coeff_degr(coeff, x_in, y_in)
    return value

def h_coeff_for_skyloc_degr_68lower(x_in, y_in):
    value = 0.

    coeff = [-1.8278833504961941E+02,
            -1.2547345922033974E-03,
            -7.9674481899317043E-03,
            1.3840640742315401E-03,
            9.2257326481924779E-04,
            -1.4028405782514903E-04
            ]

    value = fit_formula.formula_for_single_coeff_degr(coeff, x_in, y_in)
    return value

def h_coeff_for_skyloc_degr_68upper(x_in, y_in):
    value = 0.

    coeff = [-6.6207893678094280E+01,
            -1.0670794869303227E-03,
            -6.6515447531019746E-03,
            1.2700130181778990E-03,
            1.2660363319766676E-03,
            -2.0849918209815287E-04
            ]

    value = fit_formula.formula_for_single_coeff_degr(coeff, x_in, y_in)
    return value

def h_coeff_for_skyloc_degr_95lower(x_in, y_in):
    value = 0.

    coeff = [-1.6664160368439295E+02,
            -3.7549248744898115E-03,
            -3.0733786991926386E-03,
            3.4622829801293482E-05,
            1.8378985895954386E-04,
            7.2733263735944909E-04
            ]

    value = fit_formula.formula_for_single_coeff_degr(coeff, x_in, y_in)
    return value

def h_coeff_for_skyloc_degr_95upper(x_in, y_in):
    value = 0.

    coeff = [5.8941905673506774E+01,
            -1.2718958521879310E-03,
            -7.1868507726557769E-03,
            1.4438652818469329E-03,
            1.2539443822456378E-03,
            -2.1483186566472736E-04
            ]

    value = fit_formula.formula_for_single_coeff_degr(coeff, x_in, y_in)
    return value

def median(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [3.0324541313885411E+03,
            -1.4856211823653798E+03,
            2.3694972718268716E+02,
            -1.2319110773997757E+01,
            -2.2281940582053394E+03,
            1.0921076401482796E+03,
            h_coeff_for_skyloc_degr_median(z, y_in),
            9.1782438619772364E+00,
            5.0322460708904038E+02,
            -2.4685135288999788E+02,
            3.9687991439554366E+01,
            -2.0910634606466374E+00,
            -3.5958926740429028E+01,
            1.7661516238900163E+01,
            -2.8475932495203438E+00,
            1.5073107440662170E-01,
            ]

    z_c = 0.7348467697913533
    value = fit_formula.formula_for_uncertainty_degr(coeff, z_c, x_in, y_in, z)
    return value

def quantile_68lower(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [3.3262051672574571E+03,
            -1.5969014972841203E+03,
            2.5026863218028484E+02,
            -1.2810659206536140E+01,
            -2.4103399230683426E+03,
            1.1594105855610135E+03,
            h_coeff_for_skyloc_degr_68lower(z, y_in),
            9.4408600474065949E+00,
            5.3810262781400218E+02,
            -2.5906050418334621E+02,
            4.0948044860280916E+01,
            -2.1239758497574144E+00,
            -3.7979105492237288E+01,
            1.8297591357246510E+01,
            -2.8976462430993877E+00,
            1.5083233042537358E-01,
            ]

    z_c = 0.5806809392180451
    value = fit_formula.formula_for_uncertainty_degr(coeff, z_c, x_in, y_in, z)
    return value

def quantile_68upper(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [8.8028758539517344E+02,
            -4.2301992401952197E+02,
            6.3937802535088643E+01,
            -3.0494960134361899E+00,
            -8.7524141701379017E+02,
            4.2385445669711805E+02,
            h_coeff_for_skyloc_degr_68upper(z, y_in),
            3.3462014638044923E+00,
            2.3538526751504466E+02,
            -1.1465890944590828E+02,
            1.8169731728705933E+01,
            -9.3894443880611789E-01,
            -1.9015922781533064E+01,
            9.3131635821001097E+00,
            -1.4908650704289030E+00,
            7.8201482753001983E-02
            ]

    z_c = 0.6020666843323308
    value = fit_formula.formula_for_uncertainty_degr(coeff, z_c, x_in, y_in, z)
    return value

def quantile_95lower(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [2.9893968072086582E+03,
            -1.4230708606685805E+03,
            2.2058985266297944E+02,
            -1.1139029874005196E+01,
            -2.2316791698944908E+03,
            1.0659788779459348E+03,
            h_coeff_for_skyloc_degr_95lower(z, y_in),
            8.5213593268483336E+00,
            5.0589721835569748E+02,
            -2.4198210441579275E+02,
            3.7955060343220858E+01,
            -1.9511803618102590E+00,
            -3.5890931382496753E+01,
            1.7178871575960514E+01,
            -2.6994055271752870E+00,
            1.3926227079969067E-01
            ]

    z_c = 0.5693628053139097
    value = fit_formula.formula_for_uncertainty_degr(coeff, z_c, x_in, y_in, z)
    return value

def quantile_95upper(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [-1.6372187266583480E+03,
            7.9155538992113861E+02,
            -1.2868587728850866E+02,
            6.9845076061043452E+00,
            7.5408790115237434E+02,
            -3.6350424732632121E+02,
            h_coeff_for_skyloc_degr_95upper(z, y_in),
            -3.1872892235362968E+00,
            -1.0113770315928062E+02,
            4.8211234638638757E+01,
            -7.7698547004690077E+00,
            4.1821131304752157E-01,
            3.2437485800844357E+00,
            -1.4690930096910471E+00,
            2.2834514307764664E-01,
            -1.1862117886380474E-02
            ]

    z_c = 0.5907525970680451
    value = fit_formula.formula_for_uncertainty_degr(coeff, z_c, x_in, y_in, z)
    return value
