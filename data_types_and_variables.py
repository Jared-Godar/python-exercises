# Define movies as list of tuples (name, days)
movies = [('Little Mermaid',3), ('Brother Bear', 5), ('Hercules', 1)]

print('Total movie cost: ' + str((movies[0][1] + movies[1][1] + movies[2][1])*3))

########

#Define work week as list of tuples (company, rate, hours)
work_week = [('Google', 400, 10),('Amazon', 380, 6), ('Facebook', 350,4)]

pay = (work_week[0][1]*work_week[0][2]) + (work_week[1][1]*work_week[1][2]) + (work_week[2][1]*work_week[2][2])
print(pay)

#############

class_full = False
schedule_conflict = False

take_class = (not class_full) and (not schedule_conflict)

################

items_bought = 5
offer_expired = False

product_offer = (items_bought > 2) and not offer_expired