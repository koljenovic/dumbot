- $$$ DUM฿0T v0.1.3alpha - Bittrex Terminal $$$ -
Symbols and pairs MUST be written with $ sign as first character.
Example: BAL $XRP or TICK $BTC-XRP Help: Type ? or help for assistance.
QUIT or CTRL+C to stop the execution and exit.
License: CC BY-SA @Mangefort 2017
BTC Donations: 1LFZxGGjWVtQUvzm1vwyDWiG84uGA7Yag3

BAL $SYM - check current wallet balance for $SYM.
BALS - print all non-zero balances.
TICK $SYM-SYM - get latest ticker data.
NTICK $SYM-SYM - loop latest ticker data each 10s, CTRL-C to break.
LIST - list all open orders and assign local order ID's
        the first number for each order is it's ID
        you will use this ID to cancel orders.
SELL $SYM-SYM #QTY @RATE - limit sell #QTY of $SYM-SYM at @RATE.
        #QTY - #[13.37|MAX] decimal or MAX for maximum amount
        @RATE - @[0.07|L|A|B] decimal or L for Last, A for Ask or B for Bid
        Example: SELL $BTC-ETH #13.37 @0.1
                 SELL $BTC-ETH #MAX @A
BUY $SYM-SYM #QTY @RATE - limit buy #QTY of $SYM-SYM at @RATE.
        #QTY - #[13.37|MAX] decimal or MAX for maximum amount
        @RATE - @[0.07|L|A|B] decimal or L for Last, A for Ask or B for Bid
        Example: BUY $BTC-ETH #13.37 @0.08
                 BUY $BTC-ETH #MAX @B
CANCEL :ID - cancel the order with local :ID number (LIST)
/ - repeats the last issued command.
