sales_data = {
    "Store_A": {
        "Laptop": 15,
        "Phone": 30,
        "Tablet": 10
    },
    "Store_B": {
        "Laptop": 25,
        "Phone": 20,
        "Tablet": 15
    },
    "Store_C": {
        "Laptop": 10,
        "Phone": 35,
        "Tablet": 5
    }
}

def total_sales(sales_data):
    """It calculates the total sales for a sales data dictionary."""
    total = {}

    for product in sales_data.values():
        for key, value in product.items():
            total[key] = value + total.get(key, 0)

    return total

result = total_sales(sales_data)
print(result)