"""Typing test implementation"""

from utils import lower, split, remove_punctuation, lines_from_file
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    new_para = []
    for para in paragraphs:
        if select(para):
            new_para.append(para)
    if len(new_para) <= k:
        return ""
    else:
        return new_para[k]
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    def check(s):
        s = lower(remove_punctuation(s))
        s_array = split(s)
        for t in topic:
            for tmp_s in s_array:
                if t == tmp_s:
                    return True
        return False
    return check
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    n1 = len(typed_words)
    n2 = len(reference_words)
    count = 0

    if n1 == 0:
        return 0.0

    for i in range(min(n1, n2)):
        word = typed_words[i]
        ref = reference_words[i]
        if word == ref:
            count += 1
    return count / n1 * 100.0
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    return len(typed) * (60 / elapsed) / 5
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    min_value = 10000000
    min_word = user_word
    for valid_word in valid_words:
        if valid_word == user_word:
            return user_word
        
        cur_value = diff_function(user_word, valid_word, limit)
        if cur_value < min_value:
            min_value = cur_value
            min_word = valid_word
    return min_word if min_value <= limit else user_word
        
    # END PROBLEM 5


def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    if limit < 0:
        return 1
    
    if len(start) == 0:
        return len(goal)
    elif len(goal) == 0:
        return len(start)
    else:
        if start[0] == goal[0]:
            return shifty_shifts(start[1:], goal[1:], limit)
        else:
            return shifty_shifts(start[1:], goal[1:], limit-1) + 1
    # END PROBLEM 6


def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    # 本题其实有点在模拟动态规划的意思
    # 因为假设dp[i][j]表示start长度为i，goal长度为j时两个字符串之间的变动次数
    # 那么我们首先有 dp[i][0] = i 和 dp[0][j] = 0。（因为这里是纯做增加/删除）
    # 然后主要就是递推式子了，我们可以想到可能有三种情况，分别是增加/删除/修改
    # “增加”对应的是dp[i][j] = dp[i-1][j] + 1（也即在长为i-1的start串上再加上一个字母就ok了）
    # “删除”对应的是dp[i][j] = dp[i][j-1] + 1（也即在长为i的start串上再减去一个字母就ok了）
    # “修改”则需要考虑当前两个字母是否相同，
    #     相同的话为dp[i][j] = dp[i-1][j-1]，不同的话还有修改start的第i位，所以为dp[i][j] = dp[i-1][j-1] + 1
    # 最后，由于我们希望修改尽可能少，所以应当是三者种取min的那个。
    # 本题则是通过递归来模拟了dp的这一过程。

    if limit < 0:
        return 1

    if len(start) == 0: # Fill in the condition
        # BEGIN
        "*** YOUR CODE HERE ***"
        return len(goal)
        # END
    elif len(goal) == 0: # Feel free to remove or add additional cases
        # BEGIN
        "*** YOUR CODE HERE ***"
        return len(start)
        # END
    else:
        add_diff = pawssible_patches(start[:-1], goal[:], limit-1) + 1 # Fill in these lines
        remove_diff = pawssible_patches(start[:], goal[:-1], limit-1) + 1
        if start[-1] == goal[-1]:
            substitute_diff = pawssible_patches(start[:-1], goal[:-1], limit)
        else:
            substitute_diff = pawssible_patches(start[:-1], goal[:-1], limit-1) + 1
        # BEGIN
        "*** YOUR CODE HERE ***"
        return min(add_diff, remove_diff, substitute_diff)
        # END


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, user_id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    total = len(prompt)
    count = 0
    for i in range(len(typed)):
        typed_word = typed[i]
        prompt_word = prompt[i]
        if typed_word == prompt_word:
            count += 1
        else:
            break
    progress = count / total
    send({"id": user_id, "progress": progress})
    return progress
    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    import copy
    times_diff = []
    for i in range(len(times_per_player)):
        tmp = []
        for j in range(len(times_per_player[i])-1):
            tmp.append(times_per_player[i][j+1] - times_per_player[i][j])
        times_diff.append(copy.deepcopy(tmp))
    return game(words, times_diff)
    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    player_indices = range(len(all_times(game)))  # contains an *index* for each player
    word_indices = range(len(all_words(game)))    # contains an *index* for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    import copy
    result = []
    visited = [False]*len(all_words(game))
    for i in player_indices:
        tmp = []
        for j in word_indices:
            cur_time = time(game, i, j)
            all_time = [t[j] for t in all_times(game)]
            if cur_time == min(all_time) and not visited[j]:
                tmp.append(word_at(game, j))
                visited[j] = True
        result.append(copy.deepcopy(tmp))
    return result
    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

# Change to True when you're ready to race.
# enable_multiplayer = False
enable_multiplayer = True

##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)