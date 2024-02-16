
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
  DEPT INTEGER,
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
INSERT INTO EMPLOYEE VALUES (7, 'No dept', NULL, 5000, 4, "UK");

select * from EMPLOYEE;
select * from DEPARTMENT;


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

-- 3rd highest salary department wise
/*
https://app.coderpad.io/sandbox

with salary_ranks AS (
SELECT e.first_name, e.last_name, e.salary,
  d.name as department_name, ROW_NUMBER() OVER (PARTITION BY d.name ORDER BY e.salary desc) as salary_rank
FROM employees AS e
INNER JOIN departments AS d ON e.department_id = d.id
)

select * from salary_ranks where salary_rank = 1;
*/

-- Duplicate employee count
/*
select CONCAT(first_name, " ", last_name) as full_name, count(*) emp_count
from employees
group by full_name
order by full_name
;
*/

-- Department-wise budget
/*
select AVG(p1.budget) as dept_budget, d1.name as dept_name
from projects as p1
INNER join employees_projects as ep1 on p1.id = ep1.project_id
INNER join employees as e1 on ep1.employee_id = e1.id
INNER join departments as d1 on e1.department_id = d1.id
GROUP by dept_name
;
*/

/*
-- Stored procedures

DROP PROCEDURE IF EXISTS get_employees_data;

DELIMITER //
CREATE PROCEDURE get_employees_data(IN department_id INT)
BEGIN
    SELECT * FROM employees WHERE employees.department_id = department_id;
END //
DELIMITER ;

call get_employees_data(2);

*/