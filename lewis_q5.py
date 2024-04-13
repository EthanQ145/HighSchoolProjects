import math

top_left = 7
top_left_2 = -6
top_left_3 = 5
top_right = 6
top_right_2 = 1
top_right_3 = 3
bottom = -10
bottom_2 = 1
bottom_3 = 0
direction = 7
direction_2 = 20
direction_3 = -1

top_left_vect = [top_left, top_left_2, top_left_3]
top_right_vect = [top_right - top_left, top_right_2 - top_left_2, top_right_3 - top_left_3]
bottom_vect = [bottom, bottom_2, bottom_3]
bottom_direction = [direction, direction_2, direction_3]

print(top_left_vect, top_right_vect, bottom_vect, bottom_direction)
co_eff = top_right_vect[2]/top_right_vect[0]
i = 0
top_left_vect[i] *= co_eff
top_right_vect[i] *= co_eff
bottom_vect[i] *= co_eff
bottom_direction[i] *= co_eff

print(top_left_vect, top_right_vect, bottom_vect, bottom_direction)

q = (top_left_vect[0] - top_left_vect[1] - bottom_vect[0] + bottom_vect[1])/(bottom_direction[0] - bottom_direction[1])

t = (bottom_vect[1] + q * bottom_direction[1] - top_left_vect[1])/top_right_vect[1]

print(t, q)
print(7 - 1 * t - (-10 + 7*q))
print(-6 + 7 * t - (1 + 20*q))
print(5 - 2*t - (0 - q))
point_coord = [top_left_vect[i]/co_eff + t * top_right_vect[i]/co_eff,
               top_left_vect[1] + t * top_right_vect[1],
               top_left_vect[2] + t * top_right_vect[2]]
print(point_coord)
first = point_coord[0] - top_left_vect[0]/co_eff
second = point_coord[1] - top_left_vect[1]
third = point_coord[2] - top_left_vect[2]
first_2 = q * bottom_direction[0]/co_eff
second_2 = q * bottom_direction[1]
third_2 = q * bottom_direction[2]
print([first, second, third])
print([first_2, second_2, third_2])
top_denom = first * first_2 + second * second_2 + third * third_2
bottom_denom = math.sqrt(first*first + second*second + third*third) * \
               math.sqrt(first_2*first_2 + second_2*second_2 + third_2*third_2)
print(top_denom, bottom_denom)
theta = math.acos(top_denom/bottom_denom)
print(theta/math.pi)
