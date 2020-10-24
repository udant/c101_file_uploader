import dropbox
class TransferData:
    
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'DSH1SkVi1J0AAAAAAAAAAaY-FMUACD3zdyEDjG-1fB5ZH0vRSTaNSjJt3Omz6ODb'
   # transferData = TransferData(access_token)

    file_from = input("file From:")
    file_to = input("file to:")  
    # The full path to upload the file to, including the file name

    # API v2
    TransferData(access_token).upload_file(file_from, file_to)
    print("Dropbox transfer completed")

if __name__ == '__main__':
    main()