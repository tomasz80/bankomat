import clear

class Actions:
    def display_message_and_get_input(self):
        print("1. Wybierz pieniadze")
        print("2. Wplac pieniadze")
        print("3. Sprawdz stan konta")
        print("Nacisnij 's' aby zakonczyc sesje i wylogowac sie")
        arg = raw_input("Wybierz jedna z dostepnych opcji : ")
        clear.cls()
        return arg

    def select(self, states, selections):
        if selections == '1':
            states.trigger('get_money')
        elif selections == '2':
            states.trigger('input_money')
        elif selections == '3':
            states.trigger('get_account_balance')
        elif selections == 's':
            states.trigger('back_to_idle')
        else:
            print "Nie poprawny wybor"
            states.current ='select_action'

class Balance:
    def __init__(self, amount):
        self.amount = amount

    def display_message_and_get_input(self):
        print "Kwota srodkow pienieznych na koncie %.2f PLN" % self.amount
        print "Nacisnij 's' aby powrocic do poprzeniego menu"
        arg = raw_input()
        clear.cls()
        return arg

    def get_balance(self, states, arg):
        if arg == 's':
            states.trigger('back_select_action')
        else:
            states.current ='account_balance'


class Withdraw:
    def display_message_and_get_input(self):
        print "Prosze podac kwote do wyplaty (dostepne nominaly to : 10, 20, 50, 100, 200 PLN) "
        arg = raw_input("lub nacisnij 's' aby powrocic do poprzeniego menu : ")
        clear.cls()
        return arg

    def withdraw_money(self, states, arg, account):
        if arg == 's':
            states.trigger('back_select_action')
        elif not(arg.isdigit()) or len(arg) < 2 or arg[-1] !=  "0":
            print "Nie poprawna kwota - sprobuj jeszcze raz"
            states.current = 'withdraw_money'
        else:
            res = account.sub(int(arg))
            if res == False:
                print "Brak srodkow na koncie"
            else:
                print "Pieniadze wyplacone :)"
                states.trigger('back_select_action')

class Deposit:
    def display_message_and_get_input(self):
        print "Prosze wlozyc pieniadze do bankomatu i wprowadzic kwote"
        print "lub nacisnij 's' aby powrocic do poprzedniego menu"
        arg = raw_input()
        clear.cls()
        return arg

    def insert_money(self, states, arg, account):
        if arg == 's':
            states.trigger('back_select_action')
        elif arg == False:
            print "Nie poprawna kwota wprowadzona"
            states.current = 'deposit_money'
        else:
            account.add(arg)
            print "Kwota %s wplacona" % arg
            states.current = 'select_action'

