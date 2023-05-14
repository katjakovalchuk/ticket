"""
file: ticketcounter.py
"""

from arrays import Array
from list_queue import Queue
from people import TicketAgent, Passenger


class TicketCounterSimulation:
    # Create a simulation object.
    """ "
    TicketCounterSimulation"""

    def __init__(self, numAgents, numMinutes, betweenTime, serviceTime):
        """ "
        __init__"""
        # Parameters supplied by the user.
        self._arriveProb = 1.0 / betweenTime
        self._serviceTime = serviceTime
        self._numMinutes = numMinutes

        # Simulation components.
        self._passengerQ = Queue()
        self._theAgents = Array(numAgents)

        for i in range(numAgents):
            self._theAgents[i] = TicketAgent(i + 1)

        # Computed during the simulation.
        self._totalWaitTime = 0
        self._numPassengers = 0
        self._betweenTime = betweenTime

    # Run the simulation using the parameters supplied earlier.
    def run(self):
        """ "
        run"""
        for curTime in range(self._numMinutes + 1):
            self._handleArrival(curTime)
            self._handleBeginService(curTime)
            self._handleEndService(curTime)

    # Print the simulation results.
    def printResults(self):
        """ "
        Print the simulation results."""
        numServed = self._numPassengers - len(self._passengerQ)
        avgWait = float(self._totalWaitTime) / numServed

        print("")
        print("Number of passengers served = ", numServed)
        print(f"Number of passengers remaining in line = {len(self._passengerQ)}")
        print(f"The average wait time was {avgWait:.2f} minutes.")

    # Returns the print statement. It is essential for tests, don't delete or
    # modify it
    def returnResults(self):
        """ "
        Return the print statement. It is essential for tests, don't delete or
        modify it"""
        numServed = self._numPassengers - len(self._passengerQ)
        avgWait = float(self._totalWaitTime) / numServed

        return (
            f"Number of passengers served = {numServed}\n"
            f"Number of passengers remaining in line = {len(self._passengerQ)}\n"
            f"The average wait time was {avgWait:.2f} minutes."
        )

    def _handleArrival(self, curTime):
        """ "
        _handleArrival"""
        if curTime % self._betweenTime == 0:
            self._passengerQ.enqueue(self._theAgents[0])
            self._numPassengers += 1

    def _handleBeginService(self, curTime):
        """ "
        _handleBeginService"""
        for agent in self._theAgents:
            if agent.isFree():
                if not self._passengerQ.isEmpty():
                    agent.startService(
                        self._passengerQ.dequeue(), curTime + self._serviceTime
                    )

    def _handleEndService(self, curTime):
        """ "
        _handleEndService"""
        for agent in self._theAgents:
            if agent.isFinished(curTime):
                self._totalWaitTime += self._serviceTime
                agent.stopService()


# a = TicketCounterSimulation(3, 100, 2, 4)
# a.run()
# a.printResults()
