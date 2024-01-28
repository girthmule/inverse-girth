import brain 
import ears
import mouth 

from WebChatGPT import ChatGPT
log = []

def body():
    global tasks
    global listeningToTask
    
    
    """
    Must have cookies from chatGPT profile saved to path
    """
    girth = ChatGPT("/home/mintymule/Documents/ai base/chat.openai.com.cookies.json")

    while True:
        command = ears.listen_for_command()
        Keyword = "smart"
        listeningToTask = False

        if command and Keyword in command:
             log.append("Girth Mule:"+ command +'\n')
             if listeningToTask:
                tasks.add(command)
                listeningToTask = False
                mouth.respond("Adding " + command + " to your task list. You have " + str(len(tasks)) + " currently in your list.")

             elif "add a task" in command:
                listeningToTask = True
                mouth.respond("Sure Girthy, what's the task?")
             elif "list tasks" in command:
                if tasks:
                    respond("Sure, Girthy. Your tasks are:")
                    for i, task in enumerate(tasks, 1):
                        mouth.respond(f"{i}. {task}")
                else:
                    mouthrespond("No tasks currently in your list, Girthy.")
             elif "delete task" in command:
                task_to_delete = command.replace("delete task", "").strip()
                delete_task(task_to_delete)
             elif "open google" in command:
                mouth.respond("Opening Girth's Internet")
                webbrowser.open("http://www.google.com")
            
             elif "exit" in command:
                mouth.respond("Goodbye Girth, the realest there ever was. Wake me up soon.")
                break
             elif "shut up" in command:
                 mouth.respond("Sorry Girth")
                 mouth.shutup()
            

             else:
                print("Contacting Mother Ship")
                
                import brain
                brain.run_bot(command, girth)
                brain.logger(command)

