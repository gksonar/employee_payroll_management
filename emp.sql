-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 30, 2021 at 01:33 PM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `emp`
--

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `eid` bigint(255) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `department` varchar(255) DEFAULT NULL,
  `contact` varchar(255) DEFAULT NULL,
  `dob` varchar(255) DEFAULT NULL,
  `designation` varchar(255) DEFAULT NULL,
  `join_date` varchar(255) DEFAULT NULL,
  `salary` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `created_at` varchar(255) DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`eid`, `name`, `department`, `contact`, `dob`, `designation`, `join_date`, `salary`, `email`, `address`, `created_at`) VALUES
(1, 'Gaurav Sonarr', 'CM ', '12-02-2002', 'Developer', '15-02-2019', '25000', '9960141250', 'gaurav.22020272@viit.ac.in', 'Nashik', '2021-04-28 20:56:16'),
(3, 'Manali Pangare', 'CM', '8855664477', '16-07-2000', 'Developer', '15-02-2019', '35000', 'manali@viit.ac.in', 'Pune', '2021-04-28 20:59:08'),
(4, 'Vaishnavi Jadhav', 'CM', '2255556664', '12-12-2001', 'Developer', '15-02-2019', '50000', 'Vaishnavi@viit.ac.in', 'Solapur\r\n\r\n', '2021-04-29 07:13:33'),
(12, 'X Y Z ', 'Sales ', '9966556655', '12-12-1995', 'Sales Officer', '15-07-2014', '50000', 'xyz@xyz.in', 'PUNE\n', '2021-05-06 08:35:14'),
(13, 'Xyz', 'CM ', '8899966550', '12-02-1995', 'Developer', '12-05-2018', '25000', 'xy@aa.com', 'Pune\n', '2021-05-06 20:50:24'),
(14, 'Pqr ', 'IT ', '8855223366', '12-05-2000', 'Developer', '12-05-2020', '25000', 'pqr@gmail.com', 'Pune\n', '2021-05-06 20:57:19');

-- --------------------------------------------------------

--
-- Table structure for table `holiday`
--

CREATE TABLE `holiday` (
  `hid` bigint(255) NOT NULL,
  `hdate` varchar(255) DEFAULT NULL,
  `hdescription` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `holiday`
--

INSERT INTO `holiday` (`hid`, `hdate`, `hdescription`) VALUES
(1, '25-12-2021', 'Christmas'),
(2, '01-05-2021', 'Maharashtra Day '),
(6, '22-06-2021', 'ENVIROMENT DAY\n'),
(7, '15-08-2021', 'Independence Day \n'),
(8, '26-01-2021', 'National Holiday \n');

-- --------------------------------------------------------

--
-- Table structure for table `hr`
--

CREATE TABLE `hr` (
  `hr_id` bigint(255) DEFAULT NULL,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hr`
--

INSERT INTO `hr` (`hr_id`, `username`, `password`, `created_at`) VALUES
(1, 'Admin', 'admin', '2021-04-28 21:14:05'),
(1, 'Admin', 'admin', '2021-04-28 21:14:11');

-- --------------------------------------------------------

--
-- Table structure for table `salary_detail`
--

CREATE TABLE `salary_detail` (
  `rid` bigint(255) NOT NULL,
  `eid` bigint(255) DEFAULT NULL,
  `leaves` bigint(255) DEFAULT NULL,
  `overtime` bigint(255) DEFAULT NULL,
  `pf` bigint(255) DEFAULT NULL,
  `other` bigint(255) DEFAULT NULL,
  `medical` bigint(255) DEFAULT NULL,
  `leavesrs` bigint(255) DEFAULT NULL,
  `overtimers` bigint(255) DEFAULT NULL,
  `net_sal` bigint(255) DEFAULT NULL,
  `month` bigint(255) DEFAULT NULL,
  `year` bigint(255) DEFAULT NULL,
  `basic_sal` bigint(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `salary_detail`
--

INSERT INTO `salary_detail` (`rid`, `eid`, `leaves`, `overtime`, `pf`, `other`, `medical`, `leavesrs`, `overtimers`, `net_sal`, `month`, `year`, `basic_sal`) VALUES
(2, 2, 5, 8, 1500, 1000, 1000, 4129, 1225, 19196, 0, 2021, 25600),
(3, 3, 8, 4, 1500, 1000, 1000, 9032, 764, 23232, 0, 2021, 35000),
(4, 4, 12, 10, 1500, 1000, 1000, 19354, 2516, 29661, 0, 2021, 50000),
(8, 1, 5, 8, 1500, 1000, 1000, 4166, 1233, 18566, 0, 2021, 25000),
(9, 14, 5, 5, 1500, 1000, 1000, 4166, 770, 18104, 0, 2021, 25000);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`eid`);

--
-- Indexes for table `holiday`
--
ALTER TABLE `holiday`
  ADD PRIMARY KEY (`hid`);

--
-- Indexes for table `salary_detail`
--
ALTER TABLE `salary_detail`
  ADD PRIMARY KEY (`rid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `employee`
--
ALTER TABLE `employee`
  MODIFY `eid` bigint(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `holiday`
--
ALTER TABLE `holiday`
  MODIFY `hid` bigint(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `salary_detail`
--
ALTER TABLE `salary_detail`
  MODIFY `rid` bigint(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
