from cryptography.fernet import Fernet
def write_key():
    key=Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)



def load_key():
    file=open("key.key","rb")
    key=file.read() 
    file.close()
    return key 


master_pwd=input("What is the master key?")
key=load_key()+master_pwd.encode()
fer=Fernet(key)



def view():
    with open("password.txt","r") as f:
        for line in f.readlines():
            data=(line.rstrip())
            user,pwd=data.split("|")
            print("User:",user,",Password:",str(fer.decrypt(pwd.encode())))




def add():
    name=input("Account name:")
    pwd=input("Password:")
    with open("password.txt","a") as f:
        f.write(name+"|"+str(fer.encrypt(pwd.encode()))+"\n")

while True:
    mode=input("Would you like to add new pass or view existing ones(view,add or press q to quit)").lower()

    if mode=="q":
        quit()

    if mode=="view":
        view()

    elif mode=="add":
        add()
    else:
        print("Invalid mode.")
        continue
