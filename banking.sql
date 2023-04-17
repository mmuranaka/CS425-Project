CREATE SCHEMA `BankingDB` ;
CREATE TABLE `BankingDB`.`address` (
`address_id` INT UNSIGNED NOT NULL,
`house_number` INT UNSIGNED NOT NULL,
`street` VARCHAR(30) NOT NULL,
`zip_code` INT UNSIGNED NOT NULL,
`city` VARCHAR(30) NOT NULL,
`state` VARCHAR(2) NOT NULL,
PRIMARY KEY (`address_id`));
CREATE TABLE `BankingDB`.`customer` (
`customer_id` INT UNSIGNED NOT NULL,
`fname` VARCHAR(30) NULL,
`sname` VARCHAR(30) NOT NULL,
`ssn` INT UNSIGNED NOT NULL,
`address_id` INT UNSIGNED NOT NULL,
PRIMARY KEY (`customer_id`),
UNIQUE INDEX `ssn_UNIQUE` (`ssn` ASC) VISIBLE,
INDEX `customer_address_idx` (`address_id` ASC) VISIBLE,
CONSTRAINT `customer_address`
FOREIGN KEY (`address_id`)
REFERENCES `BankingDB`.`address` (`address_id`)
ON DELETE NO ACTION
ON UPDATE NO ACTION);
CREATE TABLE `BankingDB`.`branch` (
`branch_id` INT UNSIGNED NOT NULL,
`address_id` INT UNSIGNED NOT NULL,
PRIMARY KEY (`branch_id`),
INDEX `branch_address_idx` (`address_id` ASC) VISIBLE,
CONSTRAINT `branch_address`
FOREIGN KEY (`address_id`)
REFERENCES `BankingDB`.`address` (`address_id`)
ON DELETE NO ACTION
ON UPDATE NO ACTION);
CREATE TABLE `BankingDB`.`employee` (
`employee_id` INT UNSIGNED NOT NULL,
`fname` VARCHAR(30) NULL,
`sname` VARCHAR(30) NOT NULL,
`salary` VARCHAR(10) NOT NULL,
`position` VARCHAR(40) NOT NULL,
`ssn` INT UNSIGNED NOT NULL,
`address_id` INT UNSIGNED NOT NULL,
`branch_id` INT UNSIGNED NOT NULL,
PRIMARY KEY (`employee_id`),
INDEX `employee_address_idx` (`address_id` ASC) VISIBLE,
INDEX `employee_branch_idx` (`branch_id` ASC) VISIBLE,
CONSTRAINT `employee_address`
FOREIGN KEY (`address_id`)
REFERENCES `BankingDB`.`address` (`address_id`)
ON DELETE NO ACTION
ON UPDATE NO ACTION,
CONSTRAINT `employee_branch`
FOREIGN KEY (`branch_id`)
REFERENCES `BankingDB`.`branch` (`branch_id`)
ON DELETE NO ACTION
ON UPDATE NO ACTION);
CREATE TABLE `BankingDB`.`account_type` (
`type` VARCHAR(40) NOT NULL,
`interest_rate` FLOAT NULL,
`required_deposit` FLOAT NULL,
`overdraft_fee` FLOAT NULL,
`service_fee` FLOAT NULL,
`annual_percentage_fee` FLOAT NULL,
PRIMARY KEY (`type`));
CREATE TABLE `BankingDB`.`account` (
`account_num` INT UNSIGNED NOT NULL,
`account_name` VARCHAR(40) NOT NULL,
`balance` VARCHAR(45) NOT NULL,
`branch_id` INT UNSIGNED NOT NULL,
`type` VARCHAR(40) NULL,
`customer_id` INT UNSIGNED NOT NULL,
PRIMARY KEY (`account_num`),
INDEX `account_home_branch_idx` (`branch_id` ASC) VISIBLE,
INDEX `account_type_idx` (`type` ASC) VISIBLE,
INDEX `account_owner_idx` (`customer_id` ASC) VISIBLE,
CONSTRAINT `account_home_branch`
FOREIGN KEY (`branch_id`)
REFERENCES `BankingDB`.`branch` (`branch_id`)
ON DELETE NO ACTION
ON UPDATE NO ACTION,
CONSTRAINT `account_type`
FOREIGN KEY (`type`)
REFERENCES `BankingDB`.`account_type` (`type`)
ON DELETE NO ACTION
ON UPDATE NO ACTION,
CONSTRAINT `account_owner`
FOREIGN KEY (`customer_id`)
REFERENCES `BankingDB`.`customer` (`customer_id`)
ON DELETE NO ACTION
ON UPDATE NO ACTION);
CREATE TABLE `BankingDB`.`transaction` (
`trans_id` INT UNSIGNED NOT NULL,
`amount` FLOAT NOT NULL,
`date` DATE NOT NULL,
`trans_type` VARCHAR(10) NOT NULL,
`account_num` INT UNSIGNED NOT NULL,
PRIMARY KEY (`trans_id`),
INDEX `transaction_account_idx` (`account_num` ASC) VISIBLE,
CONSTRAINT `transaction_account`
FOREIGN KEY (`account_num`)
REFERENCES `BankingDB`.`account` (`account_num`)
ON DELETE NO ACTION
ON UPDATE NO ACTION);