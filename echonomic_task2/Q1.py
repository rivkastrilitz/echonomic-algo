from Agent import Agent
from typing import List

# check if option 1 is pareto improvement of option 2
def isParetoImprovement(agents: List[Agent], option1: int, option2: int) -> bool:
    if option1 == option2:
        return False
    for a in agents:
        # if one of the agent value decreases than there is no pareto improvement
        if a.value(option1) < a.value(option2):
            return False

    return True


def isParetoOptimal(agents: List[Agent], option: int, allOption: List[int]) -> bool:
    if option > len(allOption) or option < 0:
        raise IndexError("option out of range")
    for curr_option in allOption:
        # if there is 1 option that is pareto improvement of the given option
        # then the given option is not pareto optimal
        if isParetoImprovement(agents, curr_option, option):
            return False

    return True

if __name__ == '__main__':
    a = Agent([1, 1, 5])
    b = Agent([2, 3, 5])
    c = Agent([5, 5, 5])
    l = [a, b, c]
    print(isParetoImprovement(l, 1, 0))
    print(isParetoImprovement(l, 0, 1))

    ami = Agent([1, 2, 3, 4, 5])
    tami = Agent([3, 1, 2, 5, 4])
    rami = Agent([3, 5, 5, 1, 1])
    agent_list = [ami, tami, rami]
    print(isParetoImprovement(agent_list, 1, 0))
    try:
        print(isParetoImprovement(agent_list, 1, 5))
    except:
        print("index out of bound ")
    print(isParetoImprovement(agent_list, 4, 1))
    print(isParetoOptimal(agent_list, 2, [0, 1, 2, 3, 4]))