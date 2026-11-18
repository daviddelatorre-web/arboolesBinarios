class Incidente:
    def __init__(self, idIncidente, direccionIP, tipoAtaque, nivelRiesgo, estado):
        self.__idIncidente = idIncidente
        self.__direccionIP = direccionIP
        self.__tipoAtaque = tipoAtaque
        self.__nivelRiesgo = nivelRiesgo
        self.__estado = estado

    def getIdIncidente(self):
        return self.__idIncidente
    def getDireccionIP(self):
        return self.__direccionIP
    def getTipoAtaque(self):
        return self.__tipoAtaque
    def getNivelRiesgo(self):
        return self.__nivelRiesgo
    def getEstado(self):
        return self.__estado
    def setIdIncidente(self, idIncidente):
        self.__idIncidente = idIncidente
    def setDireccionIP(self, direccionIP):
        self.__direccionIP = direccionIP
    def setTipoAtaque(self, tipoAtaque):
        self.__tipoAtaque = tipoAtaque
    def setNivelRiesgo(self, nivelRiesgo):
        self.__nivelRiesgo = nivelRiesgo
    def setEstado(self, estado):
        self.__estado = estado

    def __str__(self):
        return (f"[ID: {self.__idIncidente}] IP: {self.__direccionIP} | "
                f"Ataque: {self.__tipoAtaque} | Riesgo: {self.__nivelRiesgo} | "
                f"Estado: {self.__estado}")


class Nodo:
    def __init__(self, dato):
        self.__dato = dato
        self.__hijoIzquierdo = None
        self.__hijoDerecho = None

    def getDato(self):
        return self.__dato
    def getHijoIzquierdo(self):
        return self.__hijoIzquierdo
    def getHijoDerecho(self):
        return self.__hijoDerecho
    def setDato(self, dato):
        self.__dato = dato
    def setHijoIzquierdo(self, hijoIzquierdo):
        self.__hijoIzquierdo = hijoIzquierdo
    def setHijoDerecho(self, hijoDerecho):
        self.__hijoDerecho = hijoDerecho

    def __str__(self):
        return str(self.__dato)


class ArbolBinarioBusqueda:
    def __init__(self):
        self.__raiz = None

    def getRaiz(self):
        return self.__raiz
    def setRaiz(self, raiz):
        self.__raiz = raiz
    def is_empty(self):
        return self.__raiz is None

    # Insertar incidente
    def insertar(self, incidente):
        self.__raiz = self._insertar(self.__raiz, incidente)

    def _insertar(self, actual, incidente):
        if actual is None:
            return Nodo(incidente)
        
        id_nuevo = incidente.getIdIncidente()
        id_actual = actual.getDato().getIdIncidente()

        if id_nuevo < id_actual:
            actual.setHijoIzquierdo(self._insertar(actual.getHijoIzquierdo(), incidente))
        elif id_nuevo > id_actual:
            actual.setHijoDerecho(self._insertar(actual.getHijoDerecho(), incidente))
        else:
            print(f"Error: El incidente con ID {id_nuevo} ya existe. No se permiten duplicados.")
        return actual

    # Mostrar estructura del árbol
    def imprimirArbol(self):
        self._imprimir(self.__raiz, 0)

    def _imprimir(self, actual, nivel):
        if actual is not None:
            self._imprimir(actual.getHijoDerecho(), nivel + 1)
            print("    " * nivel + str(actual.getDato().getIdIncidente()))
            self._imprimir(actual.getHijoIzquierdo(), nivel + 1)

    # Recorridos
    def recorridoInorden(self):
        self._inOrden(self.__raiz)
        print()

    def _inOrden(self, actual):
        if actual is not None:
            self._inOrden(actual.getHijoIzquierdo())
            print(actual.getDato())
            self._inOrden(actual.getHijoDerecho())

    def recorridoPostorden(self):
        self._postOrden(self.__raiz)
        print()

    def _postOrden(self, actual):
        if actual is not None:
            self._postOrden(actual.getHijoIzquierdo())
            self._postOrden(actual.getHijoDerecho())
            print(actual.getDato())

    def recorridoPreorden(self):
        self._preOrden(self.__raiz)
        print()

    def _preOrden(self, actual):
        if actual is not None:
            print(actual.getDato())
            self._preOrden(actual.getHijoIzquierdo())
            self._preOrden(actual.getHijoDerecho())

    # Buscar por ID
    def buscar(self, idIncidente):
        actual = self.__raiz
        while actual is not None:
            id_actual = actual.getDato().getIdIncidente()
            if id_actual == idIncidente:
                return actual.getDato()
            elif idIncidente < id_actual:
                actual = actual.getHijoIzquierdo()
            else:
                actual = actual.getHijoDerecho()
        return None

    # Eliminar por ID
    def eliminarNodo(self, idIncidente):
        self.__raiz = self._eliminar(self.__raiz, idIncidente)

    def _eliminar(self, actual, idIncidente):
        if actual is None:
            return None
        
        id_actual = actual.getDato().getIdIncidente()
        if idIncidente < id_actual:
            actual.setHijoIzquierdo(self._eliminar(actual.getHijoIzquierdo(), idIncidente))
        elif idIncidente > id_actual:
            actual.setHijoDerecho(self._eliminar(actual.getHijoDerecho(), idIncidente))
        else:
            if actual.getHijoIzquierdo() is None and actual.getHijoDerecho() is None:
                return None
            elif actual.getHijoIzquierdo() is None:
                return actual.getHijoDerecho()
            elif actual.getHijoDerecho() is None:
                return actual.getHijoIzquierdo()
            else:
                sucesor = self._minimo(actual.getHijoDerecho())
                actual.setDato(sucesor.getDato())
                actual.setHijoDerecho(self._eliminar(actual.getHijoDerecho(), sucesor.getDato().getIdIncidente()))
        return actual

    # Obtener menor y mayor ID
    def obtenerMenor(self):
        if self.is_empty():
            return None
        return self._minimo(self.__raiz).getDato()

    def _minimo(self, actual):
        if actual.getHijoIzquierdo() is None:
            return actual
        return self._minimo(actual.getHijoIzquierdo())

    def obtenerMayor(self):
        if self.is_empty():
            return None
        return self._maximo(self.__raiz).getDato()

    def _maximo(self, actual):
        if actual.getHijoDerecho() is None:
            return actual
        return self._maximo(actual.getHijoDerecho())

    # Contar nodos
    def contarNodos(self):
        return self._contar(self.__raiz)

    def _contar(self, actual):
        if actual is None:
            return 0
        return 1 + self._contar(actual.getHijoIzquierdo()) + self._contar(actual.getHijoDerecho())

    # Buscar por riesgo
    def buscarPorNivelRiesgo(self, nivel):
        self._buscarRiesgo(self.__raiz, nivel.lower())

    def _buscarRiesgo(self, actual, nivel):
        if actual is not None:
            self._buscarRiesgo(actual.getHijoIzquierdo(), nivel)
            if actual.getDato().getNivelRiesgo().lower() == nivel:
                print(actual.getDato())
            self._buscarRiesgo(actual.getHijoDerecho(), nivel)