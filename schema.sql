CREATE TABLE Location (
  `id` varchar(50) NOT NULL,
  `l_name` varchar(100) NOT NULL,
  CONSTRAINT location_pk PRIMARY KEY (id));

CREATE TABLE Product (
  `id` varchar(50) NOT NULL,
  `size` varchar(100),
  `name` varchar(100) NOT NULL,
  `price` decimal(15,2) NOT NULL,
  CONSTRAINT product_pk PRIMARY KEY (id));

CREATE TABLE Transaction (
  `id` varchar(50) NOT NULL,
  `date_time` int NOT NULL,
  `l_id` varchar(50) NOT NULL,
  `payment_type` varchar(4) NOT NULL,
  `total` decimal(15,2) NOT NULL,
  CONSTRAINT transaction_pk PRIMARY KEY (id),
  CONSTRAINT location_fk FOREIGN KEY (l_id)
  REFERENCES Location(id));

CREATE TABLE Orders (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date_time` int NOT NULL,
  `tsac_id` varchar(50) NOT NULL,
  `prod_id` varchar(50) NOT NULL,
  `price` decimal(15,2) NOT NULL,
  CONSTRAINT table_pk PRIMARY KEY (id),
  CONSTRAINT transaction_fk FOREIGN KEY (tsac_id)
  REFERENCES Transaction(id),
  CONSTRAINT product_fk FOREIGN KEY (prod_id)
  REFERENCES Product(id));
