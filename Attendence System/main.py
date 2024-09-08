import gradio as gr
import csv
from datetime import date
from huggingface_hub import HfApi, HfFolder, hf_hub_download, upload_file
import os


class AttendanceTracker:
    def __init__(self, dataset_id, repo_id):
        self.courses = ["AI", "DS", "ML", "DA Gray", "DA Black",
                        "DA White", "DS6", "DS7 Blue", "DS7 Green"]
        self.dataset_id = dataset_id
        self.repo_id = repo_id
        self.token = HfFolder.get_token()

    def load_original_attendance_list(self, course):
        # Download the CSV file using hf_hub_download
        local_file_path = hf_hub_download(repo_id=self.dataset_id, filename=f"{
                                          course}.csv", repo_type="dataset", use_auth_token=self.token)
        return local_file_path

    def get_new_column_name(self, existing_header, current_date):
        # Determine if the current date is already in the header and generate a new column name if needed
        if current_date not in existing_header:
            return current_date

        # Create a new column name with a suffix
        base_name = current_date
        suffix = 1
        new_column_name = f"{base_name}({suffix})"
        while new_column_name in existing_header:
            suffix += 1
            new_column_name = f"{base_name}({suffix})"
        return new_column_name

    def mark_attendance(self, attendance_file, course):
        local_file_path = self.load_original_attendance_list(course)

        # Load existing data from CSV
        existing_data = {}
        with open(local_file_path, "r") as f:
            reader = csv.reader(f)
            header = next(reader)
            for row in reader:
                if row:
                    # Preserve original case and remove any leading/trailing spaces
                    name = row[0].strip()
                    # Store the entire row with the original case
                    existing_data[name.lower()] = row

        # Debug: Print existing names
        print("Existing Names:", existing_data.keys())

        # Read the new attendance file
        new_attendance_list = []
        with open(attendance_file.name, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row:
                    # Combine first and last name and make it lowercase for comparison
                    combined_name = f"{row[0].strip()} {
                        row[1].strip()}".lower().lstrip().rstrip()
                    new_attendance_list.append(combined_name)

        # Debug: Print new attendance names
        print("New Attendance Names:", new_attendance_list)

        # Get current date and prepare the new column name
        current_date = date.today().strftime("%d-%m-%Y")
        new_column_name = self.get_new_column_name(header, current_date)

        # Prepare updated data including the new date column
        updated_rows = []
        updated_header = header[:]
        if new_column_name not in updated_header:
            updated_header.append(new_column_name)

        for name_lower, row in existing_data.items():
            # Append new status for the new column
            status = "Present" if name_lower in new_attendance_list else "Absent"
            row.append(status)
            updated_rows.append(row)

        # Save the updated attendance list locally
        with open(local_file_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(updated_header)
            writer.writerows(updated_rows)

        # Upload the updated file back to the Hugging Face dataset
        upload_file(
            path_or_fileobj=local_file_path,
            path_in_repo=f"{course}.csv",
            repo_id=self.repo_id,
            repo_type="dataset",
            token=self.token
        )

        return f"Attendance marked successfully for {course}!"


dataset_id = "omarkashif/attendace-ML"
repo_id = "omarkashif/attendace-ML"
tracker = AttendanceTracker(dataset_id, repo_id)


def upload_and_mark(file, course):
    return tracker.mark_attendance(file, course)


iface = gr.Interface(
    fn=upload_and_mark,
    inputs=[gr.File(label="Upload Attendance File (CSV)"), gr.Dropdown(choices=["AI", "DS", "ML",
                                                                                "DA Gray", "DA Black", "DA White", "DS6", "DS7 Blue", "DS7 Green"], label="Select Course")],
    outputs=gr.Textbox(label="Status"),
    title="Attendance Tracker",
    description="Upload a CSV file of today's attendance to update the attendance file for the selected course."
)

iface.launch()
