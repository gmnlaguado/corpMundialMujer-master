-- Attachment querys from legacy database

INSERT INTO countries  SELECT * FROM datos.paises

INSERT INTO departments SELECT * FROM datos.departamentos

INSERT INTO cities SELECT * FROM datos.ciudades

INSERT INTO neighborhoods SELECT * FROM datos.barrios

INSERT INTO ciiu SELECT * FROM datos.cIIU

INSERT INTO diagnosticQuestions SELECT * FROM datos.preguntasDiagnostico

SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'productionProfileDiag';


CREATE TABLE "payee" ( `project` VARCHAR(255) NOT NULL, `names` VARCHAR(255) NOT NULL, `lastNames` VARCHAR(255) NOT NULL, `docType` INT NOT NULL, `document` VARCHAR(255) NOT NULL PRIMARY KEY, `expeditionCity` INT NOT NULL, `birthdate` VARCHAR(255) NOT NULL, `city` INT NOT NULL, `department` INT NOT NULL, `country` INT NOT NULL, `sign` INT NOT NULL, `address` VARCHAR(255) NOT NULL, `neighborhood` INT NOT NULL, `indicative` INT NOT NULL, `telephone` INT NOT NULL, `cellphone` INT NOT NULL, `email` VARCHAR(255) NOT NULL, `operator` VARCHAR(255) NOT NULL, `cellphone2` INT NOT NULL, `payeeType` INT NOT NULL, `date` VARCHAR(255) NOT NULL, `ageRange` INT NOT NULL, `nationality` INT NOT NULL, `environment` INT NOT NULL, `tier` INT NOT NULL, `sex` INT NOT NULL, `gender` INT NOT NULL, `ethnicGroup` INT NOT NULL, `disability` INT NOT NULL)

INSERT INTO payee VALUES ('oficial24','jose luis','Aguero Ruiz',1,'654321',5004,'1969-12-01',52207,52,169,23,'78',5220710,2,1103145,1102145253,'joseluis@cmm.com','carlos23',1102533632,1,'2020-05-06',5,169,1,7,2,2,5,6)

buildozer android debug deploy run logcat

EXEC sp_rename 'production_profile_diag', 'productionProfileDiag';

