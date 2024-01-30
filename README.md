HTML to Markdown and Markdown to HTML Converter

This tool simplifies the conversion process between HTML and Markdown, allowing you to seamlessly switch between these two popular markup languages. Whether you need to translate HTML content to Markdown or vice versa, this tool provides an easy-to-use solution.


<Bold>1.To use this Markdown to HTML converter, follow these steps:</Bold><br>

  1.Create a New Folder:<br>
  <p> Create a new folder where you want to store your Markdown and HTML files.</p>

  2.Add Program to the Folder:<br>
  <p>  Copy the converter program (script.py or any other name) to the newly created folder.<br></p>

  3.Change Directory in Command Prompt:<br>
    <p>  Open the command prompt and navigate to the newly created folder using the cd command:<br><p>
    
             cd path\to\your\folder
  4.Check Directory Content:<br>
  Verify that the converter program is in the folder by listing the directory 
  content:
  
     dir
             
  5.Run the Program:<br>
  Execute the converter program with the desired operation, input file name 
  (without ".md"), and output file name (without ".html"):

        python script.py --operation m2h --input input --output output
Replace script.py with the actual name of your Python script, input with the Markdown file name, and output with the desired HTML output file name.

6.Check Output in the Same Folder:
<p>After running the program, you can check the converted HTML file in the same folder where the program is located.</p>

By following these steps, you can easily set up the converter in a specific folder, run it from the command prompt, and find the converted HTML file in the same directory.


2.MODULE USING IN PROGRAM: <br>
   1argsparse<br>
   2.markdown<br>
   3.markdownify<br>

3.REQUIRMENTS:<br>
   1.Installation of markdown <br>
   2.Installation of markdownify

4.CLI:

  This program runs in the command prompt, utilizing the pre-defined module argparse.

Overview of argparse:<br>

  1.Importing the module:

           #import argparse

  2.Creating a parser:

           parser = argparse.ArgumentParser(description="Description about the program")

  3.Defining the Argument:

  Adding the argument to the parser using add_argument

            parser.add_argument('--operation', help="operation")

  4.Parsing Argument:

  The parse_args() method is called to parse the command line:

            args = parser.parse_args()

  5.Accessing Argument Values:

  Accessing the argument through the attributes of the args:

                a = args.operation

This structured approach using argparse makes the command-line interface user-friendly and easy to understand. Users can specify the desired operation (--operation) to perform HTML to Markdown or Markdown to HTML conversion seamlessly. 


5.CONVERTING MARKDOWN TO HTML:

To convert Markdown to HTML, this tool utilizes the "markdown" module.We are going to use module to convert the markdown to html. Since the module is not pre-installed, you need to install it before using the converter. Follow the steps below to set up the environment.
 
ISTALLATION:

1.Open the command prompt:

2.Install the"markdown" module using the following command:
         
        pip install markdown


6.CONVERTING HTML TO MARKDOWN

To facilitate the conversion of HTML to Markdown, we'll be utilizing the "markdownify" module. Since this module isn't pre-installed, you'll need to set up your environment by installing it. Follow the steps below to ensure the proper configuration.

INSTALLATION:

  1.Open the command prompt

  2.Install the "markdownify" module using the following command:

        pip install markdownify


