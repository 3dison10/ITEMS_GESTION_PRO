-- Creación de la base de datos
CREATE DATABASE IF NOT EXISTS items;
USE items;

-- Creación de tablas
CREATE TABLE IF NOT EXISTS cliente (
    id_cliente INT (10) PRIMARY KEY NOT NULL,
    nombre_cliente VARCHAR (45) NOT NULL,
    direccion_cliente VARCHAR (10) NOT NULL,
    telefono_cliente INT (10) NOT NULL,
    correo_cliente VARCHAR (45) NOT NULL
);

CREATE TABLE IF NOT EXISTS tipoSolicitud (
    id_tipoSolicitud INT (10) PRIMARY KEY NOT NULL,
    nombre_tipoSolicitud VARCHAR (40)
);

CREATE TABLE IF NOT EXISTS solicitud (
    id_solicitud INT (10) PRIMARY KEY,
    fecha_solicitud DATE NOT NULL,
    hora_solicitud TIME NOT NULL,
    id_cliente INT (10),
    id_tipoSolicitud INT (10),
    FOREIGN KEY (id_cliente) REFERENCES cliente (id_cliente)
);

CREATE TABLE IF NOT EXISTS solicitudProducto (
    id_solicitud INT (10) NOT NULL,
    id_producto INT (10) NOT NULL,
    id_servicio INT (10) NOT NULL
);

CREATE TABLE IF NOT EXISTS producto (
    id_producto INT (10) PRIMARY KEY NOT NULL,
    nombre_producto VARCHAR (45) NOT NULL,
    descripcion_producto VARCHAR (45),
    cantidad_producto INT NOT NULL
);

CREATE TABLE IF NOT EXISTS servicios (
    id_servicio INT (10) PRIMARY KEY NOT NULL,
    nombre_servicio VARCHAR (45)
);

CREATE TABLE IF NOT EXISTS empleado (
    id_empleado INT (10) PRIMARY KEY NOT NULL,
    nombre_empleado VARCHAR (45) NOT NULL,
    apellido_empleado VARCHAR (45) NOT NULL,
    telefono_empleado INT (10),
    correo_empleado VARCHAR (45),
    id_cargo INT (10)
);

CREATE TABLE IF NOT EXISTS cargos (
    id_cargo INT (10) PRIMARY KEY NOT NULL,
    nombre_cargo VARCHAR (45)
);

-- Creación de restricciones de clave externa
ALTER TABLE solicitud ADD FOREIGN KEY (id_tipoSolicitud) REFERENCES tipoSolicitud (id_tipoSolicitud);
ALTER TABLE solicitudProducto ADD FOREIGN KEY (id_servicio) REFERENCES servicios (id_servicio);
ALTER TABLE empleado ADD FOREIGN KEY (id_cargo) REFERENCES cargos (id_cargo);
ALTER TABLE solicitudProducto ADD FOREIGN KEY (id_solicitud) REFERENCES solicitud (id_solicitud);
