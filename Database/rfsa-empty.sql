-- phpMyAdmin SQL Dump
-- version 4.7.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 19, 2017 at 08:46 AM
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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
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
