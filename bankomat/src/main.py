import main_screen
import actions
import account

from fysom import Fysom

states = Fysom({'initial': 'idle',
                'events':[
                    {'name': 'insert_card', 'src': 'idle', 'dst':'select_action'},
                    {'name': 'get_money', 'src':'select_action', 'dst':'withdraw_money'},
                    {'name': 'input_money', 'src':'select_action', 'dst':'deposit_money'},
                    {'name': 'get_account_balance', 'src':'select_action', 'dst':'account_balance'},
                    {'name':'back_select_action', 'src':[ 'withdraw_money', 'deposit_money', 'account_balance'], 'dst':'select_action'},
                    {'name':'back_to_idle', 'src':'select_action', 'dst':'idle'}
                ]})

def handle_select_action():
    _actions = actions.Actions()
    selections = _actions.display_message_and_get_input()
    _actions.select(states, selections)


def handle_get_money(account):
    withdraw = actions.Withdraw()
    money_amount = withdraw.display_message_and_get_input()
    withdraw.withdraw_money(states, money_amount, account)

def handle_insert_money(account):
    deposit = actions.Deposit()
    amount = deposit.display_message_and_get_input()
    deposit.insert_money(states, amount, account)


def handle_get_balance(account):
    balance = actions.Balance(account.amount)
    res = balance.display_message_and_get_input()
    balance.get_balance(states, res)


def handle_idle():
    _main_screen = main_screen.MainScreen()
    if _main_screen.display_message_and_get_input():
        states.trigger('insert_card')
        return account.Account()


def main():
    while 1:
        #IDLE
        if states.current == 'idle':
            account = handle_idle()

        # SELECT ACTION
        if states.current == 'select_action':
            handle_select_action()

        #GET_MONEY
        if states.current == 'withdraw_money':
            handle_get_money(account)

        #INPUT_MONEY
        if states.current == 'deposit_money':
            handle_insert_money(account)

        #BALANCE
        if states.current == 'account_balance':
            handle_get_balance(account)

if __name__ == "__main__":
    main()