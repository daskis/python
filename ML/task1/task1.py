from random import random
from math import sqrt


class Neuron:
    def __init__(self):
        self.nu = 0.5
        self.w = [random(), random()]
        divider = sqrt(self.w[0] ** 2 + self.w[1] ** 2)
        self.w[0] /= divider
        self.w[1] /= divider

    def calculate(self, x):
        return self.w[0] * x[0] + self.w[1] * x[1]

    def recalculate(self, x):
        # self.w[0] += self.nu * (x[0] - self.w[0])
        # self.w[1] += self.nu * (x[1] - self.w[1])

        self.w[0] += self.nu * x[0] * x[0]  # Правило Хебба для первого веса
        self.w[1] += self.nu * x[1] * x[1]  # Правило Хебба для второго веса


class NeuralNetwork:
    def __init__(self):
        self.x = [
            [0.97, 0.20],
            [1.00, 0.00],
            [-0.72, 0.70],
            [-0.67, 0.74],
            [-0.80, 0.60],
            [0.00, -1.00],
            [0.20, -0.97],
            [-0.30, -0.95],
        ]
        self.neurons = [Neuron() for i in range(4)]

    def __str__(self):
        s = ""
        for neuron in self.neurons:
            s += str(neuron.w) + '\n'
        return s

    def start(self, threshold_number, penalty_threshold):
        u = [0 for _ in range(4)]
        number_wins = [0, 0, 0, 0]

        for i in range(len(self.x)):
            for j in range(4):
                if number_wins[j] < threshold_number:
                    u[j] = self.neurons[j].calculate(self.x[i])
                else:
                    u[j] -= 100

            max_u = max(u)
            winners = [index for index, val in enumerate(u) if val == max_u]

            if len(winners) == 1:
                winner_index = winners[0]
            else:
                # Apply penalty to the neurons with the most wins
                max_wins = max(number_wins)
                candidates = [index for index in winners if number_wins[index] == max_wins]
                winner_index = min(candidates)  # Choose the neuron with the smallest index among candidates

            self.neurons[winner_index].recalculate(self.x[i])
            number_wins[winner_index] += 1

            # Check if any neuron needs penalty
            for j in range(4):
                if number_wins[j] >= penalty_threshold:
                    u[j] -= 100

            print(winner_index + 1)


nn = NeuralNetwork()
print(nn)
nn.start(5, 10)
print(nn)
