import json
import emoji
from flask import Flask, request


# TODO: make config file for service
sign = 'Made with ❤️  by AnnoX4uk\n'

def emojiout(text):
    r = emoji.emojize(':' + text + ':')
    return(r.replace(':', ''))

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # TODO: make somethink to work with GET
    if request.method == "GET":
        return 'Welcome to our zoo!\nWhat are you want to listen ?\n'

    if request.method == "POST":
        print(request.content_type)
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
