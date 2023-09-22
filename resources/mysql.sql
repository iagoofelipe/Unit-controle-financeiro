drop table `db_pedras_vivas`.`users`;

CREATE TABLE `db_pedras_vivas`.`users` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `user` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NULL,
  PRIMARY KEY (`id`));

CREATE TABLE `db_pedras_vivas`.`entradas` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `descricao` VARCHAR(255) NULL,
  `categoria` VARCHAR(45) NULL,
  `data` VARCHAR(45) NULL,
  `valor` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`));


CREATE TABLE `db_pedras_vivas`.`saidas` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `descricao` VARCHAR(255) NULL,
  `categoria` VARCHAR(45) NULL,
  `data` VARCHAR(45) NULL,
  `valor` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`));