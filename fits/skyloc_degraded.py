import fits.fit_formula as fit_formula

def h_coeff_for_skyloc_degr_median(x_in, y_in):
    value = 0.
    # coefficients
    coeff = [-1.5362590720499486E+02,
            -1.4829533497045283E-03,
            -1.1083750496329085E-02,
            1.4910007036007707E-03,
            1.5356946607155250E-03,
            -1.7349473490394581E-04
            ]

    value = fit_formula.formula_for_single_coeff_degr(coeff, x_in, y_in)
    return value

def h_coeff_for_skyloc_degr_68lower(x_in, y_in):
    value = 0.

    coeff = [-5.9886045786318924E+01,
            -9.6654150159886218E-04,
            -5.5517846622738917E-03,
            1.0160490863054073E-03,
            4.5966758562166301E-04,
            -7.5195109951284311E-05
            ]

    value = fit_formula.formula_for_single_coeff_degr(coeff, x_in, y_in)
    return value

def h_coeff_for_skyloc_degr_68upper(x_in, y_in):
    value = 0.

    coeff = [-1.3657665473105959E+02,
            -8.3207832973636374E-04,
            -5.5710875765884122E-03,
            1.0447942769032743E-03,
            1.2697371807064205E-03,
            -2.0299404839370578E-04
            ]

    value = fit_formula.formula_for_single_coeff_degr(coeff, x_in, y_in)
    return value

def h_coeff_for_skyloc_degr_95lower(x_in, y_in):
    value = 0.

    coeff = [-4.2987108172681651E+01,
            -1.2459782501860633E-03,
            -7.5777148574143480E-03,
            1.3701838393201883E-03,
            1.0998729707220965E-03,
            -1.8498507295541919E-04
            ]

    value = fit_formula.formula_for_single_coeff_degr(coeff, x_in, y_in)
    return value

def h_coeff_for_skyloc_degr_95upper(x_in, y_in):
    value = 0.

    coeff = [7.8434395333677305E+00,
            -9.1711762846729899E-04,
            -5.6761820214079996E-03,
            1.1198054730302525E-03,
            1.2414556027052512E-03,
            -2.0498433457694228E-04
            ]

    value = fit_formula.formula_for_single_coeff_degr(coeff, x_in, y_in)
    return value

def median(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [2.8457023092205441E+03,
            -1.3743409994304559E+03,
            2.1471357617794106E+02,
            -1.0848792769803225E+01,
            -2.0324959993835455E+03,
            9.8002820939498724E+02,
            h_coeff_for_skyloc_degr_median(z, y_in),
            7.8192633019180278E+00,
            4.4177241494019597E+02,
            -2.1249570923561649E+02,
            3.3291629235881828E+01,
            -1.6959101369918415E+00,
            -2.9845727080411464E+01,
            1.4304500965970789E+01,
            -2.2345651945720704E+00,
            1.1358425193111543E-01
            ]

    z_c = 0.7348467697913533
    value = fit_formula.formula_for_uncertainty_degr(coeff, z_c, x_in, y_in, z)
    return value

def quantile_68lower(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [1.2465381910224887E+03,
            -5.3166515192541397E+02,
            6.9340006135764682E+01,
            -2.6231710939190109E+00,
            -1.0029085039541454E+03,
            4.3711571189478315E+02,
            h_coeff_for_skyloc_degr_68lower(z, y_in),
            2.5085855756714679E+00,
            2.2338279685673797E+02,
            -9.7242482036654820E+01,
            1.3364803208426839E+01,
            -5.6560098821400118E-01,
            -1.4662680185865964E+01,
            6.2897138516024587E+00,
            -8.4776685692089870E-01,
            3.4863045058159514E-02
            ]

    z_c = 0.5806809392180451
    value = fit_formula.formula_for_uncertainty_degr(coeff, z_c, x_in, y_in, z)
    return value

def quantile_68upper(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [2.1235503930191753E+03,
            -1.0622441526685693E+03,
            1.7192167644391731E+02,
            -9.0480834063898570E+00,
            -1.6883307861407529E+03,
            8.4114930983007343E+02,
            h_coeff_for_skyloc_degr_68upper(z, y_in),
            7.2457044076971542E+00,
            4.0286888928282923E+02,
            -2.0029922300300294E+02,
            3.2552813919403476E+01,
            -1.7321118409508358E+00,
            -2.9578170416747565E+01,
            1.4681227526619065E+01,
            -2.3859192882702587E+00,
            1.2712227881161198E-01
            ]

    z_c = 0.6020666843323308
    value = fit_formula.formula_for_uncertainty_degr(coeff, z_c, x_in, y_in, z)
    return value

def quantile_95lower(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [9.5021318911793060E+02,
            -3.6797919723945603E+02,
            3.9917357950555292E+01,
            -9.0084079602867906E-01,
            -8.3677461947383324E+02,
            3.4403469738300157E+02,
            h_coeff_for_skyloc_degr_95lower(z, y_in),
            1.5121451042414709E+00,
            1.9182904263860496E+02,
            -7.9391546915186979E+01,
            1.0098908579415509E+01,
            -3.7189027540559039E-01,
            -1.2610848786693349E+01,
            5.1254117146821780E+00,
            -6.3408772187359830E-01,
            2.2158921390939668E-02
            ]

    z_c = 0.5693628053139097
    value = fit_formula.formula_for_uncertainty_degr(coeff, z_c, x_in, y_in, z)
    return value

def quantile_95upper(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [-8.7376945488669276E+02,
            3.8499068441662774E+02,
            -5.7938147381113602E+01,
            2.9477763885576111E+00,
            1.9801903871916835E+02,
            -6.8567561673040018E+01,
            h_coeff_for_skyloc_degr_95upper(z, y_in),
            -2.8913081360235182E-01,
            2.4581078394043146E+01,
            -1.8181113727943558E+01,
            3.6795387069285921E+00,
            -2.2757997386074180E-01,
            -5.0485595056846346E+00,
            2.8964450146420528E+00,
            -5.2093928063805350E-01,
            3.0117752179478430E-02
            ]

    z_c = 0.5907525970680451
    value = fit_formula.formula_for_uncertainty_degr(coeff, z_c, x_in, y_in, z)
    return value
