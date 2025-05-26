import pandas as pd

def main():
    print("Supermarket Analysis!\n\n")
    sales = pd.read_csv("sales.csv")

    print(sales[200:211])
    males = sales[sales['Gender'] == 'Male']

    print(males)

    total_gt_100 = sales[sales['Total'] > 100]
    print(total_gt_100.head(10))

# Get the Total by City
    payment_groups = sales.groupby(["City"])[["Total"]].sum().reset_index()

    print(payment_groups)

# Sales > 100 for New York
    new_york_sales_100 = sales[(sales['Total'] > 100) & (sales['City'] == "NewYork")]
    print(new_york_sales_100)

# Alternative (uncomment to see it work)
    # print(sales.query('Total>100 & City=="NewYork"'))

# .agg() is a great feature of Pandas as it can add it multiple indicates (mean, min) and you can even include your own
    print(sales['Total'].agg(['mean', 'min', 'max', 'argmax']))


if __name__ == "__main__":
    main()
