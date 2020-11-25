import json
import argparse
import subprocess


class Network:
    def __init__(self, data):
        self.id = data["id"]
        self.address = data["address"]

    def deploy(self):
        shell_exec(['services/deploy_network.sh',
                    '--id', self.id,
                    '--address', self.address])


class Router:
    def __init__(self, data):
        self.id = data["id"]
        self.interfaces = [Interface(d, self) for d in data["interfaces"]]

    def deploy(self):
        shell_exec(['services/deploy_router.sh',
                    '--id', self.id])
        self.open_interfaces()

    def open_interfaces(self):
        for interface in self.interfaces:
            interface.add()


class Interface:
    def __init__(self, data, router):
        self.in_network = data["in-network"]
        self.address = data["address"]
        self.router = router

    def add(self):
        shell_exec(['services/add_interface.sh',
                    '--nw_id', self.in_network,
                    '--address', self.address,
                    '--router_id', self.router.id])


class Machine:
    def __init__(self, data):
        self.id = data["id"]
        self.image = data["image"]
        self.in_network = data["in-network"]

    def deploy(self):
        shell_exec(['services/deploy_machine.sh',
                    '--id', self.id,
                    '--image', self.image,
                    '--in_network', self.in_network])


class Application:
    def __init__(self, data):
        self.name = data["name"]
        self.networks = [Network(d) for d in data["networks"]]
        self.routers = [Router(d) for d in data["routers"]]
        self.machines = [Machine(d) for d in data["machines"]]

    def deploy_networks(self):
        for network in self.networks:
            network.deploy()

    def deploy_routers(self):
        for router in self.routers:
            router.deploy()

    def deploy_machines(self):
        for machine in self.machines:
            machine.deploy()

    def deploy(self):
        print("Deploiement de l'application", self.name)
        self.deploy_networks()
        self.deploy_routers()
        self.deploy_machines()


def shell_exec(command):
    process = subprocess.Popen(command)
    process.wait()


# Get data
def get_data_file():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", help="Json file to read")
    args = parser.parse_args()
    if args.data is None:
        args.data = "test.json"
    return args.data


def main():
    # Configure Openstack Client
    shell_exec("Openstack_configuration/init.sh")
    with open(get_data_file()) as json_file:
        data = json.load(json_file)
        Application(data['application']).deploy()


main()
