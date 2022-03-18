{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-block alert-info\" style=\"margin-top: 20px\">\n",
    "    <a href=\"https://cocl.us/NotebooksPython101\">\n",
    "         <img src=\"https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Ad/TopAd.png\" width=\"750\" align=\"center\">\n",
    "    </a>\n",
    "</div>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a href=\"https://cognitiveclass.ai/\">\n",
    "    <img src=\"https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Ad/CCLog.png\" width=\"200\" align=\"center\">\n",
    "</a>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h1>Python - Writing Your First Python Code!</h1>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p><strong>Welcome!</strong> This notebook will teach you the basics of the Python programming language. Although the information presented here is quite basic, it is an important foundation that will help you read and write Python code. By the end of this notebook, you'll know the basics of Python, including how to write basic commands, understand some basic types, and how to perform simple operations on them.</p> "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h2>Table of Contents</h2>\n",
    "<div class=\"alert alert-block alert-info\" style=\"margin-top: 20px\">\n",
    "    <ul>\n",
    "        <li>\n",
    "            <a href=\"#hello\">Say \"Hello\" to the world in Python</a>\n",
    "            <ul>\n",
    "                <li><a href=\"version\">What version of Python are we using?</a></li>\n",
    "                <li><a href=\"comments\">Writing comments in Python</a></li>\n",
    "                <li><a href=\"errors\">Errors in Python</a></li>\n",
    "                <li><a href=\"python_error\">Does Python know about your error before it runs your code?</a></li>\n",
    "                <li><a href=\"exercise\">Exercise: Your First Program</a></li>\n",
    "            </ul>\n",
    "        </li>\n",
    "        <li>\n",
    "            <a href=\"#types_objects\">Types of objects in Python</a>\n",
    "            <ul>\n",
    "                <li><a href=\"int\">Integers</a></li>\n",
    "                <li><a href=\"float\">Floats</a></li>\n",
    "                <li><a href=\"convert\">Converting from one object type to a different object type</a></li>\n",
    "                <li><a href=\"bool\">Boolean data type</a></li>\n",
    "                <li><a href=\"exer_type\">Exercise: Types</a></li>\n",
    "            </ul>\n",
    "        </li>\n",
    "        <li>\n",
    "            <a href=\"#expressions\">Expressions and Variables</a>\n",
    "            <ul>\n",
    "                <li><a href=\"exp\">Expressions</a></li>\n",
    "                <li><a href=\"exer_exp\">Exercise: Expressions</a></li>\n",
    "                <li><a href=\"var\">Variables</a></li>\n",
    "                <li><a href=\"exer_exp_var\">Exercise: Expression and Variables in Python</a></li>\n",
    "            </ul>\n",
    "        </li>\n",
    "    </ul>\n",
    "    <p>\n",
    "        Estimated time needed: <strong>25 min</strong>\n",
    "    </p>\n",
    "</div>\n",
    "\n",
    "<hr>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h2 id=\"hello\">Say \"Hello\" to the world in Python</h2>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "When learning a new programming language, it is customary to start with an \"hello world\" example. As simple as it is, this one line of code will ensure that we know how to print a string in output and how to execute code within cells in a notebook."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<hr/>\n",
    "<div class=\"alert alert-success alertsuccess\" style=\"margin-top: 20px\">\n",
    "[Tip]: To execute the Python code in the code cell below, click on the cell to select it and press <kbd>Shift</kbd> + <kbd>Enter</kbd>.\n",
    "</div>\n",
    "<hr/>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello, Python!\n"
     ]
    }
   ],
   "source": [
    "# Try your first Python output\n",
    "\n",
    "print('Hello, Python!')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "After executing the cell above, you should see that Python prints <code>Hello, Python!</code>. Congratulations on running your first Python code!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<hr/>\n",
    "<div class=\"alert alert-success alertsuccess\" style=\"margin-top: 20px\">\n",
    "    [Tip:] <code>print()</code> is a function. You passed the string <code>'Hello, Python!'</code> as an argument to instruct Python on what to print.\n",
    "</div>\n",
    "<hr/>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3 id=\"version\">What version of Python are we using?</h3>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p>\n",
    "    There are two popular versions of the Python programming language in use today: Python 2 and Python 3. The Python community has decided to move on from Python 2 to Python 3, and many popular libraries have announced that they will no longer support Python 2.\n",
    "</p>\n",
    "<p>\n",
    "    Since Python 3 is the future, in this course we will be using it exclusively. How do we know that our notebook is executed by a Python 3 runtime? We can look in the top-right hand corner of this notebook and see \"Python 3\".\n",
    "</p>\n",
    "<p>\n",
    "    We can also ask directly Python and obtain a detailed answer. Try executing the following code:\n",
    "</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Check the Python Version\n",
    "\n",
    "import sys\n",
    "print(sys.version)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<hr/>\n",
    "<div class=\"alert alert-success alertsuccess\" style=\"margin-top: 20px\">\n",
    "    [Tip:] <code>sys</code> is a built-in module that contains many system-specific parameters and functions, including the Python version in use. Before using it, we must explictly <code>import</code> it.\n",
    "</div>\n",
    "<hr/>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3 id=\"comments\">Writing comments in Python</h3>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p>\n",
    "    In addition to writing code, note that it's always a good idea to add comments to your code. It will help others understand what you were trying to accomplish (the reason why you wrote a given snippet of code). Not only does this help <strong>other people</strong> understand your code, it can also serve as a reminder <strong>to you</strong> when you come back to it weeks or months later.</p>\n",
    "\n",
    "<p>\n",
    "    To write comments in Python, use the number symbol <code>#</code> before writing your comment. When you run your code, Python will ignore everything past the <code>#</code> on a given line.\n",
    "</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Practice on writing comments\n",
    "\n",
    "print('Hello, Python!') # This line prints a string\n",
    "# print('Hi')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p>\n",
    "    After executing the cell above, you should notice that <code>This line prints a string</code> did not appear in the output, because it was a comment (and thus ignored by Python).\n",
    "</p>\n",
    "<p>\n",
    "    The second line was also not executed because <code>print('Hi')</code> was preceded by the number sign (<code>#</code>) as well! Since this isn't an explanatory comment from the programmer, but an actual line of code, we might say that the programmer <em>commented out</em> that second line of code.\n",
    "</p>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3 id=\"errors\">Errors in Python</h3>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p>Everyone makes mistakes. For many types of mistakes, Python will tell you that you have made a mistake by giving you an error message. It is important to read error messages carefully to really understand where you made a mistake and how you may go about correcting it.</p>\n",
    "<p>For example, if you spell <code>print</code> as <code>frint</code>, Python will display an error message. Give it a try:</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Print string as error message\n",
    "\n",
    "frint(\"Hello, Python!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p>The error message tells you: \n",
    "<ol>\n",
    "    <li>where the error occurred (more useful in large notebook cells or scripts), and</li> \n",
    "    <li>what kind of error it was (NameError)</li> \n",
    "</ol>\n",
    "<p>Here, Python attempted to run the function <code>frint</code>, but could not determine what <code>frint</code> is since it's not a built-in function and it has not been previously defined by us either.</p>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p>\n",
    "    You'll notice that if we make a different type of mistake, by forgetting to close the string, we'll obtain a different error (i.e., a <code>SyntaxError</code>). Try it below:\n",
    "</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Try to see build in error message\n",
    "\n",
    "print(\"Hello, Python!)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3 id=\"python_error\">Does Python know about your error before it runs your code?</h3>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Python is what is called an <em>interpreted language</em>. Compiled languages examine your entire program at compile time, and are able to warn you about a whole class of errors prior to execution. In contrast, Python interprets your script line by line as it executes it. Python will stop executing the entire program when it encounters an error (unless the error is expected and handled by the programmer, a more advanced subject that we'll cover later on in this course)."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Try to run the code in the cell below and see what happens:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Print string and error to see the running order\n",
    "\n",
    "print(\"This will be printed\")\n",
    "frint(\"This will cause an error\")\n",
    "print(\"This will NOT be printed\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3 id=\"exercise\">Exercise: Your First Program</h3>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p>Generations of programmers have started their coding careers by simply printing \"Hello, world!\". You will be following in their footsteps.</p>\n",
    "<p>In the code cell below, use the <code>print()</code> function to print out the phrase: <code>Hello, world!</code></p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello, world!\n"
     ]
    }
   ],
   "source": [
    "# Write your code below and press Shift+Enter to execute \n",
    "\n",
    "print('hello, world!')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Double-click __here__ for the solution.\n",
    "\n",
    "<!-- Your answer is below:\n",
    "\n",
    "print(\"Hello, world!\")\n",
    "\n",
    "-->"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p>Now, let's enhance your code with a comment. In the code cell below, print out the phrase: <code>Hello, world!</code> and comment it with the phrase <code>Print the traditional hello world</code> all in one line of code.</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello,world!\n"
     ]
    }
   ],
   "source": [
    "# Write your code below and press Shift+Enter to execute \n",
    "\n",
    "# print the traditional hello world\n",
    "\n",
    "print('hello,world!')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Double-click __here__ for the solution.\n",
    "\n",
    "<!-- Your answer is below:\n",
    "\n",
    "print(\"Hello, world!\") # Print the traditional hello world\n",
    "\n",
    "-->\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<hr>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h2 id=\"types_objects\" align=\"center\">Types of objects in Python</h2>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p>Python is an object-oriented language. There are many different types of objects in Python. Let's start with the most common object types: <i>strings</i>, <i>integers</i> and <i>floats</i>. Anytime you write words (text) in Python, you're using <i>character strings</i> (strings for short). The most common numbers, on the other hand, are <i>integers</i> (e.g. -1, 0, 100) and <i>floats</i>, which represent real numbers (e.g. 3.14, -42.0).</p>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a align=\"center\">\n",
    "    <img src=\"https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%201/Images/TypesObjects.png\" width=\"600\">\n",
    "</a>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p>The following code cells contain some examples.</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Integer\n",
    "\n",
    "11"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Float\n",
    "\n",
    "2.14"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# String\n",
    "\n",
    "\"Hello, Python 101!\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p>You can get Python to tell you the type of an expression by using the built-in <code>type()</code> function. You'll notice that Python refers to integers as <code>int</code>, floats as <code>float</code>, and character strings as <code>str</code>.</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Type of 12\n",
    "\n",
    "type(12)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Type of 2.14\n",
    "\n",
    "type(2.14)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Type of \"Hello, Python 101!\"\n",
    "\n",
    "type(\"Hello, Python 101!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p>In the code cell below, use the <code>type()</code> function to check the object type of <code>12.0</code>."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "float"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Write your code below. Don't forget to press Shift+Enter to execute the cell\n",
    "\n",
    "type(12.0)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Double-click __here__ for the solution.\n",
    "\n",
    "<!-- Your answer is below:\n",
    "\n",
    "type(12.0)\n",
    "\n",
    "-->"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3 id=\"int\">Integers</h3>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p>Here are some examples of integers. Integers can be negative or positive numbers:</p>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a align=\"center\">\n",
    "    <img src=\"https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%201/Images/TypesInt.png\" width=\"600\">\n",
    "</a>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p>We can verify this is the case by using, you guessed it, the <code>type()</code> function:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Print the type of -1\n",
    "\n",
    "type(-1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Print the type of 4\n",
    "\n",
    "type(4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Print the type of 0\n",
    "\n",
    "type(0)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3 id=\"float\">Floats</h3> "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p>Floats represent real numbers; they are a superset of integer numbers but also include \"numbers with decimals\". There are some limitations when it comes to machines representing real numbers, but floating point numbers are a good representation in most cases. You can learn more about the specifics of floats for your runtime environment, by checking the value of <code>sys.float_info</code>. This will also tell you what's the largest and smallest number that can be represented with them.</p>\n",
    "\n",
    "<p>Once again, can test some examples with the <code>type()</code> function:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "float"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Print the type of 1.0\n",
    "\n",
    "type(1.0) # Notice that 1 is an int, and 1.0 is a float\n",
    "\n",
    "type(1)\n",
    "type(1.0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "float"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Print the type of 0.5\n",
    "\n",
    "type(0.5)\n",
    "\n",
    "type(0.5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "float"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Print the type of 0.56\n",
    "\n",
    "type(0.56)\n",
    "type(0.56)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "# System settings about float type\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3 id=\"convert\">Converting from one object type to a different object type</h3>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p>You can change the type of the object in Python; this is called typecasting. For example, you can convert an <i>integer</i> into a <i>float</i> (e.g. 2 to 2.0).</p>\n",
    "<p>Let's try it:</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "int"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Verify that this is an integer\n",
    "\n",
    "type(2)\n",
    "type(2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h4>Converting integers to floats</h4>\n",
    "<p>Let's cast integer 2 to float:</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2.0"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Convert 2 to a float\n",
    "\n",
    "float(2)\n",
    "float(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "float"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Convert integer 2 to a float and check its type\n",
    "\n",
    "type(float(2))\n",
    "\n",
    "type(float(2))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p>When we convert an integer into a float, we don't really change the value (i.e., the significand) of the number. However, if we cast a float into an integer, we could potentially lose some information. For example, if we cast the float 1.1 to integer we will get 1 and lose the decimal information (i.e., 0.1):</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Casting 1.1 to integer will result in loss of information\n",
    "\n",
    "int(1.1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h4>Converting from strings to integers or floats</h4>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p>Sometimes, we can have a string that contains a number within it. If this is the case, we can cast that string that represents a number into an integer using <code>int()</code>:</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Convert a string into an integer\n",
    "\n",
    "int('1')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p>But if you try to do so with a string that is not a perfect match for a number, you'll get an error. Try the following:</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Convert a string into an integer with error\n",
    "\n",
    "int('1 or 2 people')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p>You can also convert strings containing floating point numbers into <i>float</i> objects:</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Convert the string \"1.2\" into a float\n",
    "\n",
    "float('1.2')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<hr/>\n",
    "<div class=\"alert alert-success alertsuccess\" style=\"margin-top: 20px\">\n",
    "    [Tip:] Note that strings can be represented with single quotes (<code>'1.2'</code>) or double quotes (<code>\"1.2\"</code>), but you can't mix both (e.g., <code>\"1.2'</code>).\n",
    "</div>\n",
    "<hr/>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h4>Converting numbers to strings</h4>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p>If we can convert strings to numbers, it is only natural to assume that we can convert numbers to strings, right?</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'1'"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Convert an integer to a string\n",
    "\n",
    "str(1)\n",
    "\n",
    "str(1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p>And there is no reason why we shouldn't be able to make floats into strings as well:</p> "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'1.2'"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Convert a float to a string\n",
    "\n",
    "str(1.2)\n",
    "\n",
    "str(1.2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3 id=\"bool\">Boolean data type</h3>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p><i>Boolean</i> is another important type in Python. An object of type <i>Boolean</i> can take on one of two values: <code>True</code> or <code>False</code>:</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Value true\n",
    "\n",
    "True"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p>Notice that the value <code>True</code> has an uppercase \"T\". The same is true for <code>False</code> (i.e. you must use the uppercase \"F\").</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Value false\n",
    "\n",
    "False"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p>When you ask Python to display the type of a boolean object it will show <code>bool</code> which stands for <i>boolean</i>:</p> "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Type of True\n",
    "\n",
    "type(True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Type of False\n",
    "\n",
    "type(False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p>We can cast boolean objects to other data types. If we cast a boolean with a value of <code>True</code> to an integer or float we will get a one. If we cast a boolean with a value of <code>False</code> to an integer or float we will get a zero. Similarly, if we cast a 1 to a Boolean, you get a <code>True</code>. And if we cast a 0 to a Boolean we will get a <code>False</code>. Let's give it a try:</p> "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Convert True to int\n",
    "\n",
    "int(True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Convert 1 to boolean\n",
    "\n",
    "bool(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Convert 0 to boolean\n",
    "\n",
    "bool(0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.0"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Convert True to float\n",
    "\n",
    "float(True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3 id=\"exer_type\">Exercise: Types</h3>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p>What is the data type of the result of: <code>6 / 2</code>?</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3.0\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "float"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Write your code below. Don't forget to press Shift+Enter to execute the cell\n",
    "\n",
    "print(6/2)\n",
    "\n",
    "type(3.0)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Double-click __here__ for the solution.\n",
    "\n",
    "<!-- Your answer is below:\n",
    "type(6/2) # float\n",
    "-->"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p>What is the type of the result of: <code>6 // 2</code>? (Note the double slash <code>//</code>.)</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "int"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Write your code below. Don't forget to press Shift+Enter to execute the cell\n",
    "\n",
    "print(6//2)\n",
    "\n",
    "type(3)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Double-click __here__ for the solution.\n",
    "\n",
    "<!-- Your answer is below:\n",
    "type(6//2) # int, as the double slashes stand for integer division \n",
    "-->"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<hr>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h2 id=\"expressions\">Expression and Variables</h2>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3 id=\"exp\">Expressions</h3>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p>Expressions in Python can include operations among compatible types (e.g., integers and floats). For example, basic arithmetic operations like adding multiple numbers:</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Addition operation expression\n",
    "\n",
    "43 + 60 + 16 + 41"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p>We can perform subtraction operations using the minus operator. In this case the result is a negative number:</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Subtraction operation expression\n",
    "\n",
    "50 - 60"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p>We can do multiplication using an asterisk:</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Multiplication operation expression\n",
    "\n",
    "5 * 5"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p>We can also perform division with the forward slash:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Division operation expression\n",
    "\n",
    "25 / 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Division operation expression\n",
    "\n",
    "25 / 6"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p>As seen in the quiz above, we can use the double slash for integer division, where the result is rounded to the nearest integer:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Integer division operation expression\n",
    "\n",
    "25 // 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Integer division operation expression\n",
    "\n",
    "25 // 6"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3 id=\"exer_exp\">Exercise: Expression</h3>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p>Let's write an expression that calculates how many hours there are in 160 minutes:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "2.6666666666666665\n"
     ]
    }
   ],
   "source": [
    "# Write your code below. Don't forget to press Shift+Enter to execute the cell\n",
    "\n",
    "# number of hours in 160 minutes\n",
    "\n",
    "print(160//60)\n",
    "\n",
    "print(160/60)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Double-click __here__ for the solution.\n",
    "\n",
    "<!-- Your answer is below:\n",
    "160/60 \n",
    "# Or \n",
    "160//60\n",
    "-->"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p>Python follows well accepted mathematical conventions when evaluating mathematical expressions. In the following example, Python adds 30 to the result of the multiplication (i.e., 120)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Mathematical expression\n",
    "\n",
    "30 + 2 * 60"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p>And just like mathematics, expressions enclosed in parentheses have priority. So the following multiplies 32 by 60."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Mathematical expression\n",
    "\n",
    "(30 + 2) * 60"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3 id=\"var\">Variables</h3>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p>Just like with most programming languages, we can store values in <i>variables</i>, so we can use them later on. For example:</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Store value into variable\n",
    "\n",
    "x = 43 + 60 + 16 + 41"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p>To see the value of <code>x</code> in a Notebook, we can simply place it on the last line of a cell:</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Print out the value in variable\n",
    "\n",
    "x"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p>We can also perform operations on <code>x</code> and save the result to a new variable:</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use another variable to store the result of the operation between variable and value\n",
    "\n",
    "y = x / 60\n",
    "y"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p>If we save a value to an existing variable, the new value will overwrite the previous value:</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Overwrite variable with new value\n",
    "\n",
    "x = x / 60\n",
    "x"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p>It's a good practice to use meaningful variable names, so you and others can read the code and understand it more easily:</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Name the variables meaningfully\n",
    "\n",
    "total_min = 43 + 42 + 57 # Total length of albums in minutes\n",
    "total_min"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Name the variables meaningfully\n",
    "\n",
    "total_hours = total_min / 60 # Total length of albums in hours \n",
    "total_hours"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p>In the cells above we added the length of three albums in minutes and stored it in <code>total_min</code>. We then divided it by 60 to calculate total length <code>total_hours</code> in hours. You can also do it all at once in a single expression, as long as you use parenthesis to add the albums length before you divide, as shown below.</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Complicate expression\n",
    "\n",
    "total_hours = (43 + 42 + 57) / 60  # Total hours in a single expression\n",
    "total_hours"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p>If you'd rather have total hours as an integer, you can of course replace the floating point division with integer division (i.e., <code>//</code>).</p>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3 id=\"exer_exp_var\">Exercise: Expression and Variables in Python</h3>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p>What is the value of <code>x</code> where <code>x = 3 + 2 * 2</code></p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7\n"
     ]
    }
   ],
   "source": [
    "# Write your code below. Don't forget to press Shift+Enter to execute the cell\n",
    "x = 3+2*2\n",
    "print(x)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Double-click __here__ for the solution.\n",
    "\n",
    "<!-- Your answer is below:\n",
    "7\n",
    "-->\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p>What is the value of <code>y</code> where <code>y = (3 + 2) * 2</code>?</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n"
     ]
    }
   ],
   "source": [
    "# Write your code below. Don't forget to press Shift+Enter to execute the cell\n",
    "\n",
    "y=(3+2)*2\n",
    "print(y)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Double-click __here__ for the solution.\n",
    "\n",
    "<!-- Your answer is below:\n",
    "10\n",
    "-->"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<p>What is the value of <code>z</code> where <code>z = x + y</code>?</p>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "17\n"
     ]
    }
   ],
   "source": [
    "# Write your code below. Don't forget to press Shift+Enter to execute the cell\n",
    "z=x+y\n",
    "x=7\n",
    "y=10\n",
    "print(z)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Double-click __here__ for the solution.\n",
    "\n",
    "<!-- Your answer is below:\n",
    "17\n",
    "-->"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<hr>\n",
    "<h2>The last exercise!</h2>\n",
    "<p>Congratulations, you have completed your first lesson and hands-on lab in Python. However, there is one more thing you need to do. The Data Science community encourages sharing work. The best way to share and showcase your work is to share it on GitHub. By sharing your notebook on GitHub you are not only building your reputation with fellow data scientists, but you can also show it off when applying for a job. Even though this was your first piece of work, it is never too early to start building good habits. So, please read and follow <a href=\"https://cognitiveclass.ai/blog/data-scientists-stand-out-by-sharing-your-notebooks/\" target=\"_blank\">this article</a> to learn how to share your work.\n",
    "<hr>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<div class=\"alert alert-block alert-info\" style=\"margin-top: 20px\">\n",
    "<h2>Get IBM Watson Studio free of charge!</h2>\n",
    "    <p><a href=\"https://cocl.us/NotebooksPython101bottom\"><img src=\"https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Ad/BottomAd.png\" width=\"750\" align=\"center\"></a></p>\n",
    "</div>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3>About the Authors:</h3>  \n",
    "<p><a href=\"https://www.linkedin.com/in/joseph-s-50398b136/\" target=\"_blank\">Joseph Santarcangelo</a> is a Data Scientist at IBM, and holds a PhD in Electrical Engineering. His research focused on using Machine Learning, Signal Processing, and Computer Vision to determine how videos impact human cognition. Joseph has been working for IBM since he completed his PhD.</p>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Other contributors: <a href=\"www.linkedin.com/in/jiahui-mavis-zhou-a4537814a\">Mavis Zhou</a>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<hr>\n",
    "<p>Copyright &copy; 2018 IBM Developer Skills Network. This notebook and its source code are released under the terms of the <a href=\"https://cognitiveclass.ai/mit-license/\">MIT License</a>.</p>"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
