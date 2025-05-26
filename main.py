import pandas as pd

def main():
    print("Hello from supermarket!")
    sales = pd.read_csv("sales.csv")

    print(sales[200:211])
    males = sales[sales['Gender'] == 'Male']

    print(males)

    total_gt_100 = sales[sales['Total'] > 100]
    print(total_gt_100.head(10))

    payment_groups = sales.groupby(["Gender", "Payment"])[["Total"]].sum().reset_index()

    print(payment_groups)

    new_york_sales_100 = sales[(sales['Total'] > 100) & (sales['City'] == "NewYork")]
    print(new_york_sales_100)

    print(sales['Total'].agg(['mean', 'min', 'max', 'argmax']))
    # print(sales.query('City=="NewYork"'))
    print(sales.iloc[47])
    
if __name__ == "__main__":
    main()
