# EaseHack 🔏
A simple project to help hackathon organizers sign certificates digitally.

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
### Tests
```bash
py -m unittest .\tests\test_sign_data.py
```

### Sample of contents in `.env` file 🔑
```
SIGNING_KEY=b'1GYwHGMGx/yJr4zrmzuOLLICXbJwqD/Rsv+NNbqF4ok='
VERIFY_KEY=b'skkijLTUSwleSUbnlIurnz4t0TsCgBlMt+toaaz//Jo='
```