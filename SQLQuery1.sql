CREATE DATABASE Caixa;
USE Caixa;

CREATE TABLE Produtos(
Cod_Prod VARCHAR(50) NOT NULL,
ValorUnit_Prod DECIMAL(10,2),
Quantidade_Prod VARCHAR(50) NOT NULL
)

ALTER TABLE Produtos
ADD Nome_Prod VARCHAR(100);

INSERT INTO Produtos (Cod_Prod, ValorUnit_Prod, Quantidade_Prod, Nome_Prod)
VALUES (1, 10.00, 5,'Papel higienico');