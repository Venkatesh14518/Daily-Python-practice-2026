#We have 2 variables glass1 and glass2. glass1 contains milk and glass2 contains juice. Write 3 lines of code to switch the contents of the variables. You are not allowed to type the words "milk" or "juice". You are only allowed to use variables to solve this exercise.

glass1 = "milk"      # glass1 initially contains milk
glass2 = "juice"     # glass2 initially contains juice

temp = glass1        # store the value of glass1 (milk) in a temporary variable
glass1 = glass2      # assign the value of glass2 (juice) to glass1
glass2 = temp        # assign the stored value (milk) from temp to glass2
