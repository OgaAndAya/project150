from tkinter import*
import random

root=Tk()
root.title("Random Countries and Capitals")
root.geometry("500x500")

enter_name= Entry(root)
enter_name.place(relx=0.5,rely=0.2, anchor= CENTER)

country_list= Label(root)
capital_list= Label(root)
random_number_country= Label(root)
random_number_capital= Label(root)

list_country= []
list_capital= []


def addFriend():
    country_list= ["Japan","United States","Taiwan","Italy"]
    append.country("France")
    capital_list= ["Tokyo","New York","Taipei","Procida"]
    append.capital("Bordeaux")
    friend_name= enter_name.get()
    list1.append(friend_name)
    country_list["text"]= "Country Name: "+ str(country_list)
    capital_list["text"]= "Capital Name: "+ str(capital_list)
    
def random_number():
    country_list= len(length1)
    country_list= random.sample(range(0,3))
    random_no= random.randint(0,length-1)
    random_country_label["text"]= str(random_no)
    
    generated_random_number= list1[random_no]
    lucky_friend["text"]= "Your Lucky Friends: "+ str(generated_random_number)
    
btn=Button(root,text= "Display Country and City Name", command= addFriend)
btn.place(relx=0.5, rely=0.3, anchor= CENTER)

country_list.place(relx=0.5,rely=0.4, anchor= CENTER)

btn=Button(root,text= "Display Country Name and City name Randomly", command= random_number)
btn.place(relx=0.5, rely=0.5, anchor= CENTER)

random_number_label.place(relx=0.5,rely=0.6, anchor= CENTER)
lucky_friend.place(relx= 0.5, rely=0.7, anchor = CENTER) 
root.mainloop()


