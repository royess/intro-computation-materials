from game_of_life import update
import matplotlib.pyplot as plt

# spaceship as initial condiction
univ = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]

fig, ax = plt.subplots()

for t in range(60):
    ax.cla()
    ax.imshow(univ)
    update(univ)
    plt.pause(0.1)

plt.show()