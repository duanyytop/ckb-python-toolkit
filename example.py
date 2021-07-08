"""
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 example.py
"""


from ckb.transaction import extend_serialized_raw_transaction
import json

unsigned_raw_tx = {"version": "0x0", "cell_deps": [{"out_point": {"tx_hash": "0xbffab7ee0a050e2cb882de066d3dbf3afdd8932d6a26eda44f06e4b23f0f4b5a", "index": "0x1"}, "dep_type": "dep_group"}], "header_deps": ["0x"], "inputs": [{"previous_output": {"tx_hash": "0xa80a8e01d45b10e1cbc8a2557c62ba40edbdc36cd63a31fc717006ca7b157b50", "index": "0x0"}, "since": "0x0"}], "outputs": [{"capacity": "0x174876e800", "lock": {
    "code_hash": "0x9e3b3557f11b2b3532ce352bfe8017e9fd11d154c4c7f9b7aaaa1e621b539a08", "args": "0xe2193df51d78411601796b35b17b4f8f2cd85bd0", "hash_type": "data"}}, {"capacity": "0x474dec26800", "lock": {"code_hash": "0xe3b513a2105a5d4f833d1fad3d968b96b4510687234cd909f86b3ac450d8a2b5", "args": "0x36c329ed630d6ce750712a477543672adab57f4c", "hash_type": "data"}}], "outputs_data": ["0x", "0x"], "witnesses": [{"lock": "", "inputType": "", "outputType": ""}]}

tmp = []
extend_serialized_raw_transaction(tmp, unsigned_raw_tx)
serialized_raw_tx = ''.join('{:02x}'.format(x) for x in tmp)

print(serialized_raw_tx)
