import time

class RescueChatbot:
    def __init__(self):
        self.location = ""
        self.status = "Safe"
        self.help_needed = False

    def welcome_message(self):
        print("Rescue Team: Hello, how can we assist you today?")
        print("Girl: I'm in danger, I need help!")
        time.sleep(1)

    def start_conversation(self):
        self.welcome_message()
        self.girl_in_trouble()

    def girl_in_trouble(self):
        print("\nGirl: I'm in trouble, please send help!")
        self.help_needed = True
        time.sleep(1)
        self.ask_location()

    def ask_location(self):
        print("\nRescue Team: We are sending help, but we need your location.")
        location = input("Girl: (Please share your location) ")

        self.location = location
        print(f"\nRescue Team: Location received: {self.location}. Help is on the way.")
        self.provide_updates()

    def provide_updates(self):
        print("\nRescue Team: We are tracking your location and will reach you shortly.")
        time.sleep(2)
        self.confirm_rescue()

    def confirm_rescue(self):
        print("\nRescue Team: Are you in a safe place? Have you seen any rescue personnel?")
        status = input("Girl: (Yes/No) ")

        if status.lower() == "yes":
            self.status = "Safe"
            print("\nRescue Team: Glad you're safe! Stay where you are, we will assist you shortly.")
        else:
            print("\nRescue Team: We are on our way. Please stay calm, help is almost there.")
            self.update_status()

    def update_status(self):
        print("\nRescue Team: If the situation worsens, type 'Help' for immediate assistance.")
        status_update = input("Girl: (Type 'Help' to request immediate assistance) ")

        if status_update.lower() == 'help':
            print("\nRescue Team: We have prioritized your case. Help is on its way.")
            self.status = "Urgent"
            self.send_urgent_message()

    def send_urgent_message(self):
        print("\nRescue Team: We are sending backup. Stay strong. We are almost there.")
        print("Rescue Team: Sending backup unit to your location.")
        time.sleep(2)
        print(f"\nRescue Team: Your situation is marked as {self.status}. We will get you out of there soon!")

    def end_conversation(self):
        print("\nRescue Team: We have successfully reached your location. Stay calm, help is here.")
        print("Rescue Team: Thank you for staying in touch. We're happy to help you.")

def main():
    chatbot = RescueChatbot()
    chatbot.start_conversation()
    chatbot.end_conversation()

if __name__ == "__main__":
    main()
