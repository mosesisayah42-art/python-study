import psycopg2

conn = psycopg2.connect(host='localhost',port=5432,user='postgres',password='MOLLY',dbname='myduka_db')

cur=conn.cursor()
def get_products():
    cur.execute("select * from products")
    products_data = cur.fetchall()
    return products_data

    products_data=get_products
    print(products_data)

def insert_products():
    cur.execute("insert into products (name, buying_price , selling_price ) values('earphones',100,300)")
    conn.commit()

insert_products()

products_data=get_products()
print(products_data)

def get_sales():
    cur.execute("select * from sales")
    sales_data = cur.fetchall()
    return sales_data

    sales_data=get_sales
    print(sales_data)



def insert_products(prod_details):
    cur.execute("insert into products (name, buying_price , selling_price ) values(s%,s%,s%)",prod_details)
    conn.commit()


product1=('phone',200,300)
product1=('pods',100,150)


products_data=get_products()
print(products_data)








