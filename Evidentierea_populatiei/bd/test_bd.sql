create database test;
use test;
CREATE TABLE Persoane (
    ID_Persoana INT PRIMARY KEY,
    Nume VARCHAR(100) NOT NULL,
    Prenume VARCHAR(100) NOT NULL,
    Varsta INT CHECK (Varsta >= 0 AND Varsta <= 120), 
    ID_Categorie INT,
    ID_Institutie INT,
    UNIQUE(Nume, Prenume) 
);
CREATE TABLE Institutii (
    ID_Institutie INT PRIMARY KEY,
    Nume_Institutie VARCHAR(100) NOT NULL,
    Adresa VARCHAR(255),
    Tip VARCHAR(50) CHECK (Tip IN ('Educatie', 'Sanatate', 'Guvern', 'Privat')) 
);

CREATE TABLE Categorii (
    ID_Categorie INT PRIMARY KEY,
    Descriere VARCHAR(50) CHECK (Descriere IN ('Adolescent', 'Adult', 'Batran')) 
);

CREATE TABLE Casatorie (
    ID_Casatorie INT PRIMARY KEY,
    ID_Sot INT,
    ID_Sotie INT,
    Data_Casatorie DATE,
    CONSTRAINT FK_Sot FOREIGN KEY (ID_Sot) REFERENCES Persoane(ID_Persoana) ON DELETE CASCADE,
    CONSTRAINT FK_Sotie FOREIGN KEY (ID_Sotie) REFERENCES Persoane(ID_Persoana) ON DELETE CASCADE,
    CHECK (ID_Sot != ID_Sotie) 
);

CREATE TABLE Angajati (
    ID_Angajat INT PRIMARY KEY,
    ID_Persoana INT,
    ID_Institutie INT,
    Data_Angajare DATE NOT NULL,
    Salariu DECIMAL(10, 2) CHECK (Salariu > 0), 
    CONSTRAINT FK_Persoana FOREIGN KEY (ID_Persoana) REFERENCES Persoane(ID_Persoana) ON DELETE CASCADE,
    CONSTRAINT FK_Institutie FOREIGN KEY (ID_Institutie) REFERENCES Institutii(ID_Institutie) ON DELETE CASCADE
);

INSERT INTO Categorii (ID_Categorie, Descriere) VALUES 
(1, 'Adolescent'),
(2, 'Adult'),
(3, 'Batran');


INSERT INTO Institutii (ID_Institutie, Nume_Institutie, Adresa, Tip) VALUES 
(1, 'Liceul National', 'Str. Libertatii, Nr. 45', 'Educatie'),
(2, 'Spitalul Municipal', 'Bd. Independentei, Nr. 101', 'Sanatate'),
(3, 'Primaria Orasului', 'Piata Revolutiei, Nr. 1', 'Guvern'),
(4, 'Firma Tech Solutions', 'Calea Victoriei, Nr. 32', 'Privat'),
(5, 'Universitatea Tehnica', 'Str. Universitatii, Nr. 12', 'Educatie'),
(6, 'Clinica Sfantul Andrei', 'Bd. Sperantei, Nr. 45', 'Sanatate'),
(7, 'Consiliul Judetean', 'Bd. Eroilor, Nr. 22', 'Guvern'),
(8, 'Firma IT Innovate', 'Str. Tehnologiei, Nr. 5', 'Privat'),
(9, 'Scoala Generala Nr. 3', 'Str. Scolii, Nr. 10', 'Educatie'),
(10, 'Spitalul de Urgenta', 'Str. Urgentelor, Nr. 8', 'Sanatate'),
(11, 'Agentia Nationala', 'Bd. Independentei, Nr. 33', 'Guvern'),
(12, 'Firma Creative Solutions', 'Str. Inovatiei, Nr. 14', 'Privat');

INSERT INTO Persoane (ID_Persoana, Nume, Prenume, Varsta, ID_Categorie, ID_Institutie) VALUES 
(1, 'Popescu', 'Ion', 16, 1, 1),
(2, 'Ionescu', 'Maria', 28, 2, 4),
(3, 'Georgescu', 'Ana', 65, 3, NULL),
(4, 'Vasilescu', 'Mihai', 34, 2, 2),
(5, 'Dumitrescu', 'Elena', 45, 2, 3),
(6, 'Marinescu', 'Andrei', 23, 2, 4),
(7, 'Popa', 'Ioana', 37, 2, 1),
(8, 'Radu', 'Alexandru', 17, 1, NULL),
(9, 'Badea', 'Cristina', 52, 2, 2),
(10, 'Tanase', 'George', 70, 3, NULL),
(11, 'Iordache', 'Daniel', 29, 2, 4),
(12, 'Marin', 'Florin', 41, 2, 3),
(13, 'Stoica', 'Oana', 30, 2, 1),
(14, 'Barbu', 'Laura', 22, 2, 2),
(15, 'Cojocaru', 'Marius', 15, 1, 1),
(16, 'Nedelcu', 'Ioan', 63, 3, NULL),
(17, 'Petrescu', 'Elena', 38, 2, 2),
(18, 'Dobre', 'Vlad', 28, 2, 4),
(19, 'Constantinescu', 'Irina', 47, 2, 3),
(20, 'Manea', 'Sorin', 19, 1, NULL),
(21, 'Vlad', 'Andreea', 55, 2, 3),
(22, 'Lungu', 'Gabriel', 34, 2, 2),
(23, 'Popescu', 'Adriana', 26, 2, 4),
(24, 'Ciobanu', 'Razvan', 42, 2, 3),
(25, 'Rusu', 'Monica', 17, 1, NULL),
(26, 'Grigorescu', 'Daniela', 60, 3, NULL),
(27, 'Mihailescu', 'Stefan', 33, 2, 1),
(28, 'Enache', 'Carmen', 27, 2, 4),
(29, 'Preda', 'Alexandru', 36, 2, 2),
(30, 'Voinea', 'Liliana', 50, 2, 3),
(31, 'Stancu', 'Emil', 22, 2, 4),
(32, 'Dinescu', 'Bianca', 44, 2, 3),
(33, 'Florea', 'Ionela', 18, 1, 1),
(34, 'Tudor', 'Mircea', 31, 2, 2),
(35, 'Gheorghe', 'Cristina', 58, 3, NULL),
(36, 'Pop', 'Adrian', 20, 1, NULL);

INSERT INTO Casatorie (ID_Casatorie, ID_Sot, ID_Sotie, Data_Casatorie) VALUES 
(1, 2, 4, '2010-06-15'),
(2, 3, 5, '1995-09-23'),
(3, 6, 7, '2018-04-10'),
(4, 8, 9, '2010-12-25'),
(5, 11, 13, '2016-08-12'),
(6, 12, 17, '2007-03-30'),
(7, 14, 18, '2019-11-21'),
(8, 19, 21, '2001-04-07'),
(9, 22, 24, '2014-09-18'),
(10, 23, 27, '2015-10-22'),
(11, 25, 26, '2018-12-05'),
(12, 29, 30, '2013-06-17'),
(13, 31, 32, '2020-07-25'),
(14, 33, 34, '2019-01-14');

INSERT INTO Angajati (ID_Angajat, ID_Persoana, ID_Institutie, Data_Angajare, Salariu) VALUES 
(1, 2, 4, '2015-05-20', 4500.00),
(2, 4, 2, '2012-11-01', 3800.00),
(3, 5, 3, '2000-01-10', 5200.00),
(4, 11, 4, '2018-05-15', 4800.00),
(5, 12, 7, '2008-03-12', 5100.00),
(6, 13, 1, '2017-09-20', 3900.00),
(7, 14, 10, '2020-01-05', 3500.00),
(8, 17, 6, '2015-07-19', 4200.00),
(9, 18, 8, '2019-11-01', 4600.00),
(10, 19, 7, '2010-02-14', 5000.00),
(11, 21, 11, '2005-06-30', 5300.00),
(12, 22, 10, '2013-10-25', 3700.00),
(13, 23, 12, '2016-04-12', 4400.00),
(14, 24, 11, '2010-08-21', 4800.00),
(15, 27, 9, '2018-09-17', 3600.00),
(16, 28, 5, '2015-12-01', 4100.00),
(17, 29, 2, '2014-03-10', 4500.00),
(18, 30, 3, '2007-07-22', 4900.00),
(19, 31, 4, '2021-02-11', 4700.00),
(20, 32, 3, '2011-05-07', 5200.00),
(21, 34, 2, '2015-11-23', 3800.00),
(22, 35, 5, '2016-06-15', 3400.00),
(23, 36, 8, '2017-09-18', 3600.00);




DELIMITER $$
CREATE TRIGGER before_insert_persoane
BEFORE INSERT ON Persoane
FOR EACH ROW
BEGIN
    DECLARE category_exists INT;
    SET category_exists = (SELECT COUNT(*) FROM Categorii WHERE ID_Categorie = NEW.ID_Categorie);
    
    IF category_exists = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Categoria specificată nu există.';
    END IF;
END;
$$
DELIMITER ;


DELIMITER $$

CREATE PROCEDURE CountEmployeesPerInstitution()
BEGIN
    SELECT 
        I.Nume_Institutie AS Nume_Institutie,
        I.Adresa AS Adresa_Institutie,
        COUNT(A.ID_Angajat) AS Numar_Angajati
    FROM 
        Institutii I
    LEFT JOIN 
        Angajati A ON I.ID_Institutie = A.ID_Institutie
    GROUP BY 
        I.ID_Institutie;
END$$

DELIMITER ;

    SELECT 
avg(Varsta) from Persoane;

	
