#A bag contains 5 red balls and 3 blue balls.

#Find probability of not selecting a red ball.

# balls 
red_balls = 5
blue_balls = 3

p_off_red = red_balls/(red_balls+blue_balls)
p_off_not_red = blue_balls / (red_balls+blue_balls)

print("Probability of Not Red : ",p_off_not_red)