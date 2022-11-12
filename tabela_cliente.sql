CREATE TABLE cliente(
	ID int NOT NULL,
	NOME varchar(80),
	CPF varchar(11),
	DATA_CADASTRO text DEFAULT CURRENT_TIMESTAMP,
	ENDERECO varchar(80),
	PRIMARY KEY(Id)
);

insert into cliente values(1, "Danilo", "11111111111", "08/10/2022", "RIO TINTO");

select * from cliente;
