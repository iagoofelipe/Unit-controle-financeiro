drop table `users`;

CREATE TABLE `users` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `user` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NULL,
  PRIMARY KEY (`id`));

CREATE TABLE `entradas` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `descricao` VARCHAR(255) NULL,
  `categoria` VARCHAR(45) NULL,
  `data` VARCHAR(45) NULL,
  `valor` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`));


CREATE TABLE `saidas` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `descricao` VARCHAR(255) NULL,
  `categoria` VARCHAR(45) NULL,
  `data` VARCHAR(45) NULL,
  `valor` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`));