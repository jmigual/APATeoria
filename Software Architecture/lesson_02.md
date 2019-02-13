# Lesson 2

## Stakeholders
### The Architect in Scrum

 - The architect role is to avoid technical debt.
 - However there is an important management part.

### The Architect on GitHub
 - Analyse how people work on GitHub
 - Integrator: Makes the decision in what to merge

## Views
### Kruchten's "4+1 Views"

 - Logical View
 - Implementation View
 - Process View
 - Deployment View
 + Context View

### Viewpoints
Chapter 3

A collection of patterns, templates and conventions for constructing one type of view. 7 viewpoints are recognised in the book.

There are alternative catalogs for viewpoints.

## Context View

Describes the relationships, dependencies, and interactions between the system and its environment. 

You can make pictures out of this. It was done in the previous years.

> "Always design a thing by considering it in its next larger context".

### Concerns
 - System scope and responsibilities
 - External entities, services, data
    - Their nature and characteristics
    - Their identity and responsibilities
 - Impact of system on its development
    - Completeness, coherence and consistency of overall end-to-end solution.

### Models
 - UML / "boxes and arrows"
    - System itself is "black box" in context
 - Interaction scenarios (chapter 10)

## Development view
Describes the architecture that supports

Show the bigger modules and how they are connected with other bigger packages. Show how the layers call each other and interact.

> "Things to think about include... system wide design constraints and 
> system-wide integrity"
