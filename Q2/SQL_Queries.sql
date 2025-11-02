
-- ============================================================================
-- Query 1: Get the names of the running Projects
-- ============================================================================

SELECT Name
FROM Project
WHERE FinishedAt IS NULL;


-- ============================================================================
-- Query 2: Get the number of finished Projects per Company
-- ============================================================================

SELECT 
    c.Name AS CompanyName,
    COUNT(p.IdProject) AS FinishedProjectsCount
FROM Company c
LEFT JOIN Employee e ON c.IdCompany = e.IdCompany
LEFT JOIN Project p ON e.IdEmployee = p.IdEmployee AND p.FinishedAt IS NOT NULL
GROUP BY c.IdCompany, c.Name
ORDER BY FinishedProjectsCount DESC;


-- ============================================================================
-- Query 3: Get the Company Names that have 2 or more different Projects 
--          with the same Name
-- ============================================================================


SELECT DISTINCT c.Name AS CompanyName
FROM Company c
INNER JOIN Employee e ON c.IdCompany = e.IdCompany
INNER JOIN Project p ON e.IdEmployee = p.IdEmployee
GROUP BY c.IdCompany, c.Name, p.Name
HAVING COUNT(p.IdProject) >= 2;

