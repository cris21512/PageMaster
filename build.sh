source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
reflex init
reflex export --fronted-only
rm -rf public
Expand-Archive -Path "frontend.zip" -DestinationPath "public"
rm -f frontend.zip 
deactivate