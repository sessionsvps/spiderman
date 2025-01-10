from dotenv import load_dotenv
from telethon.sync import TelegramClient, events
import os
import json
import asyncio

async def getListOfGroups(client):
    try:
        dialogs = await client.get_dialogs()
        groups_info = []
        for dialog in dialogs:
            if dialog.is_group or dialog.is_channel:
                entity = await client.get_entity(dialog.id)
                can_send_messages = entity.default_banned_rights is None or not entity.default_banned_rights.send_messages
                if can_send_messages:
                    group_info = {'group_id': dialog.id, 'group_name': dialog.title}
                    groups_info.append(group_info)

        return groups_info
    except Exception as e:
        print(e)
        return []
async def getMessagesFromGroup(client, group_id):
    try:
        all_messages = []
        async for message in client.iter_messages(group_id):
            try:
                all_messages.append(message)
            except:
                pass
        return all_messages
    except Exception as e:
        print(e)
        return []
async def logUserBot():
    load_dotenv()
    api_id = int(27438790)
    api_hash = "09899f5904f0fbe2ec5e6dbf80051b40"
    phone_number = "51981086510"
    session_name = "bot_spammer"
    client = TelegramClient(session_name, api_id, api_hash)
    await client.connect()
    if not await client.is_user_authorized():
        await client.send_code_request(phone_number)
        await client.sign_in(phone_number, input('Ingrese el código de verificación: '))
    await client.send_message("@spmspider", f'<b>Bot encendido</b>', parse_mode="HTML")
    spammer_group = int("-4741104355")

    while True:
        groups_info = await getListOfGroups(client)
        messages_list = await getMessagesFromGroup(client, spammer_group)
            
        try:
            await client.send_message("@spmspider", f"<b>CANTIDAD DE MENSAJES CONSEGUIDOS PARA PUBLICAR</b> <code>{len(messages_list)-1}</code>",parse_mode="HTML")
        except:
            pass
            
        try:
            for i in groups_info:
                if i['group_name'] not in ["Spam","Publicidad","🅜🅐🅡🅚🅔🅣 🅢🅟🅘🅓🅔🅡🅜🅐🅝","BINNERS PERU 🇵🇪","Trato Admin Metodo Panel Canva Edu","👨🏻‍💻🇵🇪𝙋𝙀𝙍𝙐 𝘼𝙔𝙐𝘿𝘼🇵🇪👩🏼‍💻","Trato Admin Deuda - 3 MESES SMARTFIT","REFERENCIAS INUYASHA","Bins","MeyMDS","🍬 servicios y referencias 🍬","Referencias fre sita 🍓","闩ᗪᗪㄩ乂 丂廾ㄖ尸","Referencias TIOUBER","Infinity Chek Chat","BINS PERU🇵🇪","NO PUBLICIDAD","CURSO COCKIES","Grupos y Canales de Compra/Venta VIP","INFINITY CHECKER","REFERENCIAS Shortnamekae🇵🇪","RESPALyaDO🇵🇪BINS PERU","➳𝒀𝑨𝑷𝑬 𝑫𝑬 𝑬𝑺𝑻𝑨𝑭𝑨𝑫𝑶𝑹𝑬𝑺 ✧","QUEMANDO ESTAFADORES","𝐏𝐄𝐑Ú 𝐀𝐘𝐔𝐃𝐀","Referencias Elmer 💸","🎭 CANAL MUNDO STREAMING PERÚ 🇵🇪","TU MARKETPLACE"]:
                    j=0
                    for message_spam in messages_list:
                        j+=1
                        resultado = True
                        try:
                            await client.forward_messages(i["group_id"], message_spam)
                        except Exception as error:
                            await client.send_message("@spmspider", f'<b>Error enviando mensajes a {i["group_id"]}</b> - <code>{i["group_name"]}<code>\nCausa:{error}',parse_mode="HTML")
                            resultado = False
                        if resultado:
                            await client.send_message("@spmspider", f'<b>Mensaje enviado a {i["group_id"]}</b> - <code>{i["group_name"]}</code>',parse_mode="HTML")  
                        else: break
                        await asyncio.sleep(10)
                        if j==34: break
            await client.send_message("@spmspider", f'<b>RONDA ACABADA</b>', parse_mode="HTML")
            await asyncio.sleep(300) 
        except:
            pass
    
            
if __name__ == "__main__":
    asyncio.run(logUserBot())