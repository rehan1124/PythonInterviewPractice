
-- create
CREATE TABLE EMPLOYEE (
  empId INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  dept TEXT NOT NULL,
  salary INTEGER NOT NULL
);

-- insert
INSERT INTO EMPLOYEE VALUES (0001, 'Clark', 'Sales', 1000);
INSERT INTO EMPLOYEE VALUES (0002, 'Dave', 'Accounting', 2000);
INSERT INTO EMPLOYEE VALUES (0003, 'Ava', 'Sales', 3000);
INSERT INTO EMPLOYEE VALUES (0004, 'Ava', 'Sales', 4000);
INSERT INTO EMPLOYEE VALUES (0005, 'Ava', 'Sales', 5000);

-- fetch
DELIMITER //
CREATE PROCEDURE get_highest_salary_as_per_rank(IN rank_number INTEGER)
BEGIN
select * from (
SELECT * FROM EMPLOYEE order by salary desc limit rank_number) as T1
order by salary asc limit 1;
END //
DELIMITER ;

call get_highest_salary_as_per_rank(3);
call get_highest_salary_as_per_rank(1);
call get_highest_salary_as_per_rank(2);
