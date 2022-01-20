from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

DECIMALS = 8
STARTING_PRICE = 200000000000


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        print(f"The active network in get_account is {network.show_active()}")
        return accounts[0]
    else:
        print(f"The active network in ELSE get_account is {network.show_active()}")
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    print("len(MockV3Aggregator)", len(MockV3Aggregator))
    if len(MockV3Aggregator) <= 0:
        # constructor(uint8 _decimals, int256 _initialAnswer) public {
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
        # price_feed_address = mock_aggregator.address
        # return price_feed_address
        # print("price_feed_address inside deploy_mocks():", price_feed_address)
        print("Mocks Deployed!")
        # price_feed_address = mock_aggregator.address
        # price_feed_address = MockV3Aggregator[-1].address
