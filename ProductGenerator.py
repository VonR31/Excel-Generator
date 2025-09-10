from openpyxl import Workbook
import random
import os
import csv


lighting_workbook = Workbook()
lighting_sheet = lighting_workbook.active


headers = ["Product Name", "Category", "Price", "Quantity", "Status"]


lighting_sheet.append(headers)


categories = []
with open(os.path.join(os.path.dirname(__file__), "category_rows.csv"), 'r') as file:
    csv_reader = csv.DictReader(file)
    categories = [row['category_name'] for row in csv_reader]

# Define lighting products with their categories
lighting_products = {
    'Chandelier': ['Crystal Chandelier', 'Modern Chandelier', 'Vintage Chandelier'],
    'Bulb': ['LED Smart Bulb', 'Color Changing Bulb', 'Dimmable LED Bulb'],
    'Pendant Light': ['Glass Pendant Light', 'Industrial Pendant Light', 'Modern Pendant Light'],
    'Ceiling Light': ['Flush Mount Ceiling Light', 'LED Panel Light', 'Decorative Ceiling Light'],
    'Wall Lamp': ['Modern Wall Sconce', 'Reading Wall Lamp', 'Decorative Wall Light'],
    'Table Lamp': ['Desk Lamp', 'Bedside Table Lamp', 'Study Lamp'],
    'Floor Lamp': ['Reading Floor Lamp', 'Arc Floor Lamp', 'Modern Floor Lamp'],
    'Track Lighting': ['LED Track Light', 'Adjustable Track Light', 'Spotlight Track System'],
    'Recessed Lighting': ['LED Downlight', 'Adjustable Recessed Light', 'Smart Recessed Light'],
    'Outdoor Lighting': ['Garden Light', 'Pathway Light', 'Security Flood Light'],
    'Smart Lighting': ['Smart LED Strip', 'Smart Ceiling Light', 'Smart Wall Light'],
    'LED Strip': ['RGB LED Strip', 'White LED Strip', 'Flexible LED Tape'],
    'Lantern': ['Garden Lantern', 'Hanging Lantern', 'Solar Lantern'],
    'Spotlight': ['Adjustable Spotlight', 'Garden Spotlight', 'LED Spotlight'],
    'Emergency Light': ['LED Emergency Light', 'Exit Sign Light', 'Backup Light']
}

# Generate 20 lighting products
for _ in range(100):

    category = random.choice(categories)

    product_name = random.choice(lighting_products[category])
    price = round(random.uniform(50, 1000), 2)
    quantity = random.randint(1, 100)
    status = "Low Stock" if quantity < 20 else "In Stock"
    lighting_sheet.append([product_name, category, price, quantity, status])


lighting_file_path = os.path.join(os.path.dirname(__file__), "lighting_branch_products.xlsx")
lighting_workbook.save(lighting_file_path)

print(f"Excel file saved at: {lighting_file_path}")
