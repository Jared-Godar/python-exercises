# Define movies as list of tuples (name, days)
movies = [('Little Mermaid',3), ('Brother Bear', 5), ('Hercules', 1)]



print('Total movie cost: ' + str((movies[0][1] + movies[1][1] + movies[2][1])*3))

# Could also use dictionary
########
# Example from Ryan on Slack
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
# A list of dictionaries approach to the contractor exercise from https://ds.codeup.com/python/data-types-and-variables/

# Setup a list of dictionaries
# Each dictionary contains the client, rate, and amount of consulting hours
clients = [
    {
        "client": "Google",
        "rate": 400,
        "hours": 6,
    },
    {
        "client": "Amazon",
        "rate": 380,
        "hours": 4,
    },
    {
        "client": "Facebook",
        "rate": 350,
        "hours": 10,
    }
]

# programmatically determine the number of clients (the number of dictionaries on the list)
number_of_clients = len(clients)

# Set hours and compensation to zero
total_hours = 0
total_compensation = 0

# Iterate through each client
for client in clients:
    # Increase total_hours worked by the hours for each client
    total_hours += client["hours"]

    # calculate the rate * hours for each client
    client_subtotal = client["rate"] * client["hours"]

    print(f"After working {client['hours']} for {client['client']} at a rate of ${client['rate']} per hour, I earned ${client_subtotal}.")

    # update that subtotal to the total_compensation variable
    total_compensation += client_subtotal


print("---")
print(f"After working a grand total of {total_hours} for {number_of_clients} clients, I now have to pay taxes on ${total_compensation}.")




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

