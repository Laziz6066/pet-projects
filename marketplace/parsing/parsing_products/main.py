import vlc
from gtts import gTTS


def assitant(mytext):
    audio = gTTS(text=mytext, lang="ru", slow=False)
    audio.save("example.mp3")
    audio_file = "example.mp3"
    p = vlc.MediaPlayer(audio_file)
    p.play()
    while True:
        if p.get_state() == vlc.State.Ended:
            break
    p.release()


    # product_name = i.find('h2', class_='product-card__brand-wrap').text
    # product_image = i.find('img', class_='j-thumbnail').get('src')
    # product_price = i.find('p', class_="product-card__price price").text.strip()


# product_descriptions.append({
#     'name': product_name,
#     'image': product_image,
#     'price': product_price,
#     'description': product_description
# })
#
# with open('C:/Users/laziz/PycharmProjects/pet-projects/marketplace/static/result_list.json', 'w', encoding='utf-8') as file:
#     json.dump(product_descriptions, file, indent=4, ensure_ascii=False)