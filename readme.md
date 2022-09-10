# getCOLORed

# API that extracts 4 most dominant colors from any image.

Request
```
/api/v1/get : POST (File Upload)
```
Response
```
{
    'colors': [
        "hex1",
        "hex2",
        "hex3",
        "hex4"
    ]
}
```

### Tech Stack
- Python
- Flask
- colorgram
- webcolors
- requests
- sklearn
- scipy
- numpy