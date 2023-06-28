import json

# definitions

definitions = {
    "maximum": {
        "type": "number",
        "$comment": "exclusiveMinimum: 0"
    },
    "minimum": {
        "type": "number"
    },
}

# Define constraint definitions
# FIXME: Fix maximum and minimum references because in currently they are referencing non existing definitions
dynamicConstraintsDefinitions = {

    "maximum": {
        "type": "number",
        "$comment": "exclusiveMinimum: 0"
    },
    "minimum": {
        "type": "number"
    },
    "height": {
        "$comment": "Renamed this to height instead of heightValue",
        "type": "object",
        "properties": {
                "value": {
                    "type": "number"
                },
            "wall": {
                    "type": "object",
                    "properties": {
                        "maximum": {
                            "$ref": "#/definitions/maximum",
                            "$comment": "exclusiveMinimum: 0"
                        },
                        "minimum": {
                            "$ref": "#/definitions/minimum"
                        }
                    }
                },
            "roof": {
                    "type": "object",
                    "properties": {
                        "maximum": {
                            "$ref": "#/definitions/maximum",
                            "$comment": "exclusiveMinimum: 0"
                        },
                        "minimum": {
                            "$ref": "#/definitions/minimum"
                        }
                    }
                }
        }
    },
    "FAR": {
        "type": "object",
        "properties": {
                "residential": {
                    "type": "number"
                },
            "commercial": {
                    "type": "number"
            }
        }
    },
    "floorArea": {
        "type": "object",
        "properties": {
                "minimum": {
                    "$ref": "#/definitions/minimum"
                },
            "maximum": {
                    "$ref": "#/definitions/maximum"
            },
            "totalFloorArea": {
                    "type": "number"
            }
        }
    },
    "floorWidth": {
        "type": "object",
        "properties": {
                "minimum": {
                    "type": "object",
                    "properties": {
                        "value": {
                            "type": "number",
                            "$comment": "exclusiveMinimum: 0"
                        },
                        "applicableFloorArea": {
                            "type": "number",
                            "$comment": "exclusiveMinimum: 1, exclusiveMaximum: 1"
                        }
                    }
                }
        }
    },
    "lotArea": {
        "type": "object",
        "properties": {
                "minimum": {
                    "$ref": "#/definitions/minimum"
                },
            "maximum": {
                    "$ref": "#/definitions/maximum"
            }
        }
    },
    "lotWidth": {
        "type": "object",
        "properties": {
                "minimum": {
                    "$ref": "#/definitions/minimum"
                }
        }
    },
    "footprint": {
        "type": "object",
        "properties": {
                "maximum": {
                    "$ref": "#/definitions/maximum"
                }
        }
    },
    "stories": {
        "type": "object",
        "properties": {
                "maximum": {
                    "$ref": "#/definitions/maximum"
                }
        }
    },
    "storyFloors": {
        "type": "object",
        "properties": {
                "storyHeight": {
                    "type": "object",
                    "properties": {
                        "maximum": {
                            "$ref": "#/definitions/maximum"
                        }
                    }
                },
            "storyType": {
                    "type": "string"
            },
            "storiesContribution": {
                    "type": "number"
            },
            "floorAreaContribution": {
                    "type": "object",
                    "properties": {
                        "value": {
                            "type": "number"
                        },
                        "floorElev": {
                            "type": "object",
                            "properties": {
                                "minimum": {
                                    "$ref": "#/definitions/minimum"
                                },
                                "maximum": {
                                    "$ref": "#/definitions/maximum"
                                },
                                "floorPerimeter": {
                                    "type": "object",
                                    "properties": {
                                        "floorArea": {
                                            "type": "number"
                                        }
                                    }
                                }
                            }
                        }
                    }
            }
        }
    },
    "setbacks": {
        "type": "object",
        "properties": {
                "front": {
                    "type": "array",
                    "items": [
                        {
                            "type": "number"
                        },
                        {
                            "type": "array",
                            "items": [
                                {
                                    "type": "number"
                                },
                                {
                                    "type": "string"
                                }
                            ]
                        }
                    ]
                },
            "rear": {
                    "type": "array",
                    "items": [
                        {
                            "type": "number"
                        },
                        {
                            "type": "array",
                            "items": [
                                {
                                    "type": "number"
                                },
                                {
                                    "type": "string"
                                }
                            ]
                        }
                    ]
            },
            "sideInterior": {
                    "type": "object",
                    "properties": {
                        "interior": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "number"
                                },
                                {
                                    "type": "array",
                                    "items": [
                                        {
                                            "type": "number"
                                        },
                                        {
                                            "type": "string"
                                        }
                                    ]
                                }
                            ]
                        },
                        "corner": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "number"
                                },
                                {
                                    "type": "array",
                                    "items": [
                                        {
                                            "type": "number"
                                        },
                                        {
                                            "type": "string"
                                        }
                                    ]
                                }
                            ]
                        }
                    }
            },

            "fromAnotherStructure": {
                    "type": "object",
                    "properties": {
                        "primaryResidentialStructure": {
                            "type": "number"
                        },
                        "habitableDwelling": {
                            "type": "number"
                        }
                    }
            }
        }
    },
    "lotCoverage": {
        "type": "object",
        "properties": {
                "maximum": {
                    "$ref": "#/definitions/maximum"
                }
        }
    },
    "allowedUses": {
        "type": "object",
        "properties": {
                "permitted": {
                    "type": "array",
                    "items": {
                        "type": "string",
                        "enum": [
                            "single-family",
                            "two-family",
                            "three-family",
                            "multi-family"
                        ]
                    }
                },
            "conditional": {
                    "type": "array",
                    "items": {
                        "type": "string",
                        "enum": [
                            "single-family",
                            "two-family",
                            "three-family",
                            "multi-family"
                        ]
                    }
            },
            "accessoryStructuresPermissions": {
                    "type": "object",
                    "properties": {
                        "allowedNumADs": {
                            "type": "boolean"
                        },
                        "allowedTypesADs": {
                            "type": "boolean"
                        }
                    }
            }
        }
    }
}



# Define properties of the schema
# constraintsModule = {
#     "type": "array",
#     "items": {
#         "enum": [
#             "floor area",
#             "FAR",
#             "floor width",
#             "lot area",
#             "lot width",
#             "footprint",
#             "height",
#             "stories",
#             "story floors",
#             "lot coverage",
#             "allowed uses",
#             "district",
#             "setbacks"
#         ]
#     },
#     "minItems": 1
# }


bulkOptionality = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "bulks": {
                "type": "array",
                "items": {
                    "enum": [
                        "single-family",
                        "two-family",
                        "three-family",
                        "multi-family"
                    ]
                }
            },
            **dynamicConstraintsDefinitions
        }
    }
}

print(type(bulkOptionality))
print(bulkOptionality)

# ADbulks = {
#     "type": "array",
#     "items": {
#         "enum": ["ADU", "garage"]
#     }
# }

# ADtype = {
#     "type": "array",
#     "items": {
#         "enum": ["interior", "attached", "detached"]
#     }
# }

# ADtypeOptionality = {
#     "type": "array",
#     "items": {
#         "type": "object",
#         "properties": {
#             "ADtype": ADtype,
#             **dynamicConstraintsDefinitions
#         }
#     }
# }

# ADbulkOptionality = {
#     "type": "array",
#     "items": {
#         "type": "object",
#         "properties": {
#             "ADbulks": ADbulks,
#             **dynamicConstraintsDefinitions
#         }
#     }
# }

# accessoryStructures = {
#     "type": "object",
#     "properties": {
#         "ADbulkOptionality": ADbulkOptionality,
#         "ADtypeOptionality": ADtypeOptionality,
#         "bulkOptionality": bulkOptionality
#     }
# }

# primaryStructures = {
#     "type": "object",
#     "properties": {
#         "bulkOptionality": bulkOptionality
#     }
# }

# developmentOptionality = {
#     "type": "array",
#     "items": {
#         "type": "object",
#         "properties": {
#             "developmentType": {
#                 "enum": ["primary", "accessory"]
#             },
#             "primaryStructures": primaryStructures,
#             "accessoryStructures": accessoryStructures
#         }
#     }
# }

# districts = {
#     "type": "array",
#     "items": {
#         "$comment": "Replace with actual district values",
#         "enum": ["district1", "district2"]
#     }
# }

# districtTypeGroups = {
#     "type": "array",
#     "items": {
#         "type": "object",
#         "properties": {
#             "districts": districts,
#             **dynamicConstraintsDefinitions
#         }
#     }
# }

# lot = {
#     "type": "object",
#     "properties": {
#         "districtTypeGroups": districtTypeGroups,
#         "developmentOptionality": developmentOptionality
#     }
# }

# properties = {
#     "constraintsModule": constraintsModule,
#     "lot": lot
# }

# additional_properties = {
#     "$comment": "This seems to only validate one of the additionanl properties, not all of them, but would have to check again. Another recommneded method is to generate the schema dynamically with scripts",

# }

# # Combine components into final schema
# schema = {
#     "$schema": "http://json-schema.org/draft-07/schema#",
#     "type": "object",
    # "definitions": definitions,
#     "properties": properties,
#     "additionalProperties": additional_properties,
#     "required": ["constraintsModule"]
# }

# # Write schema to file
# with open('schema.json', 'w') as f:
#     json.dump(schema, f, indent=2)

print("Schema generated successfully!")
