# IMPORTS --------------------------------------------------------------------
from enum import Enum, auto


# CLASSES --------------------------------------------------------------------
class ActionType(Enum):
    ESCAPE = auto()
    MOVEMENT = auto()
# END ActionType()


class Action:
    def __init__(self, action_type: ActionType, **kwargs):
        self.action_type: ActionType = action_type
        self.kwargs = kwargs
    # END Action.__init__()


# END Action()

