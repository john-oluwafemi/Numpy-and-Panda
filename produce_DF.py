produce_dictionary = {'Potatoes': [0.86, 12219, 10508],
                      'Okra': [2.26, 12960, 29290],
                      'Fava beans': [2.69, 11703, 31480],
                      'Watermelon': [0.66, 11485, 7580],
                      'Garlic': [1.19, 12512, 14889],
                      'Parsnips': [2.27, 11270, 25584],
                      'Asparagus': [2.49, 12848, 31991],
                      'Avocados': [3.23, 12369, 39953],
                      'Celery': [3.07, 12334, 37866],
                      'Spinach': [4.12, 11740, 48367],
                      'Cucumber': [1.07, 11994, 12834],
                      'Apricots': [3.71, 11762, 43637],
                      'Ginger': [5.13, 11915, 61126],
                      'Corn': [1.07, 11702, 12522],
                      'Grapefruit': [0.76, 11707, 8897],
                      'Eggplant': [2.32, 11843, 27477],
                      'Green cabbage': [0.8, 11611, 9289],
                      'Yellow peppers': [2.87, 12160, 34899],
                      'Grapes': [2.63, 12294, 32333],
                      'Cherries': [9.5, 12384, 117653],
                      'Apples': [1.88, 12397, 23307],
                      'Green beans': [2.52, 11483, 28938],
                      'Tomatoes': [3.16, 12016, 37969],
                      'Red onion': [0.78, 12549, 9788],
                      'Strawberries': [4.4, 11692, 51446],
                      'Papaya': [1.34, 11775, 15779],
                      'Butternut squash': [1.28, 11495, 14713],
                      'Bananas': [0.86, 12629, 10861],
                      'Lettuce': [1.88, 11891, 22355],
                      'Carrots': [1.26, 12204, 15377],
                      'Daikon': [1.4, 12146, 17004],
                      'Lime': [1.06, 11934, 12650],
                      'Green peppers': [1.89, 11981, 22645],
                      'Beets': [1.51, 12255, 18506],
                      'Coconuts': [1.18, 11840, 13972],
                      'Orange': [1.09, 11180, 12187],
                      'Lemon': [1.29, 12382, 15974],
                      'Brussels sprouts': [1.65, 11947, 19713],
                      'Kale': [5.02, 12293, 61711],
                      'Bok choy': [1.42, 11565, 16422]}

#Create a DataFrame from the above dictionary and answer the questions below using pandas dataframe methods

import pandas as pd

columns = ['Price', 'Quantity', 'Total Price']

produce_df = pd.DataFrame(produce_dictionary, index=columns).T

print()
print(produce_df)


print()
print("Question 1: Produce that had the highest and lowest sales in total sales (both name of produce and value)")
print()

print(produce_df.loc[produce_df['Total Price'].idxmax()].name, produce_df['Total Price'].max())
print()
print(produce_df.loc[produce_df['Total Price'].idxmin()].name, produce_df['Total Price'].min())


print()
print("Question 2: Using 'loc', display the quantity and total sales for 'Orange' and 'Beets' (together)")
print()

print(produce_df.loc[['Orange', 'Beets'], ['Quantity', 'Total Price']])
print()


print()
print("Question 3: Using 'loc', display the total sales for 'Apples' through 'Lettuce'")
print()

print(produce_df.loc['Apples':'Lettuce', 'Total Price'])
print()


print()
print("Question 4: Using 'at', update the quantity sold for Apricots to 11,955 and total sales to 44,353.05")
print()

produce_df.at['Apricots', 'Quantity'] = 11955
produce_df.at['Apricots', 'Total Price'] = 44353.05
print(produce_df.loc['Apricots'])
print()

print()
print("Question 5: What is the average quantity sold across all products? print out only quantity sold")
print()

print(produce_df['Quantity'].mean())
print()

print()
print("Question 6: Create a new dataframe for only those produce that have sold \
between 11,500 to 12,000 (quantity)")
print()

produce_df1 = produce_df[(produce_df['Quantity'] >= 11500) & (produce_df['Quantity'] <= 12000)]
print(produce_df1)
print()

print()
print("Question 7: What is the total sales for the products in the above new \
dataframe? (print out ONLY total sales, not cost per pound or quantity sold)")
print()

print(produce_df1['Total Price'].sum())
print()
