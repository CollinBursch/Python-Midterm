import csv


"""

Customer.csv:

ID,FirstName,LastName,City,Country,Phone
1,Maria,Anders,Berlin,Germany,030-0074321
2,Ana,Trujillo,Mexico D.F.,Mexico,(5) 555-4729
3,Antonio,Moreno,Mexico D.F.,Mexico,(5) 555-3932
4,Thomas,Hardy,London,UK,(171) 555-7788
5,Christina,Berglund,Luleå,Sweden,0921-12 34 65
"""

def main():
    customer_infile = open('customers.csv', 'r') # Reading customer.csv file
    csv_reader = csv.reader(customer_infile)

    customer_country_outfile = open('customer_country.csv', 'w', newline='') #create new file 'custoemr_country.csv'
    csv_writer = csv.writer(customer_country_outfile)
    
    for line in csv_reader:
        customer = [line[0], line[1], line[2], line[4]]
        csv_writer.writerow(customer)

    customer_infile.close()

main()