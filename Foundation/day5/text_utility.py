def read(str_file_path):
    '''
    Get all content from text file path
    :param str_file_path: text file path
    :return: content from text file path
    '''
    file = open(str_file_path, 'r')
    text = file.read()
    file.close()
    return text

def write(str_file_path, content):
    '''
    Write content data to text file path
    :param str_file_path: text file path to write
    :param content: content text
    '''
    file = open(str_file_path, 'w')
    file.write(content)
    file.close()

def get_number_of_line(str_file_path):
    '''
    Get number of line from file path
    :param str_file_path: text file path
    :return:
    '''
    return len(read(str_file_path).split('\n'))

def get_number_of_word(str_file_path):
    '''
    Get number of word from file path
    :param str_file_path: text file path
    :return: Number of word
    '''
    return len(read(str_file_path).split())

def get_number_of_character(str_file_path):
    '''
    Get number of character from file path
    :param str_file_path: text file path
    :return: Number of character
    '''
    return len(read(str_file_path))

def erase(str_file_path):
    '''
    Delete content file
    :param str_file_path: text file path
    '''
    write(str_file_path, '')