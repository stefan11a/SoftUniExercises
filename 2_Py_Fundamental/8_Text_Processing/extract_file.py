file_location = input().split('\\')
file = file_location[-1]
filename, extension = file.split('.')
print(f'File name: {filename}')
print(f'File extension: {extension}')

