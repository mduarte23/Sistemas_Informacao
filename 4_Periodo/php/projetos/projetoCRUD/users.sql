/*
 Navicat Premium Data Transfer

 Source Server         : 00-MysqlDocker
 Source Server Type    : MySQL
 Source Server Version : 101003
 Source Host           : 127.0.0.1:3306
 Source Schema         : comercial

 Target Server Type    : MySQL
 Target Server Version : 101003
 File Encoding         : 65001

 Date: 05/12/2024 15:05:45
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users`  (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `firstName` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `lastName` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `created_at` timestamp(0) NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp(0) NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `email`(`email`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 156 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES (1, 'Gabriel', 'Vale', 'gabriela.ortiz@hotmail.com', '$2y$10$QLqFwAyfVT02yzDScUGNfeO3Uaf7.Kclm6Ec1SMyni/M8VaSiO6h.', '2024-11-25 19:35:31', '2024-11-25 19:35:31');
INSERT INTO `users` VALUES (2, 'Olívia', 'Pontes', 'jgarcia@jimenes.br', '$2y$10$gyrfKgkQ.bNRCU81Nmkk1O.8w/MpL2zICkejbjVGZ89vTfrm1UbCS', '2024-11-25 19:35:31', '2024-11-25 19:35:31');
INSERT INTO `users` VALUES (3, 'Tainara', 'Galindo', 'hugo38@escobar.com.br', '$2y$10$/6xhGCo46NAhhAq1/OqOreXVTVJKgXbc/5297SbH6mVmwk/gSmq2O', '2024-11-25 19:35:31', '2024-11-25 19:35:31');
INSERT INTO `users` VALUES (4, 'Jácomo', 'Burgos', 'alves.alma@bezerra.net.br', '$2y$10$JLjvT0V.p7E3Gp9zxZ2K8uflOUTRrOCPBXGjfoT7xCGi9iCjAmyYK', '2024-11-25 19:35:31', '2024-11-25 19:35:31');
INSERT INTO `users` VALUES (5, 'Irene', 'Camacho', 'dayana.garcia@marinho.com.br', '$2y$10$a3fyPoO5XdRfcCFGJbWim.soIt8bfmHlGQGJ.pOnSb4dgzgf6c1na', '2024-11-25 19:35:31', '2024-11-25 19:35:31');
INSERT INTO `users` VALUES (6, 'Gabrielly', 'Bezerra', 'lovato.cecilia@bonilha.com', '$2y$10$tC9vXiuldnTTWwXKbaE3fu1H0t4BBVu.oU/Q3cK2kVJXzCWA25LQu', '2024-11-25 19:35:31', '2024-11-25 19:35:31');
INSERT INTO `users` VALUES (7, 'Carolina', 'Mendonça', 'fontes.vanessa@saito.com', '$2y$10$rOfH5Lmt.ueRmbHdK7.COuLCc05Gvd6zTNcImXXvNxPw/KvRA9FtG', '2024-11-25 19:35:31', '2024-11-25 19:35:31');
INSERT INTO `users` VALUES (8, 'Helena', 'Jimenes', 'lsoares@yahoo.com', '$2y$10$HqcnwdyAdnMYf1T7Otetyedbaq9mfuO/cgaRdqFxDchQBDhEbD/Ke', '2024-11-25 19:35:31', '2024-11-25 19:35:31');
INSERT INTO `users` VALUES (9, 'Miguel', 'Perez', 'lucio.cruz@queiros.net', '$2y$10$jTmSVX3hRbFUpd9WDU6O0.1U.nLN0IMQE.3Ixwd9qmyOmSkprPlOK', '2024-11-25 19:35:31', '2024-11-25 19:35:31');
INSERT INTO `users` VALUES (10, 'Enzo', 'Domingues', 'ferraz.graziela@benez.com.br', '$2y$10$1NYRnRPhU0A65w4HjZGK7.QR4UXVRr9zDl3NK7pBTXbK45C6ylCcW', '2024-11-25 19:35:31', '2024-11-25 19:35:31');
INSERT INTO `users` VALUES (11, 'Joyce', 'Perez', 'salgado.mariana@ortega.net', '$2y$10$6gVI/JIA9OCwH6YIBifl1OeBPEQHY.0iSn3ngGOg98Sl/0TNJd.Du', '2024-11-25 19:35:31', '2024-11-25 19:35:31');
INSERT INTO `users` VALUES (12, 'Diogo', 'Gusmão', 'breno.prado@roque.com.br', '$2y$10$zfdFdnddL4UCD7L0DzsiuujvEjWj/xZ2R7bTi3C1DWyY0WBgfmBXS', '2024-11-25 19:35:31', '2024-11-25 19:35:31');
INSERT INTO `users` VALUES (13, 'Laiane', 'Barreto', 'alexandre.furtado@yahoo.com', '$2y$10$fQa4OJP.f3L2QXsvE7c6gu5w.Ys4Ufsjt4TP/.o3UPkE1oXTLAAHa', '2024-11-25 19:35:32', '2024-11-25 19:35:32');
INSERT INTO `users` VALUES (14, 'Esther', 'Perez', 'kevin.rosa@uol.com.br', '$2y$10$AEl7Ft9ZaYz.J776KEDA8e8HZ9Ujm3Nj3LNI6I8Hxnj3Qw5GGRSf6', '2024-11-25 19:35:32', '2024-11-25 19:35:32');
INSERT INTO `users` VALUES (15, 'Heitor', 'Assunção', 'yuri.matias@ig.com.br', '$2y$10$H7zg4AyqD/n0mlFJEnizaeXRYzdOFIVBNBVRCaEWJmBqk4Jti9PMm', '2024-11-25 19:35:32', '2024-11-25 19:35:32');
INSERT INTO `users` VALUES (16, 'Melinda', 'Uchoa', 'samuel73@yahoo.com', '$2y$10$zB4cbtKRsRiXKHJmmixAxO1NFeYl3/1es36rYcJiQS/fbzl.7FiW.', '2024-11-25 19:35:32', '2024-11-25 19:35:32');
INSERT INTO `users` VALUES (17, 'Allan', 'Leal', 'diogo.vega@furtado.com', '$2y$10$skOXnfrB9V0YeKUlLQBfhOvpVU56HSsAI/PI9Hvly6G4k5fy4ZfBO', '2024-11-25 19:35:32', '2024-11-25 19:35:32');
INSERT INTO `users` VALUES (18, 'Emanuelly', 'Sepúlveda', 'debora.meireles@grego.br', '$2y$10$NW9LZOreo2cmjVsU1gXIeeHCjRIOkiI/9rr4B.UftyqXItsYZM/T2', '2024-11-25 19:35:32', '2024-11-25 19:35:32');
INSERT INTO `users` VALUES (19, 'Ivan', 'Lozano', 'lucas.ferreira@uol.com.br', '$2y$10$nxMvoGj1q4ptftZniYSxeOk3USQzdRUolgaRWR5rDYEnbfw/vh4cy', '2024-11-25 19:35:32', '2024-11-25 19:35:32');
INSERT INTO `users` VALUES (20, 'Eduardo', 'Faria', 'fmarinho@uol.com.br', '$2y$10$Ufp5nYgta4sh7LajmGYwO..zft3.YUg/6JCdTGf6t5vYN0oJhrEOa', '2024-11-25 19:35:32', '2024-11-25 19:35:32');
INSERT INTO `users` VALUES (21, 'Suzana', 'Martines', 'tais.fernandes@dasneves.com', '$2y$10$A9tZjVDnfeY/AUr4ay6ph.rHpwjQNmPjdyA8FtwGs4NqlRAxZmrzW', '2024-11-25 19:35:32', '2024-11-25 19:35:32');
INSERT INTO `users` VALUES (22, 'Teobaldo', 'Pereira', 'soares.esther@hotmail.com', '$2y$10$ghmlbU7gpjBdd/GaLiSxU.hLZTs9QMUYOmUO372bS3k9rO6AaNZLi', '2024-11-25 19:35:32', '2024-11-25 19:35:32');
INSERT INTO `users` VALUES (23, 'Martinho', 'Lutero', 'quintana.elis@yahoo.com', '$2y$10$JhsRwiLpJhElNK2Cv99gPOUg9KCgE05Y6FX0Ym636dLR5ug.30s9W', '2024-11-25 19:35:32', '2024-11-25 19:35:32');
INSERT INTO `users` VALUES (24, 'Miranda', 'Ferminiano', 'davi33@hotmail.com', '$2y$10$pZLBLXT4mu/2orO9p.scGOycf4b/xpgULVcMHmBQS.b.PJxeBAsue', '2024-11-25 19:35:32', '2024-11-25 19:35:32');
INSERT INTO `users` VALUES (25, 'Gabrielly', 'Campos', 'deaguiar.miriam@ig.com.br', '$2y$10$HYQH6BNCtlhRq6ld7eXdsufjckshrV.L0ahh1vPTBz49oYGfGLuo2', '2024-11-25 19:35:32', '2024-11-25 19:35:32');
INSERT INTO `users` VALUES (26, 'Micaela', 'Duarte', 'uzamana@mendonca.org', '$2y$10$Yc7hMZvcT6yi1NkGgdLhNOtHhPceUPYxu..X/oMcM7yLfF34mUpv.', '2024-11-25 19:35:32', '2024-11-25 19:35:32');
INSERT INTO `users` VALUES (27, 'Elisa', 'Grego', 'daniele10@hotmail.com', '$2y$10$8W6X9jAqJr8IOcnwM7sgBuVsK1oScgHPE7qwdnybda6lx/E2DHMYK', '2024-11-25 19:35:32', '2024-11-25 19:35:32');
INSERT INTO `users` VALUES (28, 'Adriele', 'Medina', 'josefina20@ig.com.br', '$2y$10$sKN2x3iC29fOIFbDvtLxN.KXV8HwqUXwhV4QjGVnF3IxM/.3i0khq', '2024-11-25 19:35:32', '2024-11-25 19:35:32');
INSERT INTO `users` VALUES (29, 'Julieta', 'Leal', 'cordeiro.daniel@ferminiano.com', '$2y$10$QodjLij7Vh4Jlq9N1YcYEO1lh.jhSDfF/XITTYQLVEjwCyqxn5ljO', '2024-11-25 19:35:32', '2024-11-25 19:35:32');
INSERT INTO `users` VALUES (30, 'Felipe', 'Bittencourt', 'valdez.isabella@chaves.net', '$2y$10$RruaVL5xM1i2Cd.jmzlYAOcrKXkoTmKo1TLi5y0FY5hVmgxSNY6Xa', '2024-11-25 19:35:32', '2024-11-25 19:35:32');
INSERT INTO `users` VALUES (31, 'Nero', 'Alcantara', 'ktoledo@uol.com.br', '$2y$10$iHOFIj.t/OJ/DYeC1ZE0lenKt3rEnCWvM9ZH7zjuL1uoiBORVk19G', '2024-11-25 19:35:32', '2024-11-25 19:35:32');
INSERT INTO `users` VALUES (32, 'Kléber', 'Neves', 'wesley43@cervantes.com', '$2y$10$7wTSNgS0V2w4BPxKGA/zvO1Ok7i7fF7tJZBmZddISJJEe1rX8YRYS', '2024-11-25 19:35:32', '2024-11-25 19:35:32');
INSERT INTO `users` VALUES (33, 'Helena', 'Escobar', 'grocha@gmail.com', '$2y$10$nXrokiU7oHezCsVrR7MKN.sY9hZQQUR1lb4dZBD4JiI4JD3XaURKq', '2024-11-25 19:35:33', '2024-11-25 19:35:33');
INSERT INTO `users` VALUES (34, 'Théo', 'Batista', 'cesar42@hotmail.com', '$2y$10$EIazGWzNk6m.MSigy4WbduW074MyNa.XV.6RXsvk6jC1CjufkbLnK', '2024-11-25 19:35:33', '2024-11-25 19:35:33');
INSERT INTO `users` VALUES (35, 'Flor', 'Pontes', 'hosana70@marin.com', '$2y$10$pMKlD5Pqr20/GY7kldBnouXPyVXWJExP0bCKQvF154apA5CUuQ58.', '2024-11-25 19:35:33', '2024-11-25 19:35:33');
INSERT INTO `users` VALUES (36, 'Wesley', 'Delatorre', 'freis@hotmail.com', '$2y$10$jXhJnmvnky0qDf74CKlfOeWybLV.4Uttum1rGF6H3xRtBXTsAbKwi', '2024-11-25 19:35:33', '2024-11-25 19:35:33');
INSERT INTO `users` VALUES (37, 'Sandro', 'Rivera', 'qabreu@gmail.com', '$2y$10$qSiqlH/EkVoaWHZhaHFz5O/1jtcV/W7K7SjKVeMhUmQiqAOcbEUiq', '2024-11-25 19:35:33', '2024-11-25 19:35:33');
INSERT INTO `users` VALUES (38, 'Daniella', 'Neves', 'thiago.queiros@barreto.com.br', '$2y$10$yrCd2mY0njzPcgZy5BMQyewa6/MsCw2fd7MVedpa0OhCcl6qObOR2', '2024-11-25 19:35:33', '2024-11-25 19:35:33');
INSERT INTO `users` VALUES (39, 'Yuri', 'Zamana', 'gustavo61@faria.com', '$2y$10$C.TOJIM2B3UsJEezzxLzp.Hg2k9z4OthLNJ5o53ON6hkXLShlnmpO', '2024-11-25 19:35:33', '2024-11-25 19:35:33');
INSERT INTO `users` VALUES (40, 'Marina', 'Matias', 'fidalgo.evandro@neves.com', '$2y$10$h1459cNjV5Ayq06RWvKt8uejWaU5/eELvnq6Bu6wkrb6lVqgpNlJO', '2024-11-25 19:35:33', '2024-11-25 19:35:33');
INSERT INTO `users` VALUES (41, 'Lucio', 'Verdugo', 'furtado.wellington@r7.com', '$2y$10$MqGXx6K.GCpv.Vm5C/T4SuWsLqNXqNZhqcYGtymXFX2wVRUQ8WFFe', '2024-11-25 19:35:33', '2024-11-25 19:35:33');
INSERT INTO `users` VALUES (42, 'Ariane', 'Ferreira', 'faria.moises@domingues.br', '$2y$10$sDYYh1NZ.qdXEc/PtW9wm.XzsiNWejfnqAYKLfnep10smwkLPaAmm', '2024-11-25 19:35:33', '2024-11-25 19:35:33');
INSERT INTO `users` VALUES (43, 'Isabel', 'Velasques', 'wrivera@hotmail.com', '$2y$10$Xa9X8WGQBx29/fHuAIzjMucg.dieWyYyo7X2GXV73WACJGehqpcOC', '2024-11-25 19:35:33', '2024-11-25 19:35:33');
INSERT INTO `users` VALUES (44, 'Jasmin', 'Batista', 'alessandro14@santacruz.br', '$2y$10$3ezWkGlcLfoOrB0J1evm8.7cDPHCYG0aSoEX6EWoC2aw2HUzf.Vs.', '2024-11-25 19:35:33', '2024-11-25 19:35:33');
INSERT INTO `users` VALUES (45, 'Bella', 'Vega', 'soares.alonso@vega.com', '$2y$10$XLIz/SmLxMrJYXfG/tevx.yExe9ETbhrjgklj7CyL8W.KtBRrKbU2', '2024-11-25 19:35:33', '2024-11-25 19:35:33');
INSERT INTO `users` VALUES (46, 'Natan', 'Lira', 'juan.dias@saito.org', '$2y$10$Jm6P0.42HoOmupaw5auhHOiR.H1tEwOsQ..O914tJI8SCs0iMYtp.', '2024-11-25 19:35:33', '2024-11-25 19:35:33');
INSERT INTO `users` VALUES (47, 'Liz', 'Ramires', 'zambrano.rodrigo@terra.com.br', '$2y$10$/BLroTItR3IMIS7vnEHSouhu8aGakEAoYVg/dMkR0KrVOschh86NC', '2024-11-25 19:35:33', '2024-11-25 19:35:33');
INSERT INTO `users` VALUES (48, 'Ketlin', 'Casanova', 'gustavo.bezerra@gmail.com', '$2y$10$CiAEGUNQ8odOGB3v5jhBG.rLEuKmjDx9zRVhVammblfWingBzthIK', '2024-11-25 19:35:33', '2024-11-25 19:35:33');
INSERT INTO `users` VALUES (49, 'Kamila', 'Aranda', 'italo.saraiva@hotmail.com', '$2y$10$4gkz8ghvIu2sqCCz1jgV1uS.74mfkgCMMn8lbauvK33pcgakA8v6S', '2024-11-25 19:35:33', '2024-11-25 19:35:33');
INSERT INTO `users` VALUES (50, 'Renato', 'Galhardo', 'michelle.arruda@r7.com', '$2y$10$7OVIalRG.qet5nbxXpduseZUPm0ou7te1lL4/TekQ1mJbWpu5wxsK', '2024-11-25 19:35:33', '2024-11-25 19:35:33');
INSERT INTO `users` VALUES (51, 'Cláudio', 'Cervantes', 'natan96@perez.com', '$2y$10$CWiH8x3LMosm4s3Zqq.dOeNQqrScSBCfDJbc2Exoj2UCzWe8sehaG', '2024-11-25 19:35:33', '2024-11-25 19:35:33');
INSERT INTO `users` VALUES (52, 'Elis', 'Feliciano', 'nicolas90@abreu.org', '$2y$10$jfwC5LW1lu826E2U3yQZveI./biMsgBqt.dKnYI5XZyNHZ2Az3xuK', '2024-11-25 19:35:34', '2024-11-25 19:35:34');
INSERT INTO `users` VALUES (53, 'Gian', 'Pereira', 'gabrielly.deoliveira@colaco.com.br', '$2y$10$gAZiLddGlnP6pnhRI1m0e.x0Gtto9pqCinc1hF.mv/QMChIB2NrQi', '2024-11-25 19:35:34', '2024-11-25 19:35:34');
INSERT INTO `users` VALUES (54, 'Yuri', 'Santana', 'cdominato@gmail.com', '$2y$10$Fa6NNeX/5VVTXOW2lc7b.ehtPfeSCNcjwkqgLb1PEPTMFFdq2CUp2', '2024-11-25 19:35:34', '2024-11-25 19:35:34');
INSERT INTO `users` VALUES (55, 'Mari', 'Valente', 'analu.cordeiro@zamana.net', '$2y$10$qdwe.8Amft4X.rdK3V2PlOFpq.g.JHYYmk1y3HJccSyXG13CLlSiy', '2024-11-25 19:35:40', '2024-11-25 19:35:40');
INSERT INTO `users` VALUES (56, 'Isis', 'Salazar', 'talita.fernandes@yahoo.com', '$2y$10$DDWxnu11YaRNZU1WR9GHt.fGRGhaOiDgdbjXEqNfgSn9A9QO.GuJe', '2024-11-25 19:35:40', '2024-11-25 19:35:40');
INSERT INTO `users` VALUES (57, 'Raissa', 'Corona', 'amelia85@ig.com.br', '$2y$10$9n.Uum2/aj.3jDdMtDxXz.4jmOgIB0QGfRi8B7VdYoNOcPsj5PXzi', '2024-11-25 19:35:40', '2024-11-25 19:35:40');
INSERT INTO `users` VALUES (58, 'Théo', 'Burgos', 'quintana.joyce@barros.org', '$2y$10$3b6PEpti9WNp4GfLq0DZYuHiQLSuOVnJRax9Et.0/0xItLq.4xKc2', '2024-11-25 19:35:40', '2024-11-25 19:35:40');
INSERT INTO `users` VALUES (59, 'Jéssica', 'Molina', 'dayana.camacho@gmail.com', '$2y$10$cCB/G6PRZ3fIXLt8k8d.Ju7QbuvYDglhuWnTHCrl0etEeW5XjVUF.', '2024-11-25 19:35:40', '2024-11-25 19:35:40');
INSERT INTO `users` VALUES (60, 'Alma', 'Neves', 'robson.lira@yahoo.com', '$2y$10$JaJMHkq7E46ziccMNfRi3OvfJkZ7CuI9M4U4CO2nbF0H60XErXt4m', '2024-11-25 19:35:40', '2024-11-25 19:35:40');
INSERT INTO `users` VALUES (61, 'Téo', 'Madeira', 'natalia.valdez@guerra.com', '$2y$10$I5HfUCV4FNCgV.SOvLdTQu3koSjqZO6SDscxmvZmqdPxtbC2XzloW', '2024-11-25 19:35:40', '2024-11-25 19:35:40');
INSERT INTO `users` VALUES (62, 'Ohana', 'Carmona', 'aragao.mariah@zaragoca.com', '$2y$10$BYWcMRr47UNsZ6qc32H1BeYLBaHtfV7amKmFi7OT4Yd/zsdx9bCWe', '2024-11-25 19:35:40', '2024-11-25 19:35:40');
INSERT INTO `users` VALUES (63, 'Natal', 'de Oliveira', 'meireles.tais@r7.com', '$2y$10$l6jXTonMtYZYbPTCFP/RSOr47al07ZZXovHBTSQiavlPqww.OuC2W', '2024-11-25 19:35:40', '2024-11-25 19:35:40');
INSERT INTO `users` VALUES (64, 'Leonardo', 'Salas', 'vicente.ferraz@furtado.org', '$2y$10$yorW3iOGYvshUgsWNHLFOOCn79hSsyQMfbU2BsDgz9pEHokfAoX72', '2024-11-25 19:35:40', '2024-11-25 19:35:40');
INSERT INTO `users` VALUES (65, 'Teobaldo', 'Chaves', 'danielle.delatorre@gomes.net', '$2y$10$qQtnHC9KUKdETy3ozFprE.ryIQU.K31y3VPCEsLSr0m0dZF3fXe9C', '2024-11-25 19:35:40', '2024-11-25 19:35:40');
INSERT INTO `users` VALUES (66, 'Emanuel', 'Oliveira', 'juliana33@fernandes.org', '$2y$10$ONeCmzbw/Txg6ldI5QveCOjpg/vItzi4uqFZ9TOmGFTaq5lp9Z9su', '2024-11-25 19:35:40', '2024-11-25 19:35:40');
INSERT INTO `users` VALUES (67, 'Leandro', 'Bonilha', 'mary.marinho@ramires.net', '$2y$10$dhJRBRk.7B6p7j8qzAykE.FbPKTbc.vGvQNkwABOeH9qbhnPuzeJm', '2024-11-25 19:35:40', '2024-11-25 19:35:40');
INSERT INTO `users` VALUES (68, 'Rafael', 'Assunção', 'emeireles@perez.br', '$2y$10$qSJnT.4eRBHs/a5GJ.aG1uOhY.BQQZbqYJcXDxEeSq5qy91yGVTqu', '2024-11-25 19:35:40', '2024-11-25 19:35:40');
INSERT INTO `users` VALUES (69, 'Gabrielle', 'Santos', 'mendes.livia@darosa.net.br', '$2y$10$HhDLhsT4IuiwOG8Pzmxu/ev3mX/nRgDsj5upHpOKtuYpvj8/wIV3W', '2024-11-25 19:35:40', '2024-11-25 19:35:40');
INSERT INTO `users` VALUES (70, 'Ziraldo', 'Oliveira', 'bia.lutero@faro.org', '$2y$10$0WGSIvDUYxes.a698dfuye1VMXoIQ6HIPv3TZoySVoBWEINllnNcC', '2024-11-25 19:35:40', '2024-11-25 19:35:40');
INSERT INTO `users` VALUES (71, 'Théo', 'Cordeiro', 'augusto.dacruz@sales.net', '$2y$10$9Nl1Cvlgq5OcEvK.IXOVPuGwoseLMOgYFiW//AbPtofaVtoghG79m', '2024-11-25 19:35:40', '2024-11-25 19:35:40');
INSERT INTO `users` VALUES (72, 'Noemi', 'Mendes', 'salgado.maite@hotmail.com', '$2y$10$yU4dH9ghTHqTqWD/h0RzAO7hkP9wp1frjzbyUh91OZvw4HHXWOn8u', '2024-11-25 19:35:40', '2024-11-25 19:35:40');
INSERT INTO `users` VALUES (73, 'Kamila', 'Camacho', 'ufonseca@terra.com.br', '$2y$10$qL96rma5AAurIftHynGTd.kwOLJ0vWOYv5LDygGLWCKJyNJiQ0XUO', '2024-11-25 19:35:40', '2024-11-25 19:35:40');
INSERT INTO `users` VALUES (74, 'Paola', 'Queirós', 'erik.pena@ferreira.com', '$2y$10$STRxg.jj.OFYMOu.OCv2VukHOxJWMgA7uL8hJ227GBFGu/U5NOjUC', '2024-11-25 19:35:41', '2024-11-25 19:35:41');
INSERT INTO `users` VALUES (75, 'Pablo', 'Meireles', 'lucio52@yahoo.com', '$2y$10$lvplpKpdpFKpb6/XjrlWYOEwqaHcWOKaOXCK9wFds89EwsY807Ku6', '2024-11-25 19:35:41', '2024-11-25 19:35:41');
INSERT INTO `users` VALUES (76, 'Constância', 'Marés', 'xzambrano@fonseca.com.br', '$2y$10$9OdvR0h.KwmN2TJwwBzB/O4IaqQZQMPZD0KhoFSCoexdGvEJuJGRC', '2024-11-25 19:35:41', '2024-11-25 19:35:41');
INSERT INTO `users` VALUES (77, 'Sophie', 'Torres', 'cervantes.christian@verdara.com', '$2y$10$.lScnzrFdSQlD2yF2PXapOkdhvR6E7iSqutV4bdkN.8wvEpLadjri', '2024-11-25 19:35:41', '2024-11-25 19:35:41');
INSERT INTO `users` VALUES (78, 'Isabel', 'Leal', 'cristiana.rios@benez.com.br', '$2y$10$bUY3ZUPkRw8YoKIWH/tToelcOyNE9Z7teExeMJB95INJNFZrmYUMC', '2024-11-25 19:35:41', '2024-11-25 19:35:41');
INSERT INTO `users` VALUES (79, 'Teobaldo', 'Saito', 'ovalencia@ferreira.com', '$2y$10$lxNp0Y.lQ.WMzUTicjJdge.rIejgY2GFEAbh/7RBIFJuJDtWLbL5q', '2024-11-25 19:35:41', '2024-11-25 19:35:41');
INSERT INTO `users` VALUES (80, 'Dirce', 'Marques', 'gabi12@jimenes.net', '$2y$10$4nKSAsXXLED1hLmrvn2U2euhnrinihTKT8.uu5iMutkvcgWU.ZfY6', '2024-11-25 19:35:41', '2024-11-25 19:35:41');
INSERT INTO `users` VALUES (81, 'Milene', 'da Rosa', 'dcasanova@gmail.com', '$2y$10$j3MSHbjs0zQXmxzOqiB/pex4gzeVd2zO2jVoaVJx9Cn/FOC2GCNqW', '2024-11-25 19:35:41', '2024-11-25 19:35:41');
INSERT INTO `users` VALUES (82, 'Noemi', 'Padrão', 'guerra.tiago@arruda.com', '$2y$10$mn671UytfblGJ8JYBQOKnOxWNMfiVtZLRVvsjJqlRMG10oxdRJg4u', '2024-11-25 19:35:41', '2024-11-25 19:35:41');
INSERT INTO `users` VALUES (83, 'Malu', 'Faro', 'efontes@lira.com.br', '$2y$10$0xeCChJ8FUUfkbq/abosmu3tWo9LgtNnidHWzTkLjpeZxtjKwu.PW', '2024-11-25 19:35:41', '2024-11-25 19:35:41');
INSERT INTO `users` VALUES (84, 'Joaquin', 'Aranda', 'deverso.maisa@hotmail.com', '$2y$10$hn8vhQ5k/IDaLJSXRuCsCuR4A1TCY9xWu1XLQ58E8sdwmJ7vlI6du', '2024-11-25 19:35:41', '2024-11-25 19:35:41');
INSERT INTO `users` VALUES (85, 'Ziraldo', 'Sepúlveda', 'avalencia@gmail.com', '$2y$10$01xDRNw6h42/4sFfYXC4aeWiJQrRcSSXUewmjxywqpelpzPK9XeK6', '2024-11-25 19:35:41', '2024-11-25 19:35:41');
INSERT INTO `users` VALUES (86, 'Wagner', 'Valente', 'pamela59@fidalgo.com.br', '$2y$10$Mqq4m41NsoKGBZNXBVsYgeGlWemVmq/j3isAjhQVBOdKJwu1MRPaW', '2024-11-25 19:35:41', '2024-11-25 19:35:41');
INSERT INTO `users` VALUES (87, 'Cíntia', 'Romero', 'nvalentin@terra.com.br', '$2y$10$k36Vm44CegOF2H.CIYily.hj.ferNxFH.9HgvpAX8h4mOTIeHgQ/2', '2024-11-25 19:35:41', '2024-11-25 19:35:41');
INSERT INTO `users` VALUES (88, 'Wilson', 'Vale', 'marcos50@yahoo.com', '$2y$10$mU2Vosn35uPSESS97TF15eC9E9bDy1naj5CW1q6uUYftHOP/3ua4O', '2024-11-25 19:35:41', '2024-11-25 19:35:41');
INSERT INTO `users` VALUES (89, 'Cauan', 'Jimenes', 'jeronimo.mares@rosa.net', '$2y$10$jpcuybbr818lhtfXfmQVheTtCV4Xl3T6Shd18nZ2ChA5M1AqjcUbS', '2024-11-25 19:35:41', '2024-11-25 19:35:41');
INSERT INTO `users` VALUES (90, 'Bernardo', 'Faria', 'tessalia.barreto@dearruda.org', '$2y$10$QWi1jb0A09SHHRGdWWTYSe7tvtoYNr3/Gtvvy0XFRCGyKLJGsbogS', '2024-11-25 19:35:41', '2024-11-25 19:35:41');
INSERT INTO `users` VALUES (91, 'Michele', 'Carmona', 'garcia.leonardo@galindo.net', '$2y$10$erl6Wau29CgsUcAKvrSebOHmxhC4IuYs89Gfmlp74XMw0nyMXHCBK', '2024-11-25 19:35:41', '2024-11-25 19:35:41');
INSERT INTO `users` VALUES (92, 'Wagner', 'Faria', 'rocha.claudia@galindo.com', '$2y$10$C6VS1iwAuOYFoNsPwxwxRO2H3yX53cI7bwKXxA8rP/aJefUFDAIc.', '2024-11-25 19:35:41', '2024-11-25 19:35:41');
INSERT INTO `users` VALUES (93, 'Wellington', 'Aguiar', 'santiago.filipe@hotmail.com', '$2y$10$d6uLX927qa2sZTDlqF5Na.GIY4qll6AciobbBF9yd2VXaqZxzhIb6', '2024-11-25 19:35:41', '2024-11-25 19:35:41');
INSERT INTO `users` VALUES (94, 'Maiara', 'Rivera', 'olga.pacheco@colaco.com', '$2y$10$1rbUrV42EKRceTeNDrovBuxqQFDXghUQL8XR66L8ZSvbXg5hhdEHa', '2024-11-25 19:35:42', '2024-11-25 19:35:42');
INSERT INTO `users` VALUES (95, 'Aparecida', 'Flores', 'umontenegro@caldeira.com.br', '$2y$10$MAbXm/LSZ/dBar6M/HnodOEukRbDDCmhm6tn0R1aK42zhfzz5PSSG', '2024-11-25 19:35:42', '2024-11-25 19:35:42');
INSERT INTO `users` VALUES (96, 'Nayara', 'da Cruz', 'padilha.melina@gmail.com', '$2y$10$7jDJ7e9Vshli7H7Q6rcpKuvLIf9vxCgBjZIp/5VWKzWU0r569sY0q', '2024-11-25 19:35:42', '2024-11-25 19:35:42');
INSERT INTO `users` VALUES (97, 'Thalissa', 'Ortega', 'alessandro.ferminiano@sepulveda.net', '$2y$10$NebRMu4mdIFwasfyCv6ba.lBpHps12/6M7WfERD8OR0IP1ECKCiEW', '2024-11-25 19:35:42', '2024-11-25 19:35:42');
INSERT INTO `users` VALUES (98, 'Alexandre', 'Leal', 'perola.desouza@yahoo.com', '$2y$10$1HART67auFPtCVx6JahTk.FE.VKa2iIjE25P3z7fDB6ZltxJTzPDW', '2024-11-25 19:35:42', '2024-11-25 19:35:42');
INSERT INTO `users` VALUES (99, 'Laiane', 'Pontes', 'maldonado.antonio@r7.com', '$2y$10$7lCXvSqYLODYDUfEEaFxHeiSK7PsvRZZyHJ/sgSj.tG.kMm58WRq2', '2024-11-25 19:35:42', '2024-11-25 19:35:42');
INSERT INTO `users` VALUES (100, 'Alexandre', 'Franco', 'mari34@yahoo.com', '$2y$10$AwfCHQSikUk4tmIFQjjmgO5cvaVoHgNGY1idgOYAIv8Vva4kcbn0G', '2024-11-25 19:35:42', '2024-11-25 19:35:42');
INSERT INTO `users` VALUES (101, 'Luan', 'Marin', 'goncalves.mateus@gmail.com', '$2y$10$OJIVWUU.yVl0VC3bDkL9QOyWyQDxvGKHpSmNJLiMQCxIbFaqT3gZS', '2024-11-25 19:35:42', '2024-11-25 19:35:42');
INSERT INTO `users` VALUES (102, 'Vanessa', 'Zaragoça', 'fidalgo.esther@r7.com', '$2y$10$H9lyG.CIWKfqVL6p8flDD.Db9hvt8jG0DePqsjjvl2cVVfva6xQzW', '2024-11-25 19:35:42', '2024-11-25 19:35:42');
INSERT INTO `users` VALUES (103, 'Cristina', 'Tamoio', 'alma23@ferreira.net', '$2y$10$YnuAl06fCGbE.PF4ep.nAOD8IiUXW3lsN.0lMH9PFmN4prLV2HBqe', '2024-11-25 19:35:42', '2024-11-25 19:35:42');
INSERT INTO `users` VALUES (104, 'Eva', 'Gil', 'luisa.esteves@montenegro.com.br', '$2y$10$CLhgqPUaM9ltVr5a85VeXe8r/gt2i26lLAbdfKTKKznY/4MopNjca', '2024-11-25 19:35:42', '2024-11-25 19:35:42');
INSERT INTO `users` VALUES (105, 'Clarice', 'Delatorre', 'cortes.clarice@terra.com.br', '$2y$10$Glodk6xIG20G2.WA0xTOCe7zdoLCrA35ZSf73xwacWjNsNIdSP3i.', '2024-11-25 19:35:42', '2024-11-25 19:35:42');
INSERT INTO `users` VALUES (106, 'João', 'Barros', 'carvalho.marisa@ig.com.br', '$2y$10$px0lwAXviXiZq5LE8YPKBucSUJfyAnRbLQqW2b55L5eAM.r9mmJ9G', '2024-11-25 19:35:42', '2024-11-25 19:35:42');
INSERT INTO `users` VALUES (107, 'Antonieta', 'Verdugo', 'vasques.lorena@dasilva.com.br', '$2y$10$n.GcOB/P0nj/GSAiI/Wnkelj17JJtJ1LtFNdVQl.//N8ZYhVWjjeC', '2024-11-25 19:35:42', '2024-11-25 19:35:42');
INSERT INTO `users` VALUES (108, 'Flávia', 'Molina', 'jasmin.bittencourt@gmail.com', '$2y$10$nDoXXuv/ODV81fZxcpYufelEmLj8r7h1IgrdCwngO8A6UJkzspUEO', '2024-11-25 19:35:42', '2024-11-25 19:35:42');
INSERT INTO `users` VALUES (109, 'Moisés', 'Valente', 'ricardo.domingues@davila.org', '$2y$10$c6dnkESYkJgl/x0Vej5fu.0W9rwPaV0/hi5N0UppVfa/g/jnrjqO2', '2024-11-25 19:35:42', '2024-11-25 19:35:42');
INSERT INTO `users` VALUES (110, 'Alonso', 'Quintana', 'murilo.branco@carvalho.com.br', '$2y$10$pYT64qrh.qk5DXloaNCg0.wHIwL57pa2t4ydS4is5WnikADhnqMEe', '2024-11-25 19:35:42', '2024-11-25 19:35:42');
INSERT INTO `users` VALUES (111, 'Laiane', 'Cervantes', 'adriano.aranda@gmail.com', '$2y$10$PkHw/hPA9UAuPbWoSwckg.ZxvJ4dQydBd2ZWOCJV0S71bpwQe1Rhe', '2024-11-25 19:35:42', '2024-11-25 19:35:42');
INSERT INTO `users` VALUES (112, 'Gabriel', 'das Neves', 'maximiano.ferreira@r7.com', '$2y$10$kWxm29r5ANQwXIHbl9QkmOnyGC5WCscDaZ0Jn89/QQc54t/3Yoj6G', '2024-11-25 19:35:42', '2024-11-25 19:35:42');
INSERT INTO `users` VALUES (113, 'Lavínia', 'de Freitas', 'fabricio09@brito.net.br', '$2y$10$x4FXq.eZeZKP50TVrk65s.dpfU/aqqEdYbx4gtIdJXifkXlHdmM2i', '2024-11-25 19:35:42', '2024-11-25 19:35:42');
INSERT INTO `users` VALUES (114, 'George', 'Godói', 'bonilha.camila@hotmail.com', '$2y$10$VJYto/eLNtSc6ZKSuFetTeINOn33rP.X/7iQjZ79VizFTnaj9H/L.', '2024-11-25 19:35:43', '2024-11-25 19:35:43');
INSERT INTO `users` VALUES (115, 'Walter', 'Garcia', 'lmaldonado@alcantara.com', '$2y$10$btOUoiHR3h6OfoxRs2CuXe16UknlWAVmyU6SaFhVT7XCK0tBvWSLu', '2024-11-25 19:35:43', '2024-11-25 19:35:43');
INSERT INTO `users` VALUES (116, 'Júlio', 'Rocha', 'qalcantara@mendes.com', '$2y$10$X/MZd1LJoDztnXcLDDXAfeT4cfB6oyjb21T6hlZVca69lVdzInD5G', '2024-11-25 19:35:43', '2024-11-25 19:35:43');
INSERT INTO `users` VALUES (117, 'Leo', 'Salgado', 'erivera@vieira.com.br', '$2y$10$w3GFn7hZAcd9fQYGRVL9M..x3nMuUPMlVfMDGNLRjqO9RL6hRUQdC', '2024-11-25 19:35:43', '2024-11-25 19:35:43');
INSERT INTO `users` VALUES (118, 'Karina', 'Sepúlveda', 'andreia.cortes@dasneves.com', '$2y$10$LljauCMLsWv5CAbsS5AdBOm6KecWMKypTmSfe7HRINELd7aWlQtNG', '2024-11-25 19:35:43', '2024-11-25 19:35:43');
INSERT INTO `users` VALUES (119, 'Tâmara', 'Pontes', 'bezerra.daniele@salazar.org', '$2y$10$7g8aQZ9TDk2VW2a4qo7tZeoKOgUL8heXEeTNQ1XNV4MLiUv/.J1Ja', '2024-11-25 19:35:43', '2024-11-25 19:35:43');
INSERT INTO `users` VALUES (120, 'Ayla', 'Marinho', 'batista.luciano@batista.br', '$2y$10$7zjQyDVPmnfK6WuQjD0NiefyyTlJylcoygk1WUrDRiT7J8pr88P8G', '2024-11-25 19:35:43', '2024-11-25 19:35:43');
INSERT INTO `users` VALUES (121, 'Thalia', 'Fonseca', 'yohanna.leal@yahoo.com', '$2y$10$2dWHYPhB4Dk4a4eonkUnK.dle2BEOdFKKRb192cEpBeDtZA7PoJTG', '2024-11-25 19:35:43', '2024-11-25 19:35:43');
INSERT INTO `users` VALUES (122, 'Rafael', 'Roque', 'fabio86@abreu.com.br', '$2y$10$i1TQIriPXHXnKb1BNKFElOAbNW78tQ/msIoqkYGo3qRVVsgSYTw8e', '2024-11-25 19:35:43', '2024-11-25 19:35:43');
INSERT INTO `users` VALUES (123, 'Enzo', 'Torres', 'rafael44@uol.com.br', '$2y$10$yAmghYiq9O2QGokaA.33NO/j7.Dc7lueV9MaF/S8RVbCHIXLevufW', '2024-11-25 19:35:43', '2024-11-25 19:35:43');
INSERT INTO `users` VALUES (124, 'Maximiano', 'Roque', 'cpaz@ig.com.br', '$2y$10$fklD9qjwUA/kNVNCNqbfWODKWE9j6WFtvUKnpB3TKSKlTYqzqTvW2', '2024-11-25 19:35:43', '2024-11-25 19:35:43');
INSERT INTO `users` VALUES (125, 'Tábata', 'Serra', 'ruth43@gmail.com', '$2y$10$OOrPDXZ5QF.Idb9rLxWa6e6aK7ILa/R.cmpUFqt7TZU28GS3PyIUy', '2024-11-25 19:35:43', '2024-11-25 19:35:43');
INSERT INTO `users` VALUES (126, 'Pietra', 'Aragão', 'emilio85@terra.com.br', '$2y$10$bQYvRo9OHmvJjwLEhoqkDuJJnWyRdp1flpTEpxLqbr2Tv0t0pmh/e', '2024-11-25 19:35:43', '2024-11-25 19:35:43');
INSERT INTO `users` VALUES (127, 'Rogério', 'Serra', 'daniela87@bittencourt.org', '$2y$10$oIwYskq9EOd8zcQsWlWD.OMZOv.du7CtV5fDqYzywH4As9IT4g7Pe', '2024-11-25 19:35:43', '2024-11-25 19:35:43');
INSERT INTO `users` VALUES (128, 'Henrique', 'Montenegro', 'velasques.heitor@hotmail.com', '$2y$10$hT5diOMVWWRKy3d.6sSVwuh8W1ZjqfAUPGFGz44VaBQ6AH.ZvC8Fm', '2024-11-25 19:35:43', '2024-11-25 19:35:43');
INSERT INTO `users` VALUES (129, 'Victor', 'Chaves', 'ycamacho@ig.com.br', '$2y$10$z8GDu4MLQiIM6M1BiP9Qo./cS6fPB3ts9LJXiVRv4Noc3FEPCMa0m', '2024-11-25 19:35:43', '2024-11-25 19:35:43');
INSERT INTO `users` VALUES (130, 'Thomas', 'Correia', 'olga59@terra.com.br', '$2y$10$RtQ9Y9mw7DYueYiQwVb.z.VF/Lbmh7jvEr5FYHFOpEDPgIAyzDZgS', '2024-11-25 19:35:43', '2024-11-25 19:35:43');
INSERT INTO `users` VALUES (131, 'Inácio', 'Salas', 'lsalas@fontes.com', '$2y$10$4kfaCLuqogPXtlpdy0XyTuUEXaP9CEfV6w/0bE2AYetfRkQn.Bfw2', '2024-11-25 19:35:43', '2024-11-25 19:35:43');
INSERT INTO `users` VALUES (132, 'Benedito', 'Leal', 'deivid.pena@ig.com.br', '$2y$10$pAe0LcMMuha.vArlDQ94wuwaMJ07QvMFa5R19yT7Aa9S6cs.9WL7.', '2024-11-25 19:35:43', '2024-11-25 19:35:43');
INSERT INTO `users` VALUES (133, 'Tiago', 'Dominato', 'sramos@soto.com.br', '$2y$10$2..yFqyFdhSMiHOdbQPEneFM.qQhGpcD48M9piPdhP5gC1t3.EHXG', '2024-11-25 19:35:43', '2024-11-25 19:35:43');
INSERT INTO `users` VALUES (134, 'Francisco', 'Burgos', 'malena.pereira@ferreira.net', '$2y$10$7OyXBrZdgK7Om3gC.eBZCOz8lkYz10a48QBVFaRe8egCL2RhVTpW6', '2024-11-25 19:35:44', '2024-11-25 19:35:44');
INSERT INTO `users` VALUES (135, 'Guilherme', 'Alcantara', 'tmarinho@dominato.com', '$2y$10$gbAhB7AYBSehHLpGgaddae1ai0Ib0Hp7X0L3ke7N.Nqk77FQXLwYy', '2024-11-25 19:35:44', '2024-11-25 19:35:44');
INSERT INTO `users` VALUES (136, 'Karine', 'Camacho', 'ramires.gean@padrao.com', '$2y$10$VTCnUChwFiRQVtRFvwGSk.3EkKGcB0h5TXzlUA./FpsnN9JJ4NFOq', '2024-11-25 19:35:44', '2024-11-25 19:35:44');
INSERT INTO `users` VALUES (137, 'Simon', 'Vasques', 'ingrid.delgado@ig.com.br', '$2y$10$pCydh6ACbTfzQU5SRFDiiepZrXYa9e6vGDlQULHFTk2dCi1sKcs6y', '2024-11-25 19:35:44', '2024-11-25 19:35:44');
INSERT INTO `users` VALUES (138, 'Ítalo', 'Fernandes', 'matos.pamela@franco.com.br', '$2y$10$okprMY.lxd7kd79AMbx1DOXGGTbvGhLjnuVS/WTsxX2kf7fPiJTCa', '2024-11-25 19:35:44', '2024-11-25 19:35:44');
INSERT INTO `users` VALUES (139, 'Edilson', 'Vale', 'priscila20@gmail.com', '$2y$10$BtvD.Cv7XJCtqGn1iWWC4.43k7miVBEobwWoFEXnNtJAgADsqe.rC', '2024-11-25 19:35:44', '2024-11-25 19:35:44');
INSERT INTO `users` VALUES (140, 'Danilo', 'Faro', 'sepulveda.claudia@ortega.com', '$2y$10$dPvvMwrSzNieO.5wgyhRu.gAvo5AeIBXOQrbJK0NCjJA6Vawv6tIC', '2024-11-25 19:35:44', '2024-11-25 19:35:44');
INSERT INTO `users` VALUES (141, 'Leandro', 'Deverso', 'evandro.burgos@furtado.com.br', '$2y$10$khDPjw8L87g7up6BJnaVLOcKj5hMui8fjtmzu5e8hhl4pw3ikG4.u', '2024-11-25 19:35:44', '2024-11-25 19:35:44');
INSERT INTO `users` VALUES (142, 'Elaine', 'Maldonado', 'cervantes.louise@espinoza.net', '$2y$10$Y63diPxHztp1GdmZoJKplOAiqD1rCrl2REcFMv1DiPrbwZaw4OOb.', '2024-11-25 19:35:44', '2024-11-25 19:35:44');
INSERT INTO `users` VALUES (143, 'Luara', 'Furtado', 'brios@ferraz.br', '$2y$10$X6soNKgLWHl7My8hsNc.pOGENJuBrJ7PgqvEAZVBrNgtKE1.bjPQ.', '2024-11-25 19:35:44', '2024-11-25 19:35:44');
INSERT INTO `users` VALUES (144, 'Luara', 'Grego', 'raphael.paes@gmail.com', '$2y$10$vHxEAV813JPWV3pl1XmPWes/0AhnAjFPI1qP2s0hUZsEwOYkZTfTy', '2024-11-25 19:35:44', '2024-11-25 19:35:44');
INSERT INTO `users` VALUES (145, 'Gustavo', 'Perez', 'heloisa.aguiar@hotmail.com', '$2y$10$WyunDf3Mczi4eCvSkJrPIeiZq9YWzqkPTA6WDLt1Gevo56Voxsxpi', '2024-11-25 19:35:44', '2024-11-25 19:35:44');
INSERT INTO `users` VALUES (146, 'Edson', 'Sales', 'aline.aragao@terra.com.br', '$2y$10$9ZpwCeti58E8x.eFgQyh2OqskH6Zpo/lxT1K5SlZPISequ/WXOCBa', '2024-11-25 19:35:44', '2024-11-25 19:35:44');
INSERT INTO `users` VALUES (147, 'Laiane', 'Urias', 'stefany97@terra.com.br', '$2y$10$iUooCTltLcw3F5Pn5ma0leF7dSSEd5bWeaHnDVjr0X6S99d51NCF6', '2024-11-25 19:35:44', '2024-11-25 19:35:44');
INSERT INTO `users` VALUES (148, 'Sandra', 'Lira', 'vieira.pietra@r7.com', '$2y$10$18zD8Nhvlqs3RKc8LNJRLeI8MCiJQeymsZmca2NDHZXu0B/CVKR1G', '2024-11-25 19:35:44', '2024-11-25 19:35:44');
INSERT INTO `users` VALUES (149, 'Moisés', 'Ramos', 'furtado.allison@r7.com', '$2y$10$SZBh16mA9dkcLymD9LYx/usgVWLBemdkANgAmjWuDW068qxA86XLC', '2024-11-25 19:35:44', '2024-11-25 19:35:44');
INSERT INTO `users` VALUES (150, 'Noelí', 'Gonçalves', 'dasneves.sophie@terra.com.br', '$2y$10$ZvJDnBSuar4I2OgwgM8DRO2rOi/fiyDkzc4953L0eiYoJuxBDjAvK', '2024-11-25 19:35:44', '2024-11-25 19:35:44');
INSERT INTO `users` VALUES (151, 'Ayla', 'Zambrano', 'henrique13@pedrosa.com.br', '$2y$10$YRz4wsxBLspf1p6df.IQd.CWV3mvU/W5WR33NlFrGb9INNCWPHRvq', '2024-11-25 19:35:44', '2024-11-25 19:35:44');
INSERT INTO `users` VALUES (152, 'Allan', 'Jimenes', 'michael.delatorre@uol.com.br', '$2y$10$AsRs0oVHtA/o.tto.xJbUufD536IMoxslJaSrrvRlf4EUpZplsiB.', '2024-11-25 19:35:44', '2024-11-25 19:35:44');

SET FOREIGN_KEY_CHECKS = 1;
