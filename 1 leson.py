recidence_limit = 90
shengen_constrain= 180
recidenceCost =15


first_time_arriving = 5
first_time_leave = 17

secondTimeArive=25
secondTimeLeave = 50

thirdTimeArive = 75
thirdTimeLeave = 150
total_time_in_es=(first_time_leave-first_time_arriving+1)+\
(secondTimeLeave-secondTimeArive+1)+\
(thirdTimeLeave-thirdTimeArive+1)


totalCost = total_time_in_es*recidenceCost;
print('Days in ES',total_time_in_es)
print('Cost of trip',totalCost," 'Euros'")

if total_time_in_es<recidence_limit:
  print("You still have",recidence_limit-total_time_in_es," days")
else:
  print("GO HOME");