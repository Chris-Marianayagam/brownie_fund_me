from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)
from web3 import Web3


def deploy_fund_me():
    account = get_account()
    # print("Inside deploy_fund_me() and account = get_account")
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
        print("price_feed_address inside deploy_fund_me", price_feed_address)

    else:
        deploy_mocks()
        # price_feed_address = deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
        print("price_feed_address in else:", price_feed_address)

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )

    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
