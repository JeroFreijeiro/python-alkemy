# librerias Yenny (ejemplo en clase nº4)

""" 
class Producto
    id
    precio
    titulo
    director
    categoria (Libro, Musica, Cine)
        class Libros ---------------------------------- #esto es un producto
            editorial
            cantPaginas
            generoLiterario (novela, policial, ensayo)
            + leerSinapsis ---------------------------- #esto sería un metodo
            + leerContratapa -------------------------- #esto sería un metodo
        class Musica ---------------------------------- #esto es un producto
            sello
            duracion
            formato (CD, VINILO, CASETTE)
            generoMusical (Rock, Pop, Trap)
            + probarDisco #esto sería un metodo
        class Cine ------------------------------------- #esto es un producto
            duracion
            generoCine (terror, aventura, drama, documental)


class Usuario
    id
    nombre
    apellido
    email
    contrasenia
    userName
    dni
    carrito de compras (LISTA DE PRODUCTOS)
    lista de favoritos (LISTA DE PRODUCTOS)
    historial de compras (LISTA DE ORDENES DE COMPRAS PASADAS)


class OrdenDeCompra
    id
    precioFinal
    productos (LISTA DE PRODUCTOS)
    comprador (usuario - id)
"""