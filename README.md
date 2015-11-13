# chemistry-css
A chemistry CSS library for creating Chemical Structures and Equations with just HTML.  Similar project to: https://github.com/mathexl/math-css

![Render Example](/example/render2.png)

Chemistry CSS is a library that lets you currently construct chemical diagrams with easy HTML.    Support soon to be added for: 

* Equations, including multi-line equations
* 3D bond structure 

###A quick table of contents:

1) Setting Up <br>
2) Adding Elements <br>
3) Adding Bonds<br>
4) Types of Bonds<br>

##Setting Up
To use the board, first declare you are creating an equation by using the ```chembox``` attribute. 

```HTML
<div chembox>

</div>

```

##Adding Elements
Within the Chembox, declare elements using the ```chempart``` attribute.  You also need to add a location attribute, modeled by the format ```boxX_Y```.  For instance, the horizantal component 3 and vertical component 2 would be ```box3_2```.  The current grid works up to 10 on the X and 20 on the Y.  **You can modify the size of the grid by rerendering extra boxes using the Python script (```Python3 rerenderer/render.py```) in rerenderer/render.py and linking the created ```rerenderer/box.css``` file.**  Further, chembox utilizes the ```zoom``` attribute making resizing easy.  Since the boxes are absolute, you can resize the chembox div without interfering with the actual components within. 

Within the div, include the letter name of the element in the grid.  Format explained below: 


```HTML
<div chembox>
        <div chempart box2_2>O</div>
</div>

```

##Adding Bonds
Part of the goal of Chemistry-CSS was to keep the HTML minimal and readable.  Therefore, it uses the ```<hr>``` tag as a way of delineating bonds to other elements.  You can only declare bonds pointing right; this is to keep the code clean (therefore, all bonds have to be declared from their left element).  
The first ```<hr>``` tag is the top-right hand corner bond.  The second is the right bond, then the right-bottom bond, and then the bottom bond.  Commented HTML below of a carbon with two bonds facing right: 

```HTML
<div chempart box4_2>C</div>
    <hr singlebond> <!-- Top Right Bond -->
    <hr> <!-- null bond-->
    <hr> <!-- null bond-->
    <hr singlebond> <!-- Bottom Bond-->
```

The order of the ```<hr>``` tags matter.  This also makes editing structures easy since all the ```<hr>``` tags are already declared, even if null. If you, however, only declare, for instance, a top right bond, you can skip the next tags.  For the sake of a more complete example, the following code: 

```HTML
<div chembox>
    <div chempart box2_2>O</div>
        <hr singlebond>
        <hr>
        <hr>
        <hr partialdoublebond>
    <div chempart box3_1>C</div>
        <hr>
        <hr>
        <hr doublebond>
    <div chempart box4_2>C</div>
        <hr singlebond>
        <hr>
        <hr>
        <hr singlebond>
    <div chempart box4_3>C</div>
    <div chempart box3_4>C</div>
        <hr triplebond>
    <div chempart box2_3>N</div>
        <hr>
        <hr>
        <hr singlebond>
</div>
```
Will render the following image: 
![Render Example](/example/render.png)

##Types of Bonds
There are a few common bond attributes you can add.  They are listed below . <br>
```singlebond```, ```doublebond```, ```triplebond```, ```partialdoublebond```, 
```partialsinglebond```, ```partialtriplebond```.
