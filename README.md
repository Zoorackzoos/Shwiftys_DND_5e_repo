# Shwiftys_DND_5e_repo

# combat sim

## data entry for actions information in the spreadsheet
you have 2 options
* input info in the ```actions_only_input_file.md``` file
  * from there run ```interpret_actions_only_markdown_file.py``` from which it automatically updates the spreadsheet given the name of the monster in the "metadata" header in the markdown
  * it's important to note that the markdown file has to be very specific or else the file will have "unpredictable hevaoir"
    * like racoon.
* input info in ```actions_only_input_file.py``` file
  * from there run ```update_actions_only_python_file.py``` which is also, updates the spreadsheet automatically given the name you put in the file
  * i guess this would be more difficult for less experienced users. but who tf is gonna use this repo other than me? lbh

# difficulty predictor
This has been discontinued. if i were to continue. i would have to:
1. redesign how much data i would put into the algorithm (all of it naturally)
2. define the algorithm that would deal with both CR, PC power levels and probably some more things
3. database schema of the encounter feedback
4. integration of the combat ssim so automatic data is generated
   1. awoooga :-P

## description
used to calculate combat difficulty in dungeons

## important spreadsheet updater files
* ```interpret_markdown_stat_block.py```
  * this makes python files that are dictionaries which can then be modified further or updated into the spreadsheet database. which is both a .csv and .tsv file
* ```spreadsheet_enums.py```
  * these are enums for both the spreadsheet's keys, as well as certain close ended values a key can have. Like monster type or font
* ```convert_csv_file_into_tsv_file.py```
* ```update_encoutner_feedback_spreadsheet.py```
* ```update_homebrew_monster_spreadsehet.py```
* ```get_encounter_difficulty_from_cr_values.py```
  * this ia a derivative of the "get_enouncter_difficulty_from_xp_values" because xp values are necessary, but i call CR much mor often than i do xp
* ```print_dictionary_nicely.py```
* ```print_encounter_difficulty_concisely.py```

## custom monster to cr and spreadsheet pipline
1. make stat block on google docs using the recommended template monster
2. download stat block as .md file
3. go to ```interpret_markdown_stat_block.py``` and code it to hook up and "dictionar-ify" your Markdown file
   1. this will come with it's own ```if __name__ == "__main__"``` helper function that updates it's cr and cr helper values
   2. run the file to update the CR and the CR helper values by copying and pasting it in it's own file
4. run ```convert_csv_file_into_tsv_file.py```
5. open file explorer to the .tsv file
6. cntrl + A 
7. cntrl + C
8. go to your .tsv file on google sheets
9. cntrl + A
10. cntrl + V
11. the update cycle has finished. 

## major TODOS
```pycon
#TODO: make the database be in .tsv instead of .csv
#TODO: consult a clanker on if that would be a good idea or not
```
to plug cells from pycharm into google sheets withotu making  
a whole new file you need the file to be separated by tabs, not commas.  

so that has me thinking we just have it one way. just .tsv.

```pycon
#TODO: make a more advanced combat simulator that takes in-game difficulty statistics for me so i can manually and algorithmically analyzer encounters.
```
technically i discontinued the whole prediction of difficulty encounters feature but if i were want to start it again i would need data to create the algorithm with. 
Currently the one i have was vibe coded by Codex and it says it got the idea from teh wizards of the coast algorithm from their book.
Idk if it's having a clanker moment and i don't care to find out :-/ 