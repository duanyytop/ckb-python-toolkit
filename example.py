from ckb.core.signer import sign_tx
from ckb.core.rpc import RPCClient
from ckb.core.hash import ckb_blake160
from ckb.core.hex_coder import hex_to_bytes, hex_from_bytes
from ckb.address.address import generateShortAddress, generateFullAddress
from coincurve import PublicKey, PrivateKey
import json

unsigned_raw_tx = {'version': '0x0', 'cell_deps': [{'out_point': {'tx_hash': '0xbd262c87a84c08ea3bc141700cf55c1a285009de0e22c247a8d9597b4fc491e6', 'index': '0x2'}, 'dep_type': 'code'}, {'out_point': {'tx_hash': '0xd346695aa3293a84e9f985448668e9692892c959e7e83d6d8042e59c08b8cf5c', 'index': '0x0'}, 'dep_type': 'code'}, {'out_point': {'tx_hash': '0x03dd2a5594ed2d79196b396c83534e050ba0ad07fa5c1cd61a7094f9fb60a592', 'index': '0x0'}, 'dep_type': 'code'}, {'out_point': {'tx_hash': '0xf8de3bb47d055cdf460d93a2a6e1b05f7432f9777c8c474abf4eec1d4aee5d37', 'index': '0x0'}, 'dep_type': 'dep_group'}], 'header_deps': [
], 'inputs': [{'previous_output': {'tx_hash': '0xad375e8c40fdf42187ecbec79f7ddcae72017ce7773a4762421f3f50722dccb0', 'index': '0x1'}, 'since': '0x0'}], 'outputs': [{'capacity': '0x31eb3c002', 'lock': {'code_hash': '0x9bd7e06f3ecf4be0f2fcd2188b23f1b9fcc88e5d4b65a8637b17723bbda3cce8', 'args': '0xed893ca482474e66b5779e57dc1d5281f9033e4f', 'hash_type': 'type'}, 'type': {'code_hash': '0xb1837b5ad01a88558731953062d1f5cb547adf89ece01e8934a9f0aeed2d959f', 'args': '0xf90f9c38b0ea0815156bbc340c910d0a21ee57cf0000003700000002', 'hash_type': 'type'}}], 'outputs_data': ['0x000000000000000000c000'], 'witnesses': ['0x']}

private_key = 'd52a6cb37ce90aed79a96ea9976668fbdbe16d6eac3611d5b15de388168da2c3'
public_key = PrivateKey.from_hex(private_key).public_key.format()
args = ckb_blake160(public_key)[2:]
address = generateShortAddress(args, network = "testnet")
print(address)

lock = {'code_hash': '9bd7e06f3ecf4be0f2fcd2188b23f1b9fcc88e5d4b65a8637b17723bbda3cce8', 'hash_type': 'type', 'args': args}
full_address = generateFullAddress(lock, network = "testnet")
print(full_address)

tx = sign_tx(unsigned_raw_tx, private_key)
print(tx)

rpc = RPCClient('https://testnet.ckb.dev/rpc')
tx_hash = rpc.request('send_transaction', tx)

print(tx_hash)
