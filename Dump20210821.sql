-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: localhost    Database: registro_matricula
-- ------------------------------------------------------
-- Server version	8.0.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `registro_reportes`
--

DROP TABLE IF EXISTS `registro_reportes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `registro_reportes` (
  `id_reportes` int NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(45) DEFAULT NULL,
  `tipo` varchar(45) DEFAULT NULL,
  `matricula_vehiculo` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_reportes`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registro_reportes`
--

LOCK TABLES `registro_reportes` WRITE;
/*!40000 ALTER TABLE `registro_reportes` DISABLE KEYS */;
INSERT INTO `registro_reportes` VALUES (1,'Exceso de velocidad','1','PGI2 EEN'),(11,'Vehiculo reporte','2','CVL 657 18');
/*!40000 ALTER TABLE `registro_reportes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registro_vehiculos`
--

DROP TABLE IF EXISTS `registro_vehiculos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `registro_vehiculos` (
  `id_matricula` int NOT NULL AUTO_INCREMENT,
  `num_matricula` varchar(45) NOT NULL,
  `propietario` varchar(45) NOT NULL,
  `marca` varchar(45) NOT NULL,
  `modelo` varchar(45) NOT NULL,
  PRIMARY KEY (`id_matricula`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registro_vehiculos`
--

LOCK TABLES `registro_vehiculos` WRITE;
/*!40000 ALTER TABLE `registro_vehiculos` DISABLE KEYS */;
INSERT INTO `registro_vehiculos` VALUES (1,'PGI2 EEN','Kris','Pontiac','a'),(11,'CVL 657 18','KRIS','Chevrolet','Camaro');
/*!40000 ALTER TABLE `registro_vehiculos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tasa_peaje`
--

DROP TABLE IF EXISTS `tasa_peaje`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tasa_peaje` (
  `id_peaje` int NOT NULL AUTO_INCREMENT,
  `matricula_vehiculo` varchar(45) DEFAULT NULL,
  `monto` int DEFAULT NULL,
  `fecha` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_peaje`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tasa_peaje`
--

LOCK TABLES `tasa_peaje` WRITE;
/*!40000 ALTER TABLE `tasa_peaje` DISABLE KEYS */;
INSERT INTO `tasa_peaje` VALUES (1,'CVL 657 18',200,'21/08/2021');
/*!40000 ALTER TABLE `tasa_peaje` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_reportes`
--

DROP TABLE IF EXISTS `tipo_reportes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipo_reportes` (
  `id_tipo` int NOT NULL,
  `tipo` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_tipo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_reportes`
--

LOCK TABLES `tipo_reportes` WRITE;
/*!40000 ALTER TABLE `tipo_reportes` DISABLE KEYS */;
INSERT INTO `tipo_reportes` VALUES (1,'Infraccion'),(2,'Robo'),(3,'Defectos de fabrica'),(4,'Kilometraje'),(5,'Riesgo vial');
/*!40000 ALTER TABLE `tipo_reportes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-08-21 18:07:43
