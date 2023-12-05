# CardHostTemplate.py
import pandas as pd
import subprocess
from AutoEmail import generate_outlook_email


# Make arrays global
NameArray = []
BirthdayArray = []
EmailArray = []


def read_csv_file(file_path):
    # Read the CSV file and populate the arrays
    csv_reader = pd.read_csv(file_path)
    for index, row in csv_reader.iterrows():
        Name, Birthday, Email = row
        NameArray.append(Name)
        BirthdayArray.append(Birthday)
        EmailArray.append(Email)


def sendBirthdayCard(name, email):
    template_generator_script = "BDAY.py"
    subprocess.run(["python", template_generator_script])
    subject_line = f"Happy Birthday, {name}!"
    body_text = r"""
    Dear""" + f" {name}"+r""",<br><br>
    We are wishing you a happy birthday and hope you are in good morals.:<br><br>
    <img src="cid:template_img"><br><br>
    In order to see your birthday card to its full degree, please download this zip file and run the following program code.<br><br>
    Best wishes,<br>
    CardiGram Holiday Templates
    """
    attach_img = 'Bday.PNG'
    attach_file = 'BDAY.zip'
    generate_outlook_email(email, subject_line, body_text, attach_img, attach_file)


def sendChristmasCard(name, email):
    template_generator_script = "ChristmasTemplate.py"
    subprocess.run(["python", template_generator_script])
    subject_line = f"Merry Christmas and Happy Holidays, {name}!"
    body_text = r"""
        Merry Christmas and Happy Holidays""" + f" {name}" + r"""!,<br><br>
        We are wishing you the best with yuletide cheer:<br><br>
        <img src="cid:template_img"><br><br>
        In order to see your holiday card to its full degree. Please download this zip file and run the following program code.<br><br>
        Happy Holidays,<br>
        CardiGram Holiday Templates
        """
    attach_img = 'Holiday.PNG'
    attach_file = 'ChristmasTemplate.zip'
    generate_outlook_email(email, subject_line, body_text, attach_img, attach_file)


def sendEmployeeAppreciation(name, email):
    template_generator_script = "EmployeCardTemplate.py"
    subprocess.run(["python", template_generator_script])
    subject_line = f"Thank you for your Hard Work. We appreciate all you do {name}!"
    body_text = r"""
        Dear""" + f" {name}" + r""",<br><br>
        Thank you for your outstanding contributions and hard work!:<br><br>
        <img src="cid:template_img"><br><br>
        In order to see your appreciation card to its full degree. Please download this zip file and run the following program code.<br><br>
        Best wishes,<br>
        CardiGram Holiday Templates
        """
    attach_img = 'EmployeeAppreciationCard.png'
    attach_file = 'EmployeCardTemplate.zip'
    generate_outlook_email(email, subject_line, body_text, attach_img, attach_file)


def sendEidAlAdha(name, email):
    template_generator_script = "Eid_Card.py"
    subprocess.run(["python", template_generator_script])
    subject_line = f"Eid Mubarak!"
    body_text = r"""
        Dear""" + f" {name}" + r""",<br><br>
        Eid Mubarak!:<br><br>
        <img src="cid:template_img"><br><br>
        In order to see your holiday card to its full degree. Please download this zip file and run the following program code.<br><br>
        Best wishes,<br>
        CardiGram Holiday Templates
        """
    attach_img = 'Eid_Al-AdhaCard.png'
    attach_file = 'Eid_Card.zip'
    generate_outlook_email(email, subject_line, body_text, attach_img, attach_file)



