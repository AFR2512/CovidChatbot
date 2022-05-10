#Python libraries that we need to import for our bot
import random
from flask import Flask, request
from pymessenger.bot import Bot
import os
import chat 


app = Flask(__name__)
ACCESS_TOKEN = "EAACB6tLshnkBAIkyN6DRsvUADWKIgKHg3oZBvm5SmUeIxhtblYodpdJlffNAziRHAitmgcrArJL0RRxshWRf4VtbVQgVPr5ZCIcYIcUrKGvGfh7ebW9fs77vZCZABMqvu8FTS4GO11SSVw0ilWKZCpC38DW3kPiZAhRQGKTwZAvogZDZD"
VERIFY_TOKEN = "2f202256a96039de53867dfaaa80dd619bb9964350f4ed6ed29593662ef61d023ac58a209ddb221f64a9c11758872fdce701244cf934cad5192f6ee6666afb90"
bot = Bot (ACCESS_TOKEN)


@app.route("/", methods=['GET'])
def verify_fb_token():
	if request.args.get('hub.verify_token') == VERIFY_TOKEN:
		return request.args.get("hub.challenge")
	return 'Invalid verification token'



@app.route("/", methods=['POST'])
def receive_message():
	data = request.get_json()
	event = data['entry'][0]['messaging']
	for msg in event:
		text = msg['message']['text']
		sender_id = msg['sender']['id']
		response = chat.choix(text)
		send_message(sender_id,response)
	return "Message Processed"


def send_message(recipient_id, response):
	bot.send_text_message(recipient_id,response)
	return "success"

@app.route('/',methods = ['GET'])
def index():
	return "Bonjour je suis CovidBot"


if __name__ == "__main__":
	app.run(host="0.0.0.0")



