CREATE TABLE fornecedor (
    id INT,
    nome VARCHAR(150) NOT NULL,
    endereco VARCHAR(150),
    produtos VARCHAR(20)
);
INSERT INTO fornecedor (id, nome, endereco, produtos) VALUES (1, 'Empresa de Leite ParmaLeite', 'Rua dos Leites, 23', 'leite');
INSERT INTO fornecedor (id, nome, endereco, produtos) VALUES (2, 'Peixaria Abril', 'Rua dos Leites, 25', 'peixe');
INSERT INTO fornecedor (id, nome, endereco, produtos) VALUES (3, 'Açougue Legal', 'Rua dos Leites, 30', 'carnes');
INSERT INTO fornecedor (id, nome, endereco, produtos) VALUES (4, 'Açougue Novo', 'Rua dos Leites, 35', 'carnes');
INSERT INTO fornecedor (id, nome, endereco, produtos) VALUES (3, 'Padaria do Pão', 'Rua dos Leites, 66', 'Pães');
INSERT INTO fornecedor (id, nome, endereco, produtos) VALUES (4, 'Marcenaria Martelo', 'Rua dos Leites, 99', 'Madeiras');
UPDATE fornecedor SET endereco = 'Rua dos Peixes, 26' WHERE id = 2;
Select * from fornecedor
SELECT id, nome, endereco, produtor FROM fornecedor WHERE produtos ='carnes';
DELETE FROM fornecedor WHERE id=1;