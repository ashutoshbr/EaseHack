# EaseHack 🔏
A simple project to aid with the creation and validation of digital signatures

[Frontend prototype 🖌️](https://github.com/ashutoshbr/EaseHack/blob/main/docs/frontend.md)
[Mobile APK 📲](https://github.com/SvarnimN/EaseHack-App/releases)
[Frontend Source Code 📃](https://github.com/SvarnimN/EaseHack-App)
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
### CLI
```py
python main.py
```
### Server 
```
uvicorn app.server:app --reload
```

### Sample of contents in `.env` file 🔑
```
PV_KEY=63c2195a0a01abf82b5f3241dfb1f79b067dc15bcbcb123438ce8175f9850fbd
PB_KEY=24e3d7f257d7fb24255b1dcfa2170fb111e2e38be9369897d8cf4270452becc4
```
