import csv
import pandas as pd
import matplotlib.pyplot as plt
list_of_sales=[]
list_of_profits=[]
list_of_expenditure=[]
list_of_months=[]
dict_profits={}
dict_sales={}
def read_csvfile():
    with open('saless.csv','r') as file:
        spreadsheet=csv.DictReader(file)
        for row in spreadsheet:
            if 'sales' in row:
              sale=int(row['sales'])
              list_of_sales.append(sale)
    with open('saless.csv','r') as file:
        spreadsheet=csv.DictReader(file)
        for row in spreadsheet:
            if 'expenditure' in row:
              exp=int(row['expenditure'])
              list_of_expenditure.append(exp)          
    return list_of_sales,list_of_expenditure  


def profit_function():
    with open('saless.csv','r') as file:
        spreadsheet=csv.DictReader(file)              
        for row in spreadsheet:
            profit=float(row['sales'])-float(row['expenditure'])
            list_of_profits.append(profit)
            
    with open('saless.csv','r') as file:
        spreadsheet=csv.DictReader(file)           
        for row in spreadsheet:
           month=row['month']
           list_of_months.append(month) 
    return list_of_months,list_of_profits    


def dict_of_profit_function(months,profits):
    dict_profits=dict(zip(months,profits))
    return dict_profits

def profit_percentage(profits,sales):
    percentage_list=[]
    for profit,sale in zip(profits,sales):
        percentage=(profit/sale)*100
        percentage_list.append(percentage)
    print("-------Monthly profit percentage-------")    
    for i,percentage in enumerate(percentage_list):
        print(f"Month {i+1} profit percentage is {percentage:.2f}%")    

    


def plot(sales,profits,expenditure,months):
    x1=months
    y1=sales
    plt.plot(x1,y1,label='Sales',linestyle='dashed',color='blue',marker='o',markerfacecolor='green',markersize=5)


    x2=months
    y2=expenditure
    plt.plot(x2,y2,label='expenditure',color='orange',marker='o',markerfacecolor='darkblue',markersize=5)



    losses = [-profit if profit < 0 else 0 for profit in profits]
    adjusted_profits = [max(0, profit) for profit in profits]

    x3=months
    y3=adjusted_profits
    plt.bar(x3,y3,label='profits',width=0.8,color='green')

    x4=months
    y4=losses
    plt.bar(x4,y4,label='losses',width=0.8,color='red')
      

    plt.xlabel('Months')
    plt.ylabel('Profits and Sales')
    plt.title('YEAR-2018')
    plt.legend()
    plt.grid()
    plt.show()
    

def run():
    existing_data = pd.read_csv('saless.csv')
    print(existing_data)
    print("\n")


    list_of_sales,list_of_expenditure=read_csvfile()
    total_sales=sum(list_of_sales)
    total_expenditure=sum(list_of_expenditure)
    print("The total sales of the year is :{}".format(total_sales)) 
    print("The total expenditure of the year is :{}".format(total_expenditure)) 
    print("\n")

    
    


    months_list,profit_list=profit_function()
    dict_profits=dict_of_profit_function(months_list,profit_list)
    print("Profits of the year in each month are:\n{}".format(dict_profits))
    print("\n\n")

    dict_sales=dict_of_profit_function(months_list,list_of_sales)
    max_sale_month=max(dict_sales,key=dict_sales.get)
    min_sale_month=min(dict_sales,key=dict_sales.get)


    Max_sale=max(list_of_sales)
    Min_sale=min(list_of_sales)
    average=total_sales//len(list_of_sales)
    print("Maximum sales occured in the year are {} and in the month {}".format(Max_sale,max_sale_month))
    print("Minimum sales occured in the year are {} and in the month {}".format(Min_sale,min_sale_month))
    print("Average sales of the year 2018 are {}".format(average))
    print("\n")


    

    existing_data['Profit'] =profit_list
    existing_data.to_csv('saless.csv', index=False)
    print(existing_data)
    
    max_profit_month=max(dict_profits,key=dict_profits.get)
    print("Maximum profits occured in the month of {} and they are {}".format(max_profit_month,dict_profits[max_profit_month]))

    profit_percentage(profit_list,list_of_sales)
    plot(list_of_sales,profit_list,list_of_expenditure,months_list)



run()

