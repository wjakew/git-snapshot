# by Jakub Wawak
# kubawawak@gmail.com
# all rights reserved

# object for setting, maintaining and creating configuration file

import os
import maintanance.CPrint as cp


class Configuration:
    # configuration fields
    github_auth_code = ""
    github_auth_login = ""
    default_snapshot_path = ""
    default_zip = 0
    list_of_repos_to_clone = []

    # object fields
    configuration_file_name = ""
    current_path = ""
    properties_file = None
    exist = False
    printer = None

    # constructor
    def __init__(self):
        self.printer = cp.CPrint()
        self.configuration_file_name = "git-snapshot.properties"
        self.current_path = os.getcwd()
        self.printer.cprint("Init Configuration object", "BLUE")
        # finding configuration file
        self.properties_file = self.find_configuration_file()
        # checking found file
        if self.properties_file is not None:
            self.printer.cprint("Found properties file at " + self.properties_file, "GREEN")
            self.exist = True
        else:
            self.printer.cprint("Cannot found properties file!", "RED")
            self.exist = False

    # function for finding configuration file path
    # returns .properties file path
    def find_configuration_file(self):
        self.printer.cprint("Searching configuration file on: " + os.getcwd(), "GREEN")

        for filename in os.listdir(os.getcwd()):
            f = os.path.join(self.current_path, filename)
            if os.path.isfile(f):
                # found file, checking if file is .properties
                if (f.endswith(".properties")):
                    return f
        return None

    # function for creating new configuration file with blank data
    def create_configuration_file(self):
        file = open(self.configuration_file_name, "w")
        file.write("# git-snapshot configuration file" + "\n")
        file.write("# file is created for setting automatic repository clonning" + "\n")
        file.write("# by Jakub Wawak / kubawawak@gmail.com" + "\n")
        file.write("# till death we do art" + "\n")
        file.write("#" + "\n")
        file.write("#" + "\n")
        file.write("# github_auth_code stores your code for github connection if you using 2FA" + "\n")
        file.write("# application will not work with accounts without 2FA enabled" + "\n")
        file.write("gitub_auth_code%XXXXXXXXXXXXXXXXXXXXXX" + "\n")
        file.write("# github_auth_login stores your login for github connection" + "\n")
        file.write("# login is needed to check if auth code is connected to your account" + "\n")
        file.write("github_auth_login%XXXXXXXXXXXXXXXXXXXXXX" + "\n")
        file.write("# default_snapshot_path sets default path to save the repository snapshots" + "\n")
        file.write("default_snapshot_path%XXXXXXXXXXXXXXXXXXXXXX" + "\n")
        file.write("# default_zip is a flag that determines if snapshot is zip or normal folder" + "\n")
        file.write("# 1 - zip, 2 - folder" + "\n")
        file.write("default_zip%1" + "\n")
        file.write("# list_of_repos_to_clone is list for storing urls to repositories" + "\n")
        file.write("list_of_repos_to_clone%" + "\n")
        file.write("%XXXXXXXXXXXXXXXXXXXXXX" + "\n")
        file.write("%XXXXXXXXXXXXXXXXXXXXXX" + "\n")
        file.write("%XXXXXXXXXXXXXXXXXXXXXX" + "\n")
        file.write("%XXXXXXXXXXXXXXXXXXXXXX" + "\n")
        file.write("%XXXXXXXXXXXXXXXXXXXXXX" + "\n")
        file.write("%XXXXXXXXXXXXXXXXXXXXXX" + "\n")
        file.write("%XXXXXXXXXXXXXXXXXXXXXX" + "\n")
        file.write("%XXXXXXXXXXXXXXXXXXXXXX" + "\n")
        file.write("%XXXXXXXXXXXXXXXXXXXXXX" + "\n")
        file.write("# end of configuration file" + "\n")
        file.write("# thanks for cloning with git-snapshot" + "\n")
        file.write("# Jakub Wawak" + "\n")
        file.close()
        self.printer.cprint("Created new configuration file!", "GREEN")

    # function for loading file data
    def load_file(self):
        configuration_file = open(self.configuration_file_name, "r")
        lines = configuration_file.readlines()
        for line in lines:
            line = line.strip()
            try:
                if "gitub_auth_code" in line:
                    self.github_auth_code = line.split("%")[1]
                elif "github_auth_login" in line:
                    self.github_auth_login = line.split("%")[1]
                elif "default_snapshot_path" in line:
                    self.default_snapshot_path = line.split("%")[1]
                elif "default_zip" in line:
                    self.default_zip = int(line.split("%")[1])
                elif line.startswith("%"):
                    self.list_of_repos_to_clone.append(line)
            except Exception as e:
                self.printer.cprint("Passing line!", "RED")

    # function for validating data file
    def validate(self):
        if self.github_auth_code != "" and self.github_auth_login != "" and self.default_snapshot_path != "" and self.default_zip != "":
            if "XX" in self.github_auth_code or "XX" in self.github_auth_login or "XX" in self.default_snapshot_path or "XX" in self.default_zip:
                return False
            return True

    # function for showing object data
    def show_object(self):
        self.printer.cprint("Configuration status", "BLUE")
        self.printer.cprint("github_auth_code: " + self.github_auth_code, "BLUE")
        self.printer.cprint("gitub_auth_login: " + self.github_auth_login, "BLUE")
        self.printer.cprint("default_snapshot_path: " + self.default_snapshot_path, "BLUE")
        self.printer.cprint("default_zip: " + str(self.default_zip), "BLUE")
        self.printer.cprint("list of repos to clone", "RED")
        for path in self.list_of_repos_to_clone:
            self.printer.cprint(path, "RED")
        self.printer.cprint("Configuration status END", "BLUE")
