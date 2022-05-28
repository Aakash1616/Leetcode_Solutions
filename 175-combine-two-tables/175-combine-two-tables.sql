# Write your MySQL query statement below
select p.firstname, p.lastname, a.city, a.state from Person as p natural left join Address as a;