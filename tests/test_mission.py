import numpy as np
from uuv_mission.dynamic import Mission


def test_from_csv_shapes_and_values():
    m = Mission.from_csv('data/mission.csv')
    # Expect arrays of length 100 (based on provided CSV)
    assert isinstance(m.reference, np.ndarray)
    assert isinstance(m.cave_height, np.ndarray)
    assert isinstance(m.cave_depth, np.ndarray)
    assert m.reference.shape == (100,)
    assert m.cave_height.shape == (100,)
    assert m.cave_depth.shape == (100,)

    # Check first row values match the CSV
    assert np.isclose(m.reference[0], 0.0)
    assert np.isclose(m.cave_height[0], 30.0)
    assert np.isclose(m.cave_depth[0], -30.0)
