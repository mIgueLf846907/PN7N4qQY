# 代码生成时间: 2025-09-21 23:47:59
import gradio as gr
import shutil
import os
import json
import datetime

"""
Data Backup and Restore Application using Gradio framework.
This application allows users to backup and restore data through a simple GUI.
"""

class DataBackupRestore:
    def __init__(self):
        # Define the directories for backup and restore
        self.backup_dir = "backup/"
        self.restore_dir = "restore/"
        # Create directories if they don't exist
        os.makedirs(self.backup_dir, exist_ok=True)
        os.makedirs(self.restore_dir, exist_ok=True)

    def create_backup(self, file_path):
        """
        Creates a backup of the specified file.
        Args:
            file_path (str): The path of the file to be backed up.
        Returns:
            str: The backup file path.
        """
        try:
            # Generate a timestamped backup file name
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_file_name = f"{os.path.basename(file_path)}_{timestamp}.bak"
            backup_file_path = os.path.join(self.backup_dir, backup_file_name)
            # Copy the file to the backup directory
            shutil.copy2(file_path, backup_file_path)
            return backup_file_path
        except Exception as e:
            # Handle any exceptions and return an error message
            return f"Error: {str(e)}"

    def restore_backup(self, backup_file_path, target_path):
        """
        Restores a backup file to the specified target path.
        Args:
            backup_file_path (str): The path of the backup file to be restored.
            target_path (str): The target path where the file will be restored.
        Returns:
            str: The restored file path or an error message.
        """
        try:
            # Copy the backup file to the target path
            shutil.copy2(backup_file_path, target_path)
            return target_path
        except Exception as e:
            # Handle any exceptions and return an error message
            return f"Error: {str(e)}"

    def load_backups(self):
        """
        Loads the list of backup files.
        Returns:
            list: A list of backup file paths.
        """
        return [os.path.join(self.backup_dir, file) for file in os.listdir(self.backup_dir)]

# Initialize the DataBackupRestore class
data_backup_restore = DataBackupRestore()

# Define the Gradio interface
iface = gr.Interface(
    fn=lambda file_path: data_backup_restore.create_backup(file_path),
    inputs=gr.File(label="Select a file to backup"),
    outputs="text"
)

# Add a button to display the list of backups
iface.add_component(
    gr.Button("List Backups"),
    elem_id="list_backups_button",
    input_value=None,
    role="action"
)

# Define the callback function to handle the backup list button click
def list_backups():
    return data_backup_restore.load_backups()

iface.add_component(
    gr.Dropdown(label="Select a backup to restore", choices=list_backups),
    elem_id="restore_dropdown",
    input_value=None,
    role="action"
)

# Add a button to restore a backup
iface.add_component(
    gr.Button("Restore Backup"),
    elem_id="restore_backup_button",
    input_value=None,
    role="action"
)

# Define the callback function to handle the restore backup button click
def restore_backup_callback(backup_file_path):
    # Get the target path from the user
    target_path = gr.Textbox(label="Enter the target path for restoration")
    return data_backup_restore.restore_backup(backup_file_path, target_path)

iface.add_component(
    gr.Textbox(label="Enter the target path for restoration"),
    elem_id="restore_target_path"
)
iface.add_component(
    gr.Button("Restore Backup"),
    elem_id="restore_backup_button",
    input_value=None,
    role="action"
).link(
    restore_backup_callback,
    inputs=["restore_dropdown", "restore_target_path"],
    outputs="text"
)

# Launch the Gradio interface
iface.launch(share=True)