## Mutable_Destruction

## Description
Mutable Destruction is designed to be a modular wargame engine. AI is rapidly evolving with new capabilities emerging almost daily. In order to take advantage of these, we wanted our solution to be as "mutable" as possible.

What makes it modular is that it is simple to change anything from how input is dealt with to editing or adding entities involved, rules of arbitration or even how the game is displayed and interacted with.

The use of AI in this engine is in three parts. 
1.To parse natural language inputs for relevant elements needed to conduct the game. 
2. Behave as the opposition. 
3. Generate an output in natural language to convey the narrative. In essence, it become the piece in between the engine and the human as well as the opposition. You could just as easily have the opposition be a human player. Research has shown that most wargames, both board and computer, are played single player, often with the same player acting as both sides; so we decided to let the AI take on the role of red team for the default implementation.

The reason for the modular approach is this:
There are a lot of wargames and wargame mechanics out there. How wargames are used can vary vastly in use.They have been used in financial, corporate, humanitarian, and military scenarios. From concept testing, to simulation training to experimentation. From trying to find out what you don't know, to proving what you know is right to training chosen methodology.
The design of a wargame can actually shape the narrative, at times becoming more about training to game the game instead of test, prove or train the concept. Each wargame needs to be custom fit to the need and the ramifications of the limitations understood and the risk accepted. These are decisions that should not be made by the game designer, but instead by the scenario users. The level of fidelity should also be a decision made at the same level.

In the game presented for demonstration, instead of attempting fidelity to reality, we chose a simple ruleset that will not be a true representation of any reality. We do not have the data and any data we supplied would be uneducated guesses and become more about how real the rules are instead of what we were attempting to demonstrate. We went with a simple playout of decisions. The point is not if the rules represent reality, but that there are some set of rules to move play along.

Ideally, more information can be added for each of the elements involved in the game, the rules can be changed to be more representative of any actual situation and the interface can be as eleborate or as simple as desired.

We hope that you find this useful!

## Badges
On some READMEs, you may see small images that convey metadata, such as whether or not all the tests are passing for the project. You can use Shields to add some to your README. Many services also have instructions for adding a badge.

## Visuals
Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.

## Installation
Within a particular ecosystem, there may be a common way of installing things, such as using Yarn, NuGet, or Homebrew. However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection.

## Usage
Each turn player enters in the text input field, in plain text, any desired actions to achieve goals towards win condition. Press enter. Play continues until either all will or all lose conditions for either team are complete.

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
Initial implementation testing
Build out interactive scenario input
Build out interactive rules change
Build out interactive opposition player behaviour
Build out interactive entites entry
Build out interactive graphical interface

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
