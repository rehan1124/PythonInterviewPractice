
-- create
CREATE TABLE EMPLOYEE (
  empId INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  dept TEXT NOT NULL,
  salary numeric NOT NULL
);

-- insert
INSERT INTO EMPLOYEE VALUES (0001, 'Clark', 'Sales', 1000);
INSERT INTO EMPLOYEE VALUES (0002, 'Dave', 'Accounting', 2000);
INSERT INTO EMPLOYEE VALUES (0003, 'Ava', 'Sales', 3000);
INSERT INTO EMPLOYEE VALUES (0004, 'Ava', 'Accounting', 3000);
INSERT INTO EMPLOYEE VALUES (0005, 'Ava', 'Sales', 4000);
INSERT INTO EMPLOYEE VALUES (0006, 'Clark', 'Sales', 5000);

-- fetch
/*
select * from (
select *, ROW_NUMBER() OVER (ORDER by empId) as RN from EMPLOYEE as T1) as T2
where MOD (RN, 2) != 0;

select dept Department, count(*) EmpCount from EMPLOYEE
group by dept
having EmpCount > 1
order by EmpCount desc;

select * from EMPLOYEE
where name like "C%";
*/

/*
select * from (
select *, ROW_NUMBER() OVER (ORDER BY empId) as row_num
from EMPLOYEE as EMP1) as EMP2
where row_num in (2, 3, 5)
;

select name, salary from EMPLOYEE
union all
select name, salary from EMPLOYEE;
*/

---------------------------------------------------------------------------------------------------------------
/*

CREATE TABLE EMPLOYEE (
  empId INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  dept TEXT NOT NULL,
  salary numeric NOT NULL
);

CREATE TABLE EMPLOYEE1 (
  empId INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  dept TEXT NOT NULL
);

-- insert
INSERT INTO EMPLOYEE VALUES (0001, 'Clark', 'Sales', 5000);
INSERT INTO EMPLOYEE VALUES (0002, 'Dave', 'Accounting', 4000);
INSERT INTO EMPLOYEE VALUES (0003, 'Ava', 'Sales', 3000);
INSERT INTO EMPLOYEE VALUES (0004, 'Ava2', 'Sales', 6000);


INSERT INTO EMPLOYEE1 VALUES (0001, 'Clark', 'Sales');
INSERT INTO EMPLOYEE1 VALUES (0002, 'Dave', 'Accounting');
INSERT INTO EMPLOYEE1 VALUES (0003, 'Ava', 'Sales');

-- fetch
SELECT * FROM EMPLOYEE as E
inner join EMPLOYEE1 as E1
on E.empId = E1.empId
where E.dept in ("Sales") and E1.dept = "Sales"
;

*/

-------------------------------------------------------------------
/*
--------------------------
--- New table creation ---
--------------------------

-- create DEPARTMENT
CREATE TABLE DEPARTMENT (
  ID INTEGER PRIMARY KEY,
  NAME TEXT NOT NULL
);

-- create EMPLOYEE
CREATE TABLE EMPLOYEE (
  ID INTEGER PRIMARY KEY,
  NAME TEXT NOT NULL,
  DEPT INTEGER NOT NULL,
  SALARY numeric NOT NULL,
  MGR INTEGER NULL,
  LOCATION TEXT NOT NULL
);

-- insert DEPARTMENT
INSERT INTO DEPARTMENT VALUES (1, 'ACCOUNTS');
INSERT INTO DEPARTMENT VALUES (2, 'SALES');
INSERT INTO DEPARTMENT VALUES (3, 'CUSTOMER SUPPORT');
INSERT INTO DEPARTMENT VALUES (4, 'BADEVQA');

-- insert EMPLOYEE
INSERT INTO EMPLOYEE VALUES (1, 'Clark', 1, 1000, NULL, "INDIA");
INSERT INTO EMPLOYEE VALUES (2, 'Dave', 2, 2000, 1, "US");
INSERT INTO EMPLOYEE VALUES (3, 'Harry', 3, 2500, 1, "INDIA");
INSERT INTO EMPLOYEE VALUES (4, 'Ava', 3, 3000, NULL, "UK");
INSERT INTO EMPLOYEE VALUES (5, 'Tom', 1, 4000, 4, "UK");
INSERT INTO EMPLOYEE VALUES (6, 'Dickenson', 2, 5000, 4, "UK");

-- fetch
select * from DEPARTMENT DEPT
right join EMPLOYEE EMP
on DEPT.ID = EMP.DEPT
;

-- Full join
select * from DEPARTMENT DEPT
left join EMPLOYEE EMP
on DEPT.ID = EMP.DEPT
union
select * from DEPARTMENT DEPT
right join EMPLOYEE EMP
on DEPT.ID = EMP.DEPT
;

-- Cross join
select * from DEPARTMENT DEPT
cross join EMPLOYEE EMP
;

select * from DEPARTMENT DEPT
cross join EMPLOYEE EMP
where DEPT.NAME = "BADEVQA"
;

*/