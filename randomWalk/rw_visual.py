import matplotlib.pyplot as plt
from randomWalk.random_walk import RandomWalk

while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))
    # 突出起点位置颜色
    plt.scatter(0, 0, c='green', edgecolor='none', s=100)
    # 给其他点渐变着色
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
                edgecolor='none', s=1)
    plt.show()

    keep_running = input("Make another walk?(y/n)")
    if keep_running == 'n' or keep_running == 'N':
        break

