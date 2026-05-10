# Agnetic workshop

For my introduction to Agentic Programming workshop.

-- Paul Baumgarten

## Installation instructions

From the Github website:

* Clone this repo
* Click the green Code button
* Click the Codespaces tab
* Click Create codespace on main
* Now wait.

First build may take 3–5 minutes.

It will:

* Build your Dockerfile
* Pull Postgres image
* Install Node
* Install opencode
* Install Python deps

## Verify Environment

Once inside the Codespace terminal, test in this order.

```
# Test Python install
python --version

# Test OpenCode install
opencode --version

# Test Postgres is running
psql postgresql://postgres:postgres@postgres:5432/workshopdb
# At the prompt, \dt should say "Did not find any relations." which is correct as it is currently empty
# Then \q to quit

# Test Python can talk to the DB
python scripts/check_db.py

# Test the Flask app
cd app
python app.py

# Codespaces will pop up:
# “Port 5000 forwarded”
# Click Open in Browser
```

