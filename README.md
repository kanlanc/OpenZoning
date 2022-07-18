# Open Zoning Feed Specification Project.

The purpose of this project is to make public zoning data universally accessible. We're doing this by applying the model of a revolutionary national precedent in the transit space, the General Transit Feed Specification (GTFS), to the zoning space. We're developing the _Open Zoning Feed Specification_, a web-based data standard for zoning code that simplifies and streamlines access to **zoning data** so that everyone from _non-experts_ to _"machines"_ can know & understand **what can be built**. 

If you use an app like Google maps to get around the city on public transit, than the GTSF fuels your adventure. We're working everyday at OZFS to fuel your dream of owning a home in the ciy, of your small business developing the housing that communities are demanding, and your community's fight for the quality of life and equitable housing that your city promised . Every day we work, we get closer and closer to achieving this goal. 

### The Problem (\#Rant)
Zoning as it currently exists in the U.S. is _ridiculous_...
Basic questions are impossible to answer accurately without detailed legal analyses. Such as: What can a site be used for? What can be built on a site? Are existing structures code compliant? and; What are the impacts on housing outcomes of existing and proposed changes to zoning?

### Contents
1. [Product Criteria](#product-criteria)
2. [Anticipated OZFS Components](#anticipated-ozfs-components)
3. [The Future with OZFS](#the-future-with-ozfs)
4. [Precedents and related work](#precedents-and-related-work)
5. [Potential research questions](#potential-research-questions)

## Product Criteria
The OZFS Project is a Harvard lab-housed project with the soul (and experience) of a product startup. Our product criterion are:
- The existence of a single source of machine-readable, accurate, and openly-available zoning data
- The ability to store all zoning regulations as written, without interpretation (i.e. don't store an FAR value if there isn't one in the code)
- A data architecture flexible enough to accommodate most types of zoning regulations & regimes
- Versioning systems for both the data standard and zoning codes that allow for iteration, improvement, maintenance
- Planning and issue tracking systems for short- through long-term planning
- Governance and practices that ensure continued access and relevance, so that OZFS avoids becoming orphaned or stale

## Anticipated OZFS Components
<details>
<summary>What is a feed specification?</summary>
<br>
A _feed specification_ is a pre-defined set of files for digitally storing information on a particular instance of a topic. For OZFS, our topic is zoning codes and and our instances are individual municipalities' zoning codes. Each file within our feed specification defines the required data structure for recording the information for a specifice piece of a municipality's zoning code. The particular data structure within each of these files an example of a schema, creating what we call schema files. When packaged together, these schema files form the complete set of instructions for how to capture an entire municipality's zoning code according to the specific standared data structure that we are intentionally and methodically designing. The culmination of our work for a given municipality will be a packaged set of instructions for that municipality, the municipality's feed specification.
</details>

<details>
<summary>OZFS meta-schema and schema files</summary>
<br>
Underpinning our schema files is a standard data structure known as the Open Zoning meta-schema. We're currently crafting our meta-schema off of the great work that has been done at Mobility Data, embodied in their Mobility Data Standard (MDS) meta-schema (http://json-schema.org/draft-06/schema#). 

Our schema files fall into one of two catagories: 1) for capturing the zoning regulations of a municipality's zoning code, and: 2) for capturing the geospatial information for a municipality's districts and proximity zones. A critical challenge of this project and its research contribution in this field is our work designing the standard data structures for schemas of both file catagories that enable us to meet the criteria we've outlined in the "Product Criteria" section above. 
</details>


***v0.1***
### [Geospatial structure](/geo-standard) overview
Expectation is for multiple GIS layers to be uploaded (e.g. base + overlay districts)
Those will be merged into a single zoning layer that _atomizes_ each polygon into a single zoning district (or combination of districts)
All data stored within `GeoJSON` or other open/accessible GIS formats. 

### (Zoning) [Data structure](/data-standard) overview & rules engine
A non-tabular data structure enabling flexible definition & storage of zoning regulations.
Access to zoning maps via a lookup key(s) for each district within a municipality (e.g. `MA-Suff-BOS-SPA-ZR4B` (not an actual district!))
All data stored in within json files. 

### [Translation service](/code/translation-scripts)
1. Script(s) for converting zoning data from other zoning data standards (see [below](#regionalstate-wide-zoning-atlases)) into our schema files
2. Script(s) to perform zoning analysis research (e.g. How many (additional) triplexes are possible within a mile of downtown Minneapolis?)

### UI/UX
1. An elegant, intuitive, and interactive UI for entering and defining zoning constraints.
2. An easy-to-understand graphical summary of zoning regulations for a given lot. 
(v0.1 to include [mockup](/images/ui-ux-mockups) _only_)

### _Future_ Functionality Components of OZFS

#### Automated Zoning Code creation
Perhaps based on [PlaceCode](https://www.principle.us/placecode)

#### Existing built environment dataset(s)
A new dataset or connections to existing sources (e.g. OSM, [Regrid](https://regrid.com/buildings)) for use cases including:
- zoning additions and modifications to current structures on a parcel
- zoning regulations based on relations to adjacent lots/buildings


#### _Interpreted_ Zoning Rules
Data storage mechanism able to capture data points not directly from the zoning code. E.g.:
- Realizable units based on lot characteristics
- FAR/floor area based on other regulations
- Parking requirements with max build out

## The Future with OZFS
We hypothesize that wide-scale adoption of the OZFS will lead to radical new possibilities for land use policy and the built environment:
- Enabling wide-scale upzoning of all types
- Automating ADU siting & approval
- Supporting affordable housing development
- Facilitating improved community engagement/scenario planning
- Lowering development costs overall
- Empowering small developers/individual property owners
- Lining up policy goals with actual zoning regulations
- Enabling ecosystems of software & services engaging with the _potential_ built environment

### Potential future personas
The following are visions/case studies of the future that imagine & inform the goals & possibilities for OZFS
1. Affordable housing developer targeting sites for their existing model of 5-story buildings in the Boston region
2. Community meeting with real-time scenario planning that generates zoning text on-the-fly
3. Modular ADU fabricator targeting properties for its new 2-story ADU
4. City planner testing multiple scenarios to accomplish the mayor's new policy goal of 10% more units over the next decade
5. Multinational company deciding where to locate their new assembly facility based on _potential_ workforce housing capacity in the region
6. AR software developer looking to develop ...?
7. Institutional real estate developer/holder selecting properties for its new East Coast "Missing Middle" REIT

## Precedents and related work
### Regional/State-wide Zoning Atlases
[Sara Bronin](https://aap.cornell.edu/people/sara-bronin) is leading an effort to assemble a
[national zoning atlas](https://www.zoningatlas.org/). They have completed
a zoning atlas of [Connecticut](https://www.zoningatlas.org/connecticut)
(including 178 municipalities) with an interactive website that allows users
to filter zoning districts based on permitted residential uses, minimum lot
sizes, and occupancy restrictions. The Connecticut atlas does not have data
available for download. Other projects affiliated with the National Zoning Atlas
are underway in California, Hawaii, New Hampshire, Montana, New York, and Ohio.

The Metropolitan Area Planning Council ([MAPC](https://www.mapc.org/))
has assembled an open-source [zoning atlas](https://zoningatlas.mapc.org/)
for the Boston Metropolitan Area, including 101 municipalities. Their data is freely
available for download as shapefiles including zoning attributes. We are using
their data to test our initial hypotheses about the most flexible and efficient
data formats and data governance models. Our initial visualization of MAPC
zones is [here](https://urban-stack.github.io/OpenZoning/MAPC-files/MAPC-map_leaflet.html).

### Individual City Interactive Zoning Maps
- [New York City](https://zola.planning.nyc.gov/)
- [Chicago](https://secondcityzoning.org/) from https://derekeder.com/
- [Atlanta](https://sites.gatech.edu/atlzoningexplorer/atl-zoning-code-explorer/) from Mark Schwabacher of Georgia Tech's Center for Spatial Planning Analytics and Visualization ([CSPAV](https://cspav.gatech.edu/)). The tool allows users to interactively explore a map, search for locations where specific uses are permitted, and export data on dimensional requirements for use-specified zones. It does not allow users to download geospatial data with zoning attributes attached.

### Data Standard Precedents
- [GTFS](https://gtfs.org/) - created by Google (with/for TriMet) to enable transit trip planning. Now owned/managed by [MobilityData](https://mobilitydata.org/)
- [GBFS](https://gbfs.mobilitydata.org/)
- [MDS](https://www.openmobilityfoundation.org/about-mds/) - created by Ellis Associates for LA DOT. OMF was created to manage it
- [CDS](https://www.openmobilityfoundation.org/about-cds/) - Curb data specification - created by OMF working group (OMF's first non-MDS effort)
- [OpenLR](http://www.openlr.org/) - common standard for positioning along curb (from TomTom?)

### UI/UX Precedents
- [StreetMix](https://streetmix.net/)
- [JOSM](https://josm.openstreetmap.de/)

## Potential research questions

1. *MBTA Communities:* In January 2021, the Massachusetts legislature passed an
[economic development bill](https://malegislature.gov/Laws/SessionLaws/Acts/2020/Chapter358)
requiring [communities served by MBTA](https://www.mass.gov/info-details/multi-family-zoning-requirement-for-mbta-communities#what-is-an-%22mbta-community%22?-) to zone at least one district permitting
multifamily housing within one half-mile of a transit stop. The law specifies
the minimum number of multifamily units each community must allow, based on
its type of MBTA service and its existing number of housing units. Our data
allow us to analyze how much the changes resulting from this and similar laws
could increase housing supply and regional spatial accessibility.

2. *Small-scale housing:* This dataset would allow for the development of an
interactive web-based application that would allow developers to identify
parcels for small-scale housing developments (1-4 units).
