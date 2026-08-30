# 12 week MIT lec 1-12.   6.0001  OPENCOUSEWARE

# Week 1 — Python Foundations & Calculator

## Overview

Week 1 marked the beginning of my structured software development journey with Python. The primary objective of this week was to establish a strong understanding of fundamental programming concepts while simultaneously developing practical habits that would remain valuable throughout the rest of the portfolio. Rather than approaching programming as a purely theoretical subject, the emphasis was placed on understanding how individual programming concepts combine to form functional software.

The week began with an introduction to Python and the fundamental principles of computer science through the MIT OpenCourseWare course **6.0001 — Introduction to Computer Science and Programming in Python**. This provided a structured academic foundation for the practical work completed during the week.

In addition to studying Python, I established the infrastructure required to document and publish my work professionally. This included creating accounts on GitHub and edX and establishing the `Summer-2026-Portfolio` repository. This repository serves as a central location for recording my progress, projects, experiments, and development milestones.

## Learning Objectives

The main objectives for Week 1 were:

* Understand Python's basic syntax and structure.
* Learn how variables store and represent information.
* Understand expressions and how Python evaluates them.
* Become comfortable receiving input from users.
* Learn how to display information using output statements.
* Understand the purpose and structure of functions.
* Practise fundamental Python programming through exercises.
* Apply these concepts to a functional calculator.
* Learn the basic principles of version control and GitHub.
* Begin documenting software projects professionally.

## Python Fundamentals

One of the most important lessons from this week was understanding that programming is fundamentally about transforming information. Variables allow a program to store information, while expressions allow that information to be manipulated and evaluated.

I also worked with Python's input and output mechanisms. User input transforms a static program into an interactive application because the program can respond to information provided at runtime.

Functions were another significant concept. Instead of placing every instruction into one continuous sequence, functions allow related behaviour to be organised into reusable components. This makes programs easier to understand, maintain, debug, and expand.

Throughout the week, I completed a series of Python exercises designed to reinforce these concepts. These exercises were important because they required me to apply programming concepts rather than simply recognise them theoretically.

## Calculator Project

The main practical project for Week 1 was a command-line calculator.

The calculator was designed to perform fundamental arithmetic operations while accepting values directly from the user. Developing this project provided an opportunity to combine variables, expressions, functions, input, and output into a single application.

The project was subsequently improved through error handling and code refinement. This was particularly important because a program should not assume that users will always provide valid input.

For example, mathematical programs need to account for situations such as invalid characters, incorrect numerical input, and division by zero. Handling these situations improves the reliability and overall quality of the software.

## GitHub & Version Control

Another important component of Week 1 was learning how software development extends beyond writing code.

Creating the `Summer-2026-Portfolio` repository introduced the concept of version control and provided a professional environment in which my work could be documented. Publishing projects to GitHub allows development progress to be tracked over time and creates a public record of the skills and projects developed throughout the summer.

Documentation was also introduced through the creation of a README for the calculator project. This established an important principle that will continue throughout the portfolio: software should be understandable not only to its creator, but also to other developers who may inspect or use it.

## Challenges & Lessons Learned

The primary challenge during Week 1 was adapting from thinking about programming as a collection of commands to understanding it as a method for solving problems.

Writing code that technically works is only the beginning. Good software should also be structured, readable, predictable, and resilient to unexpected input.

The calculator demonstrated this principle particularly well. A basic implementation can perform calculations, but a more thoughtful implementation considers what happens when the user enters something unexpected.

## Conclusion

Week 1 established the foundation for the remainder of the portfolio. I developed an initial understanding of Python programming, completed practical exercises, created a functional calculator, introduced error handling, and established my GitHub development environment.

More importantly, this week introduced the mindset that programming is not simply about memorising syntax. It is about understanding problems, designing solutions, testing assumptions, and continuously improving implementations.

This foundation will support the increasingly complex projects developed throughout the following weeks.





# Week 2 — Control Flow & Number Guessing Game

## Overview

Week 2 focused on one of the most important transitions in programming: moving from sequential instructions to programs capable of making decisions and repeating operations.

The central concepts studied during this week were **conditionals, loops, and nested loops**. These concepts fundamentally expand what a program can accomplish because they allow software to respond dynamically to circumstances rather than simply executing a predetermined sequence of instructions.

The practical project for the week was a **Number Guessing Game**. Although the project is relatively simple in appearance, it provided an effective environment for applying the core control-flow concepts studied throughout the week.

## Learning Objectives

The objectives for Week 2 were:

* Understand conditional statements.
* Use `if`, `elif`, and `else` effectively.
* Understand how programs evaluate logical conditions.
* Learn how loops control repeated execution.
* Understand the difference between common looping approaches.
* Explore nested loops.
* Apply control-flow concepts to a complete program.
* Develop stronger debugging and problem-solving skills.
* Publish a completed project through GitHub.

## Conditionals

Conditionals allow programs to make decisions.

A program can evaluate information and execute different instructions depending on the result. This is one of the fundamental mechanisms behind interactive software.

For example, a number-guessing game needs to determine whether the player's guess is too high, too low, or correct. Each possibility requires a different response, making conditional logic essential to the project's functionality.

Learning to structure these decisions clearly was an important part of the week. Poorly organised conditions can make programs difficult to understand and can result in logical errors.

## Loops

Loops introduced another major programming capability: repetition.

Instead of writing the same instructions repeatedly, a loop allows a program to execute a block of code multiple times according to a specified condition or sequence.

This concept is particularly useful for interactive programs. In the Number Guessing Game, the player should normally be able to continue guessing until they either find the correct number or reach the game's limit.

Loops therefore transformed the project from a simple one-time interaction into an actual game.

## Nested Loops

Nested loops were also introduced during this week. A nested loop is a loop operating inside another loop.

Although nested loops can become computationally expensive when used carelessly, they are extremely useful for problems involving multiple layers of repetition.

Understanding their structure also improved my ability to reason about how Python executes code and how individual blocks interact with one another.

## Number Guessing Game

The major project for Week 2 was the Number Guessing Game.

The concept is straightforward: the program selects a number, and the player attempts to determine what it is. After each guess, the program evaluates the player's input and provides information about whether the guess is higher or lower than the target.

The project required several concepts to work together:

* Variables to store the target and player input.
* Input handling to receive guesses.
* Conditionals to evaluate guesses.
* Loops to allow repeated attempts.
* Logical reasoning to determine when the game should terminate.

The simplicity of the concept was beneficial because it allowed the focus to remain on programming logic rather than complicated application design.

## Testing & Debugging

Testing became increasingly important during this project.

A functioning program must be tested against multiple possible situations, not merely the ideal scenario. I therefore considered situations such as correct guesses, incorrect guesses, repeated attempts, and boundary conditions.

Debugging these scenarios helped demonstrate the difference between syntax errors and logical errors. A program can execute without producing a Python error while still behaving incorrectly.

## Lessons Learned

The most significant lesson from Week 2 was that control flow is what gives programs their intelligence and flexibility.

Variables allow programs to remember information, but conditionals and loops determine what the program actually does with that information.

The Number Guessing Game demonstrated how relatively small pieces of logic can combine to create an interactive experience.

## Conclusion

Week 2 expanded my Python knowledge beyond basic syntax and introduced the foundations of program logic.

By studying conditionals, loops, and nested loops and applying them to a complete game, I developed a stronger understanding of how programs make decisions, repeat operations, and respond to users.

The Number Guessing Game also represented an important step toward building larger projects because it required multiple concepts to operate together within one coherent application.





# Week 3 — Data Structures & Student Grade Manager

## Overview

Week 3 focused on Python's fundamental data structures: **strings, lists, tuples, and dictionaries**.

While variables are useful for storing individual pieces of information, real software frequently needs to manage collections of related data. Data structures provide the mechanisms required to organise that information efficiently and meaningfully.

The practical project for this week was a **Student Grade Manager**, which provided a realistic context for applying these structures.

## Learning Objectives

The primary objectives were:

* Understand Python strings and string manipulation.
* Learn how lists store ordered collections.
* Understand tuples and immutable collections.
* Learn how dictionaries associate keys with values.
* Determine which data structure is appropriate for different situations.
* Combine multiple structures within a practical program.
* Improve organisational thinking when designing software.
* Test and document a complete Python application.
* Publish the project to GitHub.

## Strings

Strings represent textual information and are fundamental to almost every interactive application.

During this week, I explored how strings can be created, accessed, manipulated, and processed. Understanding strings was particularly useful for handling student names, messages, labels, and other textual information within the Grade Manager.

String operations also demonstrated how programming languages allow developers to transform raw information into meaningful output.

## Lists

Lists introduced the ability to store multiple values in a single structure.

This is essential when working with collections of related information. Instead of creating separate variables for every grade, a list can contain multiple grades and allow the program to process them systematically.

Lists are particularly useful because they are ordered and mutable, meaning their contents can be changed during program execution.

## Tuples

Tuples provided an important contrast to lists.

Although tuples can also contain multiple values, their contents cannot normally be modified after creation. This immutability makes tuples useful when information should remain fixed.

Understanding the distinction between mutable and immutable structures is important because the choice of data structure can influence the safety and behaviour of a program.

## Dictionaries

Dictionaries introduced another significant programming concept: associating information through **key-value pairs**.

This structure is particularly appropriate for the Student Grade Manager because student information naturally involves relationships.

For example, a student's name can function as a key while their grades or related information can be stored as the corresponding value.

Dictionaries therefore provide a more meaningful organisational model than simply storing unrelated values in separate variables.

## Student Grade Manager

The main project for Week 3 was the Student Grade Manager.

The program was designed to organise student-related grade information and perform useful operations on that data.

Developing the project required me to consider how information should be represented before writing the code. This was an important progression from earlier projects because the problem was no longer simply about making a program respond to a single input.

Instead, the program needed to manage structured information.

The project therefore combined multiple Python concepts, including strings, lists, dictionaries, loops, conditionals, and functions.

## Problem-Solving & Data Design

One of the most important lessons from this project was that programming begins before the first line of code is written.

Before implementing functionality, it is necessary to decide what information the program needs, how that information should be represented, and how different pieces of data relate to one another.

Choosing an inappropriate data structure can make an otherwise simple problem unnecessarily complicated.

## Testing

Testing focused on ensuring that the program behaved correctly under different conditions.

I considered situations involving different students, multiple grades, varying input, and calculations based on stored information.

Testing also helped identify assumptions within the program and encouraged me to design the application in a more robust manner.

## Lessons Learned

Week 3 significantly improved my understanding of how software manages information.

The key lesson was that data structures are not merely language features to memorise. They are tools for modelling real-world information.

Understanding when to use a list, tuple, dictionary, or string makes it possible to design cleaner and more efficient solutions.

## Conclusion

Week 3 represented an important step forward in my development as a programmer.

The Student Grade Manager required me to move beyond isolated values and work with organised collections of information. By combining multiple Python data structures with previously learned programming concepts, I gained a more complete understanding of how practical applications are constructed.

This knowledge provides an essential foundation for future projects involving larger datasets and more sophisticated systems.






# Week 4 — Algorithms, Computational Thinking & Robotics Scoring

## Overview

Week 4 shifted the focus from individual Python features toward the broader principles of **algorithms, computational thinking, and structured problem solving**.

Learning programming syntax is important, but professional software development requires considerably more than knowing how to write Python statements. Developers must be able to analyse problems, identify patterns, design logical procedures, and transform abstract requirements into reliable algorithms.

The main practical project for this week was the **Robot Competition Score Manager**.

This project provided a useful bridge between programming fundamentals and real-world computational problems because competition scoring involves structured data, calculations, ranking, and decision-making.

## Learning Objectives

The primary objectives of Week 4 were:

* Understand the concept of an algorithm.
* Develop computational thinking skills.
* Break complex problems into manageable components.
* Design logical solutions before implementation.
* Apply Python fundamentals to a realistic problem.
* Work with structured competition data.
* Calculate and compare scores.
* Produce meaningful results from raw information.
* Document software professionally.

## Algorithms

An algorithm is a clearly defined sequence of steps used to solve a problem.

Although algorithms are often associated with advanced computer science, even simple programs rely on them.

For the Robot Competition Score Manager, the program needed a logical procedure for accepting scores, processing them, and determining meaningful results.

Thinking algorithmically required me to consider the problem independently from the Python syntax. The goal was first to determine what the program needed to accomplish and only then determine how Python could implement the solution.

## Computational Thinking

Computational thinking involves approaching problems in a structured manner.

Rather than attempting to solve an entire problem simultaneously, it can be divided into smaller components.

For the competition manager, these components could include:

1. Registering competition information.
2. Storing team names.
3. Recording scores.
4. Processing results.
5. Comparing teams.
6. Producing rankings.
7. Displaying the final information clearly.

This decomposition made the overall problem significantly easier to understand.

## Robot Competition Score Manager

The Robot Competition Score Manager was developed as the week's primary practical application.

The program focuses on managing scoring information for a robotics competition. Such a system provides a realistic programming scenario because it combines user input, data storage, calculations, comparisons, and output.

The project also encouraged consideration of data accuracy. A scoring system cannot simply assume that every input will be correct.

This reinforced lessons from previous weeks concerning validation, error handling, and reliable program behaviour.

## Problem Solving

One of the strongest lessons from Week 4 was the importance of separating **problem solving** from **implementation**.

When programmers immediately begin writing code, they can easily become trapped by the details of syntax before fully understanding the problem.

A better process is to identify requirements, break them down, develop an algorithm, consider edge cases, and then implement the solution.

This approach is increasingly important as projects become larger.

## Documentation

Documentation was another important part of the week.

A professional software project should explain its purpose, functionality, usage, and development decisions. A README provides users and developers with an accessible introduction to the project.

Documentation also forces the developer to understand the project clearly enough to explain it to someone else.

## Lessons Learned

Week 4 demonstrated that becoming a stronger programmer is not simply a matter of learning more Python commands.

The ability to reason about problems is equally important.

Algorithms provide the structure, computational thinking provides the methodology, and programming languages provide the implementation tools.

## Conclusion

Week 4 concluded the first major stage of my Python development plan.

Across the first four weeks, I progressed from fundamental syntax and simple calculations toward structured applications involving data, logic, and algorithms.

The Robot Competition Score Manager represented this progression by requiring multiple programming concepts to work together around a realistic problem.

The knowledge gained during this week provides a foundation for approaching increasingly complex software and robotics-related projects.






# Week 5 — GitHub Mastery & Professional Development

## Overview

Week 5 focused on an aspect of software development that extends beyond programming itself: **professional version control and collaboration using GitHub**.

Writing functional code is only one part of becoming a capable software developer. Modern development depends heavily on version control, documentation, collaboration, code review, and the ability to maintain projects over time.

This week was therefore dedicated to developing a professional GitHub workflow and understanding how software projects are managed beyond the code editor.

## Learning Objectives

The objectives for Week 5 were:

* Understand the fundamentals of GitHub.
* Learn how repositories are structured.
* Improve README documentation using Markdown.
* Understand the purpose of commits.
* Learn how branches can support development.
* Understand pull requests and code review.
* Learn how merge conflicts occur.
* Develop strategies for resolving conflicts.
* Improve the presentation of my GitHub profile.
* Build a consistent development history.

## GitHub

GitHub provides an environment for hosting and managing software projects using Git version control.

Throughout the previous weeks, GitHub was primarily used as a location for publishing completed projects. Week 5 expanded this understanding by focusing on GitHub as a development platform rather than simply a storage location.

A professional repository should communicate clearly what a project does, why it exists, how it can be used, and how it was developed.

## Commits

Commits provide a historical record of changes made to a project.

Rather than treating a project as a single finished object, version control allows development to be viewed as a sequence of improvements.

The goal for this week was to develop a consistent committing habit and contribute meaningful changes rather than creating commits solely to increase a numerical total.

The target of 25 commits encouraged regular development activity while reinforcing the importance of making changes that represent genuine progress.

## Markdown & Documentation

Markdown became another important skill during this week.

GitHub uses Markdown extensively for README files and other project documentation. Learning to structure documentation effectively allows technical information to become easier to navigate and understand.

Professional documentation should have a clear hierarchy, meaningful headings, concise explanations, and appropriate formatting.

This skill is particularly valuable because documentation is often the first part of a project that another developer or recruiter will encounter.

## Pull Requests

Pull requests provide a mechanism for proposing and reviewing changes before they become part of a project's primary codebase.

Understanding pull requests introduced the concept of code review.

Code review is valuable because another developer may identify problems, inconsistencies, or improvements that the original author did not notice.

This reinforces an important principle of professional development: software quality improves when code is examined from multiple perspectives.

## Merge Conflicts

Merge conflicts occur when Git cannot automatically reconcile competing changes.

Although conflicts can initially appear intimidating, understanding why they occur makes them significantly easier to resolve.

The important lesson is that conflicts are a normal part of collaborative software development rather than evidence that the version-control system has failed.

## Professional GitHub Profile

The final focus of Week 5 was the presentation of my GitHub profile.

A professional profile should provide a clear representation of technical interests, projects, progress, and capabilities.

Repositories should be organised and documented consistently so that someone unfamiliar with my work can understand what I have created.

## Lessons Learned

The most important lesson from Week 5 was that professional programming involves much more than writing code.

Version control, documentation, collaboration, code review, and project presentation are all essential skills.

## Conclusion

Week 5 transformed GitHub from a basic publishing platform into an important part of my development workflow.

By learning version control concepts, Markdown, pull requests, merge conflicts, and professional repository management, I developed skills that will remain relevant as future projects become larger and more collaborative.

The experience also reinforced the importance of treating software development as an organised engineering process rather than simply writing code until a program works.






# Week 6 — Tic-Tac-Toe: Initial Development

## Overview

Week 6 marked a transition from small programming exercises toward the development of a complete interactive game: **Tic-Tac-Toe**.

The purpose of this project was not simply to recreate a familiar game. Instead, Tic-Tac-Toe provided a compact environment in which fundamental programming concepts could be combined into a single system.

The project required planning, board design, user interaction, validation, game-state management, and decision-making logic.

## Project Objectives

The primary objectives were:

* Define the rules of Tic-Tac-Toe.
* Design a 3×3 game board.
* Represent the board using Python data structures.
* Display the current game state.
* Allow players to select available positions.
* Prevent invalid moves.
* Detect winning conditions.
* Detect draws.
* Manage turns correctly.
* Establish a foundation for more advanced game logic.

## Planning the Game

Before implementation, the game's rules and structure needed to be clearly defined.

Tic-Tac-Toe consists of a 3×3 board in which players take turns placing their respective symbols. A player wins by obtaining three matching symbols in a horizontal, vertical, or diagonal line.

If all positions become occupied without a winning combination, the game ends in a draw.

Although these rules are simple, translating them into program logic requires careful planning.

## Board Representation

The board was represented using a Python list containing nine positions.

Each position corresponds to one square on the 3×3 board. This representation provides a simple way to store the state of the game while allowing individual positions to be accessed and modified.

A visual representation is then generated from this underlying data.

This separation between data and presentation is an important programming concept. The board itself is stored as information, while the display function determines how that information is presented to the player.

## Player Interaction

The player needs a clear method of selecting a square.

The program therefore accepts user input and converts it into a board position. Before making a move, the program checks whether the selected square is available.

This validation is essential because allowing players to overwrite existing moves would break the rules of the game.

## Game-State Management

The program must continuously maintain an accurate representation of the current game state.

After every move, the game needs to determine:

* Whose turn it is.
* Which squares are occupied.
* Whether someone has won.
* Whether the board is full.
* Whether the game should continue.

This requires multiple components of logic to work together correctly.

## Winning Conditions

Detecting a winner is one of the central challenges of Tic-Tac-Toe.

There are eight possible winning combinations: three rows, three columns, and two diagonals.

The program must examine these combinations after each move and determine whether any contains three matching symbols.

This provided useful practice in translating a real-world rule into a precise computational condition.

## Challenges

One of the main challenges was ensuring that individual functions interacted correctly.

A change to board representation, for example, can affect the display system, input handling, and win detection.

This demonstrated why planning and modular programming are important.

## Lessons Learned

The most important lesson from Week 6 was that even a small game can contain considerable programming complexity.

Tic-Tac-Toe required me to think about data representation, user interaction, validation, game states, and logical conditions simultaneously.

The project also reinforced the importance of designing the system before implementing individual features.

## Conclusion

Week 6 established the foundation of the Tic-Tac-Toe project.

Rather than treating the game as one large block of code, the project was approached as a collection of interconnected systems.

This approach improved my understanding of program architecture and prepared the project for further refinement and improvement in the following week.






# Week 7 — Tic-Tac-Toe Refinement & Improvement

## Overview

Week 7 continued the Tic-Tac-Toe project with a focus on **refinement, debugging, reliability, and improvement**.

Developing the initial version of a program is only the first stage of software engineering. A program may function under ideal circumstances while still containing usability problems, logical weaknesses, or edge cases that have not been considered.

The purpose of Week 7 was therefore to examine the existing implementation critically and improve its overall quality.

## Objectives

The main objectives were:

* Review the existing Tic-Tac-Toe implementation.
* Identify logical and usability problems.
* Improve board interaction.
* Strengthen input validation.
* Ensure invalid moves are handled correctly.
* Improve game-state management.
* Test winning and draw conditions.
* Refine the user interface.
* Remove unnecessary or problematic code.
* Produce a more reliable final implementation.

## Debugging

Debugging became one of the most important activities during this stage.

A program can appear functional during normal gameplay while failing under less common circumstances.

For example, a player might enter invalid input, select an occupied square, or attempt to provide a value outside the expected range.

These situations require the program to respond appropriately rather than crashing or corrupting the game state.

## Input Validation

Input validation was therefore treated as an important part of the refinement process.

The program should not assume that the player will always provide valid information.

A robust game verifies that the selected position exists, that the input has the correct format, and that the selected square is available.

This makes the program more resilient and creates a better experience for the player.

## Game Logic

The winning and draw detection systems were also examined carefully.

Because Tic-Tac-Toe contains a relatively small number of possible winning combinations, it is possible to explicitly evaluate each one.

However, correctness is critical. A single incorrect condition could allow a winning move to be missed or incorrectly declare a winner.

Testing therefore needed to include horizontal victories, vertical victories, diagonal victories, and draw scenarios.

## User Experience

The refinement process also involved improving the way information was presented to the player.

A game should communicate clearly what is happening, whose turn it is, which inputs are expected, and what the result of the game is.

Even in a command-line application, thoughtful presentation makes the program considerably easier to use.

This reinforced the principle that software quality includes both technical correctness and user experience.

## Testing Strategy

Testing was performed across a variety of scenarios.

The game needed to handle:

* Valid moves.
* Invalid positions.
* Occupied squares.
* Winning rows.
* Winning columns.
* Winning diagonals.
* Draw situations.
* Repeated interaction.
* Unexpected user input.

Testing these cases increased confidence in the final implementation.

## Lessons Learned

The most valuable lesson from Week 7 was that **building software and improving software are different skills**.

The initial version demonstrates whether an idea can be implemented. Refinement determines whether the implementation is reliable enough to be considered a quality program.

This distinction is fundamental to professional development.

I also learned that debugging is not simply about fixing visible errors. It involves questioning assumptions and deliberately attempting to find situations in which the program could fail.

## Conclusion

Week 7 transformed Tic-Tac-Toe from an initial implementation into a more refined and reliable application.

Through debugging, validation, testing, and interface improvements, the project demonstrated the complete development cycle more effectively than simply creating a program from scratch.

The experience provided a practical introduction to software maintenance and reinforced the importance of testing every system against both expected and unexpected behaviour.
