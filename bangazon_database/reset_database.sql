DROP TABLE IF EXISTS Training_Program;
DROP TABLE IF EXISTS Training_Program_Sessions;
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Employee;
DROP TABLE IF EXISTS Employment_Dates;
DROP TABLE IF EXISTS Department;
DROP TABLE IF EXISTS Computer;
DROP TABLE IF EXISTS Employee_Training;
DROP TABLE IF EXISTS Product;
DROP TABLE IF EXISTS Product_Type;
DROP TABLE IF EXISTS Cust_Order;
DROP TABLE IF EXISTS Cust_Ordered_Products;
DROP TABLE IF EXISTS Payment_Options;
DROP TABLE IF EXISTS Payment_Type;


CREATE TABLE `Training_Program` (
    `Program_ID` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    `Program_Name` TEXT NOT NULL,
    `Program_Description` TEXT NOT NULL
);

CREATE TABLE `Training_Program_Sessions` (
    `Session_ID` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    `Program_ID` INTEGER NOT NULL,
    `Program_Start_Date` TEXT NOT NULL,
    `Program_End_Date` TEXT NOT NULL,
    `Max_Students` INTEGER NOT NULL,
    FOREIGN KEY (Program_ID) REFERENCES Training_Program (Program_ID)
);

CREATE TABLE `User` (
	`User_ID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`First_Name`	TEXT NOT NULL,
	`Last_Name`	TEXT NOT NULL,
	`Street`	TEXT,
	`City`	TEXT,
	`State`	TEXT,
	`Zip`	NUMERIC,
	`Phone`	TEXT,
	`Email`	TEXT,
    `Date_Created` TEXT,
    `Last_Signon` TEXT

);

CREATE TABLE `Employee` (
	`Employee_ID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    `First_Name` TEXT NOT NULL,
    `Last_Name` TEXT NOT NULL,
	`Dept_ID`	INTEGER NOT NULL,
	`Comp_ID`	INTEGER NOT NULL,
	`Employee_Is_Active`	INTEGER NOT NULL,
    FOREIGN KEY (Dept_ID) REFERENCES Department (Department_ID),
    FOREIGN KEY (Comp_ID) REFERENCES Computer (Comp_ID)
);

CREATE TABLE `Employment_Dates` (
    `Emp_Date_ID` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    `Employee_ID` INTEGER NOT NULL,
    `Hire_Date` TEXT NOT NULL,
    `Term_Date` TEXT,
    FOREIGN KEY (Employee_ID) REFERENCES Employee (Employee_ID)
);

CREATE TABLE `Department` (
    `Department_ID` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    `Dept_Name` TEXT NOT NULL,
    `Supervisor_ID` INTEGER NOT NULL,
    `Remaining_Budget` INTEGER,
    FOREIGN KEY (Supervisor_ID) REFERENCES Employee (Employee_ID)
);

CREATE TABLE `Computer` (
    `Comp_ID` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    `Comp_Name` TEXT NOT NULL,
    `Commission_Date` TEXT NOT NULL,
    `Decommission_Date` TEXT
);

CREATE TABLE `Employee_Training` (
    `Emp_Train_ID` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    `Session_ID` INTEGER NOT NULL,
    `Employee_ID` INTEGER NOT NULL,
    `Completed` INTEGER NOT NULL,
    FOREIGN KEY (Session_ID) REFERENCES Training_Program (Session_ID),
    FOREIGN KEY (Employee_ID) REFERENCES Employee (Employee_ID)
);

CREATE TABLE `Product` (
    `Product_ID` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    `Type_ID` INTEGER NOT NULL,
    `Seller_ID` INTEGER NOT NULL,
    `Title` TEXT NOT NULL,
    `Price` INTEGER NOT NULL,
    `Description` TEXT,
    `Quantity` INTEGER NOT NULL,
    FOREIGN KEY (Type_ID) REFERENCES Product_Types (Type_ID),
    FOREIGN KEY (Seller_ID) REFERENCES User (User_ID)
);

CREATE TABLE `Product_Type` (
    `Type_ID` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    `Type_Name` Text NOT NULL
);

CREATE TABLE `Cust_Order` (
    `Order_ID` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    `Customer_ID` INTEGER NOT NULL,
    `Payment_ID` INTEGER,
    `Order_Date` TEXT,
    `Ship_Date` TEXT,
    FOREIGN KEY (Customer_ID) REFERENCES User(User_ID),
    FOREIGN KEY (Payment_ID) REFERENCES Payment_Options(Payment_ID)
);

CREATE TABLE `Ordered_Products` (
    `Order_Products_ID` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    `Order_ID` INTEGER NOT NULL,
    `Product_ID` INTEGER NOT NULL,
    `Quantity` INTEGER NOT NULL,
    FOREIGN KEY (Order_ID) REFERENCES Cust_Order(Order_ID),
    FOREIGN KEY (Product_ID) REFERENCES Product(Product_ID)
);

CREATE TABLE `Payment_Options` (
    `Payment_ID` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    `Customer_ID` INTEGER NOT NULL,
    `Payment_Type_ID` INTEGER NOT NULL,
    `Account_Num` TEXT NOT NULL,
    FOREIGN KEY (Customer_ID) REFERENCES User(User_ID),
    FOREIGN KEY (Payment_Type_ID) REFERENCES Payment_Type(Payment_Type_ID)
);

CREATE TABLE `Payment_Type` (
    `Payment_Type_ID` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    `Payment_Type_Name` TEXT NOT NULL
);