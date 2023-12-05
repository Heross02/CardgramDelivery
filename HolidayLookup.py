import csv
from CardHostTemplate import sendBirthdayCard, sendChristmasCard, sendEmployeeAppreciation, sendEidAlAdha, read_csv_file
from datetime import date, datetime, timedelta
from hijri_converter import convert

def get_eid_al_adha_islamic_date():
    # Manually set the Hijri date for Eid al-Adha
    islamic_date = convert.Gregorian(year=date.today().year, month=date.today().month, day=date.today().day).to_hijri()
    islamic_date_str = f"{islamic_date.year:04d}-{islamic_date.month:02d}-{islamic_date.day:02d}"
    return islamic_date_str

def get_multiple_values(csv_file):
    values_per_iteration = []
        # Get today's date
    today_date = datetime.now().strftime('%m-%d')
    with open(csv_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            # Assuming you want to extract values from specific columns
            value1 = row.get('Name')
            value2 = row.get('Birthday')
            value3 = row.get('Email')
            birthday_month_day = datetime.strptime(row['Birthday'], '%m/%d/%Y').strftime('%m-%d')
            if birthday_month_day == today_date:
                sendEmployeeAppreciation(value1,value3)
            # Add more columns as needed

            # Store values in a list for the current iteration
            values_per_iteration.append((value1, value2,value3))

    return values_per_iteration

def get_holiday_values(csv_file):
    holidays_per_iteration = []
        # Get today's date
    today_date = datetime.now().strftime('%m-%d')
    with open(csv_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        x=0
        for row in reader:
            # Assuming you want to extract values from specific columns
            value1 = row.get('Holiday_Name')
            value2 = row.get('Holiday_Date')
            month_day = datetime.strptime(row['Holiday_Date'], '%m/%d').strftime('%m-%d')
            if month_day == today_date:
                with open('employee_info.csv', 'r') as csvfile:
                    reader = csv.DictReader(csvfile)

                    for row in reader:
                        # Assuming you want to extract values from specific columns
                        value1 = row.get('Name')
                        value2 = row.get('Email')
                        sendEmployeeAppreciation(value1, value2)
            if month_day == today_date:
                with open('employee_info.csv', 'r') as csvfile:
                    reader = csv.DictReader(csvfile)

                    for row in reader:
                        # Assuming you want to extract values from specific columns
                        value1 = row.get('Name')
                        value2 = row.get('Email')
                        sendEidAlAdha(value1, value2)
            if month_day == today_date:
                with open('employee_info.csv', 'r') as csvfile:
                    reader = csv.DictReader(csvfile)

                    for row in reader:
                        # Assuming you want to extract values from specific columns
                        value1 = row.get('Name')
                        value2 = row.get('Email')
                        sendChristmasCard(value1, value2)
            if month_day == today_date:
                with open('employee_info.csv', 'r') as csvfile:
                    reader = csv.DictReader(csvfile)

                    for row in reader:
                        # Assuming you want to extract values from specific columns
                        value1 = row.get('Name')
                        value2 = row.get('Email')
                        sendBirthdayCard(value1, value2)
            #     return row['Holiday_Date']
            # Add more columns as needed

            # Store values in a list for the current iteration
            holidays_per_iteration.append((value1, value2))
    return holidays_per_iteration

# Example usage
csv_file_path = 'employee_info.csv'  # Replace with the actual path to your CSV file
csvfilepath = "holidays.csv"
result = get_multiple_values(csv_file_path)
result2 = get_holiday_values(csvfilepath)
for values in result:
    print(f"Values for this iteration: {values}")
    
for values in result2:
    print(f"Values for this iteration: {values}")