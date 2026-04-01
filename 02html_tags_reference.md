# HTML Tags Reference

A complete reference of all HTML tags with descriptions and examples.

---

## Document Structure

| Tag | Description | Example |
|-----|-------------|---------|
| `<!DOCTYPE>` | Defines the document type and HTML version | `<!DOCTYPE html>` |
| `<html>` | Root element of an HTML page | `<html lang="en">...</html>` |
| `<head>` | Contains meta-information about the document | `<head><title>Page</title></head>` |
| `<body>` | Contains the visible page content | `<body><p>Hello</p></body>` |
| `<title>` | Defines the document title (shown in browser tab) | `<title>My Website</title>` |

---

## Metadata

| Tag | Description | Example |
|-----|-------------|---------|
| `<meta>` | Defines metadata such as charset, viewport, description | `<meta charset="UTF-8">` |
| `<link>` | Links external resources like stylesheets | `<link rel="stylesheet" href="style.css">` |
| `<style>` | Embeds CSS styles directly in the document | `<style>body { color: red; }</style>` |
| `<base>` | Sets the base URL for all relative URLs in the page | `<base href="https://example.com/">` |

---

## Headings

| Tag | Description | Example |
|-----|-------------|---------|
| `<h1>` | Largest heading (most important) | `<h1>Main Title</h1>` |
| `<h2>` | Second-level heading | `<h2>Section Title</h2>` |
| `<h3>` | Third-level heading | `<h3>Subsection</h3>` |
| `<h4>` | Fourth-level heading | `<h4>Minor Heading</h4>` |
| `<h5>` | Fifth-level heading | `<h5>Small Heading</h5>` |
| `<h6>` | Smallest heading (least important) | `<h6>Tiny Heading</h6>` |

---

## Text Content

| Tag | Description | Example |
|-----|-------------|---------|
| `<p>` | Defines a paragraph | `<p>This is a paragraph.</p>` |
| `<br>` | Inserts a line break | `Line one<br>Line two` |
| `<hr>` | Inserts a horizontal rule (thematic break) | `<hr>` |
| `<pre>` | Displays preformatted text (preserves spaces and newlines) | `<pre>  Hello  World</pre>` |
| `<blockquote>` | Defines a long quotation from another source | `<blockquote cite="https://example.com">Quote text</blockquote>` |
| `<q>` | Defines a short inline quotation | `<q>To be or not to be</q>` |
| `<abbr>` | Defines an abbreviation or acronym | `<abbr title="HyperText Markup Language">HTML</abbr>` |
| `<address>` | Defines contact information for the author | `<address>123 Main St, City</address>` |
| `<cite>` | Defines the title of a creative work | `<cite>The Great Gatsby</cite>` |
| `<bdo>` | Overrides the text direction | `<bdo dir="rtl">Right to Left</bdo>` |
| `<bdi>` | Isolates a span of text with unknown directionality | `<bdi>مرحبا</bdi>` |
| `<wbr>` | Suggests a possible line-break opportunity | `superlongword<wbr>continues` |

---

## Inline Text Formatting

| Tag | Description | Example |
|-----|-------------|---------|
| `<b>` | Bold text (stylistic, no importance) | `<b>Bold Text</b>` |
| `<strong>` | Important bold text (semantic importance) | `<strong>Important!</strong>` |
| `<i>` | Italic text (stylistic, no emphasis) | `<i>Italic Text</i>` |
| `<em>` | Emphasized italic text (semantic emphasis) | `<em>Stressed word</em>` |
| `<mark>` | Highlighted/marked text | `<mark>Highlighted</mark>` |
| `<small>` | Smaller text (fine print, side comments) | `<small>Fine print</small>` |
| `<del>` | Deleted/strikethrough text | `<del>Old price</del>` |
| `<ins>` | Inserted/underlined text | `<ins>New content</ins>` |
| `<sub>` | Subscript text | `H<sub>2</sub>O` |
| `<sup>` | Superscript text | `E=mc<sup>2</sup>` |
| `<u>` | Underlined text | `<u>Underlined</u>` |
| `<s>` | Strikethrough text (no longer accurate) | `<s>Old info</s>` |
| `<code>` | Inline code snippet | `<code>console.log()</code>` |
| `<kbd>` | Keyboard input text | `Press <kbd>Ctrl+C</kbd>` |
| `<samp>` | Sample output from a program | `<samp>Error 404</samp>` |
| `<var>` | Represents a variable in math/programming | `<var>x</var> = 5` |
| `<time>` | Defines a date/time | `<time datetime="2024-01-01">New Year</time>` |
| `<span>` | Generic inline container for styling | `<span class="red">Text</span>` |

---

## Links & Media

| Tag | Description | Example |
|-----|-------------|---------|
| `<a>` | Defines a hyperlink | `<a href="https://example.com">Click here</a>` |
| `<img>` | Embeds an image | `<img src="photo.jpg" alt="A photo">` |
| `<picture>` | Container for multiple image sources | `<picture><source srcset="img.webp"><img src="img.jpg"></picture>` |
| `<source>` | Defines multiple media resources for `<picture>`, `<audio>`, `<video>` | `<source src="video.mp4" type="video/mp4">` |
| `<audio>` | Embeds audio content | `<audio controls><source src="song.mp3"></audio>` |
| `<video>` | Embeds video content | `<video controls width="400"><source src="movie.mp4"></video>` |
| `<track>` | Adds text tracks (subtitles) for `<video>` and `<audio>` | `<track kind="subtitles" src="subs.vtt" srclang="en">` |
| `<iframe>` | Embeds another HTML page within the current page | `<iframe src="https://example.com" width="600"></iframe>` |
| `<embed>` | Embeds external content (plugin) | `<embed src="file.pdf" type="application/pdf">` |
| `<object>` | Embeds an external object (Flash, PDF, etc.) | `<object data="file.pdf" type="application/pdf"></object>` |
| `<map>` | Defines an image map | `<map name="mymap">...</map>` |
| `<area>` | Defines a clickable area inside an image map | `<area shape="rect" coords="0,0,100,100" href="page.html">` |
| `<figcaption>` | Caption for a `<figure>` element | `<figcaption>Figure 1: Chart</figcaption>` |
| `<figure>` | Self-contained content like images or diagrams | `<figure><img src="img.jpg"><figcaption>Caption</figcaption></figure>` |

---

## Lists

| Tag | Description | Example |
|-----|-------------|---------|
| `<ul>` | Unordered (bulleted) list | `<ul><li>Item</li></ul>` |
| `<ol>` | Ordered (numbered) list | `<ol><li>Step 1</li></ol>` |
| `<li>` | List item (used inside `<ul>` or `<ol>`) | `<li>List item</li>` |
| `<dl>` | Description list | `<dl><dt>HTML</dt><dd>A markup language</dd></dl>` |
| `<dt>` | Term in a description list | `<dt>CSS</dt>` |
| `<dd>` | Description of a term in a description list | `<dd>Cascading Style Sheets</dd>` |

---

## Tables

| Tag | Description | Example |
|-----|-------------|---------|
| `<table>` | Defines an HTML table | `<table>...</table>` |
| `<thead>` | Groups the header rows of a table | `<thead><tr><th>Name</th></tr></thead>` |
| `<tbody>` | Groups the body rows of a table | `<tbody><tr><td>John</td></tr></tbody>` |
| `<tfoot>` | Groups the footer rows of a table | `<tfoot><tr><td>Total</td></tr></tfoot>` |
| `<tr>` | Defines a table row | `<tr><td>Cell</td></tr>` |
| `<th>` | Defines a header cell in a table | `<th>Column Name</th>` |
| `<td>` | Defines a data cell in a table | `<td>Data</td>` |
| `<caption>` | Defines a table caption | `<caption>Monthly Sales</caption>` |
| `<col>` | Specifies column properties for a `<colgroup>` | `<col style="width:50%">` |
| `<colgroup>` | Groups columns for formatting | `<colgroup><col><col></colgroup>` |

---

## Forms & Input

| Tag | Description | Example |
|-----|-------------|---------|
| `<form>` | Defines an HTML form | `<form action="/submit" method="post">...</form>` |
| `<input>` | Defines an input control | `<input type="text" name="username">` |
| `<textarea>` | Multi-line text input | `<textarea rows="4">Write here...</textarea>` |
| `<button>` | Defines a clickable button | `<button type="submit">Submit</button>` |
| `<select>` | Defines a drop-down list | `<select><option>Option 1</option></select>` |
| `<option>` | Defines an option in a drop-down list | `<option value="1">One</option>` |
| `<optgroup>` | Groups related options in a drop-down | `<optgroup label="Colors"><option>Red</option></optgroup>` |
| `<label>` | Defines a label for an input element | `<label for="email">Email:</label>` |
| `<fieldset>` | Groups related elements in a form | `<fieldset><legend>Personal Info</legend>...</fieldset>` |
| `<legend>` | Caption for a `<fieldset>` | `<legend>Contact Details</legend>` |
| `<datalist>` | Provides autocomplete suggestions for an `<input>` | `<datalist id="colors"><option value="Red"></datalist>` |
| `<output>` | Displays the result of a calculation | `<output name="result">42</output>` |
| `<progress>` | Displays a progress bar | `<progress value="70" max="100">70%</progress>` |
| `<meter>` | Displays a scalar measurement within a known range | `<meter value="0.6">60%</meter>` |

---

## Semantic / Structural Layout

| Tag | Description | Example |
|-----|-------------|---------|
| `<header>` | Defines the header of a page or section | `<header><h1>Site Title</h1></header>` |
| `<footer>` | Defines the footer of a page or section | `<footer><p>© 2024</p></footer>` |
| `<main>` | Specifies the main content of a document | `<main><article>...</article></main>` |
| `<nav>` | Defines a navigation section | `<nav><a href="/">Home</a></nav>` |
| `<section>` | Defines a standalone section of content | `<section><h2>About</h2><p>...</p></section>` |
| `<article>` | Defines self-contained content (blog post, news item) | `<article><h2>Post Title</h2><p>...</p></article>` |
| `<aside>` | Defines content aside from main content (sidebar) | `<aside><p>Related links</p></aside>` |
| `<details>` | Creates a collapsible disclosure widget | `<details><summary>More info</summary><p>Hidden content</p></details>` |
| `<summary>` | Visible heading for a `<details>` element | `<summary>Click to expand</summary>` |
| `<dialog>` | Defines a dialog box or modal window | `<dialog open><p>Hello!</p></dialog>` |
| `<div>` | Generic block-level container for layout/grouping | `<div class="container">...</div>` |

---

## Scripting

| Tag | Description | Example |
|-----|-------------|---------|
| `<script>` | Embeds or links JavaScript code | `<script src="app.js"></script>` |
| `<noscript>` | Fallback content when JavaScript is disabled | `<noscript>Please enable JavaScript.</noscript>` |
| `<template>` | Holds client-side template content not rendered on load | `<template id="tmpl"><p>Template</p></template>` |
| `<slot>` | Placeholder inside a web component | `<slot name="content"></slot>` |
| `<canvas>` | Used for drawing graphics via JavaScript | `<canvas id="myCanvas" width="200" height="100"></canvas>` |

---

## Ruby / Annotations

| Tag | Description | Example |
|-----|-------------|---------|
| `<ruby>` | Defines a ruby annotation (East Asian typography) | `<ruby>漢<rt>Kan</rt></ruby>` |
| `<rt>` | Defines the pronunciation for ruby annotation | `<rt>Kan</rt>` |
| `<rp>` | Defines parentheses for browsers without ruby support | `<ruby>漢<rp>(</rp><rt>Kan</rt><rp>)</rp></ruby>` |

---

## Deprecated / Obsolete Tags *(avoid using)*

| Tag | Description | Modern Alternative |
|-----|-------------|-------------------|
| `<center>` | Centers content | Use CSS `text-align: center` |
| `<font>` | Sets font size, face, and color | Use CSS `font-family`, `color` |
| `<big>` | Makes text larger | Use CSS `font-size` |
| `<strike>` | Strikethrough text | Use `<s>` or `<del>` |
| `<tt>` | Teletype (monospace) text | Use `<code>` or CSS |
| `<frame>` | Defines a window in a frameset | Use `<iframe>` |
| `<frameset>` | Defines a set of frames | Use CSS layouts |
| `<noframes>` | Fallback for browsers without frame support | — |
| `<applet>` | Embeds a Java applet | Use `<object>` or JS |
| `<acronym>` | Defines an acronym | Use `<abbr>` |
| `<dir>` | Defines a directory list | Use `<ul>` |

---

*Total: 110+ HTML tags covered. Last updated: 2024.*
