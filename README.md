## D4 Nightmare Dungeon Calculator
## Version 1.1.0 in progress - Check Changelog for up to date changes during development

## <span style='color: Orange;'>[Premiss]</span>
I was tired of manually calculating it every time so I made a program to do it for me.

![D4 Dungoen Calculator](https://i.imgur.com/OSB2asr.png)
## <span style='color: Orange;'>[Features]</span>
- Genral monster level calculator for whatever tier you select.
- Optimal XP calculator, once you enter your player level this will tell you the dungeon tier you should be running to get the 30% Monster XP bonus.
- Both feature a 'Filter' where you can just type in the tier or your player level and it will automatically select the approriate item in the combo boxes.

## <span style='color: Orange;'>[Future plans]</span>
- Add additional tiers if they ever add more to the game
- conversion to base tkinter library (i just found out that tkinter can use themes for a more modern look)
- More code adjustments and optimization
- Make a separate hosted web version (This version on this github repo is written in python 3.11, I just will have to learn javascript to make this a web version, I know how to do HTML and CSS very well, as I have to learn javascript on my free time I have no idea when this will be with some other projects in mind (one being volenteering for the Skyblivion team, a mod team remaking Oblivion in Skyrim's Engine))

## <span style='color: Orange;'>[Language and modules]</span>
- Python [3.11.4](https://www.python.org/downloads/)
- Module: [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- Module: [tkinterMessageBox](https://github.com/Akascape/tkinterMessagebox)
- Module: [Numpy](https://github.com/numpy/numpy) (For some of the calculations using arrays, because numpy is generally faster than python lists)
- [AutoPy2Exe](https://pypi.org/project/auto-py-to-exe/) - To build the Exe

## <span style='color: orange;'>[Notes on Usage]</span>
[Filter Boxes]
- Enter a integer and press enter to have it automatically select the appropriate value in the combo boxes. (if you do not press enter or leave focus (tab out of the control) it will not execute the filtering command), I recommend using this feature and getting used to it as much as you can before you click calculate because the calculation only takes whats in the combo boxes as inputs and both combo boxes are read only.

## [Change-Log]
    Symbol Meaning 
        + Added Feature
        - Removed Feature
        * Changed Feature
#### [Version 1.0.0]
- initial release

#### [Version 1.1.0] (In Progress...)
- * Changed: Complete recode from scratch
- * Changed: Changed code language to C# instead of python (easier to design ui in c# and takes less time to make changes to the UI)
- + Added: NuGet package for googles material design for a modern look.
