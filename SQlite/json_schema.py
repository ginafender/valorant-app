{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "matches": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "matchInfo": {
            "type": "object",
            "properties": {
              "customGameName": {
                "type": "string"
              },
              "gameLengthMillis": {
                "type": "number"
              },
              "gameMode": {
                "type": "string"
              },
              "gameStartMillis": {
                "type": "number"
              },
              "isCompleted": {
                "type": "boolean"
              },
              "isRanked": {
                "type": "boolean"
              },
              "mapId": {
                "type": "string"
              },
              "matchId": {
                "type": "string"
              },
              "provisioningFlowId": {
                "type": "string"
              },
              "queueId": {
                "type": "string"
              },
              "seasonId": {
                "type": "string"
              }
            },
            "required": [
              "customGameName",
              "gameLengthMillis",
              "gameMode",
              "gameStartMillis",
              "isCompleted",
              "isRanked",
              "mapId",
              "matchId",
              "provisioningFlowId",
              "queueId",
              "seasonId"
            ]
          },
          "players": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "characterId": {
                  "type": "string"
                },
                "competitiveTier": {
                  "type": "string"
                },
                "partyId": {
                  "type": "string"
                },
                "playerCard": {
                  "type": "string"
                },
                "playerTitle": {
                  "type": "string"
                },
                "puuid": {
                  "type": "string"
                },
                "stats": {
                  "type": "object",
                  "properties": {
                    "abilityCasts": {
                      "type": "object",
                      "properties": {
                        "ability1Casts": {
                          "type": "number"
                        },
                        "ability2Casts": {
                          "type": "number"
                        },
                        "grenadeCasts": {
                          "type": "number"
                        },
                        "ultimateCasts": {
                          "type": "number"
                        }
                      },
                      "required": [
                        "ability1Casts",
                        "ability2Casts",
                        "grenadeCasts",
                        "ultimateCasts"
                      ]
                    },
                    "assists": {
                      "type": "number"
                    },
                    "deaths": {
                      "type": "number"
                    },
                    "kills": {
                      "type": "number"
                    },
                    "playtimeMillis": {
                      "type": "number"
                    },
                    "roundsPlayed": {
                      "type": "number"
                    },
                    "score": {
                      "type": "number"
                    }
                  },
                  "required": [
                    "assists",
                    "deaths",
                    "kills",
                    "playtimeMillis",
                    "roundsPlayed",
                    "score"
                  ]
                },
                "teamId": {
                  "type": "string"
                }
              },
              "required": [
                "characterId",
                "competitiveTier",
                "partyId",
                "playerCard",
                "playerTitle",
                "puuid",
                "stats",
                "teamId"
              ]
            }
          },
          "roundResults": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "bombPlanter": {
                  "type": "string"
                },
                "defuseLocation": {
                  "type": "object",
                  "properties": {
                    "x": {
                      "type": "number"
                    },
                    "y": {
                      "type": "number"
                    }
                  },
                  "required": [
                    "x",
                    "y"
                  ]
                },
                "defuseRoundTime": {
                  "type": "number"
                },
                "plantLocation": {
                  "type": "object",
                  "properties": {
                    "x": {
                      "type": "number"
                    },
                    "y": {
                      "type": "number"
                    }
                  },
                  "required": [
                    "x",
                    "y"
                  ]
                },
                "plantPlayerLocations": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "location": {
                        "type": "object",
                        "properties": {
                          "x": {
                            "type": "number"
                          },
                          "y": {
                            "type": "number"
                          }
                        },
                        "required": [
                          "x",
                          "y"
                        ]
                      },
                      "puuid": {
                        "type": "string"
                      },
                      "viewRadians": {
                        "type": "number"
                      }
                    },
                    "required": [
                      "location",
                      "puuid",
                      "viewRadians"
                    ]
                  }
                },
                "plantRoundTime": {
                  "type": "number"
                },
                "plantSite": {
                  "type": "string"
                },
                "playerStats": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "ability": {
                        "type": "object",
                        "properties": {},
                        "required": []
                      },
                      "damage": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "properties": {
                            "bodyshots": {
                              "type": "number"
                            },
                            "damage": {
                              "type": "number"
                            },
                            "headshots": {
                              "type": "number"
                            },
                            "legshots": {
                              "type": "number"
                            },
                            "receiver": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "bodyshots",
                            "damage",
                            "headshots",
                            "legshots",
                            "receiver"
                          ]
                        }
                      },
                      "economy": {
                        "type": "object",
                        "properties": {
                          "armor": {
                            "type": "string"
                          },
                          "loadoutValue": {
                            "type": "number"
                          },
                          "remaining": {
                            "type": "number"
                          },
                          "spent": {
                            "type": "number"
                          },
                          "weapon": {
                            "type": "string"
                          }
                        },
                        "required": [
                          "armor",
                          "loadoutValue",
                          "remaining",
                          "spent",
                          "weapon"
                        ]
                      },
                      "kills": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "properties": {
                            "assistants": {
                              "type": "array",
                              "items": {
                                "type": "string"
                              }
                            },
                            "finishingDamage": {
                              "type": "object",
                              "properties": {
                                "damageItem": {
                                  "type": "string"
                                },
                                "damageType": {
                                  "type": "string"
                                },
                                "isSecondaryFireMode": {
                                  "type": "boolean"
                                }
                              },
                              "required": [
                                "damageItem",
                                "damageType",
                                "isSecondaryFireMode"
                              ]
                            },
                            "killer": {
                              "type": "string"
                            },
                            "playerLocations": {
                              "type": "array",
                              "items": {
                                "type": "object",
                                "properties": {
                                  "location": {
                                    "type": "object",
                                    "properties": {
                                      "x": {
                                        "type": "number"
                                      },
                                      "y": {
                                        "type": "number"
                                      }
                                    },
                                    "required": [
                                      "x",
                                      "y"
                                    ]
                                  },
                                  "puuid": {
                                    "type": "string"
                                  },
                                  "viewRadians": {
                                    "type": "number"
                                  }
                                },
                                "required": [
                                  "location",
                                  "puuid",
                                  "viewRadians"
                                ]
                              }
                            },
                            "timeSinceGameStartMillis": {
                              "type": "number"
                            },
                            "timeSinceRoundStartMillis": {
                              "type": "number"
                            },
                            "victim": {
                              "type": "string"
                            },
                            "victimLocation": {
                              "type": "object",
                              "properties": {
                                "x": {
                                  "type": "number"
                                },
                                "y": {
                                  "type": "number"
                                }
                              },
                              "required": [
                                "x",
                                "y"
                              ]
                            }
                          },
                          "required": [
                            "assistants",
                            "finishingDamage",
                            "killer",
                            "playerLocations",
                            "timeSinceGameStartMillis",
                            "timeSinceRoundStartMillis",
                            "victim",
                            "victimLocation"
                          ]
                        }
                      },
                      "puuid": {
                        "type": "string"
                      },
                      "score": {
                        "type": "number"
                      }
                    },
                    "required": [
                      "ability",
                      "damage",
                      "economy",
                      "kills",
                      "puuid",
                      "score"
                    ]
                  }
                },
                "roundCeremony": {
                  "type": "string"
                },
                "roundNum": {
                  "type": "number"
                },
                "roundResult": {
                  "type": "string"
                },
                "roundResultCode": {
                  "type": "string"
                },
                "winningTeam": {
                  "type": "string"
                },
                "bombDefuser": {
                  "type": "string"
                },
                "defusePlayerLocations": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "location": {
                        "type": "object",
                        "properties": {
                          "x": {
                            "type": "number"
                          },
                          "y": {
                            "type": "number"
                          }
                        },
                        "required": [
                          "x",
                          "y"
                        ]
                      },
                      "puuid": {
                        "type": "string"
                      },
                      "viewRadians": {
                        "type": "number"
                      }
                    },
                    "required": [
                      "location",
                      "puuid",
                      "viewRadians"
                    ]
                  }
                }
              },
              "required": [
                "defuseLocation",
                "defuseRoundTime",
                "plantLocation",
                "plantRoundTime",
                "plantSite",
                "playerStats",
                "roundCeremony",
                "roundNum",
                "roundResult",
                "roundResultCode",
                "winningTeam"
              ]
            }
          },
          "teams": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "numPoints": {
                  "type": "number"
                },
                "roundsPlayed": {
                  "type": "number"
                },
                "roundsWon": {
                  "type": "number"
                },
                "teamId": {
                  "type": "string"
                },
                "won": {
                  "type": "boolean"
                }
              },
              "required": [
                "numPoints",
                "roundsPlayed",
                "roundsWon",
                "teamId",
                "won"
              ]
            }
          }
        },
        "required": [
          "matchInfo",
          "players",
          "roundResults",
          "teams"
        ]
      }
    },
    "players": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "gameName": {
            "type": "string"
          },
          "puuid": {
            "type": "string"
          },
          "tagLine": {
            "type": "string"
          }
        },
        "required": [
          "gameName",
          "puuid",
          "tagLine"
        ]
      }
    }
  },
  "required": [
    "matches",
    "players"
  ]
}