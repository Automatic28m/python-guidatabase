-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 03, 2023 at 08:56 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `myshop`
--
CREATE DATABASE IF NOT EXISTS `myshop` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `myshop`;

-- --------------------------------------------------------

--
-- Table structure for table `tbproduct`
--

CREATE TABLE `tbproduct` (
  `productID` varchar(2) NOT NULL,
  `productName` varchar(30) NOT NULL,
  `typeID` varchar(2) NOT NULL,
  `unitPrice` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `tbproduct`
--

INSERT INTO `tbproduct` (`productID`, `productName`, `typeID`, `unitPrice`) VALUES
('1', 'เค้กกล้วยหอม', '2', 12),
('2', 'เค้กโรลส้ม', '2', 25),
('3', 'Mocha', '1', 20),
('4', 'ชาเขียว', '1', 35),
('5', 'ชาไทย', '1', 35),
('6', 'น้ำส้มปั่น', '1', 65),
('7', 'ลาเต้', '1', 30);

-- --------------------------------------------------------

--
-- Table structure for table `tbsell`
--

CREATE TABLE `tbsell` (
  `sellid` varchar(5) NOT NULL,
  `sellDate` varchar(50) NOT NULL,
  `total` decimal(8,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tbselldetail`
--

CREATE TABLE `tbselldetail` (
  `sellid` varchar(5) NOT NULL,
  `itemID` varchar(2) NOT NULL,
  `Qty` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tbtype`
--

CREATE TABLE `tbtype` (
  `typeID` varchar(2) NOT NULL,
  `typeName` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `tbtype`
--

INSERT INTO `tbtype` (`typeID`, `typeName`) VALUES
('1', 'beverage'),
('2', 'bakery');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tbproduct`
--
ALTER TABLE `tbproduct`
  ADD PRIMARY KEY (`productID`);

--
-- Indexes for table `tbsell`
--
ALTER TABLE `tbsell`
  ADD PRIMARY KEY (`sellid`);

--
-- Indexes for table `tbselldetail`
--
ALTER TABLE `tbselldetail`
  ADD PRIMARY KEY (`sellid`,`itemID`),
  ADD KEY `Itemid` (`itemID`);

--
-- Indexes for table `tbtype`
--
ALTER TABLE `tbtype`
  ADD PRIMARY KEY (`typeID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
