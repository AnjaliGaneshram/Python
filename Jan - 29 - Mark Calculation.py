print("All marks should be within 200")
physics_1 = int(input("Enter your Physics score: "))
chemistry_1 = int(input("Enter your Chemistry score: "))
maths_1 = int(input("Enter your Maths score: "))
aggregate_1 = int (physics_1/4 + chemistry_1/4 + maths_1/2)
if physics_1 < 70 or chemistry_1 < 70 or maths_1 < 70:
      print("Your score is less than 70 so the result is fail")
elif physics_1 > 200 or chemistry_1 > 200 or maths_1 > 200:
        print("You have entered invalid score")
elif physics_1 > 70 and chemistry_1 > 70 and maths_1 > 70:
      print ("Pass")
      if aggregate_1 >= 190:
            print("First Class")
      elif aggregate_1 >150 and aggregate_1 < 190:
            print("Second Class")
      elif aggregate_1 >=70 and aggregate_1 <150:
            print ("Third Class")
      else:
            print("Fail Try again")

print(aggregate_1)
''' This is program is to calculate the aggregate for the given 3 marks and identify the class the marks are belongs to and also the mark should be fit within certain criterias like the mark should be above 70 and below 200.'''
    



    
