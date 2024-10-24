CREATE TABLE PROVINCIA (
    idProvincia BIGINT PRIMARY KEY NOT NULL,
    codigoProvincia INTEGER NOT NULL UNIQUE,  
    nombreProvincia VARCHAR(80) NOT NULL
);

CREATE TABLE LOCALIDAD (
    idLocalidad BIGINT PRIMARY KEY NOT NULL,
    idProvincia BIGINT NOT NULL,
    codigoLocalidad INTEGER NOT NULL UNIQUE, 
    nombreLocalidad VARCHAR(80) NOT NULL,
    CONSTRAINT fk_provincia FOREIGN KEY (idProvincia) REFERENCES PROVINCIA(idProvincia)
);

CREATE TABLE PERSONA (
    idPersona BIGINT PRIMARY KEY NOT NULL,
    idLocalidad BIGINT NOT NULL,
    nombre VARCHAR(80) NOT NULL,
    apellido VARCHAR(80),
    dni INTEGER NOT NULL UNIQUE,  
    tipoDNI SMALLINT NOT NULL,
    CONSTRAINT fk_localidad FOREIGN KEY (idLocalidad) REFERENCES LOCALIDAD(idLocalidad)
);

CREATE TABLE CLIENTE (
    idPersona BIGINT NOT NULL,
    idCliente BIGINT PRIMARY KEY NOT NULL,
    codigoCliente INTEGER NOT NULL UNIQUE,  
    CONSTRAINT fk_persona_cliente FOREIGN KEY (idPersona) REFERENCES PERSONA(idPersona)
);

CREATE TABLE EMPLEADO (
    idPersona BIGINT NOT NULL,
    idEmpleado BIGINT PRIMARY KEY NOT NULL,
    codigoEmpleado INTEGER NOT NULL UNIQUE,  
    CONSTRAINT fk_persona_empleado FOREIGN KEY (idPersona) REFERENCES PERSONA(idPersona)
);

CREATE TABLE CATEGORIA (
    idCategoria BIGINT PRIMARY KEY NOT NULL,
    descripcion VARCHAR(80) NOT NULL,
    codigo INTEGER NOT NULL UNIQUE  
);

CREATE TABLE MARCA (
    idMarca BIGINT PRIMARY KEY NOT NULL,
    descripcion VARCHAR(80) NOT NULL,
    codigo INTEGER NOT NULL UNIQUE  
);

CREATE TABLE PRODUCTO (
    idProducto BIGINT PRIMARY KEY NOT NULL,
    idCategoria BIGINT NOT NULL,
    idMarca BIGINT NOT NULL,
    descripcion VARCHAR(80) NOT NULL,
    codigo INTEGER NOT NULL UNIQUE,
    precio NUMERIC(38, 2) NOT NULL,
    CONSTRAINT fk_categoria FOREIGN KEY (idCategoria) REFERENCES CATEGORIA(idCategoria),
    CONSTRAINT fk_marca FOREIGN KEY (idMarca) REFERENCES MARCA(idMarca)
);

CREATE TABLE FORMA_PAGO (
    idFormaPago BIGINT PRIMARY KEY NOT NULL,
    codigo INTEGER NOT NULL UNIQUE,  
    descripcion VARCHAR(80) NOT NULL
);

CREATE TABLE FACTURA (
    idFactura BIGINT PRIMARY KEY NOT NULL,
    idEmpleado BIGINT NOT NULL,
    idCliente BIGINT NOT NULL,
    fecha DATE NOT NULL,
    idFormaPago BIGINT NOT NULL,
	codigo INTEGER NOT NULL UNIQUE, 
    CONSTRAINT fk_empleado FOREIGN KEY (idEmpleado) REFERENCES EMPLEADO(idEmpleado),
    CONSTRAINT fk_cliente FOREIGN KEY (idCliente) REFERENCES CLIENTE(idCliente),
    CONSTRAINT fk_forma_pago FOREIGN KEY (idFormaPago) REFERENCES FORMA_PAGO(idFormaPago)
);

CREATE TABLE DETALLE_FACTURA (
    idFactura BIGINT NOT NULL,
    idProducto BIGINT NOT NULL,
    cantidad INTEGER NOT NULL,
    precioUnitario NUMERIC(38, 2) NOT NULL,
    CONSTRAINT fk_factura FOREIGN KEY (idFactura) REFERENCES FACTURA(idFactura),
    CONSTRAINT fk_producto FOREIGN KEY (idProducto) REFERENCES PRODUCTO(idProducto),
    CONSTRAINT UNIQUE (idFactura, idProducto) 
);



-- Crear secuencias
CREATE SEQUENCE cliente_seq
    START WITH 1
    INCREMENT BY 1;

CREATE SEQUENCE empleado_seq
    START WITH 1
    INCREMENT BY 1;

CREATE SEQUENCE localidad_seq
    START WITH 1
    INCREMENT BY 1;

CREATE SEQUENCE persona_seq
    START WITH 1
    INCREMENT BY 1;

CREATE SEQUENCE producto_seq
    START WITH 1
    INCREMENT BY 1;

CREATE SEQUENCE provincia_seq
    START WITH 1
    INCREMENT BY 1;

-- Alterar tablas para usar las secuencias al insertar
ALTER TABLE CLIENTE ALTER COLUMN idCliente SET DEFAULT nextval('cliente_seq');
ALTER TABLE EMPLEADO ALTER COLUMN idEmpleado SET DEFAULT nextval('empleado_seq');
ALTER TABLE LOCALIDAD ALTER COLUMN idLocalidad SET DEFAULT nextval('localidad_seq');
ALTER TABLE PERSONA ALTER COLUMN idPersona SET DEFAULT nextval('persona_seq');
ALTER TABLE PRODUCTO ALTER COLUMN idProducto SET DEFAULT nextval('producto_seq');
ALTER TABLE PROVINCIA ALTER COLUMN idProvincia SET DEFAULT nextval('provincia_seq');
-- Nota <- lo de arriba se podía solucionar con un SERIAL en lugar de crear todos los nextval… asociar las sequence…alter table... etc
 -- Pero bueno ya lo hice asi :(