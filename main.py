# by Jakub Wawak
# kubawawak@gmail.com
# all rights reserved

# application for snapshoting selected github repositories for backup

import maintanance.CPrint as cp
import maintanance.Configuration as config
import sys

version = "v1.0.0"
build = "GITS-120623REV1"
printer = cp.CPrint()


# function for auto running from properties file
def auto_run():
    printer.cprint("Running auto mode.", "NORMAL")
    pass


# function for manual running properties file
def manual_run():
    printer.cprint("Running manual mode.", "NORMAL")
    pass


# function for running the application
def run():
    #  creating configurationFile object
    configurationFile = config.Configuration()
    #  checking if file exists
    if configurationFile.exist:
        configurationFile.load_file()
        printer.cprint("File found!", "GREEN")
        # checking if file error
        if not configurationFile.validate():
            printer.cprint("File correct!", "GREEN")
            configurationFile.show_object()  # showing objects in terminal
            args = sys.argv
            if "auto" in args:
                auto_run()
            else:
                manual_run()
        else:
            printer.cprint("Failed to read .properties file","RED")
    else:
        # create .properties file
        configurationFile.create_configuration_file()
        printer.cprint("Reload program!", "RED")


# function for showing starting header
def show_header():
    header = "git-snapshot " + version + "/" + build
    printer.cprint(header, "BLUE")


if __name__ == '__main__':
    show_header()
    run()
