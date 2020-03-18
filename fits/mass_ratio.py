import fits.fit_formula as fit_formula

def g_coeff_for_massratio_median(x_in, y_in):
    value = 0.
    # coefficients
    coeff = [3.0665742717587625E+02,
            3.6419847497791744E-04,
            5.3780371141002705E-03,
            -8.3768303692298841E-04
            ]

    value = fit_formula.formula_for_single_coeff(coeff, x_in, y_in)
    return value

def h_coeff_for_massratio_68lower(x_in, y_in):
    value = 0.

    coeff = [-5.9300759277754040E+01,
            1.2383859985957166E-04,
            1.2738119568060026E-03,
            -2.0822602889773021E-04
            ]

    value = fit_formula.formula_for_single_coeff(coeff, x_in, y_in)
    return value

def g_coeff_for_massratio_68upper(x_in, y_in):
    value = 0.

    coeff = [1.0233384717138382E+02,
            2.3309575234261299E-04,
            2.2018084046039345E-03,
            -4.7602833199574614E-04
            ]

    value = fit_formula.formula_for_single_coeff(coeff, x_in, y_in)
    return value

def h_coeff_for_massratio_95lower(x_in, y_in):
    value = 0.

    coeff = [-9.0916461083511351E+01,
            1.1957336436882464E-04,
            1.4370240564057757E-03,
            -2.2484042952445330E-04
            ]

    value = fit_formula.formula_for_single_coeff(coeff, x_in, y_in)
    return value

def h_coeff_for_massratio_95upper(x_in, y_in):
    value = 0.

    coeff = [3.0724027159156766E+01,
            1.9749503862088900E-05,
            -2.5742007337593040E-04,
            2.7838837510947919E-05
            ]

    value = fit_formula.formula_for_single_coeff(coeff, x_in, y_in)
    return value

def median(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [1.0390197896752593E+03,
            -4.4897328426584232E+02,
            6.1395462195801358E+01,
            -2.6258365698922717E+00,
            -7.0881510167461340E+02,
            g_coeff_for_massratio_median(z, y_in),
            -4.2386436481662187E+01,
            1.8507547901055545E+00,
            1.4940652338561057E+02,
            -6.4700092806838427E+01,
            8.9807491768286773E+00,
            -3.9547087200772069E-01,
            -9.9823527851997973E+00,
            4.3172415611684229E+00,
            -5.9916242114520912E-01,
            2.6434930774087206E-02
            ]

    z_c = 0.467274250539
    value = fit_formula.formula_for_uncertainty(coeff, z_c, x_in, y_in, z)
    return value

def quantile_68lower(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [1.5070837460115508E+03,
            -6.6391558231937734E+02,
            9.3944534033977348E+01,
            -4.2537619745785378E+00,
            -9.5626108278248182E+02,
            4.1922693621136824E+02,
            h_coeff_for_massratio_68lower(z, y_in),
            2.6909391576101669E+00,
            1.9268844168705243E+02,
            -8.4255719767574604E+01,
            1.1901485465085582E+01,
            -5.3980934918394041E-01,
            -1.2461904641741105E+01,
            5.4302963344199515E+00,
            -7.6442261827324387E-01,
            3.4559624765165609E-02
            ]

    z_c = 0.479755486056
    value = fit_formula.formula_for_uncertainty(coeff, z_c, x_in, y_in, z)
    return value

def quantile_68upper(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [3.0473511966683719E+02,
            -1.0338086550255460E+02,
            7.7176545509290442E+00,
            1.2836034988683487E-01,
            -2.7285231945292878E+02,
            g_coeff_for_massratio_68upper(z, y_in),
            -1.0735377301572997E+01,
            2.2949051757625005E-01,
            6.4290666383380355E+01,
            -2.4889339396717457E+01,
            2.8209875676475336E+00,
            -8.0085951181015247E-02,
            -4.5479854478935913E+00,
            1.7785780627003112E+00,
            -2.0658606091581433E-01,
            6.3339826153310241E-03
            ]

    z_c = 0.479755486056
    value = fit_formula.formula_for_uncertainty(coeff, z_c, x_in, y_in, z)
    return value

def quantile_95lower(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [2.2121939515185900E+03,
            -1.0007727341353437E+03,
            1.4698035022129179E+02,
            -7.0053439557164490E+00,
            -1.3734243616309141E+03,
            6.1918701167842892E+02,
            h_coeff_for_massratio_95lower(z, y_in),
            4.3387639532385194E+00,
            2.7440257362926263E+02,
            -1.2359829020295656E+02,
            1.8151570963327899E+01,
            -8.6716323408890617E-01,
            -1.7710339813178397E+01,
            7.9683359421051421E+00,
            -1.1694670533443912E+00,
            5.5872558550390750E-02
            ]

    z_c = 0.479755486056
    value = fit_formula.formula_for_uncertainty(coeff, z_c, x_in, y_in, z)
    return value

def quantile_95upper(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [-5.8643284347033637E+02,
            3.2388544822456390E+02,
            -5.9826767585800624E+01,
            3.6525317247399478E+00,
            2.7713448909773649E+02,
            -1.6051453943022378E+02,
            h_coeff_for_massratio_95upper(z, y_in),
            -1.9301341215338805E+00,
            -4.6090411193910725E+01,
            2.7778464384595203E+01,
            -5.4765023210710435E+00,
            3.5177559222778143E-01,
            2.6444823781483384E+00,
            -1.6482199368152122E+00,
            3.3264678448228580E-01,
            -2.1705379200170682E-02
            ]

    z_c = 0.464800142157
    value = fit_formula.formula_for_uncertainty(coeff, z_c, x_in, y_in, z)
    return value
