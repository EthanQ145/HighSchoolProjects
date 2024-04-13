import math

co_eff_1 = 3
co_eff_2 = 7
m_a = 46.7
m_b = 7.2
a_a = 6 * 9.81 * m_b/(m_a + 4 * m_b) - 9.81
a_a_2 = (2 * m_b - m_a) * 9.81/m_a

# print(co_eff_1 * a_a + co_eff_2 * a_a_2)

u_s = 0.83
alpha = 8.3
r = 0.792
w = ((u_s**2 * 9.81**2 - alpha**2 * r ** 2) / r**2)**(1/4) * (30/math.pi)

# print(w)

co_eff_x = 2
co_eff_y = 1
theta_1 = 33 * math.pi/180
theta_2 = 22 * math.pi/180
v_a = 18.6
v_a_g = (v_a * math.sin(theta_1 + theta_2)) / (2 * math.sin(math.pi/2 - theta_2))

# print(co_eff_x * (v_a * math.sin(theta_1) - v_a_g) + co_eff_y * (v_a * math.cos(theta_1)))

a = -1207.6 + 393.5 + 634.9
print(-1207.6 + 393.5 + 634.9)
print(a/44.01 * 100)
print("exothermic")
