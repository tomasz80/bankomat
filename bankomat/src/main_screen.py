import clear


class MainScreen:
    def display_message_and_get_input(self):
        print("Witamy w Bankomacie\nProsze wlozyc karte do bankomatu i postepowac zgodnie z instrukcja" )
        arg = raw_input( "(Nacisnij 's' aby zasymulowac umieszczenie karty w czytniku ) : ")
        clear.cls()
        return self.check_input(arg)

    def check_input(self, arg):
        if arg == 's':
            return 's'
        else:
            return False
