{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "data": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "abilities": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "description": {
                  "type": "string"
                },
                "displayIcon": {
                  "type": "string"
                },
                "displayName": {
                  "type": "string"
                },
                "slot": {
                  "type": "string"
                }
              },
              "required": [
                "description",
                "displayName",
                "slot"
              ]
            }
          },
          "assetPath": {
            "type": "string"
          },
          "background": {
            "type": "string"
          },
          "backgroundGradientColors": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "bustPortrait": {
            "type": "string"
          },
          "characterTags": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "description": {
            "type": "string"
          },
          "developerName": {
            "type": "string"
          },
          "displayIcon": {
            "type": "string"
          },
          "displayIconSmall": {
            "type": "string"
          },
          "displayName": {
            "type": "string"
          },
          "fullPortrait": {
            "type": "string"
          },
          "fullPortraitV2": {
            "type": "string"
          },
          "isAvailableForTest": {
            "type": "boolean"
          },
          "isBaseContent": {
            "type": "boolean"
          },
          "isFullPortraitRightFacing": {
            "type": "boolean"
          },
          "isPlayableCharacter": {
            "type": "boolean"
          },
          "killfeedPortrait": {
            "type": "string"
          },
          "role": {
            "type": "object",
            "properties": {
              "assetPath": {
                "type": "string"
              },
              "description": {
                "type": "string"
              },
              "displayIcon": {
                "type": "string"
              },
              "displayName": {
                "type": "string"
              },
              "uuid": {
                "type": "string"
              }
            },
            "required": [
              "assetPath",
              "description",
              "displayIcon",
              "displayName",
              "uuid"
            ]
          },
          "uuid": {
            "type": "string"
          },
          "voiceLine": {
            "type": "object",
            "properties": {
              "maxDuration": {
                "type": "number"
              },
              "mediaList": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "id": {
                      "type": "number"
                    },
                    "wave": {
                      "type": "string"
                    },
                    "wwise": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "id",
                    "wave",
                    "wwise"
                  ]
                }
              },
              "minDuration": {
                "type": "number"
              }
            },
            "required": [
              "maxDuration",
              "mediaList",
              "minDuration"
            ]
          }
        },
        "required": [
          "abilities",
          "assetPath",
          "backgroundGradientColors",
          "description",
          "developerName",
          "displayIcon",
          "displayIconSmall",
          "displayName",
          "isAvailableForTest",
          "isBaseContent",
          "isFullPortraitRightFacing",
          "isPlayableCharacter",
          "killfeedPortrait",
          "uuid",
          "voiceLine"
        ]
      }
    },
    "status": {
      "type": "number"
    }
  },
  "required": [
    "data",
    "status"
  ]
}