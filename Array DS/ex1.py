""" expenses = [
    {'January': 2200},
    {'February': 2350},
    {'March': 2600},
    {'April': 2130},
    {'May': 2190},
]
print('1. In Feb, how many dollars you spent extra compare to January? ${difference} difference between January and February'.format(
    difference=expenses[1]['February'] - expenses[0]['January']))

print('2. Find out your total expense in first quarter(first three months) of the year. {total}'.format(
    total=expenses[0]['January'] + expenses[1]['February'] + expenses[2]['March']))

print('3. Find out if you spent exactly 2000 dollars in any month')
for x in expenses:
    for i in x:
        print(i)
 """

expenses = [2200, 2350, 2600, 2130, 2190]
# 1. In Feb, how many dollars you spent extra compare to January?
sol1 = expenses[1] - expenses[0]
print(sol1)

# 2. Find out your total expense in first quarter (first three months) of the year.
threeQuarter = expenses[0] + expenses[1] + expenses[2]
print(threeQuarter)

# 3. Find out if you spent exactly 2000 dollars in any month
exact = True
for x in range(len(expenses)):
    # print(x)
    if expenses[x] == 2000:
        exact = True
    else:
        exact = False
print(exact)

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expenses.append(1980)
totalExpenses = 0
# for x in expenses:
#     totalExpenses += x
# print(totalExpenses)

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
expenses[3] = expenses[3] - 200
print(expenses)
# for x in expenses:
#     totalExpenses += x
# print(totalExpenses)
