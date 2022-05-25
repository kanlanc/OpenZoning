# Open Zoning Feed Specification Project.

The purpose of this project is to develop a data standard for 
zoning codes so that zoning data can be easily digitized in a machine-
readable format to allow for multi-jurisdictional analysis and ingestion/integration
into third-party applications.

## Mission and vision

Open Zoning’s mission is _to empower the nation with the knowledge of zoning_.

towards the vision of

* a zoning system heavily influenced by and that works directly for the 
communities it most impacts;
* a new class of developers with diverse development value systems that enable
new, community-centered design potentials in the (re)filling of American urban 
areas; and
* integrated transportation and housing development at the city, state, and 
national scales

## Precedents and related work

[Sara Bronin](https://aap.cornell.edu/people/sara-bronin) is 
leading an effort to assemble a 
[national zoning atlas](https://www.zoningatlas.org/). The have completed 
a zoning atlas of [Connecticut](https://www.zoningatlas.org/connecticut) with 
an interactive website that allows users to filter zoning districts based on 
permitted residential uses, minimum lot sizes, and occupancy restrictions. The 
Connecticut atlas does not have data availble for download. Other projects 
affliated with the National Zoning Atlas are underway in California, Hawaii, New 
Hampshire, Montana, New York, and Ohio. Our goal is to create a tool that can 
easily convert the data the National Zoning Atlas is collecting to the data 
standard that we are developing. 

The Metropolitan Area Planning Council ([MAPC](https://www.mapc.org/))
has assembled an open-source [zoning atlas](https://zoningatlas.mapc.org/) 
for the Boston Metropolitan Area, inlcuding 101 municipalities. Their data is freely 
available for download as shapefiles including zoning attributes. We are using 
their data to test our initial hypotheses about the most flexible and efficient 
data formats and data governance models. Our initial visualization of MAPC 
zones is [here](https://urban-stack.github.io/OpenZoning/MAPC-files/MAPC-map_leaflet.html).

Mark Schwabacher of Georgia Tech's Center for Spatial Planning Analytics
and Visualizatoin ([CSPAV](https://cspav.gatech.edu/)) has created an interactive
zoning atlas for [Atlanta](https://sites.gatech.edu/atlzoningexplorer/atl-zoning-code-explorer/)
(one municipality). The tool allows users to interactively explore a 
map, search for locations where specific uses are permitted, and export data
on dimensional requirements for use-specified zones. It does not allow users to 
download geospatial data with zoning attributes attached.

## Potential research questions

1. *MBTA Communities:* In January 2021, the Massachusetts legislature passed an 
[economic development bill](https://malegislature.gov/Laws/SessionLaws/Acts/2020/Chapter358)
requiring [communities served by MBTA](https://www.mass.gov/info-details/multi-family-zoning-requirement-for-mbta-communities#what-is-an-%22mbta-community%22?-) to zone at least one district permitting
multifamily housing within one half-mile of a transit stop. The law specifies
the minimum number of multifamily units each community must allow, based on 
its type of MBTA service and its existing number of housing units. Our data 
allow us to analyse how much the changes resulting from this and similar laws 
could increase housing supply and regional spatial accessibility.

2. *Small-scale housing:* This dataset would allow for the development of an
interactive web-based application that would allow developers to identify 
parcels for small-scale housing developments (1-4 units).
