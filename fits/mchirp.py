import fits.fit_formula as fit_formula

def g_coeff_for_mchirp_median(x_in, y_in):
    value = 0.
    # coefficients
    coeff = [8.6477486043953050E+01,
            2.4862638688299987E-04,
            8.8163909974041544E-03,
            -9.1614765106045096E-04
            ]

    value = fit_formula.formula_for_single_coeff(coeff, x_in, y_in)
    return value

def g_coeff_for_mchirp_68lower(x_in, y_in):
    value = 0.

    coeff = [6.2221610118365277E+01,
            5.2322612697924429E-04,
            1.0464294248278791E-02,
            -1.0737638833301995E-03
            ]

    value = fit_formula.formula_for_single_coeff(coeff, x_in, y_in)
    return value

def h_coeff_for_mchirp_68upper(x_in, y_in):
    value = 0.

    coeff = [5.5642103831391623E+00,
            1.2609783703503106E-04,
            2.1511656018211897E-03,
            -2.2807115058739831E-04
            ]

    value = fit_formula.formula_for_single_coeff(coeff, x_in, y_in)
    return value

def g_coeff_for_mchirp_95lower(x_in, y_in):
    value = 0.

    coeff = [9.6940176461674025E+02,
            2.0496510172294145E-03,
            1.0670334560633687E-02,
            -1.1295852644719702E-03
            ]

    value = fit_formula.formula_for_single_coeff(coeff, x_in, y_in)
    return value

def g_coeff_for_mchirp_95upper(x_in, y_in):
    value = 0.

    coeff = [-5.1862712530472585E+01,
            6.7848006948663321E-04,
            2.2645864976812351E-03,
            1.6130293961732513E-04
            ]

    value = fit_formula.formula_for_single_coeff(coeff, x_in, y_in)
    return value

def median(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [2.6515408479013962E+02,
            -7.4011897310055360E+01,
            1.5389582504745953E+00,
            5.2438069978127655E-01,
            -2.5018662363028753E+02,
            g_coeff_for_mchirp_median(z, y_in),
            -7.4993567032898643E+00,
            2.4866077491043193E-02,
            5.9853989909475494E+01,
            -2.1995109189116803E+01,
            2.2497667761391882E+00,
            -4.4626185474120561E-02,
            -4.2205403682022444E+00,
            1.5822178882031530E+00,
            -1.6969472881634751E-01,
            4.1171804649451360E-03
            ]

    z_c = 0.36382088973300003
    value = fit_formula.formula_for_uncertainty(coeff, z_c, x_in, y_in, z)
    return value

def quantile_68lower(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [2.0473348581097764E+02,
            -3.4355194451516375E+01,
            -6.6008704800909399E+00,
            1.0546526750127398E+00,
            -2.1274180052725066E+02,
            g_coeff_for_mchirp_68lower(z, y_in),
            -2.5778577002192735E+00,
            -2.9327285221723787E-01,
            5.1872124573168449E+01,
            -1.6977586474533712E+01,
            1.2522573588204731E+00,
            1.8931321518115496E-02,
            -3.6168296637446264E+00,
            1.2188314007475980E+00,
            -9.9666009821211432E-02,
            -2.4234423621294354E-04
            ]

    z_c = 0.34955137526775
    value = fit_formula.formula_for_uncertainty(coeff, z_c, x_in, y_in, z)
    return value

def quantile_68upper(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [-3.4793242448825232E+01,
            6.3025379678456744E+01,
            -1.9084807553905758E+01,
            1.5484788511155116E+00,
            -6.1196240356606161E+01,
            -2.2940986693129224E-02,
            h_coeff_for_mchirp_68upper(z, y_in),
            -6.2674959633643024E-01,
            2.1857732493363390E+01,
            -4.5544424393325480E+00,
            -3.9380009726071874E-01,
            8.7790663814946157E-02,
            -1.7707244692242383E+00,
            4.5598365327467039E-01,
            1.3989242546905700E-03,
            -4.4782854623122148E-03
            ]

    z_c = 0.32705137526775
    value = fit_formula.formula_for_uncertainty(coeff, z_c, x_in, y_in, z)
    return value

def quantile_95lower(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [3.0319269431636651E+03,
            -1.4460956060690780E+03,
            2.2499206116014489E+02,
            -1.1419300226600056E+01,
            -2.0255808648609864E+03,
            g_coeff_for_mchirp_95lower(z, y_in),
            -1.5176925396165353E+02,
            7.7639529210585749E+00,
            4.2641506324240959E+02,
            -2.0471967177067040E+02,
            3.2186945112593293E+01,
            -1.6553441880344621E+00,
            -2.8660886008196844E+01,
            1.3788346789592467E+01,
            -2.1739743245087766E+00,
            1.1222463467288435E-01
            ]

    z_c = 0.34955137526775
    value = fit_formula.formula_for_uncertainty(coeff, z_c, x_in, y_in, z)
    return value

def quantile_95upper(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [-3.1220631350614487E+02,
            1.8468850277649958E+02,
            -3.6635743030185040E+01,
            2.3886253116965235E+00,
            6.5170281619498965E+01,
            g_coeff_for_mchirp_95upper(z, y_in),
            1.2456441159500018E+01,
            -9.2561864575178898E-01,
            4.8195804232418977E+00,
            1.6224887812622517E+00,
            -1.0710281035384277E+00,
            1.0890118202660659E-01,
            -1.1548801045674000E+00,
            3.0454399785652697E-01,
            3.5937663644496354E-03,
            -3.5446480110010725E-03
            ]

    z_c = 0.34937050400175
    value = fit_formula.formula_for_uncertainty(coeff, z_c, x_in, y_in, z)
    return value
