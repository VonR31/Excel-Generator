# 🛠️ Lighting Branch Product Generator

This Python script (`ProductGenerator.py`) generates a sample Excel spreadsheet containing 100 lighting products. It assigns random names, categories, prices, quantities, and status values, making it a helpful tool for prototyping inventory systems, testing dashboards, or preparing demo datasets.

---

## 📁 Output

The script generates:

- **lighting_branch_products.xlsx** — An Excel file containing synthetic product data.

Each row in the Excel file includes:

| Product Name       | Category        | Price  | Quantity | Status     |
|--------------------|------------------|--------|----------|------------|
| LED Panel Light     | Ceiling Light    | 520.00 | 50       | In Stock   |
| Garden Lantern      | Lantern          | 99.99  | 8        | Low Stock  |
| ...                | ...              | ...    | ...      | ...        |

---

## 🧩 Features

- Loads category data from a local `category_rows.csv` file.
- Randomized:
  - Product names (based on lighting categories)
  - Prices (₱50.00–₱1000.00)
  - Quantities (1–100)
  - Status based on quantity (`Low Stock` if < 20)
- Uses `openpyxl` to generate `.xlsx` output.

---

## 📦 Requirements

- Python 3.x
- `openpyxl` module

You can install the required package using pip:

```bash
pip install openpyxl
```

---

## 📂 Files Required

- `ProductGenerator.py` – Main script
- `category_rows.csv` – CSV file containing a list of categories (must include a column: `category_name`)

Example `category_rows.csv`:
```csv
category_name
Chandelier
Bulb
Pendant Light
...
```

---

## ▶️ How to Run

Make sure `ProductGenerator.py` and `category_rows.csv` are in the same directory.

Then run:

```bash
python ProductGenerator.py
```

Output:
```bash
Excel file saved at: lighting_branch_products.xlsx
```

---

## 📜 License

This project is licensed for personal and educational use. Attribution is appreciated but not required.

---

## 🙋‍♂️ Author

Created by Von Russel 
