# Requirements: Python 2.7 - 3.9

# PYPOWER was installed with pip in .venv
# View further requirements: https://pypi.org/project/PYPOWER/
# SciPy, PyRLU were installed without problem
# Numpy v1.25 was neccessary since a class got deceprecated

from pypower.api import case14, case57, case118

# Build connection matrix from ppc
def get_connections(ppc):
    num_bus = len(ppc["bus"])
    branch_data = ppc["branch"]

    connections = [[False for _ in range(num_bus)] for _ in range(num_bus)] 

    for connection in branch_data:
        # There is a -1 in the accesses since PyPower ports from MatLab which uses 1-indexing
        connections[int(connection[0])-1][int(connection[1])-1] = True
        connections[int(connection[1])-1][int(connection[0])-1] = True
    
    return connections


# Evaluate zero-forcing for a specific bus, Returns newly colored bus if success, otherwise None
def evaluate_zero_forcing_move(connections, bus, colored):
    neighbors_uncolored = 0
    candidate_bus = None
    for i in range(len(connections)):
        if connections[bus][i] == True:
            if not i in colored:
                neighbors_uncolored = neighbors_uncolored + 1
                candidate_bus = i

    return neighbors_uncolored, candidate_bus


# Evaluate whether a set is zero-forcing
def check_zero_forcing_set(connections, colored):
    changed_state = True
    complete_buses = [] # Stores buses that we don't need to worry about anymore

    while(changed_state == True):
        # print("colored:", colored)
        # print("complete_buses:", complete_buses)
        changed_state = False
        for bus in colored:
            if not bus in complete_buses:
                neighbors_uncolored, bus_colored = evaluate_zero_forcing_move(connections, bus, colored)
                if neighbors_uncolored == 0:
                    complete_buses.append(bus)
                elif neighbors_uncolored == 1:
                    colored.append(bus_colored)
                    changed_state = True
                    # print(bus_colored, "was colored!")

    if len(colored) == len(connections):
        return True
    return False


if __name__ == "__main__":

    # Possible bus networks to try out
    """Specifically, use case["branch"] to access graph geography"""
    ppc = case14()
    # ppc = case57()
    # ppc = case118()

    connections = get_connections(ppc)

    print(check_zero_forcing_set(connections, [0,2,4]))




