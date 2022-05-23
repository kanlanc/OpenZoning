##################
# The purpose of this script is to generate a leaflet map from the 
# MAPC data where a user can highlight a zone and see some information
# about it.

library(tidyverse)
library(leaflet)
library(sf)
library(geoarrow)
library(here)
library(htmlwidgets)
library(rmapshaper)

base_districts <- here("MAPC-files",
                      "base-districts.parquet") %>%
  read_geoparquet_sf() %>%
  st_transform("WGS84") %>%
  st_zm() %>%
  mutate(long_name = paste(muni, zo_name)) %>%
  ms_simplify() %>%
  mutate(`Zone use type` = case_when(zo_usety == 0 ~ "Unzoned",
                                     zo_usety == 1 ~ "Residential",
                                     zo_usety == 2 ~ "Non-residential",
                                     zo_usety == 3 ~ "Mixed-use (residential and non-residential)",
                                     zo_usety == 4 ~ "Other (open space etc.)")) %>%
  mutate(`Zone use type` = factor(`Zone use type`, 
                                  levels = c("Unzoned",
                                             "Residential",
                                             "Non-residential",
                                             "Mixed-use (residential and non-residential)",
                                             "Other (open space etc.)")))

# Overlay district types: https://metropolitan-area-planning-counc.gitbook.io/zoning-atlas-appendix/data-sources/tabular-data
overlay_districts <- here("MAPC-files",
                          "overlay-districts.parquet") %>%
  read_geoparquet_sf() %>%
  mutate(`Overlay type` = case_when(Overlay_Ty == "FLEX" ~ "Flexible district",
                                    Overlay_Ty == "REST" ~ "Restrictive district",
                                    Overlay_Ty == "RESTR" ~ "Restrictive district",
                                    Overlay_Ty == "SD" ~ "Special district",
                                    Overlay_Ty == "SC" ~ "Special district")) %>%
  mutate(`Overlay type` = factor(`Overlay type`, 
                                  levels = c("Flexible district",
                                             "Restrictive district",
                                             "Special district"))) %>%
  st_transform("WGS84") %>%
  st_zm() 

base_pal = colorFactor(palette = c(unzoned = "#FFFFFF",
                                   all_res = "#FFFF33",
                                   non_res = "#E41A1C",
                                   mix_use = "#FF7F00",
                                   otherzo = "#4DAF4A"),
                       domain = base_districts$`Zone use type`,
                       ordered = TRUE)

overlay_pal = colorFactor(palette = c(flexi = "#377EB8",
                                      restr = "#984EA3",
                                      sp_di = "#F781BF"),
                       domain = overlay_districts$`Overlay type`,
                       ordered = TRUE)

leaflet_map <- leaflet(base_districts) %>%
  addProviderTiles(providers$CartoDB.Positron) %>%
  addPolygons(data = overlay_districts,
              color = ~overlay_pal(overlay_districts$`Overlay type`),
              weight = 0.25,
              opacity = 0.9,
              fillOpacity = 0.9,
              fillColor = ~overlay_pal(overlay_districts$`Overlay type`)) %>%
    addPolygons(color = "gray",
              weight = 0.25,
              opacity = 0.5,
              fillOpacity = 0.5,
              fillColor = ~base_pal(`Zone use type`),
              label = ~long_name,
              highlightOptions = highlightOptions(weight = 1.5,
                                                  color = "black",
                                                  opacity = 1,
                                                  fillOpacity = 0.15)) %>%

  addLegend(pal = base_pal, 
            values = ~`Zone use type`, 
            opacity = 0.5) %>%
  addLegend(pal = overlay_pal, 
            values = ~overlay_districts$`Overlay type`, 
            opacity = 0.9,
            title = "Overlay district") %>%
  addLegend(title = "Source:",
            colors = "white",
            labels = "https://zoningatlas.mapc.org/",
            opacity = 0,
            position = "bottomright")

saveWidget(leaflet_map, 
           here("MAPC-files",
                "MAPC-map_leaflet.html"))

