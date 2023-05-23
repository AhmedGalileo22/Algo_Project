import turtle
import pandas
import dijkstra
from cities import Cities

init_graph = {}
objects = []
counter1 = -1
counter2 = -1

screen = turtle.Screen()
screen.title("Courier Routing system")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

answer_state = "Washington, " + screen.textinput(title=f"Shipping To U.S. States", prompt="Enter pickup and delivery "
                                                                                          "locations separated by a "
                                                                                          "comma:").title()
guessed_states = answer_state.split(", ")

if answer_state == "Exit":
    missing_states = []
    for state in all_states:
        if state not in guessed_states:
            missing_states.append(state)

    new_data = pandas.DataFrame(missing_states)
    new_data.to_csv("states_to_learn.csv")

for state in guessed_states:
    state_data = data[data["state"] == state]
    x = int(state_data["x"])
    y = int(state_data["y"])
    name = state
    state = Cities(name=name, x=x, y=y)
    state.hideturtle()
    state.penup()
    state.goto(x=state.x, y=state.y)
    objects.append(state)

for node in guessed_states:
    init_graph[node] = {}

for node in guessed_states:
    counter1 += 1
    for element in guessed_states:
        counter2 += 1
        if node == element:
            pass
        else:
            init_graph[node][element] = objects[counter1].distance(objects[counter2])
    counter2 = -1

file = pandas.DataFrame(init_graph)
data_file = file.to_csv("data.csv")

graph = dijkstra.Graph(guessed_states, init_graph)
previous_nodes, shortest_path = dijkstra.dijkstra_algorithm(graph=graph, start_node="Washington")
path = dijkstra.print_result(previous_nodes, shortest_path, start_node="Washington", target_node=guessed_states[-1])
sha7bora = turtle.Turtle()
sha7bora.pensize(2)
for state in objects:
    sha7bora.goto(state.x, state.y)
    sha7bora.write(state.name)

screen.mainloop()