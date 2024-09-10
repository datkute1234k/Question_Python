-- TAO BANG MOI VOI CAC SAN PHAM CO GIA > 500.00
SELECT * 
INTO Price 
FROM [production].[products]
WHERE [list_price] > 500.00 

-- TAO RA BANG MOI DON HANG CHI DUOC GIAO DEN NEWYORK 
SELECT *
INTO Contry 
FROM [sales].[customers]
WHERE [state] = 'NY'

-- TAO BANG TAM THOI CUSOMERLONDON CHUA TT KHACH HANG O LONDON 

SELECT [CustomerID],
        [CompanyName],
        [ContactName],
        [City],
        [Phone],
        [Fax]
INTO CUSTOMERLONDON 
FROM [dbo].[Customers]
WHERE [City] LIKE 'LONDON'

-- XOA NHUNG NGUOI MUA HANG TRONG NAM 2016

DELETE FROM [dbo].[Price] 
WHERE [model_year] = '2016'

DELETE FROM [dbo].[Contry]

TRUNCATE TABLE [dbo].[Contry]

DELETE FROM OrderDetails_1
WHERE OrderID IN (SELECT OrderID FROM Orders_1 WHERE CustomerID = 'FRANS');
DELETE FROM Orders_1
WHERE CustomerID LIKE 'FRANS';
