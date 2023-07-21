import pandas as pd

data = [
    {
        "order_id": 11973,
        "warehouse_name": "Мордор",
        "highway_cost": -70,
        "products": [
            {
                "product": "ломтик июльского неба",
                "price": 450,
                "quantity": 1
            },
            {
                "product": "билет в Израиль",
                "price": 1000,
                "quantity": 3
            },
            {
                "product": "статуэтка Ленина",
                "price": 200,
                "quantity": 3
            }
        ]
    },
    {
        "order_id": 62239,
        "warehouse_name": "хутор близ Диканьки",
        "highway_cost": -15,
        "products": [
            {
                "product": "билет в Израиль",
                "price": 1000,
                "quantity": 1
            }
        ]
    },
    {
        "order_id": 85794,
        "warehouse_name": "отель Лето",
        "highway_cost": -50,
        "products": [
            {
                "product": "зеленая пластинка",
                "price": 10,
                "quantity": 2
            }
        ]
    },
    {
        "order_id": 33684,
        "warehouse_name": "Мордор",
        "highway_cost": -30,
        "products": [
            {
                "product": "билет в Израиль",
                "price": 1000,
                "quantity": 2
            },
            {
                "product": "зеленая пластинка",
                "price": 10,
                "quantity": 1
            }
        ]
    },
    {
        "order_id": 25824,
        "warehouse_name": "отель Лето",
        "highway_cost": -75,
        "products": [
            {
                "product": "автограф Стаса Барецкого",
                "price": 600,
                "quantity": 1
            },
            {
                "product": "статуэтка Ленина",
                "price": 200,
                "quantity": 1
            },
            {
                "product": "плюмбус",
                "price": 250,
                "quantity": 1
            }
        ]
    },
    {
        "order_id": 87044,
        "warehouse_name": "остров невезения",
        "highway_cost": -15,
        "products": [
            {
                "product": "плюмбус",
                "price": 250,
                "quantity": 3
            }
        ]
    },
    {
        "order_id": 58598,
        "warehouse_name": "гиперборея",
        "highway_cost": -160,
        "products": [
            {
                "product": "плюмбус",
                "price": 250,
                "quantity": 3
            },
            {
                "product": "статуэтка Ленина",
                "price": 200,
                "quantity": 3
            },
            {
                "product": "статуэтка Ленина",
                "price": 200,
                "quantity": 2
            }
        ]
    },
    {
        "order_id": 5430,
        "warehouse_name": "гиперборея",
        "highway_cost": -80,
        "products": [
            {
                "product": "ломтик июльского неба",
                "price": 450,
                "quantity": 1
            },
            {
                "product": "плюмбус",
                "price": 250,
                "quantity": 3
            }
        ]
    },
    {
        "order_id": 60502,
        "warehouse_name": "отель Лето",
        "highway_cost": -75,
        "products": [
            {
                "product": "автограф Стаса Барецкого",
                "price": 600,
                "quantity": 3
            }
        ]
    },
    {
        "order_id": 96473,
        "warehouse_name": "Мордор",
        "highway_cost": -20,
        "products": [
            {
                "product": "зеленая пластинка",
                "price": 10,
                "quantity": 2
            }
        ]
    },
    {
        "order_id": 64013,
        "warehouse_name": "хутор близ Диканьки",
        "highway_cost": -105,
        "products": [
            {
                "product": "плюмбус",
                "price": 250,
                "quantity": 2
            },
            {
                "product": "плюмбус",
                "price": 250,
                "quantity": 2
            },
            {
                "product": "зеленая пластинка",
                "price": 10,
                "quantity": 3
            }
        ]
    },
    {
        "order_id": 59105,
        "warehouse_name": "отель Лето",
        "highway_cost": -25,
        "products": [
            {
                "product": "статуэтка Ленина",
                "price": 200,
                "quantity": 1
            }
        ]
    },
    {
        "order_id": 85535,
        "warehouse_name": "отель Лето",
        "highway_cost": -25,
        "products": [
            {
                "product": "статуэтка Ленина",
                "price": 200,
                "quantity": 1
            }
        ]
    },
    {
        "order_id": 24928,
        "warehouse_name": "хутор близ Диканьки",
        "highway_cost": -60,
        "products": [
            {
                "product": "подписка на suppi-блог",
                "price": 150,
                "quantity": 2
            },
            {
                "product": "статуэтка Ленина",
                "price": 200,
                "quantity": 1
            },
            {
                "product": "статуэтка Ленина",
                "price": 200,
                "quantity": 1
            }
        ]
    },
    {
        "order_id": 2751,
        "warehouse_name": "гиперборея",
        "highway_cost": -80,
        "products": [
            {
                "product": "зеленая пластинка",
                "price": 10,
                "quantity": 3
            },
            {
                "product": "зеленая пластинка",
                "price": 10,
                "quantity": 1
            }
        ]
    },
    {
        "order_id": 35995,
        "warehouse_name": "гиперборея",
        "highway_cost": -20,
        "products": [
            {
                "product": "ломтик июльского неба",
                "price": 450,
                "quantity": 1
            }
        ]
    },
    {
        "order_id": 80252,
        "warehouse_name": "остров невезения",
        "highway_cost": -35,
        "products": [
            {
                "product": "статуэтка Ленина",
                "price": 200,
                "quantity": 3
            },
            {
                "product": "статуэтка Ленина",
                "price": 200,
                "quantity": 2
            },
            {
                "product": "ломтик июльского неба",
                "price": 450,
                "quantity": 2
            }
        ]
    },
    {
        "order_id": 27443,
        "warehouse_name": "Мордор",
        "highway_cost": -10,
        "products": [
            {
                "product": "статуэтка Ленина",
                "price": 200,
                "quantity": 1
            }
        ]
    },
    {
        "order_id": 1391,
        "warehouse_name": "остров невезения",
        "highway_cost": -10,
        "products": [
            {
                "product": "плюмбус",
                "price": 250,
                "quantity": 2
            }
        ]
    },
    {
        "order_id": 83474,
        "warehouse_name": "хутор близ Диканьки",
        "highway_cost": -75,
        "products": [
            {
                "product": "плюмбус",
                "price": 250,
                "quantity": 2
            },
            {
                "product": "ломтик июльского неба",
                "price": 450,
                "quantity": 3
            }
        ]
    },
    {
        "order_id": 84471,
        "warehouse_name": "хутор близ Диканьки",
        "highway_cost": -60,
        "products": [
            {
                "product": "плюмбус",
                "price": 250,
                "quantity": 1
            },
            {
                "product": "ломтик июльского неба",
                "price": 450,
                "quantity": 1
            },
            {
                "product": "подписка на suppi-блог",
                "price": 150,
                "quantity": 2
            }
        ]
    },
    {
        "order_id": 96799,
        "warehouse_name": "остров невезения",
        "highway_cost": -10,
        "products": [
            {
                "product": "ломтик июльского неба",
                "price": 450,
                "quantity": 2
            }
        ]
    },
    {
        "order_id": 99324,
        "warehouse_name": "остров невезения",
        "highway_cost": -10,
        "products": [
            {
                "product": "автограф Стаса Барецкого",
                "price": 600,
                "quantity": 1
            },
            {
                "product": "билет в Израиль",
                "price": 1000,
                "quantity": 1
            }
        ]
    }
]


def sum_of_prices(data):
    """
    Calculate the sum of prices for each "warehouse_name".
    :param data:
    :return:
    """
    sum_of_prices_of_warehouse = {}

    for order in data:
        sum_price = 0
        warehouse_name = order["warehouse_name"]
        for product in order["products"]:
            price = product["price"]
            sum_price += price
            sum_of_prices_of_warehouse[warehouse_name] = \
                sum_of_prices_of_warehouse.get(warehouse_name, 0) + price

    return sum_of_prices_of_warehouse


def sum_of_quantity(data):
    """
    Calculate the sum of quantity for each "warehouse_name"
    :param data:
    :return:
    """
    sum_of_quantity_of_warehouse = {}

    for order in data:
        sum_quantity = 0
        warehouse_name = order["warehouse_name"]
        for product in order["products"]:
            quantity = product["quantity"]
            sum_quantity += quantity
            sum_of_quantity_of_warehouse[warehouse_name] = \
                sum_of_quantity_of_warehouse.get(warehouse_name, 0) + quantity

    return sum_of_quantity_of_warehouse


def tariff_price(sum_of_prices_of_warehouse, sum_of_quantity_of_warehouse):
    """
    Calculate the tariff cost of each "warehouse"
    :param sum_of_prices_of_warehouse:
    :param sum_of_quantity_of_warehouse:
    :return:
    """
    tariff_price_every_warehouse = {key: sum_of_prices_of_warehouse[key] / sum_of_quantity_of_warehouse[key]
                                    for key in sum_of_prices_of_warehouse}
    return tariff_price_every_warehouse


def create_table_for_statistic(data):
    product_data = []

    for order in data:
        order_id = order['order_id']
        warehouse_name = order['warehouse_name']
        highway_cost = order['highway_cost']

        for product_info in order['products']:
            product_name = product_info['product']
            price = product_info['price']
            quantity = product_info['quantity']
            income = price * quantity
            expenses = highway_cost * quantity
            profit = income - expenses

            product_data.append({
                'order_id': order_id,
                'warehouse_name': warehouse_name,
                'product': product_name,
                'quantity': quantity,
                'income': income,
                'expenses': expenses,
                'profit': profit
            })

    product_profit_df = pd.DataFrame(product_data)

    # Group by 'product' and calculate total quantity, income, expenses, and profit for each product
    product_profit_summary = product_profit_df.groupby('product').agg(
        quantity=('quantity', 'sum'),
        income=('income', 'sum'),
        expenses=('expenses', 'sum'),
        profit=('profit', 'sum')
    ).reset_index()

    return product_profit_summary


def create_order_id_table(data):
    """
    Create table with columns "income", "expenses", "profit" using "order_id" for grouping.
    :param data:
    :return:
    """
    order_profit_data = []

    for order in data:
        order_id = order['order_id']
        total_profit = sum(item['price'] * item['quantity'] for item in order['products'])
        order_profit_data.append({'order_id': order_id, 'order_profit': total_profit})

    result_order_profit_df = pd.DataFrame(order_profit_data)

    result_average_profit = result_order_profit_df['order_profit'].mean()

    return result_order_profit_df, result_average_profit


def percent_gain_product_of_warehouse(data, tariff_of_warehouse):
    """
    Create table for "percent_profit_product_of_warehouse" column using "warehouse_name" for grouping.
    Percentage of the profit of a product ordered from a certain warehouse to the profit of this warehouse.
    :param data:
    :param tariff_of_warehouse:
    :return:
    """
    product_details = []

    for order in data:
        order_id = order["order_id"]
        warehouse_name = order["warehouse_name"]
        for product in order["products"]:
            product_details.append({
                "order_id": order_id,
                "warehouse_name": warehouse_name,
                "product": product["product"],
                "price": product["price"],
                "quantity": product["quantity"]
            })

    df = pd.DataFrame(product_details)

    # Calculate the income for each product (selling price * quantity)
    df['income'] = df['price'] * df['quantity']

    # Remove the 'warehouse_name' column before calculating expenses
    df['expenses'] = df['warehouse_name'].map(tariff_of_warehouse) * df['quantity']

    # Calculate the total profit (income - expenses) for each product
    df['profit'] = df['income'] - df['expenses']

    # Group the data by 'warehouse_name' and 'product' to calculate total quantity and total profit for each combination
    warehouse_product = df.groupby(['warehouse_name', 'product']).agg({
        'quantity': 'sum',
        'profit': 'sum'
    }).reset_index()

    # Calculate the total profit for each warehouse
    warehouse_profit = df.groupby('warehouse_name')['profit'].sum().reset_index()
    warehouse_profit.rename(columns={'profit': 'sum_profit_of_warehouse'}, inplace=True)

    # Merge the warehouse_product and warehouse_profit DataFrames
    result = warehouse_product.merge(warehouse_profit, on='warehouse_name')

    # Calculate the percent profit of each product in the warehouse
    result['accumulated_percent_profit_product_of_warehouse'] = \
        (result['profit'] / result['sum_profit_of_warehouse']) * 100

    return result


def accumulated_percent_product_of_warehouse(data, tariff_of_warehouse):
    """
    Create the table for "accumulated_percent_profit_product_of_warehouse" column using "profit" of each
    "warehouse_name" for grouping.
    This is the ever-increasing sum of the sorted descending column.
    :param data:
    :param tariff_of_warehouse:
    :return:
    """
    product_details = []

    for order in data:
        order_id = order["order_id"]
        warehouse_name = order["warehouse_name"]
        for product in order["products"]:
            product_details.append({
                "order_id": order_id,
                "warehouse_name": warehouse_name,
                "product": product["product"],
                "price": product["price"],
                "quantity": product["quantity"]
            })

    df = pd.DataFrame(product_details)

    # Calculate the income for each product (selling price * quantity)
    df['income'] = df['price'] * df['quantity']

    # Remove the 'warehouse_name' column before calculating expenses
    df['expenses'] = df['warehouse_name'].map(tariff_of_warehouse) * df['quantity']

    # Calculate the total profit (income - expenses) for each product
    df['profit'] = df['income'] - df['expenses']

    # Group the data by 'warehouse_name' and 'product' to calculate total quantity and total profit for each combination
    warehouse_product = df.groupby(['warehouse_name', 'product']).agg({
        'quantity': 'sum',
        'profit': 'sum'
    }).reset_index()

    # Calculate the total profit for each warehouse
    warehouse_profit = df.groupby('warehouse_name')['profit'].sum().reset_index()
    warehouse_profit.rename(columns={'profit': 'sum_profit_of_warehouse'}, inplace=True)

    # Merge the warehouse_product and warehouse_profit DataFrames
    result = warehouse_product.merge(warehouse_profit, on='warehouse_name')

    # Calculate the percent profit of each product in the warehouse
    result['accumulated_percent_profit_product_of_warehouse'] = \
        (result['profit'] / result['sum_profit_of_warehouse']) * 100

    # NEW CODE
    # Calculate the percent profit of each product in the warehouse
    result['percent_profit_product_of_warehouse'] = (result['profit'] / result['sum_profit_of_warehouse']) * 100

    # Sort the DataFrame by 'percent_profit_product_of_warehouse' in descending order
    result.sort_values(by='percent_profit_product_of_warehouse', ascending=False, inplace=True)

    # Calculate the accumulated percentage using cumulative sum
    result['accumulated_percent_profit_product_of_warehouse'] = \
        result['percent_profit_product_of_warehouse'].cumsum() / 10

    return result['accumulated_percent_profit_product_of_warehouse']


def accumulated_percent_scores(data, tariff_of_warehouse):
    """
    Create the table for "accumulated_percent_profit_product_of_warehouse" column using "profit" of each
    "warehouse_name" for grouping.
    This function scoring A, B or C to every "warehouse" using his accrued percents.
    "A" if percent <= 70
    "B" if percent 70 <= 90
    "C" if percent <= 70
    :param data:
    :param tariff_of_warehouse:
    :return:
    """
    product_details = []

    for order in data:
        order_id = order["order_id"]
        warehouse_name = order["warehouse_name"]
        for product in order["products"]:
            product_details.append({
                "order_id": order_id,
                "warehouse_name": warehouse_name,
                "product": product["product"],
                "price": product["price"],
                "quantity": product["quantity"]
            })

    df = pd.DataFrame(product_details)

    # Calculate the income for each product (selling price * quantity)
    df['income'] = df['price'] * df['quantity']

    # Remove the 'warehouse_name' column before calculating expenses
    df['expenses'] = df['warehouse_name'].map(tariff_of_warehouse) * df['quantity']

    # Calculate the total profit (income - expenses) for each product
    df['profit'] = df['income'] - df['expenses']

    # Group the data by 'warehouse_name' and 'product' to calculate total quantity and total profit for each combination
    warehouse_product = df.groupby(['warehouse_name', 'product']).agg({
        'quantity': 'sum',
        'profit': 'sum'
    }).reset_index()

    # Calculate the total profit for each warehouse
    warehouse_profit = df.groupby('warehouse_name')['profit'].sum().reset_index()
    warehouse_profit.rename(columns={'profit': 'sum_profit_of_warehouse'}, inplace=True)

    # Merge the warehouse_product and warehouse_profit DataFrames
    result = warehouse_product.merge(warehouse_profit, on='warehouse_name')

    # NEW CODE
    # Calculate the percent profit of each product in the warehouse
    result['percent_profit_product_of_warehouse'] = (result['profit'] / result['sum_profit_of_warehouse']) * 100

    # Sort the DataFrame by 'percent_profit_product_of_warehouse' in descending order
    result.sort_values(by='percent_profit_product_of_warehouse', ascending=False, inplace=True)

    # Calculate the accumulated percentage using cumulative sum
    result['accumulated_percent_profit_product_of_warehouse'] = result['percent_profit_product_of_warehouse'].cumsum()

    # Assign categories A, B, and C based on the value of the 'accumulated_percent_profit_product_of_warehouse'
    def assign_category(accumulated_percent):
        if accumulated_percent <= 70:
            return 'A'
        elif accumulated_percent <= 90:
            return 'B'
        else:
            return 'C'

    #  It calculates the category for each product based on the given conditions specified in the assign_category
    #  function and assigns the corresponding category to the 'category' column in the DataFrame
    result['category'] = result['accumulated_percent_profit_product_of_warehouse'].apply(assign_category)

    return result


sum_of_prices_every_warehouses = sum_of_prices(data=data)
sum_of_quantity_every_warehouses = sum_of_quantity(data=data)
print('------------------ TASK 1 ------------------\n')
sum_of_tariff = tariff_price(sum_of_prices_every_warehouses, sum_of_quantity_every_warehouses)
print(sum_of_tariff, '\n')

print('------------------ TASK 2 ------------------\n')
create_statistics_tabel = create_table_for_statistic(data)
print("Table with columns 'product', 'quantity', 'income', 'expenses', 'profit': ")
print(create_statistics_tabel, '\n')

print('------------------ TASK 3 ------------------\n')
order_profit_df, average_profit = create_order_id_table(data)
print("Table with columns 'order_id' and 'order_profit':")
print(order_profit_df)
print("\nAverage profit of orders:", average_profit, '\n')

print('------------------ TASK 4 ------------------\n')
gain_products = percent_gain_product_of_warehouse(data, sum_of_tariff)
print(gain_products, '\n')

print('------------------ TASK 5 ------------------\n')
accumulated_percent = accumulated_percent_product_of_warehouse(data, sum_of_tariff)
print(accumulated_percent, '\n')

print('------------------ TASK 6 ------------------\n')
score = accumulated_percent_scores(data, sum_of_tariff)
print(score, '\n')
