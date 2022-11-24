/*!40101 SET NAMES utf8 */;
/*!40014 SET FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET SQL_NOTES=0 */;
DROP TABLE IF EXISTS video;
CREATE TABLE `video` (
  `id` varchar(50) NOT NULL,
  `name` varchar(25) NOT NULL,
  `type` varchar(10) NOT NULL,
  `grade` float NOT NULL,
  `pub_year` varchar(20) DEFAULT NULL,
  `link` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
INSERT INTO video(id,name,type,grade,pub_year,link) VALUES('1','Avatar','Adventure',9,'2013','imdb.com'),('2','COCO','Animation',9,'2019','imdb.com'),('3','The Godfather','Crime',9.1,'1976','imdb.com');