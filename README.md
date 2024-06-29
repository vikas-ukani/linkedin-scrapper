

### Scrap companies details from LinkedIn based on Search Terms



### Installation Setup 

#### Create virtual environment
```bash
python3 -m venv env
```

#### Move to environment
```bash
source env/bin/activate
```

#### Install Dependency from requirment.txt file
```bash
pip install -r requirments.txt
```

---- 

#### SET CREDENTIALS AND SEARCH TERM
```python

# AUTH CREDENTIALS
LINKEDIN_EMAIL = 'LINKEDIN_EMAIL'
LINKEDIN_PASSWORD = 'LINKEDIN_PASSWORD'

# Make sure to update search term in array format. => ["Search anything inside braces."]
SEARCH_TERMS =  ["staffing recruiting", "recruting agencies"]
```

-- Update the serch terms in `main.py file`
#### Run the script 
```bash
python main.py
```

Now it will open the browser and start scrapping.

### VIDEO EXAMPLE 
[![Watch the video](./resource/sample-video.mp4)](./resource/sample-video.mp4)