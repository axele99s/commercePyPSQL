from py.Producto import Producto


class productoDB:
    def __init__(self,db_con):
        self.db_con = db_con
        self.productos : list[Producto] = []

    def cargarProductos(self):
        cursor = self.db_con.cursor()

        query = ("SELECT * FROM producto")

        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
           idprod,idmarca, idcategoria,descripcion,codigo,precio = row
           prod = Producto(idprod,idmarca,idcategoria,descripcion,codigo,precio)
           self.productos.append(prod)
            #print({"desc:"}, descripcion,{" cod:"},codigo, {"precio: "},precio)

