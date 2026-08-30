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
