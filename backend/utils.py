import os

def check_missing_columns(df, required_columns):
    """ Ensure the necessary financial columns exist in the uploaded CSV. """
    missing_cols = [col for col in required_columns if col not in df.columns]
    return missing_cols

def ensure_upload_folder_exists(folder_path):
    """ Create the upload folder if it doesn't exist. """
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
