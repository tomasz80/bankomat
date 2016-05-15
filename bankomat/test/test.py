import unittest
import src.account
import src.actions
import src.main

import sys
from StringIO import StringIO

from mock import patch

class BankomatTest(unittest.TestCase):

    # ACCOUNT
    def test_account_add_money(self):
        _account = src.account.Account()
        _account.add(100)
        self.assertEqual(_account.amount, 100)

    def test_account_amount_equal_0_when_account_created(self):
        _account= src.account.Account()
        self.assertEqual(_account.amount, 0)

    def test_account_subtract_valid_amount_of_money(self):
        _account = src.account.Account()
        _account.amount = 100
        _account.sub(100)
        self.assertEqual(_account.amount, 0)

    def test_account_get_higher_amount_of_money_than_account_contains_check_amount(self):
        _account = src.account.Account()
        _account.amount = 100
        _account.sub(1000)
        self.assertEqual(_account.amount, 100)

    def test_account_get_higher_amount_of_money_than_account_contains_check_value_returned(self):
        _account = src.account.Account()
        _account.amount = 100
        self.assertFalse(_account.sub(1000))


    # BALANCE
    @patch('__builtin__.raw_input')
    def test_display_current_account_balance(self, mock):
        mock.return_value= '1'
        balance = src.actions.Balance(50)
        out = StringIO()
        sys.stdout = out
        balance.display_message_and_get_input()
        output  = out.getvalue().strip();
        self.assertIn("Kwota srodkow pienieznych na koncie 50.00 PLN", output)

    def test_get_balance_back_to_select_action(self,):
        balance = src.actions.Balance(100)
        src.main.states.current = 'account_balance'
        balance.get_balance(src.main.states, 's')
        self.assertEqual(src.main.states.current, 'select_action')

    def test_get_balance_and_stay_at_current_state(self):
        balance = src.actions.Balance(100)
        src.main.states.current = 'account_balance'
        balance.get_balance(src.main.states, '')
        self.assertEqual(src.main.states.current, 'account_balance')

    #WITHDRAW
    #@patch('src.actions.Withdraw')
    def test_withdraw_money_back_to_select_action_state(self):
        withdraw = src.actions.Withdraw()
        states = src.main.states
        states.current = 'withdraw_money'
        withdraw.withdraw_money( states, 's', src.account.Account())
        self.assertEqual(src.main.states.current, 'select_action')

    def test_withdraw_money_not_digit(self):
        self.withdraw_money_prepare_test_conditions("daffadfa", "Nie poprawna kwota - sprobuj jeszcze raz")

    def test_withraw_money_inproper_value(self):
        self.withdraw_money_prepare_test_conditions("1234", "Nie poprawna kwota - sprobuj jeszcze raz")

    def test_withdraw_money_0_value(self):
        self.withdraw_money_prepare_test_conditions("0", "Nie poprawna kwota - sprobuj jeszcze raz")


    @patch('src.account.Account.sub')
    def test_not_enough_amount_of_money_to_withdraw(self, mock):
        mock.return_value = False
        self.withdraw_money_prepare_test_conditions("100", "Brak srodkow na koncie")

    @patch('src.account.Account.sub')
    def test_withdraw_money_when_account_has_enough_amount(self, mock):
        mock.return_value = "200"
        states = src.main.states
        states.current = 'withdraw_money'
        self.withdraw_money_prepare_test_conditions("100", "Pieniadze wyplacone :)")
        self.assertEqual(states.current, 'select_action')

    def withdraw_money_prepare_test_conditions(self, arg, expected_output):
        withdraw = src.actions.Withdraw()
        out = StringIO()
        sys.stdout = out
        withdraw.withdraw_money( src.main.states, arg, src.account.Account())
        displayed_output  = out.getvalue().strip();
        self.assertIn(expected_output, displayed_output)

    #DEPOSIT
    def test_insert_money_back_to_select_action(self):
        self.insert_money_prepate_test_condition('s', "", 'select_action')

    def test_insert_money_invalid_value(self):
        self.insert_money_prepate_test_condition(False, "Nie poprawna kwota wprowadzona", 'deposit_money')

    def test_insert_money_valid_value(self):
        self.insert_money_prepate_test_condition('100', "Kwota 100 wplacona", 'select_action')


    def insert_money_prepate_test_condition(self, arg, exp_output, exp_state):
        deposit = src.actions.Deposit()
        states = src.main.states
        states.current = 'deposit_money'
        out = StringIO()
        sys.stdout = out
        deposit.insert_money(states, arg, src.account.Account())
        displayed_output  = out.getvalue().strip();
        self.assertIn(exp_output, displayed_output)
        self.assertEqual(states.current, exp_state)

    #ACTION
    def test_select_get_money(self):
        #TODO
        pass
    def test_select_input_money(self):
        #TODO
        pass
    def test_select_get_account_balance(self):
        #TODO
        pass
    def test_select_back_to_idle(self):
        #TODO
        pass
    def test_incorrect_selection(self):
        #TODO
        pass

    #MAIN
    def test_idle_state_creates_new_account(self):
        #TODO
        pass

