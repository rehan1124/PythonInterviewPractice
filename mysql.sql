
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
*/

select * from EMPLOYEE
where name like "C%";
