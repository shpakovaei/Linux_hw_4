from cheks import func
import pytest
import yaml
import time


with open("config.yaml") as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def make_folders():
    return func(f"mkdir {data ['folderin']} {data ['folderout']} {data ['folderext']}", "")


@pytest.fixture()
def make_files():
    return func(f"cd {data['folderin']}; touch file1 file2", '')


@pytest.fixture(autouse=True)
def func_time():
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")

    with open("/home/user/stat.txt", "a") as f:
        f.write(f"{current_time}, количество файлов, размер файла, статистика загрузки процессора\n")
