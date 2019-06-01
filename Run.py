import Decoder_app
import ImageReader_app

def main():
    user_run = input('Decoder\nImageReader\n\nWhat app do you want to use? ')
    if user_run == 'Decoder':
        Decoder_app_filetype = input('\n\n\n.rar\n\nWhat files do you want to decode? ')
        print('\n\n\n')
        if Decoder_app_filetype == '.rar':
            
            Decoder_app.decoder.rar()
    if user_run == 'ImageReader':
        ImageReader_app_filetype = input('\n\n\nall\n\nWhat type of files do you want to read? ')
        if ImageReader_app_filetype == 'all':
            ImageReader_app.reader.all()

main()
