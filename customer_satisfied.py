import scipy.stats as stats

   
customer_satisfaction= []

for i in range(15):
    while True:
        try:
        value = int(input("enter a number between 0 and 20 (-1 to exit): "))
            if value == -1:
                break
            if 0 <= value <= 20:
            customer_satisfaction.append(value)  # add numbers between 0 and 20 to the list
            else:
                print("Invalid value, please enter a value between 0 and 20. Dec.")
        except ValueError:
            print("Invalid entry, please enter an integer.")
        
        
standart_number=16.0

stats.ttest_1samp(customer_satisfaction, popmean = 16.0)

alpha = 16.0

if pvalue < alpha:
    print("customers are not satisfied")
else:
    print("customers are satisfied")