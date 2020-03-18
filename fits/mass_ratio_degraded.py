import fits.fit_formula as fit_formula

def g_coeff_for_massratio_degr_median(x_in, y_in):
    value = 0.
    # coefficients
    coeff = [4.6353663573869261E+02,
            -4.3587253848136189E-04,
            -6.4486915577913074E-03,
            5.6261988140672526E-04,
            2.1754599417055692E-03,
            -1.9091850311619095E-04
            ]

    value = fit_formula.formula_for_single_coeff_degr(coeff, x_in, y_in)
    return value

def h_coeff_for_massratio_degr_68lower(x_in, y_in):
    value = 0.

    coeff = [-9.5065532036228149E+01,
            6.3880822566231198E-05,
            1.5684599023664246E-04,
            -7.9247688811624365E-05,
            2.0480162516736528E-04,
            -8.9220120331252764E-06
            ]

    value = fit_formula.formula_for_single_coeff_degr(coeff, x_in, y_in)
    return value

def g_coeff_for_massratio_degr_68upper(x_in, y_in):
    value = 0.

    coeff = [3.5730132859283674E+02,
            -4.8483848163051284E-04,
            -3.7089331733324554E-03,
            2.5457609166685500E-04,
            1.0019233828679869E-03,
            -2.1898991545350017E-05
            ]

    value = fit_formula.formula_for_single_coeff_degr(coeff, x_in, y_in)
    return value

def h_coeff_for_massratio_degr_95lower(x_in, y_in):
    value = 0.

    coeff = [-1.3771962305293692E+02,
            1.1098688116151375E-04,
            1.1099333836136485E-03,
            -2.1836587801732252E-04,
            1.4861840020840805E-05,
            1.8148805008777184E-05
            ]

    value = fit_formula.formula_for_single_coeff_degr(coeff, x_in, y_in)
    return value

def h_coeff_for_massratio_degr_95upper(x_in, y_in):
    value = 0.

    coeff = [-5.5157483680455854E+01,
            3.1289050413382992E-04,
            2.4674633174803493E-03,
            .6288045299958706E-04,
            .5011668487221083E-04,
            7.0781791290159331E-05
            ]

    value = fit_formula.formula_for_single_coeff_degr(coeff, x_in, y_in)
    return value

def median(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [1.2706659922312967E+03,
            -6.0422835548824753E+02,
            9.3119930416690920E+01,
            -4.6599988509814549E+00,
            -9.7251687403251594E+02,
            g_coeff_for_massratio_degr_median(z, y_in),
            -7.2148967094756216E+01,
            3.6682584365187552E+00,
            2.2439874977631413E+02,
            -1.0731158705357296E+02,
            1.6810488926446016E+01,
            -8.6285846606563155E-01,
            -1.6347513822967805E+01,
            7.8423187137426602E+00,
            -1.2348395397526559E+00,
            6.3870671002632662E-02
            ]

    z_c = 0.3612267063992481
    value = fit_formula.formula_for_uncertainty_degr(coeff, z_c, x_in, y_in, z)
    return value

def quantile_68lower(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [1.8916340324261409E+03,
            -8.9089513368332643E+02,
            1.3668991704355452E+02,
            -6.8425663630139164E+00,
            -1.3062689312314337E+03,
            6.1592372684198529E+02,
            h_coeff_for_massratio_degr_68lower(z, y_in),
            4.8037310953021723E+00,
            2.8320115178405666E+02,
            -1.3387719198108016E+02,
            2.0760388939639487E+01,
            -1.0561770099544958E+00,
            -1.9713394460489052E+01,
            9.3438634204992255E+00,
            -1.4549234077610436E+00,
            7.4466719805514003E-02
            ]

    z_c = 0.3535346468954887
    value = fit_formula.formula_for_uncertainty_degr(coeff, z_c, x_in, y_in, z)
    return value

def quantile_68upper(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [8.5966538925477153E+02,
            -4.1398664271180746E+02,
            6.4188427917961718E+01,
            -3.2137568534222565E+00,
            -7.3944260166642630E+02,
            g_coeff_for_massratio_degr_68upper(z, y_in),
            -5.6233403457965878E+01,
            2.8850545387406594E+00,
            1.8125870986853423E+02,
            -8.7928430586491729E+01,
            1.3951439148102679E+01,
            -7.2460209788691543E-01,
            -1.3772927684615986E+01,
            6.7048885288405309E+00,
            -1.0703362393059024E+00,
            5.6101333359492855E-02
            ]

    z_c = 0.3442742143067669
    value = fit_formula.formula_for_uncertainty_degr(coeff, z_c, x_in, y_in, z)
    return value

def quantile_95lower(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [2.8567880107095743E+03,
            -1.3497161217628445E+03,
            2.0862096130486029E+02,
            -1.0561466316294803E+01,
            -1.8779623521382312E+03,
            8.8774844180186005E+02,
            h_coeff_for_massratio_degr_95lower(z, y_in),
            7.0117574688659161E+00,
            3.9444178764809106E+02,
            -1.8683053141232136E+02,
            2.9082189459707017E+01,
            -1.4877096457871914E+00,
            -2.6738700537956269E+01,
            1.2690447695747423E+01,
            -1.9813435615605783E+00,
            1.0179344986408978E-01
            ]

    z_c = 0.35296969958909774
    value = fit_formula.formula_for_uncertainty_degr(coeff, z_c, x_in, y_in, z)
    return value

def quantile_95upper(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [7.4587127599278665E+02,
            -3.6780862433670933E+02,
            5.8538252831122037E+01,
            -3.0230721320320830E+00,
            -6.9342040746100997E+02,
            3.4228399691751059E+02,
            h_coeff_for_massratio_degr_95upper(z, y_in),
            2.9078291272542369E+00,
            1.7807086629696903E+02,
            -8.8157295433904039E+01,
            1.4303688128432062E+01,
            -7.6177173815470667E-01,
            -1.4009026433121383E+01,
            6.9565966918701196E+00,
            -1.1347409038466481E+00,
            6.0908850662940495E-02
            ]

    z_c = 0.3351163261973684
    value = fit_formula.formula_for_uncertainty_degr(coeff, z_c, x_in, y_in, z)
    return value
