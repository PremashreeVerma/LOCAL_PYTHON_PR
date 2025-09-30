History_File="history.text"

def show_history():
    file=open(History_File,'r')
    lines=file.readline()
    if len(lines)==0:
        print("No history found !")
    else:
        for line in reversed (lines):
            print(line.strip())
    file.close()
    
def clear_history():
    file=open(History_File,'w')
    lines=file.close()
    print("History is cleared")
    
def save_to_history(equation, result):
    file=open(History_File, 'w')
    