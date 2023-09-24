import os
import csv

from django import setup
setup()

from django.conf import settings
from myapp.models import Company

def load_data():
    csv_file_path = os.path.join(
        settings.BASE_DIR, 'Main_dataset.csv')

    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row if it exists

        for row in reader:
            company = Company(
                company_name=row[0],
                category=row[1],
                sector=row[2],
                share_price=float(row[3]),
                market_cap=float(row[4]),
                source=row[5],
                lot_size=int(row[6]),
                min_qty=int(row[7]),
                isin=row[8],
                special_comment=row[9],
                sell_price_rupees=int(row[10])
            )
            company.save()


if __name__ == "__main__":
    load_data()
