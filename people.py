"""
file: people.py
"""


class TicketAgent:
    """
    A ticket agent object.
    """

    # Creates a ticket agent object.
    def __init__(self, idNum):
        """
        Initializes a ticket agent object.
        :param idNum: The ticket agent's id number.
        """
        self._idNum = idNum
        self._passenger = None
        self._stopTime = -1

    # Gets the ticket agent's id number.
    def idNum(self):
        """
        Get the ticket agent's id number.
        """
        return self._idNum

    # Determines if the ticket agent is free to assist a passenger.
    def isFree(self):
        """
        Determines if the ticket agent is free to assist a passenger.
        """
        return self._passenger is None

    # Determines if the ticket agent has finished helping the passenger.
    def isFinished(self, curTime):
        """ "
        Determines if the ticket agent has finished helping the passenger."""
        return self._passenger is not None and self._stopTime == curTime

    # Indicates the ticket agent has begun assisting a passenger.
    def startService(self, passenger, stopTime):
        """ "
        Indicates the ticket agent has begun assisting a passenger."""
        self._passenger = passenger
        self._stopTime = stopTime

    # Indicates the ticket agent has finished helping the passenger.
    def stopService(self):
        """ "
        Indicates the ticket agent has finished helping the passenger"""
        thePassenger = self._passenger
        self._passenger = None
        return thePassenger


class Passenger:
    """ "
    A passenger object."""

    # Creates a passenger object.
    def __init__(self, idNum, arrivalTime):
        """ "
        Initializes a passenger object.
        :param idNum: The passenger's id number.
        :param arrivalTime: The passenger's arrival time."""
        self._idNum = idNum
        self._arrivalTime = arrivalTime

    # Gets the passenger's id number.
    def idNum(self):
        """ "
        Gets the passenger's id number.
        """
        return self._idNum

    # Gets the passenger's arrival time.
    def timeArrived(self):
        """ "
        Gets the passenger's arrival time.
        """
        return self._arrivalTime
