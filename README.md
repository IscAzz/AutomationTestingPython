# Automation-Testing---Python
# C5-CodeAnnotations

<br>

## <font color='lightblue'> General Information </font>

<br>

### Members

 Team Members: Charlon Curmi, Neville Grech

 Challenger: James Mizzi


### A brief description of the project

Our project aims to explain what are Annotations and demonstrate how to use them.

[Retresco](https://www.retresco.com/encyclopedia-article/what-are-annotations) defines annotations as: 

Annotations in programming languages are, similar to those in linguistics, structural elements containing additional or meta-information in the source code of a program.

A detailed explanation of Annotations is found in our wiki section.

### Languages Used

* Java
* Python

### Instructions on how to run the code

Our project consists of several different main classes, since we demonstrate
unrelated examples. Please download the repository and follow the instructions
in the following guide section on the order of running the classes and what inputs 
and outputs are expected.

Links are provided to the different classes, so there is no need to manually navigate
through the source code, simply return to the guide each time after you run a piece of code.

If using editors such as VS Code, there is an option to preview this MD file so that it can be read with its intended formatting. Also, the preview makes it possible to use the links to navigate to the classes which will be demonstrated.

<br>


## <font color='lightblue'> General Guide </font>

<br>

### <font color='lightblue'> Python Decorators </font>

<br>


#### <font color='lightblue'> Guess the Number Task </font>

<br>

To demonstrate the functionality of decorators in Python, a small task has been created which could be
part of some larger more complex game. The task involves guessing a random number from 1 to 10, with different levels: where choosing a harder level will give less guesses and less points. Then points are awarded or deducted accordingly. The functions and decorators of the game reside in [GuessNumber](./py/GuessNumberTask/GuessNumber.py). 

In GuessNumber, there is a decorator called 'reachOfFunction', which modifies the functionality of any function that is annotated with this decorator by outputting to the console the exact start and end of the function that was called. As with many of our examples, this particular example of showing a function's boundaries may not seem very useful, but the ability to modify a function's behaviour without modifying its code is very powerful. The decorator 'reachOfFunctionModif' shows how a function that has arguments would be dealt with by the decorator.

The other 2 decorators are 'someDecorator1' and 'someDecorator2'. Again, these have no apparent usefulness, but we will use these to show an important functionality later on in 'GuessMain2'. For now, notice how they have they have documentation, which will be accessed by the help function in Python.

Please run [GuessMain1](./py/GuessNumberTask/GuessMain1.py) to check out how the simple game works. Notice how 'Function starts/ends here' is displayed before and after the execution of function 'guessNum' which indeed was annotated with 'reachOfFunction' decorator.

Running [GuessMain2](./py/GuessNumberTask/GuessMain2.py) shows the behaviour of the functions 'welcome1' and 'welcome2', which simply display a welcome message to the user. 'welcome1' has been annotated with 'someDecorator1' while 'welcome2' has been annotated with 'someDecorator2'. The difference is that when the name of each function is outputted, 'welcome1' outputs the name of the wrapper function from 'someDecorator1' while 'weclome2' outputs its actual name. The same happens when the help function is used to print the functions' documentation. This difference is happening because the 'someDecorator2' is making use of a special tool from 'functools' to preserve the identity of any function it annotates, while 'someDecorator1' is simply not. 

<br>

#### <font color='lightblue'> Some Other Examples </font>

<br>

In Python, Annotations are called Decorators. More information can be found on [Python Decorators](https://realpython.com/primer-on-python-decorators/).


* Example 1:

In [Example One : CIS1221_MainProcess](./py/Examples/CIS1221_MainProcess.py) we are difining two classes and a main class. Both classes use the same **def School(self,mark)** function but, we are **overriding** the function in the **class CIS1221_PassOrFail(CIS1221_SchoolExams):**, as we can it extends **CIS1221_SchoolExams**. In the main class we are taking the mark, giving it to the **School()** function and then output if the student passed the exam or not.


* Example 2:

In [Example Two : CIS1221_Square](./py/Examples/CIS1221_CalculateVolume.py) we first defined the function calculate which takes self,a,b, and c as parameters. Also, in the function we are calculating the volume. The user will input the length, the breadth, and the height. The variables will be added in the calculate function and the volume will be calculated. Then the volume will be outputted.



***
<br>
<br>

### <font color='lightblue'> Java Built-in Annotations </font>

<br>

* Example 1:

In [Example One : CIS1221_DOB](./jav/builtIn/CIS1221_DOB.java), the first line which is import of java.time.*, will import the exact date for when the program is used. This programm will use the **@Deprecated** Annotation. 

A deprecated method is one that has been outdated (as said on [w3schools.com](https://www.w3schools.com/JSREF/deprecated.htm)). The method that uses the **@Deprecated** is a simple method called **dOF_Simple** which takes the date, month and year and that outputs them in a print statement. 

From line 9 to 50 a method called **dOF_Optimized**, takes in the same parameters as the method before it. A variable, months will be used to varify the input from the user. The method **dOF_Optimized** contains a switch method which takes month as a parameter. After the switch statement finishes the method will calculate the age of the person. The currYear variable will store the present year that we are in by **Year.now().getValue()**. After, the age has been calculated to print() statements are outputted. 


[Example one : CIS1221_MainDOB](./jav/builtIn/CIS1221_MainDOB.java), is the main class. In the method a **static Scanner scn = new Scanner(System.in), and a static CIS1221_DOB dob = new CIS1221_DOB()** are outlined while the command static will outline that it can be used within the whole class.

In the main class the date, the month and the year will be inputted by the user. There are two types of outputs one from the Simple method and the other from the Optimized method. Both outputs will be outputted from the [CIS_221_DOB](./jav/builtIn/CIS1221_DOB.java) class.

<br>

* Example 2:

In [Example Two : CIS1221_Square](https://github.com/CIS1221-2022-2023/C5-CodeAnnotations/blob/Built-in-Annotations-by-Charlon/Java/Built-in%20Annotations/CIS1221_Square.java) an **interface CIS1221_Square** which acts as a main class is created. In it a method called **public double calculate(double a, double b, double c)**.


[Example Two : CIS1221_CalculateVolume](./jav/builtIn/CIS1221_CalculateVolume.java), holds the main class in it. A **static Scanner scn = new Scanner (System.in)** is created to be used by the whole class, that's why it has a **static** operator. In the main class the length, the breadth and the height is being inputted. A **Lambda Expression** is being used were **(double a, double b, double c)** is being converted **(->)** to **a * b * c**. To calculate the volume of the variables inputted by the user, they are passed to the method **calculate** in the [CIS1221_Square](./jav/builtIn/CIS1221_Square.java) class. After the volume is being outputted.

<br>

* Example 3:

Both classes of [Example Three : CIS1221_SchoolExams](./jav/builtIn/CIS1221_SchoolExams.java) and [Example Three : CIS1221_PassOrFail](./jav/builtIn/CIS1221_PassOrFail.java) use the same methods. They use the same method because [Example Three : CIS1221_PassOrFail](./jav/builtIn/CIS1221_PassOrFail.java) **extends** the class [Example Three : CIS1221_SchoolExams](./jav/builtIn/CIS1221_SchoolExams.java) which the **@Override** Annotation is used due to the extends operator. A method **public boolean School** takes in a parameter double mark. The mark then is processed through the if statement were it is checking if not the student has passed or not. 


[Example Three : CIS1221_MainProcess](./jav/builtIn/CIS1221_MainProcess.java) which is the main,  will print out if the student passed or not. A **static CIS1221_SchoolExams pf = new CIS1221_PassOrFail()**, is identified creating an object **pf** because of the extends in the beginning. The main starts with the user inputting the mark of the student. While using the object **pf** and inputting the mark in the School method, the if statement will output if the student passed (if true) or not (if false).
***
<br>
<br>

### <font color='lightblue'> Java Custom Annotations </font>

<br>

This section demonstrates the purpose of custom annotations and also meta annotation which are used to code custom annotations. Please run [MainClass](./jav/custom/MainClass.java) and read the following observations to understand what is happening. There is also in-line documentation in the files of the classes and annotations, which may be accessed by clicking any of the links provided.

There exists class [FootballPerson](./jav/custom/FootballPerson.java) which has a subclass [Player](./jav/custom/Player.java), which in turn has a subclass [Goalkeeper](./jav/custom/Goalkeeper.java). The custom annotation [Complex](./jav/custom/Complex.java) exists to show that a class is complex in some way and the programmer should be careful. 

First, the program checks whether the classes 'FootballPerson', 'Player' and 'Goalkeeper' are annotated as 'Complex'. If it is, the program outputs a message. The class 'Player' is not annotated as 'Complex', however will still output a warning message. This is because, although it itself is not annotated, the annotation 'Complex' is annotated with the meta annotation @Inherited which makes subclasses of classes annotated as 'Complex' also be 'Complex' as happens here. The same happens when checking if class 'Goalkeeper' is annotated as 'Complex'. As the output shows, it is, proving that annotations are inherited down any number of subclasses.

Secondly, there exists the annotation [Event](./jav/custom/Event.java) and its container [Events](./jav/custom/Events.java) which allows it to be annotated more than once on a particular class. The program outputs all the annotations 'Event' which annotate the class [Football](./jav/custom/Football.java). As shown in the output, there are multiple annotations with different information. This shows the purpose of the meta annotation @Repeatable.

Thirdly, there exist some methods with different functionalities in the class [Player](./jav/custom/Player.java). The program checks whether these methods are annotated with a custom annotation [DontRun](./jav/custom/DontRun.java). If so, they are not run, and the reason from the annotation as to why they should not run is outputted to the user. If they are not annotated with 'DontRun', then they are executed by the program.

Finally, there exist some different fields or attributes in the class 'Player'. Again, the program checks whether these attributes are annotated with a custom annotation [ImportantAttribute](./jav/custom/ImportantAttribute.java). If an attribute is annotated with 'ImportantAttribute', it is outputted to the user according to the magnitude it was assigned. If no magnitude was provided, the annotation has a default of magnitude 1, so it is printed once.

<br>

The meta annotations @Target and @Retention are applied in different ways on the custom annotations that were created. @Target is used to inform the compiler, what types the annotation can be appplied to. Meanwhile, @Retention is used to inform the compiler, for how long to keep the annotation around, meaing till before, during or after compilation.

To summarise, the custom annotations include: 

@Complex is applicable to a class, interface, enum or record declaration
- shows the purpose of @Inherited, @Documented, @Target, @Retention

@Event is applicable to a class, interface, enum or record declaration
- shows the purpose of @Repeatable
@Events is the container for @Event

@DontRun is applicable to methods
has attribute 'reason'
- shows the purpose of @Target

@ImportantAttribute is applicable to attributes
has attribute 'magnitude'
- shows the purpose of @Target

We have not yet demonstrated the purpose of the meta annotation @Documented. The custom annotation [Complex](./jav/custom/Complex.java) has been annotated with @Documented. What this does is make the custom annotation 'Complex' visible in the documentation of any class it annotates. 

The documentation for the package 'custom' has been created and is located in the C5-CodeAnnotations/doc. The class 'FootballPerson' was annotated as 'Complex'. As shown in this [image](https://github.com/CIS1221-2022-2023/C5-CodeAnnotations/blob/main/doc/documentation%20snapshot.JPG) (a snapshot taken from the documentation of the 'FootballPerson' class), 'Complex' is included in the documentation of 'FootballPerson'. This would not be so, had 'Complex' not been annotated as @Documented. 

You can check this out yourself, by navigating to our project 'C5-CodeAnnotations' on your computer, and from there navigate to 'doc' (the folder where the documentation has been stored) > jav > custom and click on 'FootballPerson.html'. Your browser will open the documentation, where you can see what has been captured in the image above.


***
<br>
<br>

### <font color='lightblue'> Assertions </font>

<br>

To display the functionality of assertions, a very simple app called 'Directory' was built in Java. This app acts as a Database to store and manipulate telephone numbers enetered by the user. The Directory has some more self-explanatory functions, but it is outside of the scope of this guide to make use of them.

To create an assertion in Java, the keyword *assert* is used, followed by an expression that is assumed to be true, and optionally an expression to be displayed only if the assumption is found to be false.
The expression to be tested as an assumption must return a boolean value.


```java
assert someCondition : "Message to accompany Error";
```

Before we test the assertions, feel free to become familiar with the Directory Program. Simply run the [DirectoryAssertionsDisabled](./jav/assertions/DirectoryAssertionsDisabled.java) class and try this simple input:

RUNNING

Enter 1 to make a New Entry. Enter a name, and 8-digit phone number.

Enter 5 to display names in the Directory.

Enter 6 to Exit.

<br>

Assertions can be enabled and disabled as required. By default, assertions are disabled on a java file. Unfortunately, we could not enable them for you on your machine, so we will explain how do it.  For this example assertions should be enabled for the 'Directory' class.

If you are using VS Code, here's how it can be done:

1. Run the [Directory](./jav/assertions/Directory.java) class. When prompted Enter 6 to exit.
2. Navigate to 'Run and Debug' from the pane on the left hand side of VS Code
3. As you can see, there is an option: *To customize Run and Debug create a launch.json file.* Click on this option and select Java as your debugger. Click [here](../.vscode/launch.json) to access the .json file. 
4. Find the configurations of the Directory class and before the curly bracket, add this line of code: 
,"vmArgs":"-enableassertions"
5. Save this change.

That should do the job. If you are not using VS Code, you can run the 'Directory' class with assertions enabled from the command prompt. Here's how to do that:

1. From the command prompt, navigate to the folder containing our project.
2. The navigate to this path: C5-CodeAnnotations/jav/assertions - on Windows this would be achieved with this command: cd C5-CodeAnnotations/jav/assertions
3. Compile the class 'Directory' with the command: javac Directory.java
4. Run the 'Directory' class with assertions enabled with the command: java -ea Directory.java


<br>

*DirectoryAssertionsDisabled* has assertions disabled.
*Directory* should now have assertions enabled.

To imitate the testing stage, we will run the code in the two classes, to compare the outcomes of having assertions disabled vs having them enabled. Imagine you are coding, and you are testing these assertions. 

There are 3 Assertions in the code. 
* Assertion 1 of line 16, is true. 
* Assertion 2 of line 69, is false.
* Assertion 3 of line 187, is true.

1. Run the [DirectoryAssertionsDisabled](./jav/assertions/DirectoryAssertionsDisabled.java) class, no assertion error will ever occur.
2. Run the [Directory](./jav/assertions/Directory.java) class after enabling assertions. Input 2 as your option. This will cause Assertion 2 to be false which will throw an exception, as you can see.

Notice how Assertion 1 caused no error, since it is true.

3. Re-run the [Directory](./jav/assertions/Directory.java) class. Input 3 as your option. Once again no error, since Assertion 3 is true. Enter 6 to Exit.

***
<br>

## The End

That brings us to the end of this guide. Thank you for your patience.
