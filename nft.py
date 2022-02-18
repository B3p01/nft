#nft.py
from thirdweb import ThirdwebSdk, SdkOptions, MintArg
from dotenv import loadenv
import os

#choose your network
network = "https://rinkeby-light.eth.linkpool.io/"

#create the object
sdk = ThirdwebSdk(SdkOptions(), network)

#use the '.env' file inside Python
loadenv()
PRIVATE_KEY  = os.getenv('PRIVATE_KEY')\

#connect wallet via the private key stored in '.env' file
sdk.set_private_key("PRIVATE_KEY")

#pick module and enter smart contract address
nft_smart_contract_address = "0x1722eE39D8E3e3bE5EfD58Cd3AB1b9060BC058f9"
nft_module = sdk.get_nft_module(nft_smart_contract_address)

#Mint NFT on smartcontract
name_nft = "Monkey"
description_nft = "In monkey's we trust"
image_nft = "https://i.imgur.com/sizejunky.jpeg"
prop = {}

#minting with details
nft_module.mint(MintArg(name=name_nft, description=description_nft, image_uri=image_nft, properties=prop))

#check your balance to see if the nft was minted
print(nft_module.balance())