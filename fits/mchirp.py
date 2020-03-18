import fits.fit_formula as fit_formula

def g_coeff_for_mchirp_median(x_in, y_in):
    value = 0.
    # coefficients
    coeff = [2.6833264235217291E+02,
            8.9182960818769976E-04,
            5.6495138211835640E-03,
            -1.0806278363543012E-03
            ]

    value = fit_formula.formula_for_single_coeff(coeff, x_in, y_in)
    return value

def g_coeff_for_mchirp_68lower(x_in, y_in):
    value = 0.

    coeff = [4.4011022626781516E+02,
            4.0955056267140877E-04,
            8.1711278869555006E-03,
            -1.2068920937346691E-03
            ]

    value = fit_formula.formula_for_single_coeff(coeff, x_in, y_in)
    return value

def g_coeff_for_mchirp_68upper(x_in, y_in):
    value = 0.

    coeff = [1.1139422445292479E+02,
            -6.5377846466097865E-05,
            4.4098779837081492E-03,
            -5.7244798415558213E-04
            ]

    value = fit_formula.formula_for_single_coeff(coeff, x_in, y_in)
    return value

def g_coeff_for_mchirp_95lower(x_in, y_in):
    value = 0.

    coeff = [6.3075948595497346E+02,
            1.5811844551907609E-04,
            7.9004590753837152E-03,
            -1.1102201852202667E-03
            ]

    value = fit_formula.formula_for_single_coeff(coeff, x_in, y_in)
    return value

def g_coeff_for_mchirp_95upper(x_in, y_in):
    value = 0.

    coeff = [-1.4813101338688503E+02,
            -6.7028630415763655E-04,
            -1.5564394237950556E-03,
            2.0753815836581759E-04,
            ]

    value = fit_formula.formula_for_single_coeff(coeff, x_in, y_in)
    return value

def median(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [8.4635462648627197E+02,
            -3.6544400975763381E+02,
            4.9460898358472107E+01,
            -2.0672096935916229E+00,
            -6.1645205901346469E+02,
            g_coeff_for_mchirp_median(z, y_in),
            -3.7205786739175863E+01,
            1.6245900512640954E+00,
            1.3536936166476465E+02,
            -5.9235404290834275E+01,
            8.3029517832009052E+00,
            -3.6945400447373250E-01,
            -9.3258389147867078E+00,
            4.0874938802593768E+00,
            -5.7533632029224990E-01,
            2.5819186780925325E-02
            ]

    z_c = 0.485094519644
    value = fit_formula.formula_for_uncertainty(coeff, z_c, x_in, y_in, z)
    return value

def quantile_68lower(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [1.5654052623143587E+03,
            -6.9409281765826006E+02,
            9.9076505082800168E+01,
            -4.5426809872034308E+00,
            -9.9685335237821005E+02,
            g_coeff_for_mchirp_68lower(z, y_in),
            -6.2859462385036615E+01,
            2.8917391202328773E+00,
            2.0131226473013962E+02,
            -8.8699228643709318E+01,
            1.2659719501677660E+01,
            -5.8263845439687145E-01,
            -1.3043663372075942E+01,
            5.7303800251995725E+00,
            -8.1568155093668793E-01,
            3.7457918703694304E-02
            ]

    z_c = 0.466068500357
    value = fit_formula.formula_for_uncertainty(coeff, z_c, x_in, y_in, z)
    return value

def quantile_68upper(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [3.2761163036482259E+02,
            -1.1595252429745916E+02,
            9.9515830666855347E+00,
            -2.4898432368647416E-03,
            -2.8972579737854289E+02,
            g_coeff_for_mchirp_68upper(z, y_in),
            -1.2339414226614197E+01,
            3.2312533448650793E-01,
            6.7980856841957220E+01,
            -2.6867702341986448E+01,
            3.1707577176533110E+00,
            -1.0047912659057445E-01,
            -4.8042939966650255E+00,
            1.9158500231140065E+00,
            -2.3083403974138150E-01,
            7.7467626237961440E-03
            ]

    z_c = 0.436068500357
    value = fit_formula.formula_for_uncertainty(coeff, z_c, x_in, y_in, z)
    return value

def quantile_95lower(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [2.2405423089132551E+03,
            -1.0159680897931503E+03,
            1.4962676452036570E+02,
            -7.1570412970259003E+00,
            -1.3952456636027537E+03,
            g_coeff_for_mchirp_95lower(z, y_in),
            -9.2941845031714124E+01,
            4.4555207376991177E+00,
            2.7930021259473546E+02,
            -1.2620741168361594E+02,
            1.8610056492115525E+01,
            -8.9367902321109227E-01,
            -1.8055776125757912E+01,
            8.1529517400673370E+00,
            -1.2019995269668584E+00,
            5.7758804980608147E-02
            ]

    z_c = 0.466068500357
    value = fit_formula.formula_for_uncertainty(coeff, z_c, x_in, y_in, z)
    return value

def quantile_95upper(x_in, y_in, z):
    value = 0.0
    # coefficients
    coeff = [-5.5517260217432442E+02,
            3.0580592465948473E+02,
            -5.6509326534941316E+01,
            3.4555471417515737E+00,
            2.5547532270772965E+02,
            g_coeff_for_mchirp_95upper(z, y_in),
            2.8451234693377430E+01,
            -1.7952329747659519E+00,
            -4.1240383180856895E+01,
            2.5024272333750407E+01,
            -4.9737186710238799E+00,
            3.2207523735503054E-01,
            2.2941617360171387E+00,
            -1.4506828712452799E+00,
            2.9679126236217712E-01,
            -1.9595996779628422E-02
            ]

    z_c = 0.465827338669
    value = fit_formula.formula_for_uncertainty(coeff, z_c, x_in, y_in, z)
    return value
