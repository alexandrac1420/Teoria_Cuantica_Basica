import vec_matrix_complex as lb
import math
def probabilidad_posicion(vec,posicion):
    if posicion >= 0 and posicion < len(vec):
        modu = lb.norm_vec(vec)
        vec_norm = lb.norm_vec(vec[posicion])
        probability = (vec_norm**2)/(modu**2)
        return probability
    else:
        raise Exception ("Error: La posición dada esta fuera del rango del vector")

def normalizate_vec(vec1):
    norm = lb.norm_vec(vec1)
    normalizate =lb.mult_esc_vec((1/norm), vec1)
    return normalizate
def probabilidad_transicion(vec1,vec2):
    if lb.norm_vec(vec1) and lb.norm_vec(vec2):
        probabilidad =lb.prod_int_vec(vec2,vec1)
        return probabilidad

    else:
        vec1 = normalizate_vec(vec1)
        vec2 = normalizate_vec(vec2)
        probabilidad_transicion(vec1, vec2)

