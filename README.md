# Pattern Design: Object-oriented Design

### Section 1: The Purpose of the Repository

This repo talks about all the 23 design patterns and analyzes the advantages and disadvantages of them.

### Section 2: Creational Design Patterns

#### Abstract Factory Pattern

Scenario --->
Imagine that diverse products are manufactured. Each product has the same different product styles, and each manufacturing style for a product represents a variant of this product.

Problem --->
If a developer created each class for a product with a certain manufacturing style, many individual classes have to be created although some functionalities are the same, so it creates over-coding.

Solution --->
Individual interfaces (classes) shall be initialized for the distinct product family, and then each variant for each interface shall be created following these interfaces.

> Definition: a design pattern that produces families of related objects without specifying concrete classes.
