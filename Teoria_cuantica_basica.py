import vec_matrix_complex as lb
import numpy as np

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

def amplitud_transicion(vec1,vec2):
    if lb.norm_vec(vec1) and lb.norm_vec(vec2):
        probabilidad =lb.prod_int_vec(vec2,vec1)
        return probabilidad

    else:
        vec1 = normalizate_vec(vec1)
        vec2 = normalizate_vec(vec2)
        amplitud_transicion(vec1, vec2)

def probabilidad_transicion(vec1,vec2):
    amplitud = amplitud_transicion(vec1, vec2)
    modulo = np.abs(amplitud)
    return modulo

def valor_esperado(matrix, vec):
    if lb.hermitian_matrix(matrix):
        respuesta = lb.act_matrix_vec(matrix,vec)
        return lb.prod_int_vec(respuesta,vec)
    else:
        raise Exception ("Error: La matriz no es hermitiana")

def varianza (matrix, vec):
    media = valor_esperado(matrix, vec)
    row, col = matrix.shape
    identidad = np.eye(row, col)

    operador_delta = matrix - lb.mult_esc_vec(media, identidad)
    mult_operador_delta = lb.mult_matrix(operador_delta, operador_delta)

    adj_vec = lb.inv_vec_complex(vec)
    acc_matrx_vec = lb.act_matrix_vec(mult_operador_delta, vec)
    varianza = lb.prod_int_vec(adj_vec, acc_matrx_vec)

    return -varianza

def val_propio_probabilidad(vec,matrix):
    probabilades =[]
    val_propios = lb.val_prop_matrix(matrix)[1]
    for val in val_propios:
        probabilades.append(probabilidad_transicion(vec,val))

    return lb.val_prop_matrix(matrix)[0], probabilades


def dinamica_sist(vec, matrix):
    estado_final = vec
    for valores in matrix:
        estado_final = lb.act_matrix_vec(valores,estado_final)
    return estado_final


