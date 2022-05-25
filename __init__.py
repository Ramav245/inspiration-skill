from mycroft import MycroftSkill, intent_file_handler


class Inspiration(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('inspiration.intent')
    def handle_inspiration(self, message):
        self.speak_dialog('inspiration')


def create_skill():
    return Inspiration()

