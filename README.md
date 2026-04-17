# Window Manager Simulation

This project simulates a window management system similar to an operating system.

## Features
- Open, Focus, Minimize, Restore, Close windows
- Maintain z-order (top to bottom)
- O(1) operations using OrderedDict

## Input Format
Commands like:  
OPEN id  
FOCUS id  
MINIMIZE id  
RESTORE id  
CLOSE id  
TOP  
LIST  

## Example Input

8  
OPEN 1  
OPEN 2  
MINIMIZE 2  
RESTORE 2  
TOP  
LIST  
CLOSE 1  
TOP  


## Example Output

2  
2 1  
2  


## Output Rules
- Only `TOP` and `LIST` produce output
- `LIST` prints space-separated window IDs (top → bottom)

## Tech Used
- Python
- OrderedDict (collections)
