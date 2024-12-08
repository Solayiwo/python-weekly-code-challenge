#!/usr/bin/python3

class Smartphone:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
    
    def make_call(self, contact):
        call_response = f"Dailing {contact} ...."
        print(call_response)

    def send_message(self, contact, message):
        msg_response = f"Sending message to {contact}: {message}"
        print(msg_response)


class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, color, camera_megapixels):
        super().__init__(brand, model, color)
        self.camera_megapixels = camera_megapixels

    def take_photo(self):
        print(f"Taking a photo with {self.camera_megapixels}MP camera!")


smartphone = Smartphone("Sony", "Xperia", "white")
smartphone_brand = smartphone.brand
smartphone_model = smartphone.model
smartphone_color = smartphone.color

print(f"Smartphone brand is: {smartphone_brand}")
print(f"Smartphone model is: {smartphone_model}")
print(f"Smartphone color is: {smartphone_color}")

make_call = smartphone.make_call("John Smith")
message = smartphone.send_message("John Smith", "How are you?")


camera_phone = SmartphoneWithCamera("Apple", "iPhone 15", "grey", 48)
camera_phone.take_photo()
