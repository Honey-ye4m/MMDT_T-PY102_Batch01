import importlib.util
import os
from pathlib import Path
import math
import pytest

def load_lab06():
    student_dir = os.environ.get("STUDENT_DIR")
    assert student_dir, "STUDENT_DIR env var not set"

    lab_path = Path(student_dir) / "lab06.py"
    assert lab_path.exists(), f"Missing file: {lab_path}"

    spec = importlib.util.spec_from_file_location("student_lab06", lab_path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

@pytest.mark.points(3)
def test_q1_basic():
    lab = load_lab06()
    assert hasattr(lab, "schedule_new_job"), "schedule_new_job is missing"

    arr = [12, 29, 76, 31, 65, 80, 77]
    result = lab.schedule_new_job(arr[:], 10)
    assert result == [10, 12, 76, 29, 65, 80, 77, 31]

@pytest.mark.points(4)
def test_q1_level1():
    lab = load_lab06()
    arr = [12, 29, 76, 31, 65, 80, 77]
    result = lab.schedule_new_job(arr[:], 90)
    assert result == [12, 29, 76, 31, 65, 80, 77, 90]

    arr = [12, 29, 76, 31, 65, 80, 77]
    result = lab.schedule_new_job(arr[:], 29)
    assert result == [12, 29, 76, 29, 65, 80, 77, 31]

    arr = [20]
    result = lab.schedule_new_job(arr[:], 10)
    assert result == [10, 20]


@pytest.mark.points(3)
def test_q2_basic():
    lab = load_lab06()
    assert hasattr(lab, "process_next_job"), "process_next_job is missing"
    arr = [12, 29, 76, 31, 65, 80, 77, 90]
    removed, updated = lab.process_next_job(arr[:])
    assert removed == 12
    assert updated == [29, 31, 76, 90, 65, 80, 77]


@pytest.mark.points(5)
def test_q2_level2():
    lab = load_lab06()
    arr = [12]
    removed, updated = lab.process_next_job(arr[:])
    assert removed == 12
    assert updated == []
    arr = []
    result = lab.process_next_job(arr[:])
    assert result is None
    arr = [5, 10, 20, 30, 40, 50, 60]
    removed, updated = lab.process_next_job(arr[:])
    assert removed == 5
    assert updated == [10, 30, 20, 60, 40, 50]

@pytest.mark.points(2)
def test_q3_basic():
    lab = load_lab06()
    assert hasattr(lab, "personal_priority_q"), "personal_priority_q is missing"
    result = lab.personal_priority_q()
    assert isinstance(result, list), "Function must return a list"

@pytest.mark.points(3)
def test_q3_level1():
    lab = load_lab06()
    result = lab.personal_priority_q()
    assert len(result) == 6, "List must contain 6 items including 'security'"
    assert all(isinstance(item, tuple) and len(item) == 2 for item in result), \
        "Each item must be a tuple of (weight, category)"
    for weight, _ in result:
        assert weight is not None, "All weights must be filled"
        assert isinstance(weight, (int, float)), "Each weight must be a number"
