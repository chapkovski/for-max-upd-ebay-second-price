from channels import Group
from channels.sessions import channel_session
import random
from .models import Player, Group as OtreeGroup, Constants
import json
import time


def ws_connect(message, group_name):
    Group(group_name).add(message.reply_channel)



# Connected to websocket.receive
def ws_message(message, group_name):
    group_id = group_name[5:]
    print('GROUP ID', group_id)
    print('PLAYER::::', message['text'])
    jsonmessage = json.loads(message.content['text'])
    curbuyer_id = jsonmessage['id']
    curbuyer_id_in_group = jsonmessage['id_in_group']
    cur_player_bid = int(jsonmessage['cur_player_bid'])
    mygroup = OtreeGroup.objects.get(id=group_id)
    senderplayer =Player.objects.get(id_in_group=curbuyer_id_in_group,
                                     group=mygroup)
    senderplayer.price = cur_player_bid
    senderplayer.save()
    # Logic to handle the bids
    if mygroup.price < cur_player_bid:
        mygroup.price = cur_player_bid
        mygroup.winner = curbuyer_id_in_group
    mygroup.save()
    # time_left = round(mygroup.auctionenddate - now)
    textforgroup = json.dumps({
                                "price": mygroup.price,
                                "winner": mygroup.winner,
                                })
    Group(group_name).send({
        "text": textforgroup,
    })



# Connected to websocket.disconnect
def ws_disconnect(message, group_name):
    Group(group_name).discard(message.reply_channel)
