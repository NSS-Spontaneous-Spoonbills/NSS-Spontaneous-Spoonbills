CREATE TABLE `Training_Program` (
    `Program_ID` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    `Program_Name` TEXT NOT NULL,
    `Program_Description` TEXT NOT NULL
	PRIMARY KEY(`Program_ID`),
);

CREATE TABLE `Training_Program_Sessions` (
    `Session_ID` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    `Program_ID` INTEGER NOT NULL,
    `Program_Start_Date` TEXT NOT NULL,
    `Program_End_Date` TEXT NOT NULL,
    `Max_Students` INTEGER NOT NULL,
	PRIMARY KEY(`Session_ID`),
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
	PRIMARY KEY(`User_ID`),

);

CREATE TABLE `Employee` (
	`Employee_ID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    `First_Name` TEXT NOT NULL,
    `Last_Name` TEXT NOT NULL,
	`Dept_ID`	INTEGER NOT NULL,
	`Comp_ID`	INTEGER NOT NULL,
	`Employee_Is_Active`	INTEGER NOT NULL,
	PRIMARY KEY(`Employee_ID`),
    FOREIGN KEY (Dept_ID) REFERENCES Department (Department_ID),
    FOREIGN KEY (Comp_ID) REFERENCES Computer (Comp_ID)
);

CREATE TABLE `Employment_Dates` (
    `Emp_Date_ID` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    `Employee_ID` INTEGER NOT NULL,
    `Hire_Date` TEXT NOT NULL,
    `Term_Date` TEXT,
	PRIMARY KEY(`Emp_Date_ID`),
    FOREIGN KEY (Employee_ID) REFERENCES Employee (Employee_ID)
);

CREATE TABLE `Department` (
    `Department_ID` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    `Dept_Name` TEXT NOT NULL,
    `Supervisor_ID` INTEGER NOT NULL,
    `Remaining_Budget` INTEGER,
	PRIMARY KEY(`Department_ID`),
    FOREIGN KEY (Supervisor_ID) REFERENCES Employee (Employee_ID)
);

CREATE TABLE `Computer` (
    `Comp_ID` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    `Comp_Name` TEXT NOT NULL,
    `Commission_Date` TEXT NOT NULL,
    `Decommission_Date` TEXT,
	PRIMARY KEY(`Comp_ID`)
);

CREATE TABLE `Employee_Training` (
    `Emp_Train_ID` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    `Session_ID` INTEGER NOT NULL,
    `Employee_ID` INTEGER NOT NULL,
    `Completed` INTEGER NOT NULL,
	PRIMARY KEY(`Emp_Train_ID`)
    FOREIGN KEY (Session_ID) REFERENCES Training_Program (Session_ID),
    FOREIGN KEY (Employee_ID) REFERENCES Employee (Employee_ID)
);

CREATE TABLE `Product` (
    `Product_ID` INTEGER NOT NULL AUTOINCREMENT PRIMARY KEY UNIQUE,
    `Type_ID` INTEGER NOT NULL,
    `Seller_ID` INTEGER NOT NULL,
    `Title` TEXT NOT NULL,
    `Price` INTEGER NOT NULL,
    `Description` TEXT,
    `Quantity` INTEGER NOT NULL,
	PRIMARY KEY(`Product_ID`)
    FOREIGN KEY (Type_ID) REFERENCES Product_Types (Type_ID),
    FOREIGN KEY (Seller_ID) REFERENCES User (User_ID)
);

CREATE TABLE `Product_Type` (
    `Type_ID` INTEGER NOT NULL AUTOINCREMENT PRIMARY KEY UNIQUE,
    `Type_Name` Text NOT NULL
	PRIMARY KEY(`Type_ID`)
);

CREATE TABLE `Order` (
    `Order_ID` INTEGER AUTOINCREMENT PRIMARY KEY UNIQUE NOT NULL,
    `Customer_ID` TEXT NOT NULL,
    `Payment_ID` INTEGER,
    `Is_Complete` INTEGER NOT NULL,
    `Is_Shipped` INTEGER NOT NULL,
    `Order_Date` TEXT NOT NULL,
    `Total_Amount` INTEGER NOT NULL,
	PRIMARY KEY(`Order_ID`)
    FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID),
    FOREIGN KEY (Payment_ID) REFERENCES Payment_Options(Payment_ID)
);

CREATE TABLE `Ordered_Products` (
    `Order_ID` INTEGER NOT NULL,
    `Product_ID` INTEGER NOT NULL,
    FOREIGN KEY (Order_ID) REFERENCES Order(Order_ID),
    FOREIGN KEY (Product_ID) REFERENCES Product(Product_ID)
);

CREATE TABLE `Payment_Options` (
    `Payment_ID` PRIMARY KEY INTEGER NOT NULL UNIQUE AUTOINCREMENT,
    `Customer_ID` TEXT NOT NULL,
    `Account_Num` TEXT NOT NULL,
    `Payment_Type
)