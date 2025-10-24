import ollama as ai

ChatResponse = ai.ChatResponse
chat = ai.chat

# config
name = "USER"
command_prefix = "/"
msg_query_suffix = "> " # including a space is recommended
# end of config

def main():
    print("--Temp CHAT: all msgs are forgotten.--")
    print(ai.list())
    print("Select your model")
    model = input()
    while True:
        message = input(name+":"+ " " + msg_query_suffix)
        ans = send(model, message)
        if ans == 1:
            print("Stopping [!!!]")
            quit()
        else:
            print(ans)

def send(mod, msg):
    if command(msg) == 1:
        return 1
    response: ChatResponse = chat(model=mod, messages=[
        {
            'role': 'user',
            'content': msg

        },
    ])
    return (response['message']['content'])

def command(msg):
    if msg == (command_prefix + "exit") or msg == (command_prefix + "quit"):
        return 1

if __name__ == "__main__":
    main()
