import os
import csv

from django import setup
setup()

from myapp.models import Company
from django.conf import settings


def load_data():
    csv_file_path = os.path.join(
        settings.BASE_DIR, 'Main_dataset1.csv')

    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row if it exists

        for row in reader:
             # Check if share_price is a valid integer or handle non-integer values
            try:
                share_price = int(row[3])
            except ValueError:
                share_price = 0  # Set a default value for non-integer values
            # Remove commas and handle empty strings for market_cap
            market_cap = float(row[4].replace(',', '')) if row[4] else 0.0
            # Handle empty strings for lot_size
            lot_size = int(row[6]) if row[6] else 0
         
            min_qty = int(row[7].replace(',', '')) if row[7] else 0
            sell_price_rupees = int(row[10]) if row[10] else 0

            company = Company(
                company_name=row[0],
                category=row[1],
                sector=row[2],
                share_price=share_price,
                market_cap=market_cap,
                source=row[5],
                lot_size=lot_size,
                min_qty=min_qty,
                isin=row[8],
                special_comment=row[9],
                sell_price_rupees=sell_price_rupees
            )
            company.save()


if __name__ == "__main__":
    load_data()