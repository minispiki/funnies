import ollama as ai

ChatResponse = ai.ChatResponse
chat = ai.chat

# config
name = "USER"
command_prefix = "/"
msg_suffix = "> " # including a space is recommended
# end of config

def main():
    print("--Temp CHAT: all msgs are forgotten.--")

    for m in ai.list()["models"]:
        print(m["model"])

    print("Select your model")
    model = input()
    while True:
        message = input("\n"+name+":"+ " " + msg_suffix)
        ans = send(model, message)
        commmandHandle(ans)


def send(mod, msg):
    if command(msg) == 1:
        return 1
    stream = chat(
        model=mod,
        messages=[{'role': 'user', 'content': msg}],
        stream=True,
    )

    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)

def command(msg):
    if msg == (command_prefix + "exit") or msg == (command_prefix + "quit"):
        return 1
    else:
        return 0 # non error

def commmandHandle(returnval):
    if returnval == 1:
        print("Stopping [?]")
        quit()

if __name__ == "__main__":
    main()
