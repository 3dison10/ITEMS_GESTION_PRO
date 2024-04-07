create database items; 
show databases;
use items; 

show columns from empleado;

alter table solicitud add foreign key (id_tipoSolicitud) references tipoSolicitud (id_tipoSolicitud);
alter table cronograma add foreign key (id_empleado) references empleado (id_empleado);
alter table solicitudProducto add foreign key (id_servicio) references servicios (id_servicio);
alter table empleado add foreign key (id_cargo) references cargos (id_cargo);
alter table solicitudProducto add foreign key (id_producto) references producto (id_producto);
alter table cronograma add foreign key (id_solicitud) references solicitud (id_solicitud);
alter table solicitudProducto add foreign key (id_solicitud) references solicitud (id_solicitud);

alter table solicitud add primary key (id_solicitud);


create table cliente(
	id_cliente int (10) primary key not null,
    nombre_cliente varchar (45) not null,
    direccion_cliente varchar (10) not null,
    telefono_cliente int (10) not null,
    correo_cliente varchar (45) not null
);

create table tipoSolicitud(
	id_tipoSolicitud int (10) primary key not null,
    nombre_tipoSolicitud varchar (40)
);

create table solicitud(
	id_solicitud int (10),
    fecha_solicitud date,
    hora_solicitud time,
    id_cliente int (10),
    id_tipoSolicitud int (10),
    foreign key (id_cliente) references cliente (id_cliente)
 );

create table solicitudProducto(
	id_solicitud int (10) not null,
    id_producto int (10) not null,
    id_servicio int (10) not null
);

create table producto(
	id_producto int (10) primary key not null,
    nombre_producto varchar (45) not null,
    descripcion_producto varchar (45),
    cantidad_producto int not null
);

create table servicios(
	id_servicio	int (10) primary key not null,
    nombre_servicio varchar (45)
);



create table empleado(
	id_empleado int (10) primary key not null,
    nombre_empleado varchar (45) not null,
    apellido_empleado varchar (45) not null,
    telefono_empleado int (10),
    correo_empleado varchar (45),
    id_cargo int (10)
);

create table cargos(
	id_cargo int (10) primary key not null,
    nombre_cargo varchar (45)
);

create table cronograma(
	id_cronograma int (10) primary key not null,
    id_solicitud int (10) not null,
    id_empleado int (10) not null,
    fecha_cronograma date
);

