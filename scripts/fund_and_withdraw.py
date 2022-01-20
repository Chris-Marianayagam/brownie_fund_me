from brownie import network, config, accounts, MockV3Aggregator, FundMe
from scripts.deploy import deploy_fund_me
from scripts.helpful_scripts import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    # fund_me = FundMe.deploy({"from": account})
    entrance_fee = FundMe.getEntranceFee()
    print(entrance_fee)
    print(f"The current entry fee is {entrance_fee}")
    print("Funding")
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.fund({"from": account})


def main():
    fund()
    withdraw()
