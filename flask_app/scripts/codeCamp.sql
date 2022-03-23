-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema esquema_code_camp
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema esquema_code_camp
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `esquema_code_camp` ;
USE `esquema_code_camp` ;

-- -----------------------------------------------------
-- Table `esquema_code_camp`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_code_camp`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(150) NULL,
  `last_name` VARCHAR(150) NULL,
  `email` VARCHAR(150) NULL,
  `password` VARCHAR(150) NULL,
  `image` TEXT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_code_camp`.`technologies`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_code_camp`.`technologies` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `tech_name` VARCHAR(150) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_code_camp`.`rooms`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_code_camp`.`rooms` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` TEXT NULL,
  `level` VARCHAR(100) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `technologie_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_rooms_technologies1_idx` (`technologie_id` ASC) VISIBLE,
  CONSTRAINT `fk_rooms_technologies1`
    FOREIGN KEY (`technologie_id`)
    REFERENCES `esquema_code_camp`.`technologies` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_code_camp`.`users_has_rooms`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_code_camp`.`users_has_rooms` (
  `user_id` INT NOT NULL,
  `room_id` INT NOT NULL,
  PRIMARY KEY (`user_id`, `room_id`),
  INDEX `fk_users_has_rooms_rooms1_idx` (`room_id` ASC) VISIBLE,
  INDEX `fk_users_has_rooms_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_has_rooms_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `esquema_code_camp`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_rooms_rooms1`
    FOREIGN KEY (`room_id`)
    REFERENCES `esquema_code_camp`.`rooms` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_code_camp`.`messages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_code_camp`.`messages` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `message` TEXT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  `room_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_messages_users1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_messages_rooms1_idx` (`room_id` ASC) VISIBLE,
  CONSTRAINT `fk_messages_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `esquema_code_camp`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_messages_rooms1`
    FOREIGN KEY (`room_id`)
    REFERENCES `esquema_code_camp`.`rooms` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
