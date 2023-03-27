# qs_interview
There are three programming questions of QSearch's interview.

### Q1: Simple Math Parser
Simple math calculator for nonzero integers.
```
python3 math_parser.py
```

### Q2: API Server (coded by chatgpt)
First, Run the API server:
```
python3 api_server.py
```

Next, input width and height to modify parameters of the url, then you will access the corresponding image through this url.  
Example (width:400, height: 300): http://localhost:8000/image?width=400&height=300


### Q3: Unit/E2E Testing for API Server
Open the API server: 
```
python3 api_server.py
```
Then run the API testing on other window:
```
python3 api_test.py
```
Unit testing will test the result with valid and invlid parameters by requests method. E2E testing will test API through selenium packages.  
Note: please replace 'chromedriver' by your browser's version.
