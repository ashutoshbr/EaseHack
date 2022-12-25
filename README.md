# EaseHack 🔏
A simple project to help hackathon organizers sign certificates digitally.

## How it works ⚙️
1. Scan the QR code.
2. Set `encoded_data` in the query parameter to the data obtianed from QR.
3. Send the POST request to `localhost:8000/`
4. Response can be:
    - "Forged!" --> if the signature was tampered
    - "Certificate belongs to Someone" --> if the signature is genuine

## Running locally 🚀
1. Activate virtual environment.
2. Install all the packages.
3. Place the `.env` file in the root directory.
```bash
pip install -r requirements.txt
```
### Server 
```
uvicorn app.server:app --reload
```
### Generate new QRs
```bash
py -m unittest .\utils\qr_stuff.py
```
### Tests
```bash
py -m unittest .\tests\test_sign_data.py
```

### Sample of contents in `.env` file 🔑
```
SIGNING_KEY=15c805c23e3cbe1659a872bb27117f7433ebcc5b549baf43143ec35b922350de
VERIFY_KEY=0c27d89d44f424ac79278e218baa4a7c2842072c816a692ac0d84d84da03e003
```