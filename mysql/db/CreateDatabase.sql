USE db;


CREATE TABLE cadastro (
    id integer not null auto_increment,
    sexo varchar(200),
    titulo varchar(200),
    nome varchar(200),
    sobrenome varchar(200),
    cidade varchar(200),
    estado varchar(200),
    pais varchar(200),
    email varchar(200),
    data_nascimento date,
    load_date datetime not null,
    KEY (id)    
);

CREATE TABLE cadastro_raw (
    id integer not null auto_increment,
    gender varchar(200),
    email varchar(200),
    phone varchar(200),
    cell varchar(200),
    nat varchar(200),
    name_title varchar(200),
    name_first varchar(200),
    name_last varchar(200),
    location_street_number varchar(200),
    location_street_name varchar(200),
    location_city varchar(200),
    location_state varchar(200),
    location_country varchar(200),
    location_postcode varchar(200),
    location_coordinates_latitude varchar(200),
    location_coordinates_longitude varchar(200),
    location_timezone_offset varchar(200),
    location_timezone_description varchar(200),
    login_uuid varchar(200),
    login_username varchar(200),
    login_password varchar(200),
    login_salt varchar(200),
    login_md5 varchar(200),
    login_sha1 varchar(200),
    login_sha256 varchar(200),
    dob_date varchar(200),
    dob_age varchar(200),
    registered_date varchar(200),
    registered_age varchar(200),
    id_name varchar(200),
    id_value varchar(200),
    picture_large varchar(200),
    picture_medium varchar(200),
    picture_thumbnail varchar(200),
    load_date datetime not null,
    KEY (id) 
);   

SET character_set_client = utf8;
SET character_set_connection = utf8;
SET character_set_results = utf8;
SET collation_connection = utf8_general_ci;
INSERT INTO cadastro (id, sexo, titulo, nome, sobrenome, cidade, estado, pais, email, data_nascimento, load_date) 
VALUES (1, "female", "Miss", "Victoria", "Lambert", "Gloucester", "Rutland", "United Kingdom", "victoria.lambert@example.com", "1965-06-20", "2024-03-16");