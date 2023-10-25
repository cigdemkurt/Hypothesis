import scipy.stats as stats

# Örneklem verileri (ürün ağırlıkları)
pro_weight = [12.5, 17.1, 19.0, 12.5, 13.1, 12.2, 10.3, 14.9, 13.0, 11.6]


#standard_weight = 23.0  (population parameter)

# single sample T test
stats.ttest_1samp(pro_weight, popmean= 23.0)
#the p value is compared with the alpha level
alpha = 0.05

if p_value < alpha:
    print("The average weight of the products produced on the production line is not the same as the specific standard weight.")
else:
    print("The average weight of the products produced on the production line is the same as the specific standard weight.")