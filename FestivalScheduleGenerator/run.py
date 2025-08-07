from assign_stages import assign_stages
from gantt import plot_gantt_chart
from load_input import load_input

# shows = [
#     ("show_1", 36, 39),
#     ("show_2", 30, 33),
#     ("show_3", 29, 36),
#     ("show_4", 33, 35),
#     ("show_5", 40, 42),
#     ("show_6", 36, 40),
# ]

shows = load_input("list.txt")
print(shows)

planning = assign_stages(shows)
plot_gantt_chart(planning)
