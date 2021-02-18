from enum import Enum
import logger
from typing import Final


class State(Enum):
    STATE_STOPPED: Final[int] = 0
    STATE_LOGGING: Final[int] = 1