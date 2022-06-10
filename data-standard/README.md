# OZFS Data Standard
_Will go here_
TODO: Link to definitions in the [Glossary](glossary.md) where possible. E.g. [Lot Area](glossary.md#lot-area)

Testing/working files to go in [Examples folder](/examples)


## Constraint Structure
Stored in hierarchy of:

- lot
  - structure
    - floor

Repeatable structures within above:
- bulk (option)
- base
  - height
  - setback
  - plane

  
## constraints & modifiers
#### Edges:
- front
- rear
- side

#### Dimensions:
in ft / sq ft
- width
- depth
- area
- frontage

#### Counts:
- min
- max
- numberOf
- per
  - Acre
  - DU (dwelling unit)
  - Lot


## special definitions

### roof
TBD

### max
when used as a _suffix_, defines or applies to the top-most floor, height, etc.

### corner

## other constraints
- FAR / Floor Area
- Parking
- Units
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