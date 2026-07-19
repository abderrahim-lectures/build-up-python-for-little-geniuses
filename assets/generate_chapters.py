"""Generate web pages, notebooks, and code_project modules+tests for
Chapters 1-15, from a single source-of-truth CHAPTERS list below.

Usage:
    python assets/generate_chapters.py
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WEB_SRC = ROOT / "web" / "src"
NOTEBOOKS = ROOT / "notebooks"
FOUNDATIONS = ROOT / "code_project" / "foundations"
TESTS = ROOT / "code_project" / "tests"

CHAPTERS = [
    dict(
        num=1, slug="variables", title="Variables", icon="tag", theme="theme-crates",
        hook="A variable is like a labelled storage crate: put a value inside, write a name on it, and Python remembers it until you change it.",
        objectives=["Store a value in a variable", "Explain why we give variables meaningful names", "Update a variable and see the new value take effect"],
        lesson_title="1.1 Naming your values",
        lesson_body='In math you might write <code>x = 5</code> and know <code>x</code> stands for 5 from then on. Python works the same way: <code>player_name = "Ari"</code> stores the text <code>"Ari"</code> under the name <code>player_name</code>. Change what\'s on the right of the <code>=</code> sign, and the crate\'s label stays the same but what\'s inside changes.',
        worked_example='Say you\'re tracking three separate facts about a hero: their name is "Ari", their score starts at 0, and their health starts at 100. Each fact gets its own crate: <code>player_name = "Ari"</code>, <code>score = 0</code>, <code>health = 100</code>. Later, when Ari earns 10 points, you don\'t relabel anything – you just replace what\'s inside the score crate: <code>score = score + 10</code> makes <code>score</code> become <code>10</code>, while <code>player_name</code> and <code>health</code> stay untouched.',
        code_title="variables.py",
        code_demo='player_name = "Ari"\nscore = 0\nhealth = 100\nprint(player_name, score, health)',
        func_name="describe_player", func_sig="name: str, score: int, health: int",
        func_doc="Return a one-line status string for a player.",
        func_body='return f"{name} - score: {score}, health: {health}"',
        tests=[
            ("test_describe_player_includes_name", 'assert "Ari" in describe_player("Ari", 0, 100)'),
            ("test_describe_player_includes_score_and_health", 'assert "score: 10" in describe_player("Ari", 10, 50) and "health: 50" in describe_player("Ari", 10, 50)'),
        ],
        notebook_intro="Change `player_name` below to your own name, then run both cells.",
        notebook_code=['player_name = "Ari"\nscore = 0\nhealth = 100\nprint(player_name, score, health)',
                       'def describe_player(name, score, health):\n    return f"{name} - score: {score}, health: {health}"\n\n\nprint(describe_player(player_name, score, health))'],
        knowledge_check=["What symbol stores a value in a variable?", "What happens if you use a variable before giving it a value?",
                          "If score = 5 and you then run score = score + 3, what does score equal afterward, and why doesn't Python get confused about which crate to update?"],
        retrieval='Use <code>print()</code> (Chapter 0) to print your <code>score</code> variable by itself.',
        track_b="Your player character gets its first real data: name, health, and starting position – all stored in variables you'll reuse in every later chapter.",
    ),
    dict(
        num=2, slug="arithmetic", title="Arithmetic", icon="calculator", theme="theme-ch02",
        hook="Order of operations isn't just a math-class rule – Python follows it exactly, so knowing it tells you exactly what your code will compute.",
        objectives=["Use +, -, *, / and // in Python", "Predict a multi-step expression using order of operations", "Explain the difference between / and //"],
        lesson_title="2.1 Order of operations",
        lesson_body='Python evaluates <code>*</code> and <code>/</code> before <code>+</code> and <code>-</code>, exactly like in math class: <code>2 + 3 * 4</code> is <code>14</code>, not <code>20</code>, because multiplication happens first. <code>//</code> is "floor division" – divide, then drop anything after the decimal point, useful when you need a whole number (like splitting players into whole teams).',
        worked_example='Try 24 players splitting into teams of 5, step by step: <code>24 // 5</code> asks "how many whole 5s fit in 24?" – the answer is 4 full teams (4 * 5 = 20). What\'s left over comes from <code>24 % 5</code>, which is 24 - 20 = 4 leftover players. Together, <code>split_into_teams(24, 5)</code> returns <code>(4, 4)</code>: four full teams of 5, plus 4 players still waiting for a team.',
        code_title="arithmetic.py",
        code_demo="total_points = 2 + 3 * 4\nteams = 17 // 5\nleftover_players = 17 % 5\nprint(total_points, teams, leftover_players)",
        func_name="split_into_teams", func_sig="players: int, team_size: int",
        func_doc="Return (full_teams, leftover_players) for splitting players into teams.",
        func_body="return players // team_size, players % team_size",
        tests=[
            ("test_split_into_teams_full_teams", "assert split_into_teams(17, 5) == (3, 2)"),
            ("test_split_into_teams_no_leftover", "assert split_into_teams(20, 5) == (4, 0)"),
        ],
        notebook_intro="Change the number of players below and see how the teams and leftovers change.",
        notebook_code=["total_points = 2 + 3 * 4\nteams = 17 // 5\nleftover_players = 17 % 5\nprint(total_points, teams, leftover_players)",
                       "def split_into_teams(players, team_size):\n    return players // team_size, players % team_size\n\n\nprint(split_into_teams(25, 4))"],
        knowledge_check=["Why is 2 + 3 * 4 equal to 14 and not 20?", "If 17 players split into teams of 5, how many leftover players are there?",
                          "26 players split into teams of 6 – work out both the whole teams and the leftover by hand, then check your answer against split_into_teams(26, 6)."],
        retrieval='Store the result of <code>17 // 5</code> in a variable (Chapter 1) called <code>teams</code> and print it.',
        track_b="Movement math: turning a direction and a speed number into how far your player moves each frame.",
    ),
    dict(
        num=3, slug="strings", title="Strings & Words", icon="speech-bubble", theme="theme-ch03",
        hook="Word problems mix numbers and words – Python's f-strings let your code do the same, dropping a variable's value right into a sentence.",
        objectives=["Combine text and variables with an f-string", "Use len() to find how many characters are in a string", "Explain the difference between a string and a number in Python"],
        lesson_title="3.1 Mixing words and numbers",
        lesson_body='<code>"5"</code> and <code>5</code> look similar but behave differently: <code>"5"</code> is text (a string), <code>5</code> is a number. An f-string – <code>f"..."</code> – lets you drop a variable straight into a sentence: <code>f"{player_name} has {score} points"</code>. <code>len(text)</code> counts characters, which is handy for things like limiting a player name to a certain length.',
        worked_example='Suppose <code>player_name = "Nadia"</code> and <code>score = 42</code>. <code>f"{player_name} has {score} points"</code> builds the sentence piece by piece: first "Nadia" replaces <code>{player_name}</code>, then 42 (converted to text automatically) replaces <code>{score}</code> – the final string is "Nadia has 42 points", built from a string and a number without you ever converting <code>score</code> to text yourself.',
        code_title="strings.py",
        code_demo='player_name = "Ari"\nscore = 10\nmessage = f"{player_name} has {score} points"\nprint(message)\nprint(len(player_name))',
        func_name="player_status", func_sig="name: str, score: int",
        func_doc="Return a friendly status sentence combining a name and score.",
        func_body='return f"{name} has {score} points"',
        tests=[
            ("test_player_status_includes_name", 'assert "Ari" in player_status("Ari", 10)'),
            ("test_player_status_includes_score", 'assert "10" in player_status("Ari", 10)'),
        ],
        notebook_intro="Change the name and score below, then run both cells.",
        notebook_code=['player_name = "Ari"\nscore = 10\nmessage = f"{player_name} has {score} points"\nprint(message)\nprint(len(player_name))',
                       'def player_status(name, score):\n    return f"{name} has {score} points"\n\n\nprint(player_status(player_name, score))'],
        knowledge_check=['What does <code>f"..."</code> let you do that a plain string can\'t?', 'What does <code>len("Ari")</code> return?',
                          'If name = "Sam" and points = 7, write out exactly what f"{name} scored {points}!" produces, character by character if you\'re not sure.'],
        retrieval="Use a variable (Chapter 1) inside an f-string to print your own score sentence.",
        track_b="Show the player's name and health as real on-screen text instead of just numbers in the console.",
    ),
    dict(
        num=4, slug="conditionals", title="Making Choices", icon="fork", theme="theme-ch04",
        hook="A number line splits into 'less than', 'equal to', and 'greater than' – if/elif/else lets your code make exactly that kind of choice.",
        objectives=["Write an if/elif/else chain", "Use comparison operators (<, >, ==)", "Explain why only one branch of an if/elif/else ever runs"],
        lesson_title="4.1 Choosing a branch",
        lesson_body="Comparing numbers is something you already do on a number line: is 7 greater than 4? Python asks the same question with <code>&gt;</code>, <code>&lt;</code>, <code>==</code>, <code>&gt;=</code>, <code>&lt;=</code>. An if/elif/else chain checks conditions in order and runs only the first branch that's true – like a flowchart with one path through it.",
        worked_example='Walk <code>health = 40</code> through the chain step by step: Python asks first "is 40 &lt;= 0?" – no, so it moves to the next check. Then "is 40 &lt; 25?" – also no, so it moves on again. Since no elif matched, the else branch runs and status becomes "ok". Change health to 10: the first check still fails, but the second now succeeds, so status becomes "low health" instead – and Python never even looks at the else.',
        code_title="conditionals.py",
        code_demo='health = 15\nif health <= 0:\n    status = "defeated"\nelif health < 25:\n    status = "low health"\nelse:\n    status = "ok"\nprint(status)',
        func_name="health_status", func_sig="health: int",
        func_doc="Return a status string for the given health value.",
        func_body='if health <= 0:\n        return "defeated"\n    elif health < 25:\n        return "low health"\n    else:\n        return "ok"',
        tests=[
            ("test_health_status_defeated", 'assert health_status(0) == "defeated"'),
            ("test_health_status_low", 'assert health_status(24) == "low health"'),
            ("test_health_status_ok_at_boundary", 'assert health_status(25) == "ok"'),
        ],
        notebook_intro="Change `health` below and see which branch runs.",
        notebook_code=['health = 15\nif health <= 0:\n    status = "defeated"\nelif health < 25:\n    status = "low health"\nelse:\n    status = "ok"\nprint(status)',
                       'def health_status(health):\n    if health <= 0:\n        return "defeated"\n    elif health < 25:\n        return "low health"\n    else:\n        return "ok"\n\n\nprint(health_status(25))'],
        knowledge_check=["Why does only one branch of an if/elif/else run, even if two conditions could be true?", 'What status does health = 25 give, and why not "low health"?',
                          "Trace through health_status(3) by hand, one condition at a time, before running the code – were you right?"],
        retrieval="Print (Chapter 0) the health_status message using an f-string (Chapter 3).",
        track_b="Check whether the player has walked off the edge of the game world before letting them move.",
    ),
    dict(
        num=5, slug="lists", title="Lists", icon="list", theme="theme-inventory",
        hook="A list is an ordered sequence of values, the same idea as a numbered sequence in math – item 1, item 2, item 3.",
        objectives=["Create a list and add items with append()", "Access an item by its index", "Explain why Python lists start counting at 0"],
        lesson_title="5.1 Ordered collections",
        lesson_body='<code>inventory = ["sword", "shield"]</code> stores two items in order. <code>inventory[0]</code> is the first item – Python counts from 0, not 1, so the second item is <code>inventory[1]</code>. <code>append()</code> adds a new item to the end, exactly like picking up a new item in a game.',
        worked_example='Start with <code>inventory = ["sword"]</code>. After <code>inventory.append("shield")</code>, the list becomes <code>["sword", "shield"]</code> – "sword" is still at index 0, and "shield" is now at index 1, the last position. Append once more with "potion" and the list grows to <code>["sword", "shield", "potion"]</code>, with "potion" now at index 2 – append always adds to whatever the current last position is, so the index of the newest item keeps changing as the list grows.',
        code_title="lists.py",
        code_demo='inventory = ["sword", "shield"]\ninventory.append("potion")\nprint(inventory)\nprint(inventory[0])\nprint(len(inventory))',
        func_name="add_item", func_sig="inventory: list, item: str",
        func_doc="Return a new inventory list with item added to the end.",
        func_body="return inventory + [item]",
        tests=[
            ("test_add_item_appends", 'assert add_item(["sword"], "potion") == ["sword", "potion"]'),
            ("test_add_item_grows_length_by_one", 'assert len(add_item(["sword", "shield"], "potion")) == 3'),
        ],
        notebook_intro="Add your own item to the inventory below.",
        notebook_code=['inventory = ["sword", "shield"]\ninventory.append("potion")\nprint(inventory)\nprint(inventory[0])\nprint(len(inventory))',
                       'def add_item(inventory, item):\n    return inventory + [item]\n\n\nprint(add_item(inventory, "map"))'],
        knowledge_check=["What index gets the FIRST item in a list?", "What does append() do to a list?",
                          "After three appends to an empty list, what index holds the very first item you added, and does that ever change?"],
        retrieval='Use an if statement (Chapter 4) to check whether <code>"potion"</code> is already in <code>inventory</code> before adding it.',
        track_b="Build the player's inventory system – a real Python list that tracks every item they pick up.",
    ),
    dict(
        num=6, slug="for_loops", title="Repeat With For", icon="loop-arrow", theme="theme-ch06",
        hook="Repeated addition – <code>4 + 4 + 4</code> – is multiplication; a for loop is Python's way of repeating an action a set number of times without writing it out by hand.",
        objectives=["Write a for loop over a range()", "Write a for loop over a list", "Explain what a loop variable is"],
        lesson_title="6.1 Repeating on purpose",
        lesson_body='<code>3 * 4</code> means "add 4, three times." A for loop makes that repetition explicit: <code>for i in range(3): total += 4</code> runs the addition three times. Looping over a list – <code>for item in inventory:</code> – visits every item in order, much shorter than writing one line per item.',
        worked_example='<code>for i in range(5): total += 2</code> runs the loop body five times, once for each value range(5) produces: 0, 1, 2, 3, 4. The loop variable <code>i</code> changes each pass, but since the code never uses <code>i</code>, only <code>total</code>, what matters here is just that the addition happens five times: total goes 0, then 2, 4, 6, 8, 10 – the same as 2 * 5.',
        code_title="for_loops.py",
        code_demo='total = 0\nfor i in range(4):\n    total = total + 3\nprint(total)\n\nfor item in ["sword", "shield", "potion"]:\n    print(item)',
        func_name="repeated_addition", func_sig="value: int, times: int",
        func_doc="Add value to a running total, times times, using a for loop.",
        func_body="total = 0\n    for _ in range(times):\n        total += value\n    return total",
        tests=[
            ("test_repeated_addition_basic", "assert repeated_addition(3, 4) == 12"),
            ("test_repeated_addition_zero_times", "assert repeated_addition(5, 0) == 0"),
        ],
        notebook_intro="Change how many times the loop repeats below.",
        notebook_code=['total = 0\nfor i in range(4):\n    total = total + 3\nprint(total)',
                       'def repeated_addition(value, times):\n    total = 0\n    for _ in range(times):\n        total += value\n    return total\n\n\nprint(repeated_addition(3, 6))'],
        knowledge_check=["What does range(4) produce?", "How many times does the loop body run for range(4)?",
                          "Without running it, predict what repeated_addition(5, 3) returns, then check your prediction."],
        retrieval="Use append() (Chapter 5) inside a for loop to build a list of the numbers 0-4.",
        track_b="Draw an entire row of ground tiles by looping instead of placing each one by hand.",
    ),
    dict(
        num=7, slug="while_loops", title="Repeat Until", icon="hourglass", theme="theme-ch07",
        hook="A running total that keeps going until you reach a target is exactly what a while loop does: repeat until a condition becomes false.",
        objectives=["Write a while loop with a running total", "Explain the risk of an infinite loop", "Use a while loop to count down"],
        lesson_title="7.1 Repeating until a condition changes",
        lesson_body="A for loop repeats a fixed number of times; a while loop repeats until a condition stops being true – useful when you don't know the count in advance, like health counting down to 0. Forgetting to change the condition inside the loop causes an infinite loop, so always make sure something inside the loop moves you toward stopping.",
        worked_example='Trace <code>health = 3</code> through the loop: is 3 &gt; 0? Yes – print 3, health becomes 2. Is 2 &gt; 0? Yes – print 2, health becomes 1. Is 1 &gt; 0? Yes – print 1, health becomes 0. Is 0 &gt; 0? No – the loop stops, and "game over" prints. Three numbers printed, matching <code>countdown(3) == [3, 2, 1]</code>.',
        code_title="while_loops.py",
        code_demo='health = 5\nwhile health > 0:\n    print(health)\n    health = health - 1\nprint("game over")',
        func_name="countdown", func_sig="start: int",
        func_doc="Return a list counting down from start to 1 (a while loop, but bounded and testable).",
        func_body="values = []\n    health = start\n    while health > 0:\n        values.append(health)\n        health -= 1\n    return values",
        tests=[
            ("test_countdown_basic", "assert countdown(3) == [3, 2, 1]"),
            ("test_countdown_zero_gives_empty_list", "assert countdown(0) == []"),
        ],
        notebook_intro="Change the starting health below and watch the countdown.",
        notebook_code=['health = 5\nwhile health > 0:\n    print(health)\n    health = health - 1\nprint("game over")',
                       'def countdown(start):\n    values = []\n    health = start\n    while health > 0:\n        values.append(health)\n        health -= 1\n    return values\n\n\nprint(countdown(7))'],
        knowledge_check=["What could go wrong if you forget to decrease health inside the loop?", "What's the difference between a for loop and a while loop?",
                          "If you swapped the order so health = health - 1 happened BEFORE the print, what would the very first number printed be instead of 3?"],
        retrieval="Store each health value (Chapter 1 variables) into a list (Chapter 5) instead of just printing it.",
        track_b="The main game loop itself is a while loop: keep updating and drawing the game until the player quits.",
    ),
    dict(
        num=8, slug="functions", title="Functions", icon="gear", theme="theme-ch08",
        hook="A math formula like <code>area = length * width</code> takes inputs and produces an output – a Python function is exactly that: input in, answer out.",
        objectives=["Define a function with def, parameters, and return", "Call a function with different arguments", "Explain why functions help avoid repeating code"],
        lesson_title="8.1 Formulas as functions",
        lesson_body='<code>def area(length, width): return length * width</code> defines a reusable formula. Call it with <code>area(4, 5)</code> and it returns <code>20</code>, just like plugging numbers into a math formula. Functions let you write the logic once and reuse it everywhere.<br><br><strong>From this chapter on, Track B needs a real window on your own computer</strong> – pgzero can\'t draw a window inside MyBinder, so this is when you install Python locally.',
        worked_example='<code>area(4, 5)</code> substitutes length=4 and width=5 into <code>return length * width</code>, giving 20. Call it again with different numbers, <code>area(7, 2)</code>, and the SAME function returns 14 – nothing about the function itself changed, only the numbers you handed it. That\'s the whole point: one formula, reused for as many rectangles as you need, the same way one math formula works for every rectangle you ever measure.',
        code_title="functions.py",
        code_demo="def area(length, width):\n    return length * width\n\ndef move_player(x, dx):\n    return x + dx\n\nprint(area(4, 5))\nprint(move_player(10, 3))",
        func_name="area", func_sig="length: float, width: float",
        func_doc="Return the area of a rectangle.",
        func_body="return length * width",
        tests=[
            ("test_area_basic", "assert area(4, 5) == 20"),
            ("test_area_zero_width", "assert area(4, 0) == 0"),
        ],
        notebook_intro="Call area() with a few different lengths and widths below.",
        notebook_code=["def area(length, width):\n    return length * width\n\n\nprint(area(4, 5))",
                       "def move_player(x, dx):\n    return x + dx\n\n\nprint(move_player(10, 3))"],
        knowledge_check=["What two things does a function need to give back an answer?", "Why is a function better than copy-pasting the same code three times?",
                          "Without running it, what does area(9, 3) return? What about move_player(0, -2)?"],
        retrieval="Call your area() function inside a for loop (Chapter 6) to print the area for a few different widths.",
        track_b="Refactor player movement into its own function – and install Python locally, since pgzero needs a real window from here on.",
    ),
    dict(
        num=9, slug="area_perimeter", title="Area & Perimeter", icon="map", theme="theme-fence",
        hook="Fencing off a rectangular plot of land needs its perimeter; covering it with grass needs its area – both are just formulas turned into functions.",
        objectives=["Write functions for area and perimeter of a rectangle", "Explain the difference between area and perimeter", "Combine variables, arithmetic, and functions in one program"],
        lesson_title="9.1 Two formulas, one shape",
        lesson_body="<code>area = length * width</code> tells you how much surface a rectangle covers; <code>perimeter = 2 * (length + width)</code> tells you the distance all the way around it – like the fence you'd need to build around a plot of land. Writing both as functions means any part of your program can ask 'how big is this plot?' without recalculating by hand.",
        worked_example='A 6-by-4 plot: <code>area(6, 4)</code> computes 6 * 4 = 24 (24 square units of grass to cover). <code>perimeter(6, 4)</code> computes 2 * (6 + 4) = 2 * 10 = 20 (20 units of fence to build all the way around). Notice a 6x4 plot and a 4x6 plot have the exact same area and perimeter – length and width are interchangeable in both formulas, since multiplication and addition don\'t care about order.',
        code_title="area_perimeter.py",
        code_demo='def area(length, width):\n    return length * width\n\ndef perimeter(length, width):\n    return 2 * (length + width)\n\nplot_length, plot_width = 6, 4\nprint("area:", area(plot_length, plot_width))\nprint("perimeter:", perimeter(plot_length, plot_width))',
        func_name="perimeter", func_sig="length: float, width: float",
        func_doc="Return the perimeter of a rectangle.",
        func_body="return 2 * (length + width)",
        tests=[
            ("test_perimeter_basic", "assert perimeter(6, 4) == 20"),
            ("test_perimeter_square", "assert perimeter(5, 5) == 20"),
        ],
        notebook_intro="Change plot_length and plot_width below and compare area vs. perimeter.",
        notebook_code=['def area(length, width):\n    return length * width\n\ndef perimeter(length, width):\n    return 2 * (length + width)\n\n\nplot_length, plot_width = 6, 4\nprint("area:", area(plot_length, plot_width))\nprint("perimeter:", perimeter(plot_length, plot_width))'],
        knowledge_check=["Which formula tells you how much fence to buy: area or perimeter?", "If a plot is 6 by 4, what's its area?",
                          "A square plot is 5 by 5. Work out its area and perimeter by hand, then check with the functions."],
        retrieval="Use an if statement (Chapter 4) to compare two plots and print which one has the larger area.",
        track_b="Fence off your first land plot in the game world, sized by real area/perimeter math.",
    ),
    dict(
        num=10, slug="grid", title="The Grid", icon="target", theme="theme-ch10",
        hook="The coordinate plane from math class – an x and a y telling you exactly where a point is – is exactly how a 2D game world tracks where everything stands.",
        objectives=["Represent a position as an (x, y) pair", "Update a position by adding a movement delta", "Explain how a 2D grid maps to the game screen"],
        lesson_title="10.1 Positions as coordinates",
        lesson_body="A point on a coordinate plane is just two numbers: (x, y). A game position works the same way – a tuple <code>(x, y)</code> tells you exactly where the player stands on the grid. Moving right adds to x; moving down adds to y (screens count y downward, unlike most math classes!).",
        worked_example='Starting at (2, 3), <code>move(pos, 1, 0)</code> adds 1 to the x-coordinate only: (2+1, 3+0) = (3, 3) – the point slides right, same height. <code>move(pos, 0, -1)</code> adds -1 to y instead: (2, 3-1) = (2, 2) – since y counts downward on screen, a NEGATIVE dy actually moves the point UP, which can feel backwards coming from math class.',
        code_title="grid.py",
        code_demo="player_pos = (2, 3)\ndx, dy = 1, 0\nnew_pos = (player_pos[0] + dx, player_pos[1] + dy)\nprint(new_pos)",
        func_name="move", func_sig="pos: tuple, dx: int, dy: int",
        func_doc="Return a new (x, y) position after moving by (dx, dy).",
        func_body="return (pos[0] + dx, pos[1] + dy)",
        tests=[
            ("test_move_right", "assert move((2, 3), 1, 0) == (3, 3)"),
            ("test_move_down", "assert move((2, 3), 0, 1) == (2, 4)"),
        ],
        notebook_intro="Change dx and dy below to move the point in different directions.",
        notebook_code=["player_pos = (2, 3)\ndx, dy = 1, 0\nnew_pos = (player_pos[0] + dx, player_pos[1] + dy)\nprint(new_pos)",
                       'def move(pos, dx, dy):\n    return (pos[0] + dx, pos[1] + dy)\n\n\nprint(move(player_pos, 0, 1))'],
        knowledge_check=["What two numbers make up a position on the grid?", "If you add 1 to y, does the point move up or down on the screen?",
                          "Starting at (5, 5), what position do you get after move(pos, -2, 3)? Which direction did the point move overall?"],
        retrieval="Write a for loop (Chapter 6) that moves the player right 3 times and prints the position after each step.",
        track_b="The whole game world becomes a real grid of coordinates the camera can scroll across.",
    ),
    dict(
        num=11, slug="dictionaries", title="Dictionaries", icon="key", theme="theme-shop",
        hook="A lookup table – like a times table where you look up 4 × 7 and get 28 – pairs a key with a value; Python's dict does exactly that.",
        objectives=["Create a dictionary and look up a value by key", "Add and update key-value pairs", "Explain when a dict is better than a list"],
        lesson_title="11.1 Looking things up by name",
        lesson_body='A list finds things by position (index 0, 1, 2...); a dictionary finds things by name: <code>prices = {"potion": 5, "sword": 20}</code> lets you ask <code>prices["sword"]</code> and get <code>20</code> straight back, no counting needed – exactly how a shop\'s price list works.',
        worked_example='<code>cart = ["sword", "potion", "potion"]</code> with <code>prices = {"sword": 20, "potion": 5}</code>: total_cost loops through the cart one item at a time – sword looks up to 20, the first potion looks up to 5, the second potion looks up to 5 again – and sums them: 20 + 5 + 5 = 30 coins total, even though "potion" only appears once as a KEY in the dictionary.',
        code_title="dictionaries.py",
        code_demo='prices = {"potion": 5, "sword": 20, "shield": 15}\nprices["potion"] = 4\nprint(prices["sword"])\nprint(prices)',
        func_name="total_cost", func_sig="cart: list, prices: dict",
        func_doc="Return the total price of every item in cart, looked up from prices.",
        func_body="return sum(prices[item] for item in cart)",
        tests=[
            ('test_total_cost_basic', 'assert total_cost(["sword", "potion"], {"sword": 20, "potion": 5}) == 25'),
            ('test_total_cost_empty_cart', 'assert total_cost([], {"sword": 20}) == 0'),
        ],
        notebook_intro="Add a new item and price to the dictionary below.",
        notebook_code=['prices = {"potion": 5, "sword": 20, "shield": 15}\nprices["potion"] = 4\nprint(prices["sword"])\nprint(prices)',
                       'def total_cost(cart, prices):\n    return sum(prices[item] for item in cart)\n\n\nprint(total_cost(["sword", "shield"], prices))'],
        knowledge_check=['How do you look up the price of "sword" in the prices dictionary?', "What's one thing a dictionary can do that a list can't?",
                          'If a shopper\'s cart is ["shield", "shield"] and shield costs 15, what does total_cost return, and why does it not matter that "shield" is only one key in prices?'],
        retrieval="Use a for loop (Chapter 6) to print every item and price in the shop's dictionary.",
        track_b="Build the shop economy: a real price dictionary the player spends coins against.",
    ),
    dict(
        num=12, slug="chance", title="Chance", icon="dice", theme="theme-ch12",
        hook="Rolling a die or flipping a coin is probability in action – Python's random module lets your code do the same roll.",
        objectives=["Use random.randint() to simulate a dice roll", "Use random.choice() to pick from a list", "Explain what 'equally likely' means for random.randint()"],
        lesson_title="12.1 Simulating randomness",
        lesson_body='<code>random.randint(1, 6)</code> picks a whole number from 1 to 6, each equally likely – a simulated die roll. <code>random.choice([...])</code> picks one item from a list at random, useful for things like loot drops after defeating an enemy.',
        worked_example="random.randint(1, 6) doesn't favor any number – over many rolls, 1 through 6 each come up roughly 1/6 of the time, the same probability you'd calculate for a fair six-sided die. That's different from random.choice(['sword','shield','potion']): with three equally-likely items, each one shows up roughly 1/3 of the time, no matter how many times you've rolled 'sword' in a row before.",
        code_title="chance.py",
        code_demo='import random\n\nroll = random.randint(1, 6)\nloot = random.choice(["sword", "shield", "potion"])\nprint(roll, loot)',
        func_name="roll_die", func_sig="sides: int = 6",
        func_doc="Return a random integer from 1 to sides (inclusive), like rolling a die.",
        func_body="import random\n\n    return random.randint(1, sides)",
        tests=[
            ("test_roll_die_default_in_range", "assert 1 <= roll_die() <= 6"),
            ("test_roll_die_custom_sides_in_range", "assert 1 <= roll_die(20) <= 20"),
        ],
        notebook_intro="Run the cell below a few times – the numbers should change each time.",
        notebook_code=['import random\n\nroll = random.randint(1, 6)\nloot = random.choice(["sword", "shield", "potion"])\nprint(roll, loot)',
                       'def roll_die(sides=6):\n    return random.randint(1, sides)\n\n\nprint(roll_die(20))'],
        knowledge_check=["What numbers can random.randint(1, 6) return?", "Why might two different runs of your code give different loot?",
                          "If you called roll_die(2) a hundred times, roughly how many times would you expect to see a 1? Why doesn't a run of five 2s in a row mean a 1 is 'due'?"],
        retrieval="Use random.choice() inside an if statement (Chapter 4) that reacts differently depending on which item was picked.",
        track_b="Loot drops and enemy spawns become genuinely random, using this exact roll_die() function.",
    ),
    dict(
        num=13, slug="classes", title="Blueprints", icon="blueprint", theme="theme-classes",
        hook="Grouping related facts about one thing – a shape's length AND width together – is what a class does: it bundles data and behavior into one blueprint.",
        objectives=["Define a class with __init__ and a method", "Create an object (instance) from a class", "Explain the difference between a class and an object"],
        lesson_title="13.1 Bundling data and behavior",
        lesson_body='A class is a blueprint; an object is one specific thing built from that blueprint. <code>class Player:</code> with an <code>__init__</code> bundles a player\'s name and health together, and a method like <code>take_damage</code> can update <code>self.health</code> directly – no more passing health around as a separate variable everywhere.',
        worked_example='<code>Player("Ari", 100)</code> runs <code>__init__</code> with name="Ari", health=100, setting <code>self.name</code> and <code>self.health</code> on that ONE object. Create a second one, <code>Player("Kofi", 80)</code>, and it gets its OWN <code>self.name</code>/<code>self.health</code>, completely separate from Ari\'s – calling <code>ari.take_damage(30)</code> only changes <code>ari.health</code> to 70; <code>kofi.health</code> stays at 80. Same blueprint, two independent objects.',
        code_title="classes.py",
        code_demo='class Player:\n    def __init__(self, name, health):\n        self.name = name\n        self.health = health\n\n    def take_damage(self, amount):\n        self.health = self.health - amount\n\nhero = Player("Ari", 100)\nhero.take_damage(30)\nprint(hero.name, hero.health)',
        is_class=True,
        class_name="Player",
        class_body='def __init__(self, name: str, health: int):\n        self.name = name\n        self.health = health\n\n    def take_damage(self, amount: int) -> None:\n        """Reduce health by amount, but never below 0."""\n        self.health = max(0, self.health - amount)',
        tests=[
            ("test_player_init_sets_attributes", 'hero = Player("Ari", 100)\n    assert hero.name == "Ari" and hero.health == 100'),
            ("test_player_take_damage_reduces_health", 'hero = Player("Ari", 100)\n    hero.take_damage(30)\n    assert hero.health == 70'),
            ("test_player_health_never_negative", 'hero = Player("Ari", 10)\n    hero.take_damage(999)\n    assert hero.health == 0'),
        ],
        notebook_intro="Create your own Player below and take some damage.",
        notebook_code=['class Player:\n    def __init__(self, name, health):\n        self.name = name\n        self.health = health\n\n    def take_damage(self, amount):\n        self.health = max(0, self.health - amount)\n\n\nhero = Player("Ari", 100)\nhero.take_damage(30)\nprint(hero.name, hero.health)'],
        knowledge_check=['What\'s the difference between the Player class and hero = Player("Ari", 100)?', "What does self refer to inside a method?",
                          'If you create Player("Ari", 100) and Player("Kofi", 100), then call only kofi.take_damage(50), what is ari.health afterward? What is kofi.health?'],
        retrieval="Notice take_damage() already uses an if-like idea (Chapter 4) via max() so health can't go below 0.",
        track_b="Turn Player, Enemy, and Item into real classes instead of separate loose variables.",
    ),
    dict(
        num=14, slug="debugging", title="Debugging", icon="wrench", theme="theme-ch14",
        hook="Checking your work – the same habit from math class – is what debugging and testing are: verifying your code's answer is actually right.",
        objectives=["Read a Python traceback to find where an error happened", "Write a pytest test that checks a function's answer", "Fix a bug using print() to inspect a variable's value"],
        lesson_title="14.1 Checking your work",
        lesson_body="When Python hits an error, it prints a traceback – read it from the bottom up, the last line usually names the actual problem. Adding <code>print(variable)</code> before a suspicious line shows you exactly what's inside it, the same way you'd double check a math answer by re-adding the numbers. A pytest test like <code>assert area(4, 5) == 20</code> checks your function's answer automatically, every time you run it.",
        worked_example='Suppose <code>safe_divide(10, 0)</code> crashed instead of returning None – Python would print a traceback ending in something like <code>ZeroDivisionError: division by zero</code>. Reading bottom-up, that last line tells you exactly what went wrong even before you look at which line caused it. Adding <code>if b == 0: return None</code> catches the problem BEFORE Python ever attempts the division, turning a crash into a safe, testable answer.',
        code_title="debugging.py",
        code_demo='def safe_divide(a, b):\n    if b == 0:\n        return None\n    return a / b\n\nprint(safe_divide(10, 2))\nprint(safe_divide(10, 0))',
        func_name="safe_divide", func_sig="a: float, b: float",
        func_doc="Return a / b, or None instead of crashing when b is 0.",
        func_body="if b == 0:\n        return None\n    return a / b",
        tests=[
            ("test_safe_divide_normal", "assert safe_divide(10, 2) == 5"),
            ("test_safe_divide_by_zero_returns_none", "assert safe_divide(10, 0) is None"),
        ],
        notebook_intro="Try calling safe_divide with b = 0 below – it shouldn't crash.",
        notebook_code=['def safe_divide(a, b):\n    if b == 0:\n        return None\n    return a / b\n\n\nprint(safe_divide(10, 2))\nprint(safe_divide(10, 0))'],
        knowledge_check=["Where in a traceback do you usually find the actual error message?", "What does assert do in a pytest test?",
                          "Why does test_safe_divide_by_zero_returns_none check `is None` instead of `== None`? (Hint: try both in a notebook cell and see if Python warns you.)"],
        retrieval="Write a pytest-style assert (this chapter) that checks your Chapter 9 area() function gives the right answer.",
        track_b="A full playtest and bugfix pass across everything built so far, backed by real pytest coverage.",
    ),
    dict(
        num=15, slug="capstone", title="Capstone", icon="trophy", theme="theme-capstone",
        hook="Every math unit ends with a review that mixes every skill you've learned – this chapter does the same for everything you've built.",
        objectives=["Combine variables, functions, and classes in one program", "Explain how this chapter's code connects back to Chapters 1-14", "Describe one thing you'd add next to your game"],
        lesson_title="15.1 Putting it all together",
        lesson_body="Your game world now has players (Ch.1, Ch.13), math-driven movement and land plots (Ch.2, Ch.9, Ch.10), an inventory and shop (Ch.5, Ch.11), loops that draw and run everything (Ch.6, Ch.7), choices and randomness (Ch.4, Ch.12), and tests that check it all still works (Ch.14). The code below shows all of it working together in one small scene.",
        worked_example='<code>build_summary("Ari", ["sword", "shield"], {"potion": 5, "map": 12})</code> pulls together three chapters at once: <code>", ".join(inventory)</code> (a list, Ch.5) becomes "sword, shield"; <code>min(prices.values())</code> (a dictionary, Ch.11) finds the cheapest price, 5; and the f-string (Ch.3) weaves both into one sentence – "Ari is carrying: sword, shield. Cheapest shop item: 5 coins." Every earlier chapter is still doing real work here, just combined.',
        code_title="capstone.py",
        code_demo='class Player:\n    def __init__(self, name, health):\n        self.name = name\n        self.health = health\n\nhero = Player("Ari", 100)\ninventory = ["sword"]\nprices = {"potion": 5}\n\nfor item in inventory:\n    print(f"{hero.name} is carrying a {item}")\nprint(f"A potion costs {prices[\'potion\']} coins")',
        func_name="build_summary", func_sig="name: str, inventory: list, prices: dict",
        func_doc="Return a one-line summary combining a player's name, inventory, and the shop's prices.",
        func_body='items = ", ".join(inventory)\n    cheapest = min(prices.values()) if prices else 0\n    return f"{name} is carrying: {items}. Cheapest shop item: {cheapest} coins."',
        tests=[
            ('test_build_summary_includes_name', 'assert "Ari" in build_summary("Ari", ["sword"], {"potion": 5})'),
            ('test_build_summary_includes_item', 'assert "sword" in build_summary("Ari", ["sword"], {"potion": 5})'),
        ],
        notebook_intro="This is the last notebook in the book – change hero's name and inventory to make it your own.",
        notebook_code=['class Player:\n    def __init__(self, name, health):\n        self.name = name\n        self.health = health\n\n\nhero = Player("Ari", 100)\ninventory = ["sword"]\nprices = {"potion": 5}\n\nfor item in inventory:\n    print(f"{hero.name} is carrying a {item}")\nprint(f"A potion costs {prices[\'potion\']} coins")',
                       'def build_summary(name, inventory, prices):\n    items = ", ".join(inventory)\n    cheapest = min(prices.values()) if prices else 0\n    return f"{name} is carrying: {items}. Cheapest shop item: {cheapest} coins."\n\n\nprint(build_summary(hero.name, inventory, prices))'],
        knowledge_check=["Which earlier chapter taught you the inventory list you're using here?", "What's one feature you'd add to the game next?",
                          'Trace build_summary("Nadia", [], {"potion": 5}) by hand – what does an EMPTY inventory look like once it\'s been joined into a sentence?'],
        retrieval="Look back at Chapter 1 – how much has this same 'variable' idea grown by Chapter 15?",
        track_b="The finished small village – every system from every chapter, working together.",
    ),
]


def slug_id(ch):
    return f"ch{ch['num']:02d}_{ch['slug']}"


def make_web_page(ch):
    sid = slug_id(ch)
    obj_items = "\n".join(f"      <li>{o}</li>" for o in ch["objectives"])
    kc_items = "\n".join(f"      <li>{q}</li>" for q in ch["knowledge_check"])
    btn = f"binder-btn-{sid}"
    loading = f"binder-loading-{sid}"
    frame = f"binder-frame-{sid}"
    return f'''---
title: "Chapter {ch['num']}: {ch['title']}"
layout: base.njk
---
{{% from "chapter-band.njk" import render as chapterBand %}}
{{{{ chapterBand({ch['num']}, "{ch['title']}", "{ch['theme'].replace('theme-', '')}") }}}}

<p>{ch['hook']}</p>

<div class="box box-objectives">
  <div class="icon-badge"><img src="/images/icons/{ch['icon']}.png" alt=""></div>
  <div class="box-title">By the end of this chapter, you can...</div>
  <div class="box-body">
    <ul>
{obj_items}
    </ul>
  </div>
</div>

<h2>{ch['lesson_title']}</h2>
<p>{ch['lesson_body']}</p>
<p><strong>Worked example:</strong> {ch['worked_example']}</p>

<p>Run this chapter's notebook right here on the page, powered by MyBinder.</p>

<button id="{btn}" class="binder-btn" onclick="
  this.style.display='none';
  document.getElementById('{loading}').style.display='flex';
  var f = document.getElementById('{frame}');
  f.addEventListener('load', function () {{
    document.getElementById('{loading}').style.display='none';
    f.style.display='block';
  }});
  f.src = f.dataset.src;
">
  <img src="/images/icons/play.png" alt="">
  Run this chapter's notebook
</button>

<div id="{loading}" class="binder-loading" style="display:none">
  <div class="icon-badge"><img src="/images/icons/gear.png" alt=""></div>
  <img class="mascot" src="/images/mascot-waiting.png" alt="">
  <div>
    <div class="status-text">Launching your Jupyter session&hellip;</div>
    <div class="dots"><span></span><span></span><span></span></div>
  </div>
</div>
<div class="binder-frame-wrap">
  <div class="icon-badge"><img src="/images/icons/play.png" alt=""></div>
  <iframe id="{frame}" class="binder-frame" style="display:none" data-src="https://mybinder.org/v2/gh/abderrahim-lectures/build-up-python-for-little-geniuses/master?filepath=notebooks/{sid}.ipynb"
    title="Chapter {ch['num']} notebook, running live via MyBinder"></iframe>
</div>
<p class="binder-note">&#128205; First launch can take 1–5 minutes while MyBinder builds your Python environment.</p>

<div class="box box-code">
  <div class="icon-badge"><img src="/images/icons/gear.png" alt=""></div>
  <div class="box-title">{ch['code_title']}</div>
  <div class="box-body">{ch['code_demo']}</div>
</div>

<div class="box box-knowledgecheck">
  <div class="icon-badge"><img src="/images/icons/question.png" alt=""></div>
  <div class="box-title">Check My Knowledge</div>
  <div class="box-body">
    <ol>
{kc_items}
    </ol>
  </div>
</div>

<div class="box box-retrieval">
  <div class="icon-badge"><img src="/images/icons/star.png" alt=""></div>
  <div class="box-title">Retrieval Challenge</div>
  <div class="box-body">{ch['retrieval']}</div>
</div>

<div class="box box-retrieval">
  <div class="icon-badge"><img src="/images/icons/wrench.png" alt=""></div>
  <div class="box-title">Track B: Build</div>
  <div class="box-body">{ch['track_b']}</div>
</div>
'''


def make_notebook(ch):
    sid = slug_id(ch)
    cells = [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": f"# Chapter {ch['num']}: {ch['title']}\n\n"
                      f"[![Launch on MyBinder](https://mybinder.org/badge_logo.svg)]"
                      f"(https://mybinder.org/v2/gh/abderrahim-lectures/build-up-python-for-little-geniuses/master?filepath=notebooks/{sid}.ipynb)\n\n"
                      f"{ch['hook']}\n\n**By the end of this chapter you can:**\n"
                      + "\n".join(f"- {o}" for o in ch["objectives"]),
        },
        {"cell_type": "markdown", "metadata": {}, "source": f"## Try it yourself\n\n{ch['notebook_intro']}"},
    ]
    for i, code in enumerate(ch["notebook_code"]):
        cells.append({"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": code})
        if i == 0 and len(ch["notebook_code"]) > 1:
            cells.append({"cell_type": "markdown", "metadata": {}, "source": "## Now make it your own"})
    kc = "\n".join(f"{i+1}. {q}" for i, q in enumerate(ch["knowledge_check"]))
    cells.append({
        "cell_type": "markdown", "metadata": {},
        "source": f"## Check My Knowledge\n\n{kc}\n\n"
                  '*(Answers: this is a "not yet" zone – there\'s no wrong guess here, just try it and see!)*',
    })
    nb = {
        "cells": cells,
        "metadata": {
            "colab": {"name": f"{sid}.ipynb", "provenance": []},
            "kernelspec": {"display_name": "Python 3", "name": "python3"},
            "language_info": {"name": "python"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    return nb


def make_foundations_module(ch):
    sid = slug_id(ch)
    header = f'"""Chapter {ch["num"]}: {ch["title"]}. {ch["hook"]}"""\n\n\n'
    if ch.get("is_class"):
        body = f"class {ch['class_name']}:\n    {ch['class_body']}\n"
    else:
        body = (
            f"def {ch['func_name']}({ch['func_sig']}):\n"
            f'    """{ch["func_doc"]}"""\n'
            f"    {ch['func_body']}\n"
        )
    return header + body


def make_test_module(ch):
    sid = slug_id(ch)
    name = ch["class_name"] if ch.get("is_class") else ch["func_name"]
    lines = [f"from code_project.foundations.{sid} import {name}\n\n"]
    for test_name, body in ch["tests"]:
        lines.append(f"def {test_name}():\n    {body}\n\n")
    return "\n".join(lines).rstrip() + "\n"


def main():
    for ch in CHAPTERS:
        sid = slug_id(ch)

        page_dir = WEB_SRC / f"chapter{ch['num']}"
        page_dir.mkdir(parents=True, exist_ok=True)
        (page_dir / "index.njk").write_text(make_web_page(ch), encoding="utf-8")

        NOTEBOOKS.mkdir(parents=True, exist_ok=True)
        (NOTEBOOKS / f"{sid}.ipynb").write_text(json.dumps(make_notebook(ch), indent=1), encoding="utf-8")

        FOUNDATIONS.mkdir(parents=True, exist_ok=True)
        (FOUNDATIONS / f"{sid}.py").write_text(make_foundations_module(ch), encoding="utf-8")

        TESTS.mkdir(parents=True, exist_ok=True)
        (TESTS / f"test_{sid}.py").write_text(make_test_module(ch), encoding="utf-8")

        print(f"Chapter {ch['num']:2d} ({ch['title']}) -- wrote page, notebook, module, tests")


if __name__ == "__main__":
    main()
