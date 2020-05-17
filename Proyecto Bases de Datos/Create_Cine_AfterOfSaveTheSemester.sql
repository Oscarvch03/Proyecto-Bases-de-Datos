----------------------------------------------------
-- TABLAS ------------------------------------------

create TABLE cliente
(cliente_id VARCHAR(12) not null,
 cliente_nombre1 VARCHAR(12) not null,
 cliente_nombre2 VARCHAR(12),
 cliente_apellido1 VARCHAR(12) not null,
 cliente_apellido2 VARCHAR(12) not null,
 cliente_edad NUMERIC(5),
 cliente_telefono VARCHAR(12),
 cliente_contraseña VARCHAR(20) not null,
 primary key (cliente_id));
 
 
create TABLE pelicula
(pelicula_id SERIAL not null,
 pelicula_nombre VARCHAR(50) not null,
 pelicula_genero VARCHAR(20) not null, 
 pelicula_idioma VARCHAR(20) not null, 
 pelicula_clasificacion NUMERIC(5) not null,
 pelicula_duracion NUMERIC(5) not null,
 primary key (pelicula_id));
 
 
create TABLE funcion
(funcion_id SERIAL not null,
 funcion_hora_inicio VARCHAR(10) not null,
 funcion_hora_fin VARCHAR(10) not null,
 primary key (funcion_id));
  
  
create TABLE sala
(sala_id SERIAL not null,
 sala_genero VARCHAR(20) not null,
 primary key (sala_id));
   
   
create TABLE empleado
(empleado_id VARCHAR(12) not null,
 empleado_nombre1 VARCHAR(12) not null,
 empleado_nombre2 VARCHAR(12),
 empleado_apellido1 VARCHAR(12) not null,
 empleado_apellido2 VARCHAR(12) not null,
 empleado_edad NUMERIC(5),
 empleado_contraseña VARCHAR(20) not null,
 primary key (empleado_id));
 
 
create TABLE producto
(producto_id SERIAL not null,
 producto_nombre VARCHAR(20) not null,
 producto_precio NUMERIC(10, 2) not null,
 primary key (producto_id));
 
 
create TABLE tarjeta
(tarjeta_id SERIAL not null,
 tarjeta_nombre VARCHAR(30) not null,
 tarjeta_beneficio NUMERIC(5, 2) not null,
 primary key (tarjeta_id));
 
 
create TABLE trabajo
(trabajo_id SERIAL not null,
 trabajo_nombre VARCHAR(20),
 primary key (trabajo_id));
 
 
----------------------------------------------------
-- RELACIONES --------------------------------------
 
 
create TABLE funcionDePelicula
(funcionDePelicula_id SERIAL not null,
 funcion_id INTEGER not null,
 funcionDePelicula_fecha VARCHAR(20) not null,
 pelicula_id INTEGER not null,
 sala_id INTEGER not null,
 primary key (funcionDePelicula_id),
 foreign key (funcion_id) references funcion,
 foreign key (pelicula_id) references pelicula,
 foreign key (sala_id) references sala);
 
 
create TABLE clienteCompraProducto
(compra_id SERIAL not null,
 cliente_id VARCHAR(12) not null,
 producto_id INTEGER not null,
 primary key (compra_id),
 foreign key (cliente_id) references cliente,
 foreign key (producto_id) references producto);
 
 
create TABLE clienteTieneTarjeta
(c_t_t_id SERIAL not null,
 cliente_id VARCHAR(12) not null,
 tarjeta_id INTEGER not null,
 tarjeta_contraseña VARCHAR(20) not null,
 primary key (c_t_t_id),
 foreign key (cliente_id) references cliente,
 foreign key (tarjeta_id) references tarjeta);
 
 
create TABLE empleadoTrabajaEn
(e_t_e_id SERIAL not null,
 empleado_id VARCHAR(12) not null,
 trabajo_id INTEGER not null,
 sueldo NUMERIC(15, 2) not null,
 primary key (e_t_e_id),
 foreign key (empleado_id) references empleado,
 foreign key (trabajo_id) references trabajo);
 
 
 
 