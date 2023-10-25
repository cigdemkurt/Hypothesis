
import scipy.stats as stats

#before the advertising campaign
monthly_sales1 = [1250, 1400, 1350, 1550, 1600, 1450, 1525, 1575, 1620, 1680, 1700, 1800]

#after the advertising campaign
monthly_sales2= [3000,3750,4700,3900,7952,5856,4752,3992,3987,5776,6500]


t_stats, p_value = stats.ttest_ind(monthly_sales1,monthly_sales2)

alpha = 0.05

if p_value < alpha:
    print("The hypothesis that advertising increases sales is accepted. There is a significant Deciency between the two groups.")
else:
    print("The hypothesis that advertising increases sales is rejected. There is no significant Deciency between the two groups.")
