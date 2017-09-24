-- phpMyAdmin SQL Dump
-- version 4.7.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 20, 2017 at 12:33 PM
-- Server version: 10.1.25-MariaDB
-- PHP Version: 7.1.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rfsa`
--

-- --------------------------------------------------------

--
-- Table structure for table `files`
--

CREATE TABLE `files` (
  `id` int(11) NOT NULL,
  `file_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `files`
--

INSERT INTO `files` (`id`, `file_name`) VALUES
(1, '2015 Rooms Segmentation.xlsx'),
(2, '2016 ROOMS SEGMENTATION.xlsx');

-- --------------------------------------------------------

--
-- Table structure for table `forecast_uses_actual`
--

CREATE TABLE `forecast_uses_actual` (
  `ACTUAL_ID` varchar(20) NOT NULL,
  `FORECAST_ID` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `group_segment_master`
--

CREATE TABLE `group_segment_master` (
  `GRP_SEG_ID` varchar(25) NOT NULL,
  `GRP_SEG_NAME` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `group_segment_master`
--

INSERT INTO `group_segment_master` (`GRP_SEG_ID`, `GRP_SEG_NAME`) VALUES
('CON/ASSOC', 'CONVENTION/ASSOCIATION'),
('CORPM', 'CORPORATE MEETINGS'),
('GOV/NGO', 'GOVERNMENT/NGO'),
('GRPO', 'GROUP OTHERS'),
('GRPT', 'GROUP TOURS');

-- --------------------------------------------------------

--
-- Table structure for table `individual_segment_master`
--

CREATE TABLE `individual_segment_master` (
  `IND_SEG_ID` varchar(25) NOT NULL,
  `IND_SEG_NAME` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `individual_segment_master`
--

INSERT INTO `individual_segment_master` (`IND_SEG_ID`, `IND_SEG_NAME`) VALUES
('CORP', 'CORPORATE'),
('CORPO', 'CORPORATE OTHERS'),
('INDO', 'INDIVIDUAL OTHERS'),
('INDR', 'INDUSTRY RATE'),
('PKG/PRM', 'PACKAGES/PROMO'),
('QD', 'QUALIFIED DISCOUNT'),
('RCK', 'RACK'),
('WSOF', 'WHOLESALE OFFLINE'),
('WSOL', 'WHOLESALE ONLINE');

-- --------------------------------------------------------

--
-- Table structure for table `room_actual`
--

CREATE TABLE `room_actual` (
  `ACTUAL_ID` varchar(20) NOT NULL,
  `SEG_ID` varchar(25) NOT NULL,
  `DATE` date DEFAULT NULL,
  `BUDGET_RNS` double DEFAULT NULL,
  `BUDGET_ARR` double DEFAULT NULL,
  `BUDGET_REVENUE` double DEFAULT NULL,
  `ACTUAL_RNS` double DEFAULT NULL,
  `ACTUAL_ARR` double DEFAULT NULL,
  `ACTUAL_REVENUE` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `room_actual`
--

INSERT INTO `room_actual` (`ACTUAL_ID`, `SEG_ID`, `DATE`, `BUDGET_RNS`, `BUDGET_ARR`, `BUDGET_REVENUE`, `ACTUAL_RNS`, `ACTUAL_ARR`, `ACTUAL_REVENUE`) VALUES
('APR15', 'CON/ASSOC', '2015-04-30', 670, 3299, 2210, 446, 3664, 1634),
('APR15', 'CORP', '2015-04-30', 605, 3910, 2366, 152, 3932, 598),
('APR15', 'CORPM', '2015-04-30', 960, 3400, 3264, 1025, 4202, 4307),
('APR15', 'CORPO', '2015-04-30', 0, 0, 0, 265, 4197, 1112),
('APR15', 'GOV/NGO', '2015-04-30', 290, 3196, 927, 125, 4330, 541),
('APR15', 'GRPO', '2015-04-30', 12, 3070, 37, 88, 5210, 458),
('APR15', 'GRPT', '2015-04-30', 90, 3052, 275, 0, 0, 0),
('APR15', 'INDO', '2015-04-30', 95, 4623, 439, 11, 5176, 57),
('APR15', 'INDR', '2015-04-30', 11, 2185, 24, 7, 2037, 14),
('APR15', 'PKG/PRM', '2015-04-30', 700, 3510, 2457, 269, 4358, 1172),
('APR15', 'RCK', '2015-04-30', 1000, 5608, 5608, 1074, 5964, 6405),
('APR15', 'WSOF', '2015-04-30', 85, 4000, 340, 88, 3161, 278),
('APR15', 'WSOL', '2015-04-30', 650, 4000, 2600, 630, 4528, 2852),
('APR16', 'CON/ASSOC', '2016-04-30', 600, 3800, 2280, 2153, 4379, 9427),
('APR16', 'CORP', '2016-04-30', 200, 4100, 820, 258, 3586, 925),
('APR16', 'CORPM', '2016-04-30', 1250, 4300, 5375, 524, 3874, 2030),
('APR16', 'CORPO', '2016-04-30', 350, 4200, 1470, 120, 4165, 500),
('APR16', 'GOV/NGO', '2016-04-30', 275, 4800, 1320, 162, 4083, 661),
('APR16', 'GRPO', '2016-04-30', 100, 5300, 530, 0, 0, 0),
('APR16', 'GRPT', '2016-04-30', 50, 3200, 160, 22, 2687, 59),
('APR16', 'INDO', '2016-04-30', 50, 5200, 260, 239, 5349, 1278),
('APR16', 'INDR', '2016-04-30', 3, 2500, 8, 0, 0, 0),
('APR16', 'PKG/PRM', '2016-04-30', 400, 4400, 1760, 323, 4996, 1614),
('APR16', 'RCK', '2016-04-30', 900, 6200, 5580, 734, 6209, 4557),
('APR16', 'WSOF', '2016-04-30', 80, 3900, 312, 36, 4321, 156),
('APR16', 'WSOL', '2016-04-30', 700, 4400, 3080, 302, 4758, 1437),
('AUG15', 'CON/ASSOC', '2015-08-31', 0, 0, 0, 39, 3111, 121),
('AUG15', 'CORP', '2015-08-31', 330, 3757, 1240, 103, 4147, 427),
('AUG15', 'CORPM', '2015-08-31', 800, 3200, 2560, 1037, 3837, 3979),
('AUG15', 'CORPO', '2015-08-31', 0, 0, 0, 188, 3657, 688),
('AUG15', 'GOV/NGO', '2015-08-31', 375, 2800, 1050, 455, 3535, 1609),
('AUG15', 'GRPO', '2015-08-31', 65, 3000, 195, 0, 0, 0),
('AUG15', 'GRPT', '2015-08-31', 250, 2484, 621, 138, 2890, 399),
('AUG15', 'INDO', '2015-08-31', 80, 3209, 257, 110, 3814, 420),
('AUG15', 'INDR', '2015-08-31', 5, 2640, 13, 0, 0, 0),
('AUG15', 'PKG/PRM', '2015-08-31', 1100, 3510, 3861, 690, 3652, 2520),
('AUG15', 'RCK', '2015-08-31', 500, 5500, 2750, 831, 5291, 4397),
('AUG15', 'WSOF', '2015-08-31', 150, 3300, 495, 75, 4315, 324),
('AUG15', 'WSOL', '2015-08-31', 600, 3731, 2239, 616, 3994, 2460),
('AUG16', 'CON/ASSOC', '2016-08-31', 100, 3700, 370, 127, 4323, 549),
('AUG16', 'CORP', '2016-08-31', 150, 4200, 630, 431, 3811, 1643),
('AUG16', 'CORPM', '2016-08-31', 1000, 4100, 4100, 761, 3656, 2782),
('AUG16', 'CORPO', '2016-08-31', 200, 3700, 740, 197, 3894, 767),
('AUG16', 'GOV/NGO', '2016-08-31', 400, 4000, 1600, 399, 3944, 1574),
('AUG16', 'GRPO', '2016-08-31', 50, 5000, 250, 0, 0, 0),
('AUG16', 'GRPT', '2016-08-31', 200, 3000, 600, 93, 2750, 256),
('AUG16', 'INDO', '2016-08-31', 30, 5000, 150, 56, 4647, 260),
('AUG16', 'INDR', '2016-08-31', 10, 2300, 23, 0, 0, 0),
('AUG16', 'PKG/PRM', '2016-08-31', 700, 3800, 2660, 283, 4514, 1277),
('AUG16', 'RCK', '2016-08-31', 800, 5500, 4400, 1003, 5470, 5487),
('AUG16', 'WSOF', '2016-08-31', 90, 4400, 396, 49, 3739, 183),
('AUG16', 'WSOL', '2016-08-31', 500, 4000, 2000, 427, 3891, 1662),
('DEC15', 'CON/ASSOC', '2015-12-31', 296, 3950, 1169, 290, 3975, 1153),
('DEC15', 'CORP', '2015-12-31', 498, 4236, 2109, 167, 3457, 577),
('DEC15', 'CORPM', '2015-12-31', 910, 3800, 3458, 953, 3915, 3731),
('DEC15', 'CORPO', '2015-12-31', 0, 0, 0, 173, 3723, 644),
('DEC15', 'GOV/NGO', '2015-12-31', 400, 3600, 1440, 492, 4068, 2001),
('DEC15', 'GRPO', '2015-12-31', 0, 0, 0, 72, 5460, 393),
('DEC15', 'GRPT', '2015-12-31', 250, 3312, 828, 184, 3066, 564),
('DEC15', 'INDO', '2015-12-31', 540, 3105, 1677, 321, 4405, 1414),
('DEC15', 'INDR', '2015-12-31', 8, 2640, 21, 0, 0, 0),
('DEC15', 'PKG/PRM', '2015-12-31', 1350, 5000, 6750, 1287, 6318, 8131),
('DEC15', 'RCK', '2015-12-31', 1250, 5800, 7250, 1402, 6436, 9023),
('DEC15', 'WSOF', '2015-12-31', 210, 3105, 652, 58, 3774, 219),
('DEC15', 'WSOL', '2015-12-31', 950, 4600, 4370, 715, 5246, 3751),
('DEC16', 'CON/ASSOC', '2016-12-31', 100, 4000, 400, 0, 0, 0),
('DEC16', 'CORP', '2016-12-31', 100, 4200, 420, 294, 3518, 1034),
('DEC16', 'CORPM', '2016-12-31', 850, 4000, 3400, 282, 4422, 1247),
('DEC16', 'CORPO', '2016-12-31', 200, 4000, 800, 111, 3523, 391),
('DEC16', 'GOV/NGO', '2016-12-31', 150, 3800, 570, 235, 3675, 864),
('DEC16', 'GRPO', '2016-12-31', 245, 4200, 1029, 38, 4185, 159),
('DEC16', 'GRPT', '2016-12-31', 115, 3400, 391, 67, 3752, 251),
('DEC16', 'INDO', '2016-12-31', 500, 5200, 2600, 304, 4855, 1476),
('DEC16', 'INDR', '2016-12-31', 10, 2800, 28, 0, 0, 0),
('DEC16', 'PKG/PRM', '2016-12-31', 1200, 5900, 7080, 479, 6089, 2917),
('DEC16', 'RCK', '2016-12-31', 1300, 6500, 8450, 2686, 6452, 17331),
('DEC16', 'WSOF', '2016-12-31', 100, 3700, 370, 165, 3210, 530),
('DEC16', 'WSOL', '2016-12-31', 950, 5000, 4750, 596, 4938, 2943),
('FEB15', 'CON/ASSOC', '2015-02-28', 300, 3820, 1146, 436, 3459, 1508),
('FEB15', 'CORP', '2015-02-28', 402, 4319, 1736, 107, 3722, 398),
('FEB15', 'CORPM', '2015-02-28', 1175, 3900, 4583, 1256, 3840, 4823),
('FEB15', 'CORPO', '2015-02-28', 0, 0, 0, 283, 3640, 1030),
('FEB15', 'GOV/NGO', '2015-02-28', 300, 3221, 966, 64, 5226, 334),
('FEB15', 'GRPO', '2015-02-28', 80, 3800, 304, 36, 3970, 143),
('FEB15', 'GRPT', '2015-02-28', 120, 3018, 362, 86, 2920, 251),
('FEB15', 'INDO', '2015-02-28', 165, 4621, 762, 150, 3476, 521),
('FEB15', 'INDR', '2015-02-28', 6, 2566, 15, 3, 2756, 8),
('FEB15', 'PKG/PRM', '2015-02-28', 800, 3705, 2964, 686, 3345, 2295),
('FEB15', 'RCK', '2015-02-28', 580, 5608, 3253, 578, 6215, 3592),
('FEB15', 'WSOF', '2015-02-28', 330, 3300, 1089, 176, 3176, 559),
('FEB15', 'WSOL', '2015-02-28', 480, 3795, 1822, 398, 4643, 1848),
('FEB16', 'CON/ASSOC', '2016-02-28', 450, 3600, 1620, 0, 0, 0),
('FEB16', 'CORP', '2016-02-28', 130, 4000, 520, 362, 3277, 1186),
('FEB16', 'CORPM', '2016-02-28', 1300, 4100, 5330, 1392, 4009, 5581),
('FEB16', 'CORPO', '2016-02-28', 320, 3700, 1184, 158, 3560, 562),
('FEB16', 'GOV/NGO', '2016-02-28', 100, 5500, 550, 136, 3877, 527),
('FEB16', 'GRPO', '2016-02-28', 60, 4200, 252, 58, 4843, 281),
('FEB16', 'GRPT', '2016-02-28', 200, 3100, 620, 71, 3866, 274),
('FEB16', 'INDO', '2016-02-28', 200, 4000, 800, 208, 4046, 842),
('FEB16', 'INDR', '2016-02-28', 5, 2800, 14, 0, 0, 0),
('FEB16', 'PKG/PRM', '2016-02-28', 700, 3600, 2520, 490, 4706, 2306),
('FEB16', 'RCK', '2016-02-28', 635, 6400, 4064, 1186, 5797, 6875),
('FEB16', 'WSOF', '2016-02-28', 250, 3300, 825, 135, 4058, 548),
('FEB16', 'WSOL', '2016-02-28', 500, 4600, 2300, 462, 4622, 2136),
('JAN15', 'CON/ASSOC', '2015-01-31', 550, 4500, 2475, 0, 0, 0),
('JAN15', 'CORP', '2015-01-31', 493, 4269, 2105, 166, 3809, 632),
('JAN15', 'CORPM', '2015-01-31', 1850, 3900, 7215, 1121, 3484, 3905),
('JAN15', 'CORPO', '2015-01-31', 0, 0, 0, 342, 3543, 1212),
('JAN15', 'GOV/NGO', '2015-01-31', 250, 3259, 815, 0, 0, 0),
('JAN15', 'GRPO', '2015-01-31', 115, 3836, 441, 42, 4751, 200),
('JAN15', 'GRPT', '2015-01-31', 80, 2884, 231, 188, 2949, 555),
('JAN15', 'INDO', '2015-01-31', 110, 4298, 473, 285, 3515, 1002),
('JAN15', 'INDR', '2015-01-31', 18, 2760, 50, 4, 2719, 11),
('JAN15', 'PKG/PRM', '2015-01-31', 450, 3500, 1575, 1098, 3109, 3413),
('JAN15', 'RCK', '2015-01-31', 1200, 5750, 6900, 1072, 6349, 6806),
('JAN15', 'WSOF', '2015-01-31', 335, 3000, 1005, 256, 3194, 818),
('JAN15', 'WSOL', '2015-01-31', 350, 4400, 1540, 513, 4943, 2536),
('JAN16', 'CON/ASSOC', '2016-01-31', 300, 4000, 1200, 24, 5253, 126),
('JAN16', 'CORP', '2016-01-31', 200, 4000, 800, 252, 3404, 858),
('JAN16', 'CORPM', '2016-01-31', 1200, 4000, 4800, 1082, 3503, 3791),
('JAN16', 'CORPO', '2016-01-31', 400, 3600, 1440, 179, 3708, 664),
('JAN16', 'GOV/NGO', '2016-01-31', 100, 4000, 400, 344, 4093, 1408),
('JAN16', 'GRPO', '2016-01-31', 60, 4900, 294, 60, 7158, 429),
('JAN16', 'GRPT', '2016-01-31', 200, 3100, 620, 215, 3369, 724),
('JAN16', 'INDO', '2016-01-31', 300, 4000, 1200, 142, 7398, 1050),
('JAN16', 'INDR', '2016-01-31', 5, 2900, 15, 0, 0, 0),
('JAN16', 'PKG/PRM', '2016-01-31', 600, 3600, 2160, 508, 4863, 2471),
('JAN16', 'RCK', '2016-01-31', 1100, 6400, 7040, 1482, 6095, 9033),
('JAN16', 'WSOF', '2016-01-31', 280, 3300, 924, 216, 3551, 767),
('JAN16', 'WSOL', '2016-01-31', 550, 5000, 2750, 553, 4670, 2582),
('JUL15', 'CON/ASSOC', '2015-07-31', 0, 0, 0, 511, 3269, 1670),
('JUL15', 'CORP', '2015-07-31', 410, 3785, 1552, 78, 4515, 352),
('JUL15', 'CORPM', '2015-07-31', 1100, 3100, 3410, 1007, 3450, 3474),
('JUL15', 'CORPO', '2015-07-31', 0, 0, 0, 228, 3721, 848),
('JUL15', 'GOV/NGO', '2015-07-31', 200, 3000, 600, 468, 4551, 2130),
('JUL15', 'GRPO', '2015-07-31', 0, 0, 0, 66, 6210, 410),
('JUL15', 'GRPT', '2015-07-31', 350, 3745, 1311, 0, 0, 0),
('JUL15', 'INDO', '2015-07-31', 80, 4500, 360, 11, 10556, 116),
('JUL15', 'INDR', '2015-07-31', 5, 2640, 13, 7, 2153, 15),
('JUL15', 'PKG/PRM', '2015-07-31', 1100, 3359, 3695, 837, 3465, 2900),
('JUL15', 'RCK', '2015-07-31', 200, 5631, 1126, 467, 5881, 2747),
('JUL15', 'WSOF', '2015-07-31', 50, 3200, 160, 69, 3262, 226),
('JUL15', 'WSOL', '2015-07-31', 500, 3661, 1831, 469, 3816, 1790),
('JUL16', 'CON/ASSOC', '2016-07-31', 150, 3700, 555, 25, 3092, 77),
('JUL16', 'CORP', '2016-07-31', 150, 4000, 600, 319, 3720, 1187),
('JUL16', 'CORPM', '2016-07-31', 1300, 4100, 5330, 1234, 3992, 4927),
('JUL16', 'CORPO', '2016-07-31', 300, 3600, 1080, 257, 3932, 1011),
('JUL16', 'GOV/NGO', '2016-07-31', 250, 4500, 1125, 127, 3205, 407),
('JUL16', 'GRPO', '2016-07-31', 50, 5300, 265, 0, 0, 0),
('JUL16', 'GRPT', '2016-07-31', 200, 3000, 600, 29, 3500, 101),
('JUL16', 'INDO', '2016-07-31', 50, 5100, 255, 106, 4653, 493),
('JUL16', 'INDR', '2016-07-31', 10, 2300, 23, 0, 0, 0),
('JUL16', 'PKG/PRM', '2016-07-31', 800, 3600, 2880, 322, 4415, 1422),
('JUL16', 'RCK', '2016-07-31', 600, 5900, 3540, 1100, 5333, 5866),
('JUL16', 'WSOF', '2016-07-31', 90, 3600, 324, 47, 4172, 196),
('JUL16', 'WSOL', '2016-07-31', 500, 4250, 2125, 477, 3973, 1895),
('JUN15', 'CON/ASSOC', '2015-06-30', 0, 0, 0, 0, 0, 0),
('JUN15', 'CORP', '2015-06-30', 285, 3941, 1123, 91, 3924, 357),
('JUN15', 'CORPM', '2015-06-30', 1050, 3100, 3255, 555, 3953, 2194),
('JUN15', 'CORPO', '2015-06-30', 0, 0, 0, 409, 2348, 960),
('JUN15', 'GOV/NGO', '2015-06-30', 80, 2680, 214, 142, 3760, 534),
('JUN15', 'GRPO', '2015-06-30', 35, 3900, 137, 118, 5227, 617),
('JUN15', 'GRPT', '2015-06-30', 150, 2555, 383, 0, 0, 0),
('JUN15', 'INDO', '2015-06-30', 190, 3335, 634, 113, 5700, 644),
('JUN15', 'INDR', '2015-06-30', 3, 2716, 8, 5, 3145, 16),
('JUN15', 'PKG/PRM', '2015-06-30', 1200, 3390, 4068, 634, 3847, 2439),
('JUN15', 'RCK', '2015-06-30', 440, 5530, 2433, 590, 5653, 3336),
('JUN15', 'WSOF', '2015-06-30', 106, 2785, 295, 56, 3582, 201),
('JUN15', 'WSOL', '2015-06-30', 455, 3791, 1725, 563, 4043, 2276),
('JUN16', 'CON/ASSOC', '2016-06-30', 100, 3800, 380, 16, 3500, 56),
('JUN16', 'CORP', '2016-06-30', 130, 4000, 520, 372, 3736, 1390),
('JUN16', 'CORPM', '2016-06-30', 1100, 4100, 4510, 711, 3873, 2754),
('JUN16', 'CORPO', '2016-06-30', 450, 3600, 1620, 365, 3930, 1434),
('JUN16', 'GOV/NGO', '2016-06-30', 120, 4500, 540, 321, 3585, 1151),
('JUN16', 'GRPO', '2016-06-30', 100, 5300, 530, 30, 4739, 142),
('JUN16', 'GRPT', '2016-06-30', 70, 3000, 210, 70, 2801, 196),
('JUN16', 'INDO', '2016-06-30', 130, 5700, 741, 268, 4801, 1287),
('JUN16', 'INDR', '2016-06-30', 5, 3200, 16, 0, 0, 0),
('JUN16', 'PKG/PRM', '2016-06-30', 800, 3600, 2880, 583, 4405, 2568),
('JUN16', 'RCK', '2016-06-30', 650, 5900, 3835, 791, 5416, 4284),
('JUN16', 'WSOF', '2016-06-30', 80, 3600, 288, 79, 4226, 334),
('JUN16', 'WSOL', '2016-06-30', 550, 4250, 2338, 400, 3998, 1599),
('MAR15', 'CON/ASSOC', '2015-03-31', 350, 3173, 1110, 127, 2988, 379),
('MAR15', 'CORP', '2015-03-31', 550, 3932, 2163, 141, 3533, 498),
('MAR15', 'CORPM', '2015-03-31', 1550, 3900, 6045, 1026, 3777, 3876),
('MAR15', 'CORPO', '2015-03-31', 0, 0, 0, 243, 3735, 908),
('MAR15', 'GOV/NGO', '2015-03-31', 100, 2778, 278, 827, 7059, 5838),
('MAR15', 'GRPO', '2015-03-31', 30, 2825, 85, 98, 3290, 322),
('MAR15', 'GRPT', '2015-03-31', 380, 3046, 1157, 52, 2989, 155),
('MAR15', 'INDO', '2015-03-31', 153, 4595, 703, 79, 6066, 479),
('MAR15', 'INDR', '2015-03-31', 2, 2037, 4, 0, 0, 0),
('MAR15', 'PKG/PRM', '2015-03-31', 870, 3762, 3273, 489, 3932, 1923),
('MAR15', 'RCK', '2015-03-31', 500, 5608, 2804, 447, 6002, 2683),
('MAR15', 'WSOF', '2015-03-31', 120, 3200, 384, 64, 3466, 222),
('MAR15', 'WSOL', '2015-03-31', 530, 3242, 1718, 435, 4388, 1909),
('MAR16', 'CON/ASSOC', '2016-03-31', 400, 3500, 1400, 65, 4277, 278),
('MAR16', 'CORP', '2016-03-31', 200, 4200, 840, 249, 3366, 838),
('MAR16', 'CORPM', '2016-03-31', 1100, 4000, 4400, 747, 3605, 2693),
('MAR16', 'CORPO', '2016-03-31', 300, 4250, 1275, 167, 3975, 664),
('MAR16', 'GOV/NGO', '2016-03-31', 250, 5000, 1250, 244, 3837, 936),
('MAR16', 'GRPO', '2016-03-31', 100, 4000, 400, 153, 4591, 702),
('MAR16', 'GRPT', '2016-03-31', 100, 3300, 330, 99, 3886, 385),
('MAR16', 'INDO', '2016-03-31', 100, 5000, 500, 135, 4653, 628),
('MAR16', 'INDR', '2016-03-31', 5, 2800, 14, 0, 0, 0),
('MAR16', 'PKG/PRM', '2016-03-31', 400, 4200, 1680, 570, 4632, 2640),
('MAR16', 'RCK', '2016-03-31', 1100, 6400, 7040, 1268, 5882, 7459),
('MAR16', 'WSOF', '2016-03-31', 100, 3500, 350, 121, 3154, 382),
('MAR16', 'WSOL', '2016-03-31', 800, 4600, 3680, 467, 4585, 2141),
('MAY15', 'CON/ASSOC', '2015-05-31', 700, 4800, 3360, 1117, 3316, 3704),
('MAY15', 'CORP', '2015-05-31', 443, 4258, 1887, 228, 3511, 801),
('MAY15', 'CORPM', '2015-05-31', 1100, 3600, 3960, 859, 4343, 3731),
('MAY15', 'CORPO', '2015-05-31', 0, 0, 0, 345, 4194, 1447),
('MAY15', 'GOV/NGO', '2015-05-31', 600, 3388, 2033, 124, 4641, 575),
('MAY15', 'GRPO', '2015-05-31', 118, 3750, 443, 136, 5262, 716),
('MAY15', 'GRPT', '2015-05-31', 330, 2483, 819, 0, 0, 0),
('MAY15', 'INDO', '2015-05-31', 150, 4725, 709, 122, 5682, 693),
('MAY15', 'INDR', '2015-05-31', 7, 2037, 14, 18, 2376, 43),
('MAY15', 'PKG/PRM', '2015-05-31', 900, 3460, 3114, 343, 4288, 1471),
('MAY15', 'RCK', '2015-05-31', 600, 6000, 3600, 955, 5620, 5367),
('MAY15', 'WSOF', '2015-05-31', 100, 3500, 350, 41, 3871, 159),
('MAY15', 'WSOL', '2015-05-31', 580, 4000, 2320, 564, 4068, 2295),
('MAY16', 'CON/ASSOC', '2016-05-31', 750, 3800, 2850, 27, 3534, 95),
('MAY16', 'CORP', '2016-05-31', 250, 4100, 1025, 501, 3704, 1856),
('MAY16', 'CORPM', '2016-05-31', 1150, 4300, 4945, 622, 4255, 2647),
('MAY16', 'CORPO', '2016-05-31', 380, 4200, 1596, 384, 4259, 1636),
('MAY16', 'GOV/NGO', '2016-05-31', 70, 4800, 336, 374, 3753, 1403),
('MAY16', 'GRPO', '2016-05-31', 190, 5300, 1007, 0, 0, 0),
('MAY16', 'GRPT', '2016-05-31', 100, 3200, 320, 10, 2685, 27),
('MAY16', 'INDO', '2016-05-31', 150, 5700, 855, 294, 5210, 1532),
('MAY16', 'INDR', '2016-05-31', 5, 2500, 13, 0, 0, 0),
('MAY16', 'PKG/PRM', '2016-05-31', 400, 4400, 1760, 629, 4754, 2990),
('MAY16', 'RCK', '2016-05-31', 1050, 6200, 6510, 798, 6249, 4987),
('MAY16', 'WSOF', '2016-05-31', 60, 3900, 234, 38, 4267, 162),
('MAY16', 'WSOL', '2016-05-31', 700, 4200, 2940, 333, 5076, 1690),
('NOV15', 'CON/ASSOC', '2015-11-30', 700, 3800, 2660, 949, 3779, 3587),
('NOV15', 'CORP', '2015-11-30', 680, 4273, 2905, 164, 3680, 604),
('NOV15', 'CORPM', '2015-11-30', 1850, 3800, 7030, 536, 4031, 2161),
('NOV15', 'CORPO', '2015-11-30', 0, 0, 0, 221, 3793, 838),
('NOV15', 'GOV/NGO', '2015-11-30', 600, 3600, 2160, 205, 3679, 754),
('NOV15', 'GRPO', '2015-11-30', 70, 3000, 210, 62, 5464, 339),
('NOV15', 'GRPT', '2015-11-30', 220, 3312, 729, 0, 0, 0),
('NOV15', 'INDO', '2015-11-30', 85, 3312, 282, 215, 4548, 978),
('NOV15', 'INDR', '2015-11-30', 8, 2640, 21, 0, 0, 0),
('NOV15', 'PKG/PRM', '2015-11-30', 1290, 3580, 4618, 458, 3713, 1701),
('NOV15', 'RCK', '2015-11-30', 700, 5800, 4060, 1088, 5747, 6253),
('NOV15', 'WSOF', '2015-11-30', 155, 4000, 620, 98, 3847, 377),
('NOV15', 'WSOL', '2015-11-30', 460, 4100, 1886, 375, 4140, 1553),
('NOV16', 'CON/ASSOC', '2016-11-30', 600, 4000, 2400, 421, 4000, 1684),
('NOV16', 'CORP', '2016-11-30', 100, 4300, 430, 279, 4161, 1161),
('NOV16', 'CORPM', '2016-11-30', 1150, 4300, 4945, 1127, 3904, 4400),
('NOV16', 'CORPO', '2016-11-30', 200, 3800, 760, 100, 4273, 427),
('NOV16', 'GOV/NGO', '2016-11-30', 750, 4000, 3000, 375, 3768, 1413),
('NOV16', 'GRPO', '2016-11-30', 100, 5000, 500, 19, 5287, 100),
('NOV16', 'GRPT', '2016-11-30', 200, 3300, 660, 186, 4636, 862),
('NOV16', 'INDO', '2016-11-30', 100, 5000, 500, 405, 4064, 1646),
('NOV16', 'INDR', '2016-11-30', 10, 2800, 28, 0, 0, 0),
('NOV16', 'PKG/PRM', '2016-11-30', 500, 3900, 1950, 112, 4510, 505),
('NOV16', 'RCK', '2016-11-30', 900, 5800, 5220, 1161, 5852, 6794),
('NOV16', 'WSOF', '2016-11-30', 100, 3700, 370, 74, 3600, 266),
('NOV16', 'WSOL', '2016-11-30', 750, 4200, 3150, 287, 4424, 1270),
('OCT15', 'CON/ASSOC', '2015-10-31', 720, 3800, 2736, 25, 3611, 90),
('OCT15', 'CORP', '2015-10-31', 530, 4141, 2194, 217, 3645, 791),
('OCT15', 'CORPM', '2015-10-31', 1200, 3800, 4560, 555, 4079, 2264),
('OCT15', 'CORPO', '2015-10-31', 0, 0, 0, 254, 3410, 866),
('OCT15', 'GOV/NGO', '2015-10-31', 500, 3600, 1800, 232, 3240, 752),
('OCT15', 'GRPO', '2015-10-31', 75, 3650, 274, 186, 4752, 884),
('OCT15', 'GRPT', '2015-10-31', 260, 3105, 807, 0, 0, 0),
('OCT15', 'INDO', '2015-10-31', 300, 3312, 994, 160, 5228, 836),
('OCT15', 'INDR', '2015-10-31', 8, 2640, 21, 0, 0, 0),
('OCT15', 'PKG/PRM', '2015-10-31', 1220, 3330, 4063, 631, 3669, 2315),
('OCT15', 'RCK', '2015-10-31', 425, 5608, 2383, 636, 5218, 3319),
('OCT15', 'WSOF', '2015-10-31', 105, 3550, 373, 90, 3529, 318),
('OCT15', 'WSOL', '2015-10-31', 410, 4084, 1674, 778, 3958, 3080),
('OCT16', 'CON/ASSOC', '2016-10-31', 400, 3900, 1560, 0, 0, 0),
('OCT16', 'CORP', '2016-10-31', 150, 4200, 630, 512, 3337, 1709),
('OCT16', 'CORPM', '2016-10-31', 1000, 4200, 4200, 650, 3949, 2567),
('OCT16', 'CORPO', '2016-10-31', 200, 3800, 760, 164, 3904, 640),
('OCT16', 'GOV/NGO', '2016-10-31', 400, 4000, 1600, 189, 3688, 697),
('OCT16', 'GRPO', '2016-10-31', 60, 5000, 300, 187, 3771, 705),
('OCT16', 'GRPT', '2016-10-31', 270, 3300, 891, 213, 3908, 832),
('OCT16', 'INDO', '2016-10-31', 70, 5000, 350, 239, 4372, 1045),
('OCT16', 'INDR', '2016-10-31', 10, 2800, 28, 0, 0, 0),
('OCT16', 'PKG/PRM', '2016-10-31', 700, 3800, 2660, 195, 4850, 946),
('OCT16', 'RCK', '2016-10-31', 700, 5600, 3920, 1440, 5703, 8212),
('OCT16', 'WSOF', '2016-10-31', 100, 3600, 360, 56, 4169, 233),
('OCT16', 'WSOL', '2016-10-31', 600, 4000, 2400, 329, 4905, 1614),
('SEPT15', 'CON/ASSOC', '2015-09-30', 100, 3800, 380, 602, 3133, 1886),
('SEPT15', 'CORP', '2015-09-30', 380, 3878, 1473, 167, 3892, 650),
('SEPT15', 'CORPM', '2015-09-30', 1400, 3400, 4760, 809, 3890, 3147),
('SEPT15', 'CORPO', '2015-09-30', 0, 0, 0, 151, 3714, 561),
('SEPT15', 'GOV/NGO', '2015-09-30', 360, 3312, 1192, 132, 3211, 424),
('SEPT15', 'GRPO', '2015-09-30', 100, 3000, 300, 53, 3708, 197),
('SEPT15', 'GRPT', '2015-09-30', 230, 3105, 714, 0, 0, 0),
('SEPT15', 'INDO', '2015-09-30', 150, 3395, 509, 83, 4514, 375),
('SEPT15', 'INDR', '2015-09-30', 5, 2640, 13, 0, 0, 0),
('SEPT15', 'PKG/PRM', '2015-09-30', 910, 3320, 3021, 540, 3770, 2036),
('SEPT15', 'RCK', '2015-09-30', 370, 5500, 2035, 467, 6174, 2883),
('SEPT15', 'WSOF', '2015-09-30', 100, 3650, 365, 45, 3329, 150),
('SEPT15', 'WSOL', '2015-09-30', 360, 3750, 1350, 500, 4025, 2012),
('SEPT16', 'CON/ASSOC', '2016-09-30', 400, 3900, 1560, 60, 3181, 191),
('SEPT16', 'CORP', '2016-09-30', 150, 4200, 630, 376, 3412, 1283),
('SEPT16', 'CORPM', '2016-09-30', 900, 4100, 3690, 873, 3740, 3265),
('SEPT16', 'CORPO', '2016-09-30', 200, 3700, 740, 141, 4008, 565),
('SEPT16', 'GOV/NGO', '2016-09-30', 300, 4000, 1200, 252, 3482, 877),
('SEPT16', 'GRPO', '2016-09-30', 60, 5000, 300, 80, 3239, 259),
('SEPT16', 'GRPT', '2016-09-30', 200, 3300, 660, 85, 4384, 373),
('SEPT16', 'INDO', '2016-09-30', 80, 5000, 400, 105, 4368, 459),
('SEPT16', 'INDR', '2016-09-30', 10, 2800, 28, 0, 0, 0),
('SEPT16', 'PKG/PRM', '2016-09-30', 500, 3800, 1900, 267, 4227, 1129),
('SEPT16', 'RCK', '2016-09-30', 600, 5500, 3300, 1223, 5169, 6321),
('SEPT16', 'WSOF', '2016-09-30', 50, 3600, 180, 62, 3719, 231),
('SEPT16', 'WSOL', '2016-09-30', 500, 4000, 2000, 336, 4013, 1348);

-- --------------------------------------------------------

--
-- Table structure for table `room_forecast`
--

CREATE TABLE `room_forecast` (
  `FORECAST_ID` varchar(20) NOT NULL,
  `SEG_ID` varchar(25) NOT NULL,
  `DATE` date NOT NULL,
  `FORECAST_RNS` double NOT NULL,
  `FORECAST_ARR` double NOT NULL,
  `FORECAST_REVENUE` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `segmentation_list`
--

CREATE TABLE `segmentation_list` (
  `SEG_ID` varchar(25) NOT NULL,
  `SEG_TYPE` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `segmentation_list`
--

INSERT INTO `segmentation_list` (`SEG_ID`, `SEG_TYPE`) VALUES
('CON/ASSOC', 'GRP'),
('CORP', 'IND'),
('CORPM', 'GRP'),
('CORPO', 'IND'),
('GOV/NGO', 'GRP'),
('GRPO', 'GRP'),
('GRPT', 'GRP'),
('INDO', 'IND'),
('INDR', 'IND'),
('PKG/PRM', 'IND'),
('QD', 'IND'),
('RCK', 'IND'),
('WSOF', 'IND'),
('WSOL', 'IND');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `files`
--
ALTER TABLE `files`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `forecast_uses_actual`
--
ALTER TABLE `forecast_uses_actual`
  ADD PRIMARY KEY (`ACTUAL_ID`,`FORECAST_ID`),
  ADD KEY `fk_ROOM_ACTUAL_has_ROOM_FORECAST_ROOM_FORECAST1_idx` (`FORECAST_ID`),
  ADD KEY `fk_ROOM_ACTUAL_has_ROOM_FORECAST_ROOM_ACTUAL1_idx` (`ACTUAL_ID`);

--
-- Indexes for table `group_segment_master`
--
ALTER TABLE `group_segment_master`
  ADD PRIMARY KEY (`GRP_SEG_ID`),
  ADD KEY `fk_GROUP_SEGMENT_MASTER_SEGMENTATION_LIST1_idx` (`GRP_SEG_ID`);

--
-- Indexes for table `individual_segment_master`
--
ALTER TABLE `individual_segment_master`
  ADD PRIMARY KEY (`IND_SEG_ID`),
  ADD KEY `fk_INDIVIDUAL_SEGMENT_MASTER_SEGMENTATION_LIST_idx` (`IND_SEG_ID`);

--
-- Indexes for table `room_actual`
--
ALTER TABLE `room_actual`
  ADD PRIMARY KEY (`ACTUAL_ID`,`SEG_ID`),
  ADD KEY `fk_ROOM_ACTUAL_SEGMENTATION_LIST1_idx` (`SEG_ID`);

--
-- Indexes for table `room_forecast`
--
ALTER TABLE `room_forecast`
  ADD PRIMARY KEY (`FORECAST_ID`,`SEG_ID`),
  ADD KEY `fk_ROOM_FORECAST_SEGMENTATION_LIST1_idx` (`SEG_ID`);

--
-- Indexes for table `segmentation_list`
--
ALTER TABLE `segmentation_list`
  ADD PRIMARY KEY (`SEG_ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `files`
--
ALTER TABLE `files`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `forecast_uses_actual`
--
ALTER TABLE `forecast_uses_actual`
  ADD CONSTRAINT `fk_ROOM_ACTUAL_has_ROOM_FORECAST_ROOM_ACTUAL1` FOREIGN KEY (`ACTUAL_ID`) REFERENCES `room_actual` (`ACTUAL_ID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_ROOM_ACTUAL_has_ROOM_FORECAST_ROOM_FORECAST1` FOREIGN KEY (`FORECAST_ID`) REFERENCES `room_forecast` (`FORECAST_ID`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `group_segment_master`
--
ALTER TABLE `group_segment_master`
  ADD CONSTRAINT `fk_GROUP_SEGMENT_MASTER_SEGMENTATION_LIST1` FOREIGN KEY (`GRP_SEG_ID`) REFERENCES `segmentation_list` (`SEG_ID`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `individual_segment_master`
--
ALTER TABLE `individual_segment_master`
  ADD CONSTRAINT `fk_INDIVIDUAL_SEGMENT_MASTER_SEGMENTATION_LIST` FOREIGN KEY (`IND_SEG_ID`) REFERENCES `segmentation_list` (`SEG_ID`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `room_actual`
--
ALTER TABLE `room_actual`
  ADD CONSTRAINT `fk_ROOM_ACTUAL_SEGMENTATION_LIST1` FOREIGN KEY (`SEG_ID`) REFERENCES `segmentation_list` (`SEG_ID`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `room_forecast`
--
ALTER TABLE `room_forecast`
  ADD CONSTRAINT `fk_ROOM_FORECAST_SEGMENTATION_LIST1` FOREIGN KEY (`SEG_ID`) REFERENCES `segmentation_list` (`SEG_ID`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
