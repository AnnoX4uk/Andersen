import json
import emoji
from flask import Flask, request


# TODO: make config file for service
sign = 'Made with ❤️  by AnnoX4uk\n'

# Big thx  MikeKozhevnikov for qrcode idea, i think it's awesome!
# Look his amazing repository

curl_funny_out = 'Big thx  MikeKozhevnikov for idea!' + '''
█████████████████████████████████████
█████████████████████████████████████
████ ▄▄▄▄▄ █▀▀ ██▀█▀▀  ▄▀█ ▄▄▄▄▄ ████
████ █   █ █▄▀██▀▀▀▄█▄█▄▄█ █   █ ████
████ █▄▄▄█ █ ▄ █ ██▀▄  ▀██ █▄▄▄█ ████
████▄▄▄▄▄▄▄█ █ ▀▄█ █▄▀ ▀▄█▄▄▄▄▄▄▄████
████▄▄█ █▀▄ █▀█  ▀ █ ▀▀█▀█ ▄▄▀▄▄▀████
████▀▀█  ▀▄▄ ▀▀  ▀██ ▄▀▄▄█▄▀▀▄  █████
████▄▀██▀▀▄▄█▀▄ █ █▄▄ █ ▄ ▄▀█▄█▄▄████
████▄▀▄▄▄█▄█▄▄█ █ ▀█▄  ▀ ▄▀██ ▄ ▄████
████▄ █▄▀▀▄ ▄  █ █▀▄▀▄▀▄▄▄▀ █▀█▄▀████
████▄█   ▀▄▄██▄▄ ▄▀▀█▀█▀▄▄ ▄███  ████
████▄██▄██▄▄▀ █▀█▀▄▄█▀█▀ ▄▄▄ █ ▀▀████
████ ▄▄▄▄▄ █▄█ ██▀▄█▀▄ █ █▄█ ▀▀▄▀████
████ █   █ █▀▄ ▀ ████▄█▀▄▄ ▄ ▀▀▀█████
████ █▄▄▄█ █▀▄▄█ ▀ █▀ ▄▄▀▄██ ▄▄▀▄████
████▄▄▄▄▄▄▄█▄██▄▄▄▄▄▄▄▄█▄██▄▄██▄█████
█████████████████████████████████████
█████████████████████████████████████
'''
funny_out_browser = '<iframe width="560" height="315"\
        src="https://www.youtube.com/embed/jofNR_WkoCE"\
        title="YouTube video player" frameborder="0" allow="accelerometer;\
        autoplay; clipboard-write; encrypted-media; gyroscope;\
        picture-in-picture" allowfullscreen></iframe>'


def emojiout(text):
    r = emoji.emojize(':' + text + ':')
    return(r.replace(':', ''))


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    # TODO: make somethink to work with GET
    if request.method == "GET":
        if 'curl' in request.user_agent.string:
            return (curl_funny_out)
        else:
            return(funny_out_browser)

    if request.method == "POST":
        try:
            data = request.get_json(force=True)
        except Exception as err:
            return('Can not convert your data to json\n')

        try:
            if data.keys().isdisjoint(['animal']):
                return ('Error while parse arguments, animal not found. Please try again.\
                     format: /{animal:"someanimal", sound:"anysound", count: "anycount"/}\n')
            if data.keys().isdisjoint(['sound']):
                return ('Error while parse arguments, sound not found Please try again.\
                     format: /{animal:"someanimal", sound:"anysound", count: "anycount"/}\n')
            if data.keys().isdisjoint(['count']):
                return ('Error while parse arguments, count not found. Please try again.\
                     format: /{animal:"someanimal", sound:"anysound", count: "anycount"/}\n')
            # TODO: need check that animal is animal, sound in a sound
            else:
                try:
                    if int(data['count']) < 1:
                        return (sign)
                except Exception as err:
                    print('Got Error: {} '.format(err))
                    return ('Server got error, can not convert count to integer\n')

        except Exception as err:
            print('Got error while rescv json args: {}\n'.format(err))

        animalsay = ''
        for i in range(0, int(data['count'])):
            animalsay = animalsay + \
                '{animal} says {sound}\n'.format(
                    animal=emojiout(data['animal']), sound=data['sound'])

        return (animalsay + sign)


if __name__ == "__main__":
    app.run()
