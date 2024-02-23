while True:
    import win32com.client as wincom
    speak=wincom.Dispatch("SAPI.spvoice") 
    x=input("enter the message  ")
    speak.speak(x)
         
    if (x == "q"):
        break
    
         
