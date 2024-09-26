from is_wire.core import Channel, Message

#Conncet to the broker
channel = Channel("amqp://guest:guest@10.10.0.91:5672")

message = Message()
#message.body = "Arthur@abacaxi na pizza é crime".encode('latin1')
message.reply_to = "Arthur"
message.correlation_id = 69

while True:
    #Broadcast message to anyone interested (subscribed)
    msg = input("Digite a mensagem:")
    dest = input("Digite o destinatário:")
    message.body = msg.encode('utf-8')
    channel.publish(message, topic=f"Aluno.{dest}")
