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
