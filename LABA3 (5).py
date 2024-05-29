class MailServer:
    def __init__(self, name):
        self.name = name
        self.users = {}

    def add_user(self, user):
        self.users[user] = []

    def send_mail(self, recipient_server, recipient_user, message):
        if recipient_server in servers_list:
            recipient_server_obj = servers_list[recipient_server]
            if recipient_user in recipient_server_obj.users:
                recipient_server_obj.users[recipient_user].append(message)
                print(f"Message sent to {recipient_user} on {recipient_server}")
            else:
                print(f"User {recipient_user} not found on {recipient_server}")
        else:
            print(f"Server {recipient_server} not found")

    def get_mail(self, user):
        if user in self.users:
            messages = self.users[user]
            del self.users[user]
            return messages
        else:
            return []

class MailClient:
    def __init__(self, server, user):
        self.server = server
        self.user = user

    def receive_mail(self):
        messages = servers_list[self.server].get_mail(self.user)
        return messages

    def send_mail(self, recipient_server, recipient_user, message):
        servers_list[self.server].send_mail(recipient_server, recipient_user, message)

# Создание списка серверов
servers_list = {}

# Пример использования
server1 = MailServer("Server1")
server2 = MailServer("Server2")
servers_list["Server1"] = server1
servers_list["Server2"] = server2

server1.add_user("User1")
server2.add_user("User2")

client1 = MailClient("Server1", "User1")
client2 = MailClient("Server2", "User2")

client1.send_mail("Server2", "User2", "Hello from User1")
received_messages = client2.receive_mail()
print(received_messages)
