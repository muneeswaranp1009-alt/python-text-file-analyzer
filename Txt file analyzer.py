import os

current_file = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_file,"text.txt")

def txt_file_analyze(file_path):
    try:
        with open(file_path,'r',encoding='utf-8') as file:
            content = file.read()
            
            tot_char =  len(content)
            tot_words = len(content.split())
            num_lines = len(content.split('\n'))
            
            
            print(f"\n--- File Analysis: {file_path} ---\n")
            print(f"Total Lines      : {num_lines}")
            print(f"Total Words      : {tot_words}")
            print(f"Total Characters : {tot_char}\n")
            
    except FileNotFoundError :
        print("\nError : File not Found,Check Again!")
    except Exception as e :
        print(f"\n Error : {e}")
        
txt_file_analyze(file_path)