import logging

from connectors.binance import BinanceClient
from connectors.bitmex import BitmexClient

from interface.root_component import Root


# Create and configure the logger object

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)  # Overall minimum logging level

stream_handler = logging.StreamHandler()  # Configure the logging messages displayed in the Terminal
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)  # Minimum logging level for the StreamHandler

file_handler = logging.FileHandler('info.log')  # Configure the logging messages written to a file
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)  # Minimum logging level for the FileHandler

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


if __name__ == '__main__':  # Execute the following code only when executing main.py (not when importing it)

    binance = BinanceClient("bea4bef75f7d7f5ff43d24a2d381ac84170008dc60ad8d7f435b5ce7fbb9ba24",
                            "7c10acb8a5d9a9fe3b0cdaf031b56548c959a5c1f469376df6d1f9a695924242",
                            testnet=True, futures=True)
    bitmex = BitmexClient("413eRVhNtrkUkgbA1Npyjv05", "ghh5mKdSueFOdl1Ic_EA7k5Y-YYlQzXoU6rz43rTOR4Y_a03", testnet=True)

    root = Root(binance, bitmex)
    root.mainloop()
