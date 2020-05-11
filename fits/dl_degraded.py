import fits.fit_formula as fit_formula

def h_coeff_for_dl_degr_median(x_in, y_in):
    value = 0.
    # coefficients
    coeff = [-4.3563660436290974E+01,
            -4.9641979795061759E-04,
            -3.4680073213304305E-03,
            6.2278781944068238E-04,
            7.7058578032161967E-04,
            -1.2153329738524718E-04
            ]

    value = fit_formula.formula_for_single_coeff_degr(coeff, x_in, y_in)
    return value

def h_coeff_for_dl_degr_68lower(x_in, y_in):
    value = 0.

    coeff = [-6.8369261027859352E+01,
            -5.2260885949863170E-04,
            -4.1546377092750207E-03,
            7.3745910582120031E-04,
            9.3437157189700418E-04,
            -1.5128144753839579E-04
            ]

    value = fit_formula.formula_for_single_coeff_degr(coeff, x_in, y_in)
    return value

def h_coeff_for_dl_degr_68upper(x_in, y_in):
    value = 0.

    coeff = [-3.4911256921783654E+01,
            -4.2679035739665705E-04,
            -2.2958708289436700E-03,
            4.5048899937996737E-04,
            4.2687477119070905E-04,
            -6.9593115455577671E-05
            ]

    value = fit_formula.formula_for_single_coeff_degr(coeff, x_in, y_in)
    return value

def h_coeff_for_dl_degr_95lower(x_in, y_in):
    value = 0.

    coeff = [-9.6409399085926452E+01,
            -3.7915970795769806E-04,
            -2.6188323473362190E-03,
            4.5791703798447441E-04,
            4.8055288222700882E-04,
            -6.8833556967006068E-05
            ]

    value = fit_formula.formula_for_single_coeff_degr(coeff, x_in, y_in)
    return value

def c_coeff_for_dl_degr_95upper(x_in, y_in):
    value = 0.

    coeff = [-5.7413370910002399E+00,
            -2.6550480055033548E-03,
            -1.6785340688949539E-02,
            3.2858890945583713E-03,
            4.0111252535514844E-03,
            -6.9343295969164116E-04
            ]

    value = fit_formula.formula_for_single_coeff_degr(coeff, x_in, y_in)
    return value

def median(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [8.0391341572972931E+02,
            -3.6986896436120571E+02,
            5.4020391370719892E+01,
            -2.4891911926904968E+00,
            -6.2895349113882821E+02,
            2.9180709926436793E+02,
            h_coeff_for_dl_degr_median(z, y_in),
            2.0831603590791907E+00,
            1.4319372303013498E+02,
            -6.6556028797141636E+01,
            9.9976087684236674E+00,
            -4.8337991643279565E-01,
            -9.8865830515359345E+00,
            4.5838856450466103E+00,
            -6.8778344406265290E-01,
            3.3278950485168934E-02
            ]

    z_c = 0.28863839319097745
    value = fit_formula.formula_for_uncertainty_degr(coeff, z_c, x_in, y_in, z)
    return value

def quantile_68lower(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [1.3808636388946959E+03,
            -6.4182596315324656E+02,
            9.6286773396675670E+01,
            -4.6516334615305333E+00,
            -9.7059546494459607E+02,
            4.5212313686780260E+02,
            h_coeff_for_dl_degr_68lower(z, y_in),
            3.3460523598831422E+00,
            2.0739834073564381E+02,
            -9.6519310146513959E+01,
            1.4606245467534528E+01,
            -7.1645794447563560E-01,
            -1.3752233528992607E+01,
            6.3768212839695799E+00,
            -9.6166253635520604E-01,
            4.7022475138305708E-02
            ]

    z_c = 0.29082312627781953
    value = fit_formula.formula_for_uncertainty_degr(coeff, z_c, x_in, y_in, z)
    return value

def quantile_68upper(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [4.9473683393202504E+02,
            -2.3927674396837460E+02,
            3.6401416102336590E+01,
            -1.7509090490919390E+00,
            -4.6115843319589129E+02,
            2.2378917207856858E+02,
            h_coeff_for_dl_degr_68upper(z, y_in),
            1.7561232704339460E+00,
            1.1677906280675273E+02,
            -5.6730283951842075E+01,
            8.9206150121733430E+00,
            -4.5507126395882125E-01,
            -8.7048515477317228E+00,
            4.2256233623649493E+00,
            -6.6595836858979851E-01,
            3.4155791138488212E-02
            ]

    z_c = 0.29044140424135334
    value = fit_formula.formula_for_uncertainty_degr(coeff, z_c, x_in, y_in, z)
    return value

def quantile_95lower(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [1.9664199451451052E+03,
            -9.2900665018717621E+02,
            1.4275363274662467E+02,
            -7.1307773805937140E+00,
            -1.3230254859889239E+03,
            6.2511885922657279E+02,
            h_coeff_for_dl_degr_95lower(z, y_in),
            4.8453064965904815E+00,
            2.7565837069357849E+02,
            -1.3005859569566366E+02,
            2.0050392228814484E+01,
            -1.0081232732255501E+00,
            -1.8052245880872238E+01,
            8.4914871656316997E+00,
            -1.3053965295960381E+00,
            6.5471847806520600E-02
            ]

    z_c =  0.2876975804417293
    value = fit_formula.formula_for_uncertainty_degr(coeff, z_c, x_in, y_in, z)
    return value

def quantile_95upper(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [-5.5805132377241542E+01,
            2.7982912070311507E+01,
            c_coeff_for_dl_degr_95upper(z, y_in),
            4.0503889992627751E-01,
            -9.7626367059612150E+01,
            4.7644773444667621E+01,
            -7.1097606197328655E+00,
            3.3153342244428641E-01,
            4.4147258832646173E+01,
            -2.1649237407048389E+01,
            3.3952527469853560E+00,
            -1.7259028246107633E-01,
            -4.1522877946664138E+00,
            2.0365067468384059E+00,
            -3.2255957245318534E-01, 
            1.6682956115293024E-02
            ]

    z_c = 0.2853228215725564
    value = fit_formula.formula_for_uncertainty_degr(coeff, z_c, x_in, y_in, z)
    return value
