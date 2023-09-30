from cheks import func
import pytest
import yaml
import time

with open("config.yaml") as f:
    data = yaml.safe_load(f)

class TestPositive:

    def test_step1(self):
        assert func(f"cd {data ['folderin']}; 7z a {data ['folderout']}/arh1", "Everything is Ok"), "test_step1 FAIL"

    def test_step2(self):
        assert func(f"cd {data ['folderout']}; 7z d arh1.7z", "Everything is Ok"), "test_step2 FAIL"

    def test_step3(self):
        assert func(f"cd {data ['folderext']}; 7z u {data ['folderout']}/arh1", "Everything is Ok"), "test_step3 FAIL"

    def test_step4(self):
        # Test listing files in the archive
        assert func(f"cd {data ['folderout']}; 7z l arx2.7z", "Everything is Ok"), "test_step4 FAIL"

    def test_step5(self):
        # Test extracting with preserving paths
        assert func(f"cd {data ['folderout']}; 7z x arx2.7z {data ['folderext']}", "Everything is Ok"), "test_step5 FAIL"


if __name__ == '__min__':
    pytest.main(["-vv"])
