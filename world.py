#!/usr/bin/env python
# TODO Import the TurtleBot environment when ROS is installed
from turtlesim_enacter import TurtleSimEnacter


class Agent:
    def __init__(self, _hedonist_table):
        """ Creating our agent """
        self.hedonist_table = _hedonist_table
        self._action = 0
        self.anticipated_outcome = 0
        self.anticipation_0 = 0
        self.anticipation_1 = 0
        self.ennui = 0


    def action(self, outcome):
        """ Computing the next action to enact """
        # TODO: Implement the agent's decision mechanism
        if self._action == 0:
            self.anticipation_0 = outcome
        else:
            self.anticipation_1 = outcome

        if outcome == self.anticipated_outcome:
            pass
        if self.ennui >= 3:
            self._action = Environment2.outcome(self, self._action)

        self.ennui = self.ennui + 1
        if self.ennui >= 4:
            self.ennui = 1

        return self._action

    def anticipation(self):
        """ computing the anticipated outcome from the latest action """
        # TODO: Implement the agent's anticipation mechanism
        if self._action == 0:
            self.anticipated_outcome = self.anticipation_0
        else:
            self.anticipated_outcome = self.anticipation_1
        return self.anticipated_outcome

    def satisfaction(self, new_outcome):
        """ Computing a tuple representing the agent's satisfaction after the last interaction """
        # True if the anticipation was correct
        anticipation_satisfaction = (self.anticipated_outcome == new_outcome)
        # The value of the enacted interaction
        hedonist_satisfaction = self.hedonist_table[self._action][new_outcome]
        return anticipation_satisfaction, hedonist_satisfaction


class Environment1:
    """ In Environment 1, action 0 yields outcome 0, action 1 yields outcome 1 """

    def outcome(self, action):
        if action == 0:
            return 0
        else:
            return 1


class Environment2:
    """ In Environment 2, action 0 yields outcome 1, action 1 yields outcome 0 """

    def outcome(self, action):
        if action == 0:
            return 1
        else:
            return 0

liste_action = []


def ennui(liste):  # return vrai quand le robot s'ennuit
    if len(liste) >= 3:
        if liste[0] == liste[1] and liste[1] == liste[2]:
            liste.clear()
            return True
        else:
            return False
    else:
        return False


def world(agent, environment):
    """ The main loop controlling the interaction of the agent with the environment """
    outcome = 0
    for i in range(10):
        action = agent.action(outcome)
        liste_action.append(action)
        outcome = environment.outcome(action)
        print(" Action: " + str(action) + ", Anticipation: " + str(agent.anticipation()) + ", Outcome: " + str(outcome)
              + ", Satisfaction: " + str(agent.satisfaction(outcome)))


# TODO Define the hedonist values of interactions (action, outcome)
hedonist_table = [[-1, 1], [-1, 1]]
# TODO Choose an agent
a = Agent(hedonist_table)
# TODO Choose an environment
# e = Environment1()
# e = Environment2()
e = TurtleSimEnacter()

world(a, e)
