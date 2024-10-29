from py.Producto import Producto


class productoDB:
    def __init__(self,db_con):
        self.db_con = db_con
        self.productos : list[Producto] = []
        self.cargarProductos()
    def cargarProductos(self):
        cursor = self.db_con.cursor()

        query = ("SELECT * FROM producto")

        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
           idprod,idmarca, idcategoria,descripcion,codigo,precio,estado = row
           prod = Producto(idprod,idmarca,idcategoria,descripcion,codigo,precio,estado)
           self.productos.append(prod)

    def agregarProducto(self, prod: Producto):
        try:
            idcat = prod.getCategoria()
            idmar = prod.getMarca()
            desc = prod.getDescripcion()
            cod = prod.getCodigo()
            price = prod.getPrecio()

            cursor = self.db_con.cursor()

            query = ("""INSERT INTO producto (idcategoria, idmarca, descripcion, codigo, precio)
                         VALUES (%s, %s, %s, %s, %s)""")

            cursor.execute(query, (idcat, idmar, desc, cod, price))
            self.db_con.commit()  # Guarda los cambios

            return None  # No hay error

        except Exception as e:
            return str(e)  # Retorna el mensaje de error como string



    def getProductos(self):
        return self.productos

    def cambiarEstado(self, id,estado):
        cursor = self.db_con.cursor()

        query2 = "UPDATE producto SET estado = %s WHERE idproducto = %s"

        try:
            cursor.execute(query2, (estado,id,))
            self.db_con.commit()
            return None
        except Exception as e:
            return str(e)


    def verProducto(self,id):
        for producto in self.productos:
            if producto.idProducto == id :
                return producto
        return None
