from py.productoIMG import productoIMG


class productoIMGDB:
    def __init__(self,conn):
        self.conn = conn
        self.imagenes : list[productoIMG] = []
    def cargarImagenes(self):
        cursor = self.conn.cursor()

        query = ("SELECT * FROM imagenes_productos")

        cursor.execute(query)

        rows = cursor.fetchall()

        for row in rows:
            id,idprod,imagen,url,desc = row
            prod_img = productoIMG(id,idprod,imagen,url,desc)
            print(url)
            self.imagenes.append(prod_img)
