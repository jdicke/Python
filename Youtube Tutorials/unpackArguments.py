def health_calculator(age, apples_ate, cigs_smoked):
    answer = (100-age) + (apples_ate * 3.5) - (cigs_smoked * 2)
    print(answer)

bucks_data = [27, 20, 0]

health_calculator(bucks_data[0], bucks_data[1], bucks_data[2])
health_calculator(*bucks_data) #This is unpacking an argument list and passes each item in one at a time


