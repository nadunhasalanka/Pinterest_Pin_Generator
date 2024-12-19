import os
import time

import g4f
import gspread
from google.oauth2.service_account import Credentials
from modules.base import Pinterest


class Writer(Pinterest):
    def __init__(self, project_folder):
        super().__init__(project_folder)


    def open_data(self, mode, google_sheet = True, table_id = None):
        if google_sheet:
            # if the value of the google_sheet argument is true , we will read data from table via API
            # Obtain Google Sheets credentials
            creds = self._get_google_creds()

            # authorize the connection using gspread
            client = gspread.authorize(creds)

            #Open the Google Sheets table using its key
            table = client.open_by_key(table_id)

            #Choose the appropriate worksheet based on the mode (image or video)
            if mode == self.WRITER_MODE_2:
                worksheet = table.get_worksheet(2)
            elif mode == self.WRITER_MODE_1:
                worksheet = table.get_worksheet(1)
            else:
                #Raise an error for an invalid mode
                raise ValueError(f"invalid mode: {mode}. Please choose between 'image' and 'video'")

            # Retrieve all values from the choosen worksheet
            all_values = worksheet.get_all_values()

            # Parse the rows and obtain the data based on the specified mode
            data = self._parse_rows(all_values, mode)

        else:
            #otherwise , we will  read data frpm a csv file
            if mode == self.WRITER_MODE_2:
                filename = self.IMAGE_PROMPTS_FILE
            elif mode == self.WRITER_MODE_1:
                filename = self.VIDEO_PROMPTS_FILE
            else:
                raise ValueError(f"Invalid mode: {mode}. Please set the mod to 'image' or or 'video'.")

            # Open the CSV file with the specified filename and retrieve data
            data = self.open_csv(filename)

        return data

    @staticmethod
    def _parse_rows(rows, mode):
        data = []
        for index, row in enumerate(rows):
            # Skip the first iteration
            if index == 0:
                continue

            row_dict = {
                'keyword': row[0],
                'title_prompt': row[1],
                'description_prompt': row[2],
            }
            #Add 'tips_prompt' to the library if the mode is 'image'
            if mode == 'image':
                row_dict['tips_prompt'] = row[3]
            data.append(row_dict)
        return data


    def _get_google_creds(self):
        #specify the path to the JSON key file
        json_key_path = os.path.join(self.data_path, 'keyfile.json')

        #define the required OAuth2.0 scopes for Google Sheets API
        scopes = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']

        #create the credential object based on the JSON key File
        credentials = Credentials.from_service_account_file(json_key_path, scopes=scopes)

        return credentials


    def write_single_prompt(self, prompt):
        max_retries = 5  # Maximum number of retries
        retries = 0

        while retries < max_retries:
            try:
                response = g4f.ChatCompletion.create(
                    model=g4f.models.gpt_35_turbo,
                    messages=[{'role': 'user', 'content': prompt}]
                )

                if response and len(response.strip()) > 20:  # Ensure meaningful content
                    return response.strip('"')

            except Exception as e:
                self._log_error("Error generating prompt: ", e)
                time.sleep(2)  # Brief pause before retry
                retries += 1

        raise ValueError("Failed to generate valid prompt after multiple attempts")


    def write(self, row, mode):
        # Check if the mode is valid
        if mode not in [self.WRITER_MODE_1, self.WRITER_MODE_2]:
            raise ValueError(f"invalid mode: {mode}. Please choose between 'image' or 'video'.")

        # Initialize results dictionary with default values
        results = {
            'mode': mode,
            'file_path': '',
            'board_name': '',
            'pin_link': '',
        }

        def is_valid_content(content):
            # Add more robust validation checks here
            return content and "Model not found or too long input" not in content and len(content) > 20

        try:
            # Extract keywords from the row or set it to an empty string if not present
            results['keyword'] = row.get('keyword', '')

            # Write title and log the process
            self._log_message('Writing title...')
            title_prompt = row.get('title_prompt', '')
            title = self.write_single_prompt(title_prompt)
            while not is_valid_content(title):
                title = self.write_single_prompt(title_prompt)
            results['title'] = title.strip('"')

            # Write description and log the process
            self._log_message('Writing description...')
            description_prompt = row.get('description_prompt', '').replace('SELECTED TITLE',
                                                                           title if title else row.get('keyword', ''))
            description = self.write_single_prompt(description_prompt)
            while not is_valid_content(description):
                description = self.write_single_prompt(description_prompt)
            results['description'] = description.strip('"')

            if mode == self.WRITER_MODE_2:
                # Write tips for image and log the process
                self._log_message('Writing Tips...')
                tips_prompt = row.get('tips_prompt', '').replace('SELECTED TITLE',
                                                                 title if title else row.get('keyword', ''))
                tips = self.write_single_prompt(tips_prompt)
                while not is_valid_content(tips):
                    tips = self.write_single_prompt(tips_prompt)
                results['tips'] = tips.strip('"')
        except Exception as e:
            # Log an error if an exception occurs during writing
            self._log_error(f"Error while writing: ", e)
            return None

        # Determine the filename based on the mode and write the results to the corresponding CSV file
        filename = self.GENERATOR_DATA_FILE if mode == self.WRITER_MODE_2 else self.UPLOADING_DATA_FILE
        self.write_csv(results, filename)
        return results




