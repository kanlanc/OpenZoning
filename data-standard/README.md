# OZFS Data Standard
A portion of OZFS's work is establishing a minimum viable set of "core" constraints needed to bulk on any given lot across America. The work-in-progress list of these constraints are captured within this airtable titled [OZFS meta-data](https://airtable.com/invite/l?inviteId=invIE9Rq8BJxoRZe9&inviteToken=c24d20d82c00f933e02ca4d7f9b78088b2eaefcef049f3691df85eb48f858fbc&utm_medium=email&utm_source=product_team&utm_content=transactional-alerts). 

_Will go here_

Testing/working files to go in [Examples folder](/examples)


## Constraint Classifying Structure
Stored in a hierarchy of:

- [lot](glossary.md#lot)
  - [structure](glossary.md#structure)
    - [story](glossary.md#story) (i.e. floor)

Structures and their constraints are nested within the above hierarchy:
- [bulk](glossary.md#building-mass) (option) (i.e. mass)
- [base](glossary.md#base)
  - [height](glossary.md#building-height)
  - [setback](glossary.md#setback)
  - plane

  
## Constraints & Modifiers
#### Edges:
- [front](glossary.md#frontage) (lot line)
- [rear](glossary.md#lot-line-rear) (lot line)
- [side](glossary.md#lot-line-side) (lot line)

#### Dimensions:
in ft / sq ft
- [width](glossary.md#width)
- [depth](glossary.md#depth)
- area
- [frontage](glossary.md#frontage)

#### Counts:
- min
- max
- numberOf
- per
  - [Acre]
  - [DU (dwelling unit)](glossary.md#dwelling-unit)
  - Lot


## Special Definitions

### roof
TBD

### max
when used as a _suffix_, defines or applies to the top-most floor, height, etc.

### corner

## other constraints
- [FAR](glossary.md#FAR) / [Floor Area](glossary.md#floor-area)
- Parking
- [Units](glossary.md#units)
- Use types
  - Use groups
    - Uses

## variants
### bonuses


## Open questions:
- how to store ratios/formulas
  - purely numeric (e.g. `6:1` sky exposure plane)
  - relating to fixed figures (e.g. height can be 2X lot width)
  - relating to development decisions (e.g. tower can contain at most 45% of lot FAR)
