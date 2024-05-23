#0x01. AirBnB clone - Web static

* During this project, you will learn how to manipulate HTML and CSS languages. HTML is the structure of your page, it should be the first thing to write. CSS is the styling of your page, the design. I really encourage you to fix your HTML part before starting the styling. Indeed, without any structure, you can’t apply any design.

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of google

General
What is HTML?

HTML (HyperText Markup Language) is the standard language for creating web pages and web applications. It describes the structure of a webpage using a series of elements and tags.
How to create an HTML page:

To create an HTML page, you need to write HTML code within a .html file. Here is a basic example:

html
Copy code
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My First HTML Page</title>
</head>
<body>
    <h1>Hello, World!</h1>
</body>
</html>
What is a markup language?

A markup language is a system for annotating a document in a way that is syntactically distinguishable from the text. In web development, HTML is a markup language used to structure content on the web.
What is the DOM?

The DOM (Document Object Model) is a programming interface for web documents. It represents the structure of a document as a tree of nodes, where each node is an object representing a part of the document.
What is an element / tag?

An element is a fundamental building block of HTML, defined by a start tag, content, and an end tag. For example, <p>This is a paragraph.</p>. Tags are the parts of the element, with the start tag being <p> and the end tag being </p>.
What is an attribute?

An attribute provides additional information about an element and is included within the start tag. For example, <a href="https://www.example.com">Visit Example</a> has an href attribute specifying the URL of the link.
How does the browser load a webpage?

The browser loads a webpage by:
Sending a request to the web server for the HTML document.
Parsing the HTML document and loading linked resources (CSS, JavaScript, images).
Constructing the DOM and CSSOM (CSS Object Model).
Combining the DOM and CSSOM into a render tree.
Painting the render tree onto the screen.
What is CSS?

CSS (Cascading Style Sheets) is a style sheet language used to describe the presentation of a document written in HTML or XML. It controls the layout, colors, fonts, and overall look of a webpage.
How to add style to an element:

You can add style to an element using inline styles, internal stylesheets, or external stylesheets. Here are examples for each method:

Inline Styles:

html
Copy code
<p style="color: blue;">This is a blue paragraph.</p>
Internal Stylesheet:

html
Copy code
<head>
    <style>
        p {
            color: blue;
        }
    </style>
</head>
<body>
    <p>This is a blue paragraph.</p>
</body>
External Stylesheet:

html
Copy code
<head>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <p>This is a blue paragraph.</p>
</body>
In styles.css:

css
Copy code
p {
    color: blue;
}
What is a class?

A class is an attribute that you can add to an HTML element to apply specific styles to that element or to group elements for styling. For example:

html
Copy code
<p class="highlight">This is a highlighted paragraph.</p>
In CSS:

css
Copy code
.highlight {
    background-color: yellow;
}
What is a selector?

A selector is a pattern used in CSS to select the elements you want to style. Examples include element selectors (p), class selectors (.class-name), and ID selectors (#id-name).
How to compute CSS Specificity Value:

CSS specificity determines which styles are applied to an element when there are multiple conflicting rules. It is calculated based on the types of selectors used:

Inline styles: 1000
ID selectors: 100
Class selectors, attributes, and pseudo-classes: 10
Element selectors and pseudo-elements: 1
The specificity value is computed by adding the values for each type of selector in a rule. For example, #id .class element has a specificity of 111.

What are Box properties in CSS:

Box properties in CSS refer to the properties that control the layout and dimensions of elements. They include:

width and height: Control the dimensions of the content area.
padding: Space inside the element, between the content and the border.
border: The edge around the element.
margin: Space outside the element, between the border and other elements.
These properties follow the Box Model, which represents the structure of a web page element.
