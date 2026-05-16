# GitHub Push Instructions

## Step-by-Step Guide to Push to GitHub

### Prerequisites
- GitHub account (create one at https://github.com if you don't have one)
- Git installed on your system
- Personal Access Token (PAT) or SSH key configured

---

## Option 1: Using Personal Access Token (PAT) - RECOMMENDED

### Step 1: Create a Personal Access Token
1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Name it: `olg-web-automation-token`
4. Select scope: `repo` (full control of private repositories)
5. Click "Generate token"
6. **COPY THE TOKEN** (you won't see it again!)

### Step 2: Create Repository on GitHub
1. Go to https://github.com/new
2. Repository name: `olg-web-automation`
3. Description: `Professional Web Automation Test Framework - Part 1 & Part 2 Tests`
4. Choose **Public** (required for submission)
5. Do NOT initialize with README (we have one)
6. Click "Create repository"

### Step 3: Push Local Repository

```powershell
cd C:\Users\ujjwa\Desktop\olg\olg-web-automation

# Add remote origin
git remote add origin https://github.com/YOUR_USERNAME/olg-web-automation.git

# Rename branch to main (if needed)
git branch -M main

# Push to GitHub (will prompt for PAT when you press Enter)
git push -u origin main
```

When prompted for password, **paste your Personal Access Token** (not your GitHub password)

---

## Option 2: Using SSH Key

### Step 1: Generate SSH Key (if you don't have one)
```powershell
ssh-keygen -t rsa -b 4096 -f $env:USERPROFILE\.ssh\id_rsa
```

### Step 2: Add SSH Key to GitHub
1. Copy your public key: `cat $env:USERPROFILE\.ssh\id_rsa.pub`
2. Go to GitHub Settings → SSH and GPG keys → New SSH key
3. Paste the public key
4. Click "Add SSH key"

### Step 3: Create Repository and Push
```powershell
cd C:\Users\ujjwa\Desktop\olg\olg-web-automation

git remote add origin git@github.com:YOUR_USERNAME/olg-web-automation.git
git branch -M main
git push -u origin main
```

---

## Verify Push Success

After running `git push`, you should see:
```
Enumerating objects: 23, done.
Counting objects: 100% (23/23), done.
...
remote:
remote: Create a pull request for 'main' on GitHub by visiting:
remote:      https://github.com/YOUR_USERNAME/olg-web-automation
```

Visit `https://github.com/YOUR_USERNAME/olg-web-automation` to verify!

---

## What Gets Pushed

```
olg-web-automation/
├── tests/
│   ├── part1_basic/
│   │   └── test_google_homepage.py  (3 tests - ALL PASSING ✓)
│   └── part2_restaurant/
│       └── test_restaurant_search.py (4 tests)
├── page_objects/
│   ├── google_homepage.py
│   └── google_maps.py
├── utils/
│   ├── driver_factory.py
│   ├── logger.py
│   ├── screenshot_manager.py
│   └── wait_helper.py
├── config/
│   └── settings.py
├── logs/                           (generated)
├── screenshots/                    (generated)
├── reports/                        (generated)
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .env
├── .gitignore
├── README.md
└── setup_verify.py
```

---

## After Push: Show Results

1. Go to repository URL: `https://github.com/YOUR_USERNAME/olg-web-automation`
2. Share the URL with the evaluator
3. They can now:
   - View all source code
   - Review test structure
   - Read comprehensive README
   - Clone and run tests locally

---

## Quick Terminal Commands Reference

```powershell
# Check git status
git status

# View commit history
git log --oneline

# View remote
git remote -v

# Update README on GitHub after local changes
git add README.md
git commit -m "Update README"
git push origin main
```

---

## Troubleshooting

### Issue: "fatal: remote origin already exists"
```powershell
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/olg-web-automation.git
git push -u origin main
```

### Issue: Authentication failed
- Make sure you're using Personal Access Token, not GitHub password
- For SSH: Verify SSH key is added to SSH agent: `ssh-add $env:USERPROFILE\.ssh\id_rsa`

### Issue: "Repository already exists"
Create repository with different name, or delete existing GitHub repo and create new one

---

## Repository Contents Checklist

After pushing, verify these exist on GitHub:

✓ Source code (tests, page objects, utils, config)
✓ README.md with full documentation
✓ .gitignore (excludes logs, screenshots, venv)
✓ requirements.txt with dependencies
✓ .env file with configuration
✓ pytest.ini with test settings
✓ conftest.py with fixtures

---

**Status**: Ready to push to GitHub ✓

**Test Results Summary**:
- ✓ Part 1 Tests: 3/3 PASSED (100%)
  - test_page_title_assertion: PASSED
  - test_search_box_is_visible: PASSED
  - test_search_button_is_visible: PASSED

- Part 2 Tests: Network-dependent (requires internet)
  - test_google_maps_page_loads
  - test_restaurant_search_returns_results
  - test_first_restaurant_has_name
  - test_restaurant_results_verification
