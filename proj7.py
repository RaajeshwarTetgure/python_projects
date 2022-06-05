import smtplib 
try: 
    #Create your SMTP session 
    smtp = smtplib.SMTP('smtp.gmail.com', 587) 

   #Use TLS to add security 
    smtp.starttls() 

    #User Authentication 
    smtp.login("tetgureraajeshwar2@gmail.com","xcwimxlaxxrwayrk")

    #Defining The Message 
    message = "Heii , Hello Its Me Raaj" 

    #Sending the Email
    smtp.sendmail("tetgureraajeshwar2@gmail.com", "raajeshwar.tetgure@gmail.com",message) 

    #Terminating the session 
    smtp.quit() 
    print ("Email sent successfully!") 

except Exception as ex: 
    print("Something went wrong....",ex)


# from redmail import gmail
# gmail.user_name = "tetgureraajeshwar2@gmail.com"
# gmail.password = "xcwmxlaxxriwayrk"

# # Send an email
# gmail.send(
#     subject="An example email",
#     receivers=["praveentetgure@gmail.com"],
#     text="Hi, this is text body.",
#     html="<h1>Hi, this is HTML body.</h1>"
#         "{{myimg}}",
#     body_images={"myimg":"C:\coding Revision\Sample.jpg"}
# )
