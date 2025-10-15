from dataclasses import dataclass
import numpy as np


@dataclass
class PDController:
    kp: float = 0.15
    kd: float = 0.6

    def __post_init__(self):
        # keep a small memory of last error for discrete derivative
        self._last_error: float | None = None

    def reset(self):
        self._last_error = None

    def __call__(self, reference: float, observation: float) -> float:
        """Compute control action for scalar reference and observation.

        u[t] = kp*e[t] + kd*(e[t] - e[t-1])
        where e[t] = r[t] - y[t]
        """
        error = float(reference) - float(observation)
        if self._last_error is None:
            derivative = 0.0
        else:
            derivative = error - self._last_error

        u = self.kp * error + self.kd * derivative
        self._last_error = error
        return float(u)
