class Node:
    def __init__(self, data):
        self.data = data
class Bank:
    def __init__(self):
        self.tree = Node(None)
        self.tree.data = [None] * 10

    def construct_tree(self, depth, node):
        if (depth < 2):
            return
        nodes = [Node(None) for i in range(10)]
        node.data = nodes
        for i in range(6):
            self.construct_tree(depth - 1, node.data[i])
    
    def search_tree(self, number):
        digits = [0] * 6
        for i in range(5, -1, -1):
            digits[i] = number % 10
            number //= 10
        result = self.tree
        for j in range(6):
            if (result.data[digits[i]] == None):
                result.data[digits[i]] = Node(None)
                if (j < 5):
                    result.data[digits[i]].data = [None] * 10
            result = result.data[digits[i]]
    
        return result
    
    def get_all_balances(self, node, currentNumber = [0] * 6, position = 0, summarry = []):
        if (node == None or node.data == None):
            return
        if (position == 6):
            number = 0
            for i in range(6):
                number += currentNumber[i] * (10 ** i)
            summarry.append(str(number) + ":" + str(node.data))
            return
    
        for i in range(10):
            currentNumber[position] = i
            self.get_all_balances(node.data[i], currentNumber, position + 1, summarry)
        currentNumber[position] = 0
        if (position == 0):
            return summarry
    
    def create_account(self, number, balance):
        node = self.search_tree(number)
        if (node.data == None):
            node.data = balance
            return True
        else:
            return False
    
    def delete_account(self, number):
        node = self.search_tree(number)
        if (node.data == None):
            return False
        else:
            node.data = None
            return True
    
    def increase_balance(self, number, amount):
        node = self.search_tree(number)
        if (node.data == None):
            return False
        else:
            node.data += amount
            return True
    
    def decrease_balance(self, number, amount):
        node = self.search_tree(number)
        if (node.data == None):
            raise Exception("Account does not exist")
        elif (node.data - amount < 0) :
            raise Exception("Not sufficient balance")
        else:
            node.data -= amount

if __name__ == "__main__":
    transactions = open("bank.in", "r")
    text = transactions.readlines()
    log = open("bank.out", "w")
    transactions.close()
    
    bank = Bank()
    
    for j in range(len(text)):
        line = text[j]
        day = line.split(';')
        log.write("=== " + str(j + 1) + " ===\n")
        for i in range(len(day) - 1):
            command = day[i].split(':')
            account = command[0]
            code = command[1]
            amount = command[2]
    
            command_result = False
    
            if (code == "N"):
                command_result = bank.create_account(int(account), int(amount))
                if (not command_result):
                    log.write(day[i] + " chyba: ucet uz existuje!\n")
            elif (code == "Q"):
                command_result = bank.delete_account(int(account))
                if (not command_result):
                    log.write(day[i] + " chyba: ucet neexistuje!\n")
            elif (code == "I"):
                command_result = bank.increase_balance(int(account), int(amount))
                if (not command_result):
                    log.write(day[i] + " chyba: ucet neexistuje!\n")
            else:
                try:
                    bank.decrease_balance(int(account), int(amount))
                except Exception as ex:
                    if (ex.args[0] == "Account does not exist"):
                        log.write(day[i] + " chyba: ucet neexistuje!\n")
                    elif (ex.args[0] == "Not sufficient balance"):
                        log.write(day[i] + " chyba: nizky stav uctu!\n")
    
            if (command_result):
                log.write(day[i] + " OK\n")
    
        summary = bank.get_all_balances(bank.tree, summarry=[])
        log.write("======\n")
        for i in range(len(summary)):
            if (j == len(text) - 1 and i == len(summary) - 1):
                log.write(summary[i])
            else:
                log.write(summary[i] + "\n")
    log.close()
    