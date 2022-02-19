# Bank

## Aim of this programme
This application was developed as a homework. It simulates a bank transactions. At the end of each day, the programme generates a report of all the transactions made during that day and all available balances on the accounts in the bank. The instructions are read from bank.in

## Data structure used for storing information
All account numbers are 6-digit numbers which do not start with 0. Therefore, I store information in trie tree which ensures constant time complexity for searching for certain account.

## Operations
1. N - new account
2. Q - close account
3. I - increase account balance
4. D - decrease account balance

## Instruction format
Instructions have the following format: *account_number:operation:amount;*

## bank.in
Each line of **bank.in** represents one day. On one line there can be multiple instructions (bank transactions) for that day.

## bank.out
Days are separated by numbers of each day. In first block there is a summary of the transactions made during that day and the result of those transactions. In the second block there are listed all balances from open accounts.
