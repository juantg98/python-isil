#http://github.com/oskargicast/bamtang/tree/master/prob2

import string


MENSAJE_ENCRIPTADO = """
uid nx, aex jcdjipx iu wzux zp, ta wxtpa jtdaws, ai etkx vis.
dcos zyexdzaxr aex jxdw jezwipijes iu etkzyg nidx aety iyx hts
ai ri aex ptnx aezyg. z zyexdzaxr aeta jezwipijes udin wtdds htww,
hei zp ns exdi tqactwws. z htya ai ntfx dcos cpxdp udxx. z htya ai
gzkx aexn aex udxxrin ai qeiipx. jxijwx tdx rzuuxdxya. jxijwx qeiipx
rzuuxdxya qdzaxdzt. oca zu aexdx zp t oxaaxd hts tniyg ntys
twaxdytazkxp, z htya ai xyqicdtgx aeta hts os ntfzyg za qinuidatowx.
pi aeta'p heta z'kx adzxr ai ri.
z htya ai piwkx jdiowxnp z nxxa zy aex rtzws wzux os cpzyg qinjcaxdp,
pi z yxxr ai hdzax jdigdtnp. os cpzyg dcos, z htya ai qiyqxyadtax aex
aezygp z ri, yia aex ntgzqtw dcwxp iu aex wtygctgx, wzfx patdazyg hzae
jcowzq kizr  pinxaezyg pinxaezyg pinxaezyg ai pts, "jdzya exwwi hidwr."
z vcpa htya ai pts, "jdzya aezp!" z riy'a htya tww aex pcddicyrzyg
ntgzq fxshidrp. z vcpa htya ai qiyqxyadtax iy aex atpf. aeta'p aex otpzq
zrxt. pi z etkx adzxr ai ntfx dcos qirx qiyqzpx tyr pcqqzyqa.
scfzezdi ntapcniai. (hhh.tdaznt.qin/zyak/dcos)
"""

FREQ_CODE = "TEOIARNSHLMYUCWDGPFBVKJ".lower()

def principal():
    #Contabilizar cuantas veces se repite un caracter.

    freq_dict = {} #freq_list = dict()
    for letra in string.ascii_lowercase:
        repeticiones = MENSAJE_ENCRIPTADO.count(letra)
        if repeticiones:
            freq_dict[letra] = repeticiones
    freq = sorted(freq_dict, key=freq_dict.get, reverse=True)
    freq = "".join(freq)

    mensaje = [""] * len(MENSAJE_ENCRIPTADO)
    for i, letra in enumerate(MENSAJE_ENCRIPTADO):
        index = freq.find(letra)
        if index == -1:
            mensaje[i] = letra
            continue
        mensaje[i] = FREQ_CODE[index]
    print("".join(mensaje))
           
if __name__ == '__main__':
    principal()