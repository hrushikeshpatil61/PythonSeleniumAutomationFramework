import os
import shutil
import sys
import time

import allure
import datetime


class ReportUtils:
    date_time_directory = ""
    pass_folder_path = ""
    fail_folder_path = ""

    def __init__(self, driver):
        self.driver = driver

    def get_date_time_folder(self):
        if self.date_time_directory == "":
            current_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            source_directory = "Reports"
            self.date_time_directory = os.path.join(source_directory, current_datetime)
            # Create the destination (date_time) directory
            os.makedirs(self.date_time_directory, exist_ok=True)
        return self.date_time_directory

    def get_pass_fail_folders(self):
        if self.pass_folder_path == "":
            allure_dir_path = "Reports"
            self.pass_folder_path = os.path.join(allure_dir_path, "Pass_screenshots")
            os.makedirs(self.pass_folder_path, exist_ok=True)
            self.fail_folder_path = os.path.join(allure_dir_path, "Fail_screenshots")
            os.makedirs(self.fail_folder_path, exist_ok=True)
        return self.pass_folder_path, self.fail_folder_path

    def take_pass_screenshot(self, name):
        # timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        pass_folder_path, fail_folder_path = self.get_pass_fail_folders()
        screenshot_path = os.path.join(pass_folder_path, f"{name}.png")
        self.driver.save_screenshot(screenshot_path)
        # Attach the screenshot to the Allure report
        allure.attach.file(screenshot_path, name=name, attachment_type=allure.attachment_type.PNG)

    def move_reports_to_current_date_time(self):
        date_time_directory = self.get_date_time_folder()
        pass_folder_path, fail_folder_path = self.get_pass_fail_folders()

        source_directory = "Reports"  # Replace with the actual source path
        destination_directory = date_time_directory  # Replace with the actual destination path

        # Create the destination directory if it doesn't exist
        os.makedirs(destination_directory, exist_ok=True)
        # List all files in the source directory

        shutil.move(pass_folder_path, date_time_directory)
        shutil.move(fail_folder_path, date_time_directory)
        self.driver.implicitly_wait(10)
        files = os.listdir(source_directory)

        len_files = len(files)
        print(f"*****************************{len_files}****")
        # Loop through the files and move JSON files to the destination directory
        for file in files:
            if file.endswith(".json"):
                source_file_path = os.path.join(source_directory, file)
                destination_file_path = os.path.join(destination_directory, file)

                # Move the JSON file to the destination directory
                try:
                    # Move the JSON file to the destination directory
                    shutil.move(source_file_path, destination_file_path)
                    print(f"File '{file}' moved successfully.")
                except Exception as e:
                    print(f"Error moving file '{file}': {e}")


    def second_move_reports_to_current_date_time(self):
        self.driver.implicitly_wait(5)
        source_directory = "Reports"
        all_reports_directory = "all_reports"
        os.makedirs(all_reports_directory, exist_ok=True)
        # Get the current date and time in a specific format (e.g., "YYYY-MM-DD_HH-MM-SS")
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        # Create a new directory name using the current date and time
        new_directory_name = os.path.join(all_reports_directory, current_datetime)

        # Rename the "Reports" directory to the new directory name
        os.rename(source_directory, new_directory_name)

        # Move the renamed directory to the "all_reports" directory
        shutil.move(new_directory_name, all_reports_directory)