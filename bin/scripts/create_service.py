"""Script used to create new microservice into the project.

This script autogenerate the scanfolding for the new service and also creates
the service into the docker-compose.
"""
import os, sys

from fixtures.docker_service import (dockerfile, requirements, service, 
    service_init)
from constants import BASE_DIR, CYAN, GREEN, RED, RESET, YELLOW


class MicroServiceScript:

    """Class representation for Micro Service Script."""

    def __init__(self, service_name, service_port):
        """Class constructor."""
        self.service_name = service_name
        self.service_port = service_port
        self.init_attrs(self.service_name, self.service_port)
        self.read_docker_file()
        self.add_service_into_docker_file()
        self.create_service_directory()

    def init_attrs(self, service_name, service_port):
        """Based on the service_name and the service_port this function 
        initialize the atributes of the class.
        
        Arguments
        ---------
            service_name : str
                name of the new service.
            service_port : str
                port of the service to be created.
        """
        self.service = service.format(service_name, service_port)
        self.docker_file_url = "{}/docker-compose.yml".format(BASE_DIR)
        self.docker_folder = "{}/{}/docker/development/env".format(BASE_DIR, service_name)
        self.development_folder = "{}/{}/docker/development".format(BASE_DIR, service_name)
        self.service_src_folder = "{}/{}/src".format(BASE_DIR, service_name)

    def read_docker_file(self):
        """Read docker file function and validate if either service name and 
        port aren't in use."""
        print(("{}Validating the service {} and the port {} aren't in use.{}")
            .format(YELLOW, self.service_name, self.service_port, RESET))
        with open(self.docker_file_url, "r") as myfile:
            lines = myfile.readlines()
            for line in lines:
                if not self.service_name not in line:
                    raise ValueError("{}Microservice: {} already in use.{}"
                        .format(RED, self.service_name, RESET))
                if not self.service_port not in line:
                    raise ValueError("{}Port: {} already in use.{}"
                        .format(RED, self.service_port, RESET))
    
    def add_service_into_docker_file(self):
        """Add service into docker-compose."""
        print(("{}Creating service {} with port {}{}")
            .format(YELLOW, self.service_name, self.service_port, RESET))
        self.add_code_into_file(service, self.docker_file_url)
        print("{}Microservice {} successfully added to docker-compose.yml{}"
            .format(GREEN, self.service_name, RESET))

    def create_service_directory(self):
        """Create the scanfolding for the service created."""
        try:
            os.makedirs(self.docker_folder)
            os.makedirs(self.service_src_folder)
        except OSError:
            print("{}Creation of the directory {} failed.{}"
                .format(RED, self.service_name, RESET))
        else:  
            files_folders = [
                ("__init__.py", self.service_src_folder),
                ("private", self.docker_folder),
                ("public", self.docker_folder),
                ("Dockerfile", self.development_folder),
                ("requirements.txt", self.development_folder)
            ]
            self.create_files_into_folders(files_folders)
            self.add_code_into_file(service_init, self.service_src_folder, "__init__.py")
            self.add_code_into_file(dockerfile, self.development_folder, "Dockerfile")
            self.add_code_into_file(requirements, self.development_folder, "requirements.txt")
            print("{}Successfully created service {} directory.{}"
                .format(GREEN, self.service_name, RESET))

    @staticmethod
    def create_files_into_folders(files_folders):
        """Create files into created service folder.
        
        Arguments
        ---------
            files_folders : list
                tuple with the file's and folder's name.
        """
        for ff in files_folders:
            file_name, folder_name = ff
            f = open("{}/{}".format(folder_name, file_name), "w+")
            f.close()

    def add_code_into_file(self, fixture, url_path, file=None):
        """Add fixture code into corresponding file.
        
        Arguments
        ---------
            fixture : str
                commom code for the file to be created.
            url_path : str
                route to the file.
            file : str
                file where the fixture is beeing to be added.
        """
        route = "{}"
        if file:
            route = "{}/{}"
        with open(route.format(url_path, file), "a") as f:
            f.write(fixture.format(self.service_name, self.service_port))
        f.close()


if __name__ == "__main__":
    MicroServiceScript(sys.argv[1], sys.argv[2])
    print("{}Stoping and removing all docker containers.{}".format(CYAN, RESET))
    os.system("docker-compose down && docker-compose stop")
    print("{}Starting and building all docker containers.{}".format(CYAN, RESET))
    os.system("docker-compose up")