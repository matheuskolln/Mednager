USE backend;




# Consulta 1 -> Valor médio, total, quantidade para cada plano
SELECT
	plans.name `Plan name`,
	SUM(plans.price) `Total price`,
	COUNT(plans.id) `Amount`,
	(SUM(plans.price)/ (
	SELECT
		SUM(plans.price)
	FROM
		plans
	RIGHT JOIN
	patients ON
		patients.plan_id = plans.id)) `% value`
FROM
	plans
RIGHT JOIN
	patients ON
	patients.plan_id = plans.id
GROUP BY
	plans.name;
	

# Consulta 2 -> Quantidade de doutores em cada unidade medica
SELECT 
	count(doctors.id) `Doctors`,
	medical_units.name `Medical Unit`
FROM 
	medical_units
LEFT JOIN
	doctor_medical_unit ON
	medical_units.id = doctor_medical_unit.medical_unit_id
LEFT JOIN
	doctors ON
	doctor_medical_unit.doctor_id = doctors.id
GROUP BY
	medical_units.name;
	
# Consulta 3 -> Quantidade de doutores por especialidade que tem uma unidade medica
SELECT 
	count(doctors.id) `Doctors`,
	specialities.name `Speciality`
FROM 
	medical_units
LEFT JOIN
	doctor_medical_unit ON
	medical_units.id = doctor_medical_unit.medical_unit_id
LEFT JOIN
	doctors ON
	doctor_medical_unit.doctor_id = doctors.id
LEFT JOIN 
	specialities ON
	specialities.id = doctors.speciality_id 
GROUP BY
	specialities.name;