import fits.fit_formula as fit_formula

def h_coeff_for_dl_degr_median(x_in, y_in):
    value = 0.
    # coefficients
    coeff = [-7.9026243882866211E+01,
            -4.6353196939112948E-04,
            -2.8092934642717938E-03,
            5.4052875252087848E-04,
            4.7590664780863042E-04,
            -7.8385224073684943E-05
            ]

    value = fit_formula.formula_for_single_coeff_degr(coeff, x_in, y_in)
    return value

def h_coeff_for_dl_degr_68lower(x_in, y_in):
    value = 0.

    coeff = [-1.0679803928894746E+02,
            -4.8448672209232502E-04,
            -2.6999831765199575E-03,
            5.0068954515922702E-04,
            2.7525904442070006E-04,
            -4.2939114947207816E-05
            ]

    value = fit_formula.formula_for_single_coeff_degr(coeff, x_in, y_in)
    return value

def h_coeff_for_dl_degr_68upper(x_in, y_in):
    value = 0.

    coeff = [-4.2560468712329119E+01,
            -4.1431824423470023E-04,
            -2.1041023812490719E-03,
            4.5626950791884764E-04,
            2.4968812675111793E-04,
            -4.6438558820219365E-05
            ]

    value = fit_formula.formula_for_single_coeff_degr(coeff, x_in, y_in)
    return value

def h_coeff_for_dl_degr_95lower(x_in, y_in):
    value = 0.

    coeff = [-1.3238568541282362E+02,
            -4.2137788769149785E-04,
            -2.5262026846167899E-03,
            4.8369053673502242E-04,
            2.7050189164747106E-04,
            -4.3535968811264647E-05
            ]

    value = fit_formula.formula_for_single_coeff_degr(coeff, x_in, y_in)
    return value

def c_coeff_for_dl_degr_95upper(x_in, y_in):
    value = 0.

    coeff = [6.8077006240568679E+01,
            -2.9420290644181645E-03,
            -1.5101258848690718E-02,
            3.1042432388353877E-03,
            1.7633686874465272E-03,
            -3.1451883617775352E-04
            ]

    value = fit_formula.formula_for_single_coeff_degr(coeff, x_in, y_in)
    return value

def median(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [1.3851297839309786E+03,
            -6.6955491235435125E+02,
            1.0534833299906097E+02,
            -5.4087022607842696E+00,
            -1.0287030536481177E+03,
            4.9843490914118871E+02,
            h_coeff_for_dl_degr_median(z, y_in),
            4.1040162001962806E+00,
            2.3514355986531370E+02,
            -1.1420640899990315E+02,
            1.8193527571658546E+01,
            -9.5133076012089646E-01,
            -1.7038189308361915E+01,
            8.2979330828395561E+00,
            -1.3277442458415720E+00,
            6.9871023804353172E-02,
            ]

    z_c = 0.28863839319097745
    value = fit_formula.formula_for_uncertainty_degr(coeff, z_c, x_in, y_in, z)
    return value

def quantile_68lower(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [1.9757397377590969E+03,
            -9.5329473183490722E+02,
            1.5037672657283096E+02,
            -7.7646866016529366E+00,
            -1.3929490076929112E+03,
            6.7339891147223489E+02,
            h_coeff_for_dl_degr_68lower(z, y_in),
            5.5571494290035872E+00,
            3.0616609813391102E+02,
            -1.4826025571054711E+02,
            2.3588082911263367E+01,
            -1.2329317746428785E+00,
            -2.1449004200514171E+01,
            1.0406111991017905E+01,
            -1.6604823362561945E+00,
            8.7164851378815911E-02
            ]

    z_c = 0.29082312627781953
    value = fit_formula.formula_for_uncertainty_degr(coeff, z_c, x_in, y_in, z)
    return value

def quantile_68upper(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [6.0387003595687690E+02,
            -2.9549264860544105E+02,
            4.6253843347647816E+01,
            -2.3329429862938427E+00,
            -5.4475801979786627E+02,
            2.6722951584433849E+02,
            h_coeff_for_dl_degr_68upper(z, y_in),
            2.2096004267128908E+00,
            1.4018540496077117E+02,
            -6.8984719955260644E+01,
            1.1081790835908526E+01,
            -5.8294496870870205E-01,
            -1.1081478538432087E+01,
            5.4737809542569176E+00,
            -8.8551602917709715E-01,
            4.7062522190799427E-02
            ]

    z_c = 0.29044140424135334
    value = fit_formula.formula_for_uncertainty_degr(coeff, z_c, x_in, y_in, z)
    return value

def quantile_95lower(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [2.4992993213866303E+03,
            -1.2121306960894033E+03,
            1.9250485289355433E+02,
            -1.0020909578835838E+01,
            -1.7105895027766683E+03,
            8.3045613948335836E+02,
            h_coeff_for_dl_degr_95lower(z, y_in),
            6.9293656829289105E+00,
            3.6785690865573804E+02,
            -1.7875865215803648E+02,
            2.8557598443461657E+01,
            -1.4995582837778727E+00,
            -2.5280078727801900E+01,
            1.2298051253360313E+01,
            -1.9684780198375904E+00,
            1.0367527788616826E-01
            ]

    z_c =  0.2876975804417293
    value = fit_formula.formula_for_uncertainty_degr(coeff, z_c, x_in, y_in, z)
    return value

def quantile_95upper(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [8.0030869729069912E+02,   
            -4.0828244675338590E+02,
            c_coeff_for_dl_degr_95upper(z, y_in),
            -3.7344545411740659E+00,  
            -6.8533205506489332E+02,  
            3.4760122719375062E+02,   
            -5.7944993774672483E+01,  
            3.1879213723731201E+00,   
            1.7724749395361204E+02,   
            -8.9728038987497143E+01, 
            1.4956857592885918E+01,  
            -8.2368358760521687E-01, 
            -1.4404453631123273E+01,  
            7.2930060592003318E+00,   
            -1.2172214315153198E+00,  
            6.7177699860621942E-02
            ]

    z_c = 0.2853228215725564
    value = fit_formula.formula_for_uncertainty_degr(coeff, z_c, x_in, y_in, z)
    return value
