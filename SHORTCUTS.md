# ?? FIREPIT MANAGER - KEYBOARD SHORTCUTS & QUICK COMMANDS

## ??? DESKTOP SHORTCUTS
Double-click these icons on your desktop:

- **?? Firepit Manager** ? Launch the application
- **?? Firepit Manager Menu** ? Open quick menu for all commands
- **?? FirepitManager Folder** ? Open project folder

## ? BATCH FILE SHORTCUTS
Open PowerShell/CMD in the FirepitManager folder and run:

| Command       | Action                                    |
|---------------|-------------------------------------------|
| un.bat     | Launch the application                    |
| save.bat    | Quick save & push to GitHub               |
| push.bat    | Push to GitHub with custom message        |
| pull.bat    | Update from GitHub                        |
| status.bat  | Check git status and recent commits       |
| github.bat  | Open repository in browser                |
| menu.bat    | Open interactive menu                     |

## ?? POWERSHELL ALIASES
Open any PowerShell window and type:

| Command      | Action                                    |
|--------------|-------------------------------------------|
| p         | Navigate to project folder                |
| p-run     | Launch the application                    |
| p-save    | Quick save & push to GitHub               |
| p-status  | Check git status                          |
| p-pull    | Update from GitHub                        |
| p-code    | Open in VS Code                           |
| p-github  | Open GitHub repository                    |
| p-help    | Show all commands                         |

## ?? QUICK START WORKFLOW

### Starting Work:
1. Double-click **?? Firepit Manager** on desktop
2. Make your changes
3. Test in the app

### Saving Work:
**Method 1 (Fastest):**
- Double-click **?? Firepit Manager Menu** ? Select option 2

**Method 2 (PowerShell):**
```powershell
fp-save
```

**Method 3 (Manual):**
```bash
git add .
git commit -m "Your message"
git push origin main
```

### Checking Status:
- Open menu ? Select option 3
- Or in PowerShell: p-status
- Or run: status.bat

## ?? MOST COMMON COMMANDS

### Daily Use:
1. Launch app: **Double-click desktop icon**
2. Save changes: **Double-click menu ? Option 2**
3. Check status: **PowerShell ? p-status**

### Weekly:
1. Pull updates: **Menu ? Option 4** or p-pull
2. Review commits: **Menu ? Option 3**

## ?? FIRST TIME SETUP
If PowerShell aliases don't work immediately:
1. Restart PowerShell (close and reopen)
2. Or run: . $PROFILE to reload
3. Then type: p-help to verify

## ?? PIN TO TASKBAR
Right-click the desktop shortcut ? Pin to taskbar
Now press **Windows Key + [Number]** to launch instantly!

## ?? WINDOWS SHORTCUTS
Create your own keyboard shortcut:
1. Right-click desktop shortcut ? Properties
2. Click in "Shortcut key" field
3. Press your desired combo (e.g., Ctrl+Alt+F)
4. Click OK

---
Last Updated: 2025-10-31
