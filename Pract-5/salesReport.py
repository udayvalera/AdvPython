import pandas as pd
import csv
import os

def read_csv_files():
    getcwd = os.getcwd()
    data = pd.DataFrame()
    product_names = pd.DataFrame()

    for root, dirs, files in os.walk(getcwd):
        for file in files:
            if file.endswith('.csv') and file != 'sales_summary.csv':
                file_path = os.path.join(root, file)
                if file != 'product_names.csv':
                    each_file = pd.read_csv(file_path)
                    data = pd.concat([data, each_file], axis=0, ignore_index=True)
                else:
                    product_names = pd.read_csv(file_path)
    return data, product_names

def calculate_total_sales(data):
    prod_ids = data['Product ID'].unique()
    total_sales = {}
    for prod_id in prod_ids:
        total_sales[str(prod_id)] = int(data[data['Product ID'] == prod_id]['Quantity Sold'].sum())
    sorted_sales = sorted(total_sales.items(), key=lambda x: x[1], reverse=True)
    return sorted_sales

def write_sales_summary(sorted_sales, product_names):
    with open('sales_summary.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Product Name', 'Product ID', 'Total Sales', 'Average Quantity Sold Per Month'])
        for i in sorted_sales:
            csv_writer.writerow([product_names[product_names['Product ID'] == int(i[0])]['Product Name'].values[0], i[0], i[1], i[1]//12])

def main():
    data, product_names = read_csv_files()
    sorted_sales = calculate_total_sales(data)
    write_sales_summary(sorted_sales, product_names)

    while True:
        print('1. View Sales Summary')
        print('2. View Top 5 Products')
        print('3. Exit')
        choice = input('Enter your choice: ')
        if choice == '1':
            print(pd.read_csv('sales_summary.csv'))
            print('-' * 100)
        elif choice == '2':
            print(pd.read_csv('sales_summary.csv').head())
            print('-' * 80)
        elif choice == '3':
            break
        else:
            print('Invalid choice. Please try again.')
            print('-' * 80)

if __name__ == '__main__':
    main()