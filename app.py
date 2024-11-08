import os
import datetime
from flask import Flask, redirect, url_for, session, render_template, request
from authlib.integrations.flask_client import OAuth
import subprocess

# Set environment variables for GitHub OAuth (Replace with your actual values)
os.environ['GITHUB_CLIENT_ID'] = 'Ov23liy0PPSPZMZYeHN4'
os.environ['GITHUB_CLIENT_SECRET'] = '57e1101894d535278fe4afdf56344daf39c840d6'

# Initialize the Flask app and OAuth object
app = Flask(__name__)

# Secret key for session management
app.secret_key = os.urandom(24)

# Configure session to persist correctly
app.config['SESSION_COOKIE_NAME'] = 'flask_oauth_session'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'  # Store session in filesystem
oauth = OAuth(app)

# GitHub OAuth setup
github = oauth.register(
    name='github',
    client_id=os.getenv('GITHUB_CLIENT_ID'),
    client_secret=os.getenv('GITHUB_CLIENT_SECRET'),
    authorize_url='https://github.com/login/oauth/authorize',
    access_token_url='https://github.com/login/oauth/access_token',
    client_kwargs={'scope': 'repo'},
)

@app.route('/')
def index():
    # Main page with form to input repository details
    return render_template('index.html')

@app.route('/login')
def login():
    # GitHub OAuth redirect
    return github.authorize_redirect(redirect_uri=url_for('authorized', _external=True))

@app.route('/logout')
def logout():
    # Logout user
    session.pop('github_token', None)
    session.pop('github_username', None)  # Remove username session
    return redirect(url_for('index'))

@app.route('/login/authorized')
def authorized():
    # Handle OAuth callback and retrieve user info
    token = github.authorize_access_token()
    session['github_token'] = token

    user_info = github.get('https://api.github.com/user')
    user_data = user_info.json()
    name = user_data.get('name', 'No name provided')
    login = user_data.get('login', 'No username provided')
    avatar_url = user_data.get('avatar_url', '')

    # Get repositories
    repos_url = user_data.get('repos_url', '')
    repos_info = github.get(repos_url)
    repos_data = repos_info.json()

    # Store GitHub username in session for later use
    session['github_username'] = login

    # Render profile page with list of repositories
    return render_template('profile.html', name=name, login=login, avatar_url=avatar_url, repos_data=repos_data)

@app.route('/generate_commits', methods=['POST'])
def generate_commits():
    # Get user info from session
    token = session.get('github_token')
    if not token:
        return redirect(url_for('login'))

    # Get the authenticated user's GitHub username from their token
    github_user = github.get('https://api.github.com/user', token=token)
    github_user_data = github_user.json()
    username = github_user_data['login']  # GitHub username
    
    # Get selected repository name from form input
    repo_name = request.form['repo_name']
    total_days = int(request.form['total_days'])
    commit_frequency = int(request.form['commit_frequency'])

    # Construct the correct repository link
    repo_link = f"https://github.com/{username}/{repo_name}.git"  # User's own repo

    # Initialize git repository
    os.system("git init")

    # Add the correct remote URL
    os.system(f"git remote set-url origin {repo_link}")

    # Generate commits logic
    now = datetime.datetime.now()
    pointer = 0
    ctr = 1
    for day in range(total_days, 0, -1):
        for commit in range(commit_frequency):
            commit_date = now + datetime.timedelta(days=-pointer)
            formatted_date = commit_date.strftime("%Y-%m-%d")
            
            # Write to commit.txt
            with open("commit.txt", "a") as f:
                f.write(f"commit {ctr}: {formatted_date}\n")
            
            # Commit with date
            os.system("git add .")
            os.system(f'git commit --date="{formatted_date} 12:15:10" -m "commit {ctr}: {formatted_date}"')
            ctr += 1
        
        pointer += 1

    # Push commits to the selected GitHub repository
    os.system(f"git push -u origin main --force")

    return "Commits generated and pushed successfully to the selected repository!"

@app.route('/generate_commits_for_public', methods=['POST'])
def generate_commits_for_public():
    # Generate commits for public repositories as well
    token = session.get('github_token')
    if not token:
        return redirect(url_for('login'))

    repo_name = request.form['repo_name']
    total_days = int(request.form['total_days'])
    commit_frequency = int(request.form['commit_frequency'])

    # Use a public repository for commit generation
    repo_link = f"https://github.com/{repo_name}.git"

    # Initialize git repository
    os.system("git init")

    # Add the correct remote URL
    os.system(f"git remote set-url origin {repo_link}")

    # Generate commits logic
    now = datetime.datetime.now()
    pointer = 0
    ctr = 1
    for day in range(total_days, 0, -1):
        for commit in range(commit_frequency):
            commit_date = now + datetime.timedelta(days=-pointer)
            formatted_date = commit_date.strftime("%Y-%m-%d")
            
            # Write to commit.txt
            with open("commit.txt", "a") as f:
                f.write(f"commit {ctr}: {formatted_date}\n")
            
            # Commit with date
            os.system("git add .")
            os.system(f'git commit --date="{formatted_date} 12:15:10" -m "commit {ctr}: {formatted_date}"')
            ctr += 1
        
        pointer += 1

    # Push commits to the selected GitHub repository
    os.system(f"git push -u origin main --force")

    return "Commits generated and pushed successfully to public repo!"

if __name__ == '__main__':
    app.run(debug=True)
