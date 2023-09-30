from sshcheckers import ssh_checkout, upload_files
import yaml
from cheks import getout

with open('config.yaml') as f:
    my_dict = yaml.safe_load(f)

class TestDeployPositive:

    def save_log(self, starttime, name):
        with open(name, 'w') as f:
            f.write(getout("journalctl --since '{}'".format(starttime)))
    def test_step1_deploy(self):
        res = []
        upload_files(my_dict['address'], 'user2', my_dict['passwordssh'], my_dict['username1'], my_dict['username2'])
        res.append(ssh_checkout(my_dict['address'], 'user2', my_dict['passwordssh'],
                                f"echo {my_dict['passwordssh']} | sudo -S dpkg -i {my_dict['username2']}","Настраивается пакет"))
        res.append(ssh_checkout("0.0.0.0", "user2", "11", "echo '11' | sudo -S dpkg -s p7zip-full",
                                "Status: install ok installed"))
        assert all(res)

    def test_step2_deploy(self, start_time):
        res = []
        upload_files(my_dict['address'], my_dict['user'], my_dict['passwordssh'], my_dict['username2'] + ".deb",
                     "/home/{}/{}.deb".format(my_dict['user'],my_dict['username2']))
        res.append(ssh_checkout(['address'], my_dict['user'], my_dict['passwordssh'], "echo '{}' | sudo -S dpkg -i"
                                                                          " /home/{}/{}.deb".format(my_dict["passwdordssh"],
                                                                                                    my_dict["user"],
                                                                                                    my_dict["username2"]),
                                "Настраивается пакет"))
        res.append(ssh_checkout(my_dict['address'], my_dict['user'], my_dict['passwordssh'], "echo '{}' | "
                                                                          "sudo -S dpkg -s {}".format(my_dict["passwordssh"],
                                                                                                      my_dict["username2"]),
                                "Status: install ok installed"))
        self.save_log(start_time, "log1.txt")
        assert all(res), "test1 FAIL"
