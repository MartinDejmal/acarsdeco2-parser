CREATE TABLE `messages` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `reg` varchar(8) CHARACTER SET utf8 DEFAULT NULL,
  `flight` varchar(6) CHARACTER SET utf8 DEFAULT NULL,
  `mode` char(1) CHARACTER SET utf8 DEFAULT NULL,
  `label` char(2) CHARACTER SET utf8 DEFAULT NULL,
  `blockid` char(1) CHARACTER SET utf8 DEFAULT NULL,
  `ack` char(1) CHARACTER SET utf8 DEFAULT NULL,
  `msgno` char(4) CHARACTER SET utf8 DEFAULT NULL,
  `message` varchar(1000) CHARACTER SET utf8 DEFAULT NULL,
  `msgfreq` decimal(6,3) DEFAULT NULL,
  `timestamp` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `reg` (`reg`,`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_czech_ci;
