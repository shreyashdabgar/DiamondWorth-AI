## steps for coustem exception
# 1. import sys
# 2. cerate one def function with two arguments error and error_details:sys
# 3. in def function use _,_,exc_tb = error_details.exc_info() to get file name and line number
# 4. use file_name = exc_tb.tb_frame.f_code.co_filename to get file name
# 5. created one variable for error , in which file , and at which line number and store into that variable
# 6. return that variable

# 7. create one class with name coustemexception and inherit from Exception
# 8. crdeated one def init function becuase we want to use it as pacakge and import everywhere, and take two values error and error_details:sys from def error function which we created above
# 9. use super.__init__(error) to take error from def error and put into init class
# 10. use self.error = why_error(error_details=error_details, error = error) to take error and error_details from def error and put into init class
# 11. create one def str function to return error in string format


import sys 


def why_error(error, error_details: sys):
    _, _, exc_tb = error_details.exc_info()  # this ( _,_, ) means exc_info() return 3 values but we dont need first two thats why we use ( _ ) to ignore them
    file_name = exc_tb.tb_frame.f_code.co_filename  # for finding file name which file we get error from
    error_message = f"Error in file: {file_name} at line number: {exc_tb.tb_lineno} and the error is: {str(error)}"
    return error_message

class CustomException(Exception):
    def __init__(self, error, error_details: sys):  # we are taking error and error_details from def error and put into init class because init is package which is used as package and import everywhere
        super().__init__(error)  # we are taking error from def error and put into init class
        self.error = why_error(error_details=error_details, error=error)

    # return error in string format so we can understand easily and read easily 
    def __str__(self):
        return self.error
    
            