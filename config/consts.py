from datetime import datetime
from domain.entities.employee import IEmployee
from domain.entities.medical_unit import IMedicalUnit
from domain.entities.patient import IPatient
from domain.entities.plan import IPlan
from domain.entities.speciality import ISpeciality
from domain.entities.doctor import IDoctor

DEFAULT_PLANS = [
    IPlan(
        name="Monthly Plan",
        description="This plan is valid for one month and can be renewed monthly",
        price=450.00,
    ),
    IPlan(
        name="Annual Plan",
        description="This plan is for one year and has a contract that can not be canceled after 2 months of purchase. ",
        price=1500.00,
    ),
    IPlan(
        name="Particular",
        description="The price of medical appointments depends only on the patient",
        price=350.00,
    ),
]


DEFAULT_SPECIALITIES = [
    ISpeciality(
        name="Neurology",
        description="Is a branch os medicine that deals with the diagnosis and treatment of all categories of conditions and disease involving the central and peripheral nervous systems ",
    ),
    ISpeciality(
        name="Cardiology",
        description="Is a branch of medicine that deals with the disorders of the heart as well as some parts of the cardiovascular system",
    ),
    ISpeciality(
        name="Pulmonology",
        description=" Is a branch of medicine that deals with diseases involving the respiratory tract.",
    ),
    ISpeciality(
        name="Otology",
        description="Is a branch of medicine which studies normal and pathological anatomy and physiology of the ear",
    ),
    ISpeciality(
        name="Pediatrics",
        description="Is the branch of medicine that involves the medical care of infants, children and adolescents",
    ),
    ISpeciality(
        name="Hepatology",
        description="Is the branch of medicine that incorporates the study of liver, gallbladder, biliary tree, and pancreas",
    ),
    ISpeciality(
        name="Osteology",
        description="Is the detailed study of the structure of bones, skeletal elements, teeth, microbone morphology, function, disease and pathology",
    ),
    ISpeciality(
        name="Otorhinolaryngology",
        description="Is a surgical subspecialty within medicine that deals with the surgical and medical management of conditions of the head and neck",
    ),
    ISpeciality(
        name="Gynecology",
        description="Is the medical practice dealing with the health of the female reproductive system",
    ),
    ISpeciality(
        name="Ophthalmology",
        description="Is a branch of medicine that deals with the diagnosis and treatment of eye disorders",
    ),
    ISpeciality(
        name="Urology",
        description="Is the branch of medicine that focuses on surgical and medical diseases of the male and female urinary-tract system and the male reproductive organs",
    ),
    ISpeciality(
        name="Gastroenterology",
        description="Is the branch of medicine focused on the digestive system and its disorders",
    ),
    ISpeciality(
        name="General ,Practitioner",
        description="Is a medical doctor who treats acute and chronic illnesses and provides preventive care and health education to patients of all ages",
    ),
]

DEFAULT_DOCTORS = [
    IDoctor(
        fullname="Pedro Luiz",
        birthdate=datetime.strptime("04-11-1980 01:01:01", "%d-%m-%Y %H:%M:%S"),
        crm=45612,
        speciality_id=2,
    ),
    IDoctor(
        fullname="Amanda Lemos",
        birthdate=datetime.strptime("03-08-1996 01:01:01", "%d-%m-%Y %H:%M:%S"),
        crm=78940,
        speciality_id=1,
    ),
    IDoctor(
        fullname="Luisa de Melo",
        birthdate=datetime.strptime("11-06-1991 01:01:01", "%d-%m-%Y %H:%M:%S"),
        crm=23476,
        speciality_id=5,
    ),
    IDoctor(
        fullname="Carlos Rodrigo",
        birthdate=datetime.strptime("28-02-1985 01:01:01", "%d-%m-%Y %H:%M:%S"),
        crm=67292,
        speciality_id=4,
    ),
    IDoctor(
        fullname="Sandra Lima",
        birthdate=datetime.strptime("17-09-1970 01:01:01", "%d-%m-%Y %H:%M:%S"),
        crm=12347,
        speciality_id=6,
    ),
    IDoctor(
        fullname="Alex Lima",
        birthdate=datetime.strptime("09-10-1967 01:01:01", "%d-%m-%Y %H:%M:%S"),
        crm=12567,
        speciality_id=7,
    ),
    IDoctor(
        fullname="Wanda de Sá",
        birthdate=datetime.strptime("01-01-1991 01:01:01", "%d-%m-%Y %H:%M:%S"),
        crm=54901,
        speciality_id=3,
    ),
    IDoctor(
        fullname="Lucas Amaro",
        birthdate=datetime.strptime("15-04-1965 01:01:01", "%d-%m-%Y %H:%M:%S"),
        crm=9724,
        speciality_id=8,
    ),
    IDoctor(
        fullname="Fabiana Aparecida",
        birthdate=datetime.strptime("21-12-1976 01:01:01", "%d-%m-%Y %H:%M:%S"),
        crm=18273,
        speciality_id=9,
    ),
    IDoctor(
        fullname="Fabio José",
        birthdate=datetime.strptime("03-03-1983 01:01:01", "%d-%m-%Y %H:%M:%S"),
        crm=1838,
        speciality_id=10,
    ),
    IDoctor(
        fullname="Igor de Salo",
        birthdate=datetime.strptime("30-10-1980 01:01:01", "%d-%m-%Y %H:%M:%S"),
        crm=1282,
        speciality_id=11,
    ),
    IDoctor(
        fullname="Ana Beatriz",
        birthdate=datetime.strptime("24-06-1988 01:01:01", "%d-%m-%Y %H:%M:%S"),
        crm=1929,
        speciality_id=12,
    ),
    IDoctor(
        fullname="Paulo Alan",
        birthdate=datetime.strptime("12-12-1962 01:01:01", "%d-%m-%Y %H:%M:%S"),
        crm=17272,
        speciality_id=6,
    ),
    IDoctor(
        fullname="Henrique Alura",
        birthdate=datetime.strptime("18-08-1978 01:01:01", "%d-%m-%Y %H:%M:%S"),
        crm=10283,
        speciality_id=10,
    ),
    IDoctor(
        fullname="Fernanda Souza",
        birthdate=datetime.strptime("05-05-1985 01:01:01", "%d-%m-%Y %H:%M:%S"),
        crm=48383,
        speciality_id=2,
    ),
    IDoctor(
        fullname="Sandra Lima",
        birthdate=datetime.strptime("17-09-1970 01:01:01", "%d-%m-%Y %H:%M:%S"),
        crm=12347,
        speciality_id=6,
    ),
    IDoctor(
        fullname="Nícolas André",
        birthdate=datetime.strptime("11-03-1989 01:01:01", "%d-%m-%Y %H:%M:%S"),
        crm=71828,
        speciality_id=1,
    ),
    IDoctor(
        fullname="Matheus Henrique",
        birthdate=datetime.strptime("24-05-1977 01:01:01", "%d-%m-%Y %H:%M:%S"),
        crm=89901,
        speciality_id=6,
    ),
    IDoctor(
        fullname="Isabela de Lara",
        birthdate=datetime.strptime("25-12-1990 01:01:01", "%d-%m-%Y %H:%M:%S"),
        crm=19283,
        speciality_id=9,
    ),
    IDoctor(
        fullname="Pablo Avante",
        birthdate=datetime.strptime("16-06-1960 01:01:01", "%d-%m-%Y %H:%M:%S"),
        crm=56373,
        speciality_id=8,
    ),
    IDoctor(
        fullname="Felipe dos Santos",
        birthdate=datetime.strptime("19-04-1973 01:01:01", "%d-%m-%Y %H:%M:%S"),
        crm=18728,
        speciality_id=3,
    ),
    IDoctor(
        fullname="Luana Sansa",
        birthdate=datetime.strptime("18-04-1990 01:01:01", "%d-%m-%Y %H:%M:%S"),
        crm=1728,
        speciality_id=2,
    ),
    IDoctor(
        fullname="Rafael Falz",
        birthdate=datetime.strptime("21-01-1977 01:01:01", "%d-%m-%Y %H:%M:%S"),
        crm=36748,
        speciality_id=2,
    ),
    IDoctor(
        fullname="Alana Har",
        birthdate=datetime.strptime("17-07-1987 01:01:01", "%d-%m-%Y %H:%M:%S"),
        crm=178,
        speciality_id=2,
    ),
    IDoctor(
        fullname="Harold Sun",
        birthdate=datetime.strptime("09-09-1969 01:01:01", "%d-%m-%Y %H:%M:%S"),
        crm=28,
        speciality_id=2,
    ),
]

DEFAULT_MEDICAL_UNITS = [
    IMedicalUnit(
        name="Matrix Unit",
        address="Araranguá",
        doctors=DEFAULT_DOCTORS[0:7],
        employee_id=1,
    ),
    IMedicalUnit(
        name="North Unit",
        address="Jaraguá do Sul",
        doctors=DEFAULT_DOCTORS[5:10],
        employee_id=2,
    ),
    IMedicalUnit(
        name="South Unit",
        address="Criciúma ",
        doctors=DEFAULT_DOCTORS[9:17],
        employee_id=3,
    ),
    IMedicalUnit(
        name="Capital Unit",
        address="Florianópolis",
        doctors=DEFAULT_DOCTORS[17:25],
        employee_id=4,
    ),
]

DEFAULT_EMPLOYEES = [
    IEmployee(
        fullname="Carlos Luis",
        birthdate=datetime.strptime("11-12-1980 01:01:01", "%d-%m-%Y %H:%M:%S"),
        email="carlosluis@gmail.com",
        password="012345",
    ),
    IEmployee(
        fullname="Fernanda de Moraes",
        birthdate=datetime.strptime("07-03-1990 01:01:01", "%d-%m-%Y %H:%M:%S"),
        email="fernandademoraes@gmail.com",
        password="112345",
    ),
    IEmployee(
        fullname="Pedro Sampai",
        birthdate=datetime.strptime("01-04-1985 01:01:01", "%d-%m-%Y %H:%M:%S"),
        email="pedrosampaio@gmail.com",
        password="212345",
    ),
    IEmployee(
        fullname="Isabela de Carvalho",
        birthdate=datetime.strptime("08-08-1991 01:01:01", "%d-%m-%Y %H:%M:%S"),
        email="isabeladecarvalho@gmail.com",
        password="312345",
    ),
]

DEFAULT_PATIENTS = [
    IPatient(
        fullname="Adalberto da Luz",
        birthdate=datetime.strptime("12-04-1958 01:01:01", "%d-%m-%Y %H:%M:%S"),
        document="18916575690",
        plan_id=1,
    ),
    IPatient(
        fullname="Felipe de Oliveira",
        birthdate=datetime.strptime("06-08-1999 01:01:01", "%d-%m-%Y %H:%M:%S"),
        document="18612167823",
        plan_id=1,
    ),
    IPatient(
        fullname="Evandro Pereira",
        birthdate=datetime.strptime("01-11-1968 01:01:01", "%d-%m-%Y %H:%M:%S"),
        document="11178954628",
        plan_id=2,
    ),
    IPatient(
        fullname="Edilton da Costa",
        birthdate=datetime.strptime("08-04-1978 01:01:01", "%d-%m-%Y %H:%M:%S"),
        document="16576878911",
        plan_id=2,
    ),
    IPatient(
        fullname="Luis Divar",
        birthdate=datetime.strptime("03-02-1980 01:01:01", "%d-%m-%Y %H:%M:%S"),
        document="12387614500",
        plan_id=2,
    ),
    IPatient(
        fullname="Matheus dos Santos",
        birthdate=datetime.strptime("16-10-2000 01:01:01", "%d-%m-%Y %H:%M:%S"),
        document="17865689010",
        plan_id=3,
    ),
]
