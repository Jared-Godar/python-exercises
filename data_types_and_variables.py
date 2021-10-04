# Define movies as list of tuples (name, days)
movies = [('Little Mermaid',3), ('Brother Bear', 5), ('Hercules', 1)]



print('Total movie cost: ' + str((movies[0][1] + movies[1][1] + movies[2][1])*3))

# Could also use dictionary
########

#Define work week as list of tuples (company, rate, hours)
work_week = [('Google', 400, 10),('Amazon', 380, 6), ('Facebook', 350,4)]

pay = (work_week[0][1]*work_week[0][2]) + (work_week[1][1]*work_week[1][2]) + (work_week[2][1]*work_week[2][2])
print(pay)

#Alternate

rate = []
for index in 0, 1, 2:
    rate.append(work_week[index][1]) #[400,380,350]

hours = []
for index in 0, 1, 2:
    hours.append(work_week[index][2]) #[10,6,4]

pay = [rate * hours for rate, hours in zip(rate, hours)] #[4000, 2280, 1400]

total_pay = sum(pay) #[7680]

#############
# Conditions should return true for take class only when the class isn't full and there's no scheduling conflict

class_full = False
schedule_conflict = False

take_class = (not class_full) and (not schedule_conflict)

################
# Product offer should return true when the offer is not expired and the customer buys over two items


########

username = 'codeup'
password = 'notastrongpassword'

#Boolean check if password over 5 chars
is5 = len(password)>=5

#Boolean check user under 20
u20 = len(username)<=20

#Boolean user and password not same

same = password == username
not_same = password != username

# Bonus neither the username or password can start or end with whitespace

no_white = password[0] != ' ' and password[-1] != ' ' and username[0] != ' ' and username[-1] != ' '

