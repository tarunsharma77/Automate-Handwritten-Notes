import pywhatkit as py
print("For writting paragraph Enter : para")
print("Otherwise given text printed")
take= input("")
if take=='para':
    c = False
    print("Enter your text here , use q/Q for quit")
    # Loop for taking input text
    while c == False:
        inp = input()
        # For quiting the loop
        if inp == "q" or inp == "Q":
            c = True
        # For writting all input in txt file
        else:
            with open("tanya.txt", "a") as f:
                f.write(f"{inp}\n")

        # Reading all Lines from txt file
    with open("tanya.txt", 'r') as f:
        lines = f.readlines()
        py.text_to_handwriting(f'{lines}', 'C:/Users/tarun/PycharmProjects/PythonTuts/writing_code.png')
        #          (string to be converted into handwritten image)                    (path to store the image as )
else:
    py.text_to_handwriting("Python is a programming language.\nPython can be used on a server to create web applications.", 'C:/Users/tarun/PycharmProjects/PythonTuts/cp.png')