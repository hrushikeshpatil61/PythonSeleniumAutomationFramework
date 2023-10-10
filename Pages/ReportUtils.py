import os
import shutil
import sys

import allure
import datetime


class ReportUtils:
    def __init__(self, driver):
        self.driver = driver

    def create_date_time_folder(self):
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        source_directory = "Reports"
        date_time_directory = os.path.join(source_directory, current_datetime)
        # Create the destination (date_time) directory
        os.makedirs(date_time_directory, exist_ok=True)
        return date_time_directory

    def create_pass_fail_folders(self):
        allure_dir_path = "Reports"
        pass_folder = os.path.join(allure_dir_path, "Pass_screenshots")
        os.makedirs(pass_folder, exist_ok=True)
        fail_folder = os.path.join(allure_dir_path, "Fail_screenshots")
        os.makedirs(fail_folder, exist_ok=True)
        return pass_folder, fail_folder

    def take_pass_screenshot(self, name):
        # timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        pass_folder, fail_folder = self.create_pass_fail_folders()
        screenshot_path = os.path.join(pass_folder, f"{name}.png")
        self.driver.save_screenshot(screenshot_path)
        # Attach the screenshot to the Allure report
        allure.attach.file(screenshot_path, name=name, attachment_type=allure.attachment_type.PNG)

    def move_reports_to_current_date_time(self):
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        # Define the source and destination directories
        source_directory = "Reports"
        date_time_directory = os.path.join(source_directory, current_datetime)

        # Create the destination (date_time) directory
        os.makedirs(date_time_directory, exist_ok=True)

        # Move the Pass_screenshots folder to the date_time folder
        pass_folder, fail_folder = self.create_pass_fail_folders()

        if os.path.exists(pass_folder):
            shutil.move(pass_folder, date_time_directory)

        # Move the Fail_screenshots folder to the date_time folder
        if os.path.exists(fail_folder):
            shutil.move(fail_folder, date_time_directory)

        # Move JSON files to the date_time folder
        for root, dirs, files in os.walk(source_directory):
            for file in files:
                if file.endswith(".json"):
                    json_file_path = os.path.join(root, file)
                    shutil.move(json_file_path, date_time_directory)
