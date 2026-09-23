def combat_sim_user_creates_own_monster_list(
    spreadsheet_monsters_dict_in_question
):
    """
    GUI should look like this:
    ```
    combat_sim_user_creates_own_monster_list
        From here you can use UP, DOWN, LEFT, RIGHT freely to navigate any of the keys i have dhowed below.
        If you want to sort a column, then you can click ENTER and a prompt will give you that option
        You can also select a monster by doing the same thing. Press ENTER then click "add monster".
            from there it will ask you how many monsters you want.
        The yellow color of a value indicates you have it selected.
            Example here *<-- this would be yellow*

    Selected    :   quantity    :   Name                            :   CR      :   Font            :   Author                  :   HP  :   AC  :   URL
    False       :   0           :   Goblin                          :   0.25    :   Monster Manual  :   Wizards of the Coast    :   7   :   13  :   link
    True        :   2           :   Skeleton                        :   0.25    :   Monster Manual  :   Wizards of the Coast    :   13  :   13  :   link
    True        :   1           :   Dragon, Chromatic, Black, Young :   7       :   Monster Manual  :   Wizards of the Coast    :   127 :   18  :   link
    ```

    when you select a row content
    ```
    Selected    :   quantity    :   Name                            :   CR      :   Font            :   Author                  :   HP  :   AC  :   URL
        you have selected *selected value* from *selected key*
        what do you want to do?
            → change number of these monsters in the list
              sort column from greatest to least
              sort column from least to greatest
    False       :   0           :   Goblin                          :   0.25    :   Monster Manual  :   Wizards of the Coast    :   7   :   13  :   link
    True        :   2           :   Skeleton                        :   0.25    :   Monster Manual  :   Wizards of the Coast    :   13  :   13  :   link
    True        :   1           :   Dragon, Chromatic, Black, Young :   7       :   Monster Manual  :   Wizards of the Coast    :   127 :   18  :   link
    ```

    with sorting columns, they would be alphabetically sorted if the value were strings

    :param spreadsheet_monsters_dict_in_question:
    :return:
    """
    """
    currently the front end GUI prevents this from even triggering
    but hypothetically if it did then it would go here. 
    """

    print("combat_sim_user_creates_own_monster_list")
    print("this feature is not implemented yet. please come back later.")
    exit(999)