# b1-coding-practical-mt24
Coding practical task for the B1 Scientific Coding course at Oxford (MT24)

## Usage

Load a mission from the provided CSV and inspect the arrays:

```python
from uuv_mission.dynamic import Mission

mission = Mission.from_csv('data/mission.csv')
print(mission.reference.shape, mission.cave_height.shape, mission.cave_depth.shape)
```

This project requires the dependencies listed in `requirements.txt` (pandas, numpy, matplotlib).
