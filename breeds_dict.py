import cairn_terrier
import breed_characteristics as bc


logo = ('''
    ********************************************          
                        |\|\
                       ..    \       .
                     o--     \\    / @)
                      v__///\\\\__/ @
                        {           }
                         {  } \\\{  }
                         <_|      <_|
    ********************************************
    ''')

breed_group = {
    1: {
        "name": "Sheepdogs and Cattle dogs",
        "subgroups":
            {
                1: {
                    "name": "Australian Shepherd",
                    "characteristics":
                        {
                            1: {"name": "Description", "value": bc.australian_shepherd.description},
                            2: {"name": "Personality", "value": bc.australian_shepherd.personality},
                            3: {"name": "Grooming", "value": bc.australian_shepherd.grooming},
                            4: {"name": "Living condition", "value": bc.australian_shepherd.living_conditions},
                            5: {"name": "Training", "value": bc.australian_shepherd.training},
                            6: {"name": "Usefulness", "value": bc.australian_shepherd.usefulness}
                         }
                    },
                2: {
                    "name": "Belgian Shepherd Malinois",
                    "characteristics":
                        {
                            1: {"name": "Description", "value": bc.belgian_shepherd_malinois.description},
                            2: {"name": "Personality", "value": bc.belgian_shepherd_malinois.personality},
                            3: {"name": "Grooming", "value": bc.belgian_shepherd_malinois.grooming},
                            4: {"name": "Living condition", "value": bc.belgian_shepherd_malinois.living_conditions},
                            5: {"name": "Training", "value": bc.belgian_shepherd_malinois.training},
                            6: {"name": "Usefulness", "value": bc.belgian_shepherd_malinois.usefulness}
                         }
                    },
                3: {
                    "name": "Mioritic",
                    "characteristics":
                        {
                            1: {"name": "Description", "value": bc.mioritic_dog.description},
                            2: {"name": "Personality", "value": bc.mioritic_dog.personality},
                            3: {"name": "Grooming", "value": bc.mioritic_dog.grooming},
                            4: {"name": "Living condition", "value": bc.mioritic_dog.living_conditions},
                            5: {"name": "Training", "value": bc.mioritic_dog.training},
                            6: {"name": "Usefulness", "value": bc.mioritic_dog.usefulness}
                        }
                    }
            }
    },
    2: {
        "name": "Pinscher and Schnauzer - Molossoid and Swiss Mountain and Cattledogs",
        "subgroups":
            {
                1: {
                    "name": "Boerboel",
                    "characteristics":
                        {
                            1: {"name": "Description", "value": bc.boerbol.description},
                            2: {"name": "Personality", "value": bc.boerbol.personality},
                            3: {"name": "Grooming", "value": bc.boerbol.grooming},
                            4: {"name": "Living condition", "value": bc.boerbol.living_conditions},
                            5: {"name": "Training", "value": bc.boerbol.training},
                            6: {"name": "Usefulness", "value": bc.boerbol.usefulness}
                        }
                    },
                2: {
                    "name": "Affenpinscher",
                    "characteristics":
                        {
                            1: {"name": "Description", "value": bc.affenpinscher.description},
                            2: {"name": "Personality", "value": bc.affenpinscher.personality},
                            3: {"name": "Grooming", "value": bc.affenpinscher.grooming},
                            4: {"name": "Living condition", "value": bc.affenpinscher.living_conditions},
                            5: {"name": "Training", "value": bc.affenpinscher.training},
                            6: {"name": "Usefulness", "value": bc.affenpinscher.usefulness}
                        }
                    },
                3: {
                    "name": "Cavalier King Charles Spaniel",
                    "characteristics":
                        {
                            1: {"name": "Description", "value": bc.cavalier_king_charles_spaniel.description},
                            2: {"name": "Personality", "value": bc.cavalier_king_charles_spaniel.personality},
                            3: {"name": "Grooming", "value": bc.cavalier_king_charles_spaniel.grooming},
                            4: {"name": "Living condition", "value": bc.cavalier_king_charles_spaniel.living_conditions},
                            5: {"name": "Training", "value": bc.cavalier_king_charles_spaniel.training},
                            6: {"name": "Usefulness", "value": bc.cavalier_king_charles_spaniel.usefulness}
                        }
                    }
            }
    },
    3: {
        "name": "Terriers",
        "subgroups":
            {
                1: {
                    "name": "Airedale Terrier",
                    "characteristics":
                        {
                            1: {"name": "Description", "value": bc.airedale_terrier.description},
                            2: {"name": "Personality", "value": bc.airedale_terrier.personality},
                            3: {"name": "Grooming", "value": bc.airedale_terrier.grooming},
                            4: {"name": "Living condition", "value": bc.airedale_terrier.living_conditions},
                            5: {"name": "Training", "value": bc.airedale_terrier.training},
                            6: {"name": "Usefulness", "value": bc.airedale_terrier.usefulness}
                        }
                    },
                2: {
                    "name": "American Pit Bull Terrier",
                    "characteristics":
                        {
                            1: {"name": "Description", "value": bc.american_pit_ull_terrier.description},
                            2: {"name": "Personality", "value": bc.american_pit_ull_terrier.personality},
                            3: {"name": "Grooming", "value": bc.american_pit_ull_terrier.grooming},
                            4: {"name": "Living condition", "value": bc.american_pit_ull_terrier.living_conditions},
                            5: {"name": "Training", "value": bc.american_pit_ull_terrier.training},
                            6: {"name": "Usefulness", "value": bc.american_pit_ull_terrier.usefulness}
                        }
                    },
                3: {
                    "name": "Australian Terrier",
                    "characteristics":
                        {
                            1: {"name": "Description", "value": bc.australian_terrier.description},
                            2: {"name": "Personality", "value": bc.australian_terrier.personality},
                            3: {"name": "Grooming", "value": bc.australian_terrier.grooming},
                            4: {"name": "Living condition", "value": bc.australian_terrier.living_conditions},
                            5: {"name": "Training", "value": bc.australian_terrier.training},
                            6: {"name": "Usefulness", "value": bc.australian_terrier.usefulness}
                        }
                    },
                4: {
                    "name": "Australian Silky Terrier",
                    "characteristics":
                        {
                            1: {"name": "Description", "value": bc.australian_silky_terrier.description},
                            2: {"name": "Personality", "value": bc.australian_silky_terrier.personality},
                            3: {"name": "Grooming", "value": bc.australian_silky_terrier.grooming},
                            4: {"name": "Living condition", "value": bc.australian_silky_terrier.living_conditions},
                            5: {"name": "Training", "value": bc.australian_silky_terrier.training},
                            6: {"name": "Usefulness", "value": bc.australian_silky_terrier.usefulness}
                        }
                    },
                5: {
                    "name": "Cairn Terrier",
                    "characteristics":
                        {
                            1: {"name": "Description", "value": bc.cairn_terrier.description},
                            2: {"name": "Personality", "value": bc.cairn_terrier.personality},
                            3: {"name": "Grooming", "value": bc.cairn_terrier.grooming},
                            4: {"name": "Living condition", "value": bc.cairn_terrier.living_conditions},
                            5: {"name": "Training", "value": bc.cairn_terrier.training},
                            6: {"name": "Usefulness", "value": bc.cairn_terrier.usefulness}
                        }
                    },
                6: {
                    "name": "West Highland White Terrier",
                    "characteristics":
                        {
                            1: {"name": "Description", "value": bc.west_highland_white_terrier.description},
                            2: {"name": "Personality", "value": bc.west_highland_white_terrier.personality},
                            3: {"name": "Grooming", "value": bc.west_highland_white_terrier.grooming},
                            4: {"name": "Living condition", "value": bc.west_highland_white_terrier.living_conditions},
                            5: {"name": "Training", "value": bc.west_highland_white_terrier.training},
                            6: {"name": "Usefulness", "value": bc.west_highland_white_terrier.usefulness}
                        }
                    },
                7: {
                    "name": "Norfolk Terrier",
                    "characteristics":
                        {
                            1: {"name": "Description", "value": bc.norfolk_terrier.description},
                            2: {"name": "Personality", "value": bc.norfolk_terrier.personality},
                            3: {"name": "Grooming", "value": bc.norfolk_terrier.grooming},
                            4: {"name": "Living condition", "value": bc.norfolk_terrier.living_conditions},
                            5: {"name": "Training", "value": bc.norfolk_terrier.training},
                            6: {"name": "Usefulness", "value": bc.norfolk_terrier.usefulness}
                        }
                    },
                8: {
                    "name": "Norwich Terrier",
                    "characteristics":
                        {
                            1: {"name": "Description", "value": bc.norwich_terrier.description},
                            2: {"name": "Personality", "value": bc.norwich_terrier.personality},
                            3: {"name": "Grooming", "value": bc.norwich_terrier.grooming},
                            4: {"name": "Living condition", "value": bc.norwich_terrier.living_conditions},
                            5: {"name": "Training", "value": bc.norwich_terrier.training},
                            6: {"name": "Usefulness", "value": bc.norwich_terrier.usefulness}
                        }
                    },
                9: {
                    "name": "Scottish Terrier",
                    "characteristics":
                        {
                            1: {"name": "Description", "value": bc.scottish_terrier.description},
                            2: {"name": "Personality", "value": bc.scottish_terrier.personality},
                            3: {"name": "Grooming", "value": bc.scottish_terrier.grooming},
                            4: {"name": "Living condition", "value": bc.scottish_terrier.living_conditions},
                            5: {"name": "Training", "value": bc.scottish_terrier.training},
                            6: {"name": "Usefulness", "value": bc.scottish_terrier.usefulness}
                        }
                    },
                10: {
                    "name": "Scottish Sky Terrier",
                    "characteristics":
                        {
                            1: {"name": "Description", "value": bc.scottish_sky_terrier.description},
                            2: {"name": "Personality", "value": bc.scottish_sky_terrier.personality},
                            3: {"name": "Grooming", "value": bc.scottish_sky_terrier.grooming},
                            4: {"name": "Living condition", "value": bc.scottish_sky_terrier.living_conditions},
                            5: {"name": "Training", "value": bc.scottish_sky_terrier.training},
                            6: {"name": "Usefulness", "value": bc.scottish_sky_terrier.usefulness}
                        }
                    }
            }
    },
    4: {
        "name": "Dachshunds",
        "subgroups":
            {
                1: {
                    "name": "Dachshund",
                    "characteristics":
                        {
                            1: {"name": "Description", "value": bc.dachshund.description},
                            2: {"name": "Personality", "value": bc.dachshund.personality},
                            3: {"name": "Grooming", "value": bc.dachshund.grooming},
                            4: {"name": "Living condition", "value": bc.dachshund.living_conditions},
                            5: {"name": "Training", "value": bc.dachshund.training},
                            6: {"name": "Usefulness", "value": bc.dachshund.usefulness}
                        }
                    },
                2: {
                    "name": "Dachshund -The Wiry Hair Variety",
                    "characteristics":
                        {
                            1: {"name": "Description", "value": bc.dachshund_the_wiry_hair_variety.description},
                            2: {"name": "Personality", "value": bc.dachshund_the_wiry_hair_variety.personality},
                            3: {"name": "Grooming", "value": bc.dachshund_the_wiry_hair_variety.grooming},
                            4: {"name": "Living condition", "value": bc.dachshund_the_wiry_hair_variety.living_conditions},
                            5: {"name": "Training", "value": bc.dachshund_the_wiry_hair_variety.training},
                            6: {"name": "Usefulness", "value": bc.dachshund_the_wiry_hair_variety.usefulness}
                        }
                    },
                3: {
                    "name": "Long-Haired Dachshund",
                    "characteristics":
                        {
                            1: {"name": "Description", "value": bc.long_haired_dachshund.description},
                            2: {"name": "Personality", "value": bc.long_haired_dachshund.personality},
                            3: {"name": "Grooming", "value": bc.long_haired_dachshund.grooming},
                            4: {"name": "Living condition", "value": bc.long_haired_dachshund.living_conditions},
                            5: {"name": "Training", "value": bc.long_haired_dachshund.training},
                            6: {"name": "Usefulness", "value": bc.long_haired_dachshund.usefulness}
                        }
                    }
            }
    },
    5: {
        "name": "Spitz and primitive types",
        "subgroups":
            {
                1: {
                    "name": "Akita Inu",
                    "characteristics":
                        {
                            1: {"name": "Description", "value": bc.akita_inu.description},
                            2: {"name": "Personality", "value": bc.akita_inu.personality},
                            3: {"name": "Grooming", "value": bc.akita_inu.grooming},
                            4: {"name": "Living condition", "value": bc.akita_inu.living_conditions},
                            5: {"name": "Training", "value": bc.akita_inu.training},
                            6: {"name": "Usefulness", "value": bc.akita_inu.usefulness}
                        }
                    },
                2: {
                    "name": "Swedish Wallhund",
                    "characteristics":
                        {
                            1: {"name": "Description", "value": bc.swedish_wallhund.description},
                            2: {"name": "Personality", "value": bc.swedish_wallhund.personality},
                            3: {"name": "Grooming", "value": bc.swedish_wallhund.grooming},
                            4: {"name": "Living condition", "value": bc.swedish_wallhund.living_conditions},
                            5: {"name": "Training", "value": bc.swedish_wallhund.training},
                            6: {"name": "Usefulness", "value": bc.swedish_wallhund.usefulness}
                        }
                    },
                3: {
                    "name": "Norwegian Elkhound",
                    "characteristics":
                        {
                            1: {"name": "Description", "value": bc.norwegian_elkhound.description},
                            2: {"name": "Personality", "value": bc.norwegian_elkhound.personality},
                            3: {"name": "Grooming", "value": bc.norwegian_elkhound.grooming},
                            4: {"name": "Living condition", "value": bc.norwegian_elkhound.living_conditions},
                            5: {"name": "Training", "value": bc.norwegian_elkhound.training},
                            6: {"name": "Usefulness", "value": bc.norwegian_elkhound.usefulness}
                        }
                    }
            }
    },
    6: {
        "name": "Scent hounds and related breeds",
        "subgroups":
            {
                1: {
                    "name": "Dalmatian",
                    "characteristics":
                        {
                            1: {"name": "Description", "value": bc.dalmatian.description},
                            2: {"name": "Personality", "value": bc.dalmatian.personality},
                            3: {"name": "Grooming", "value": bc.dalmatian.grooming},
                            4: {"name": "Living condition", "value": bc.dalmatian.living_conditions},
                            5: {"name": "Training", "value": bc.dalmatian.training},
                            6: {"name": "Usefulness", "value": bc.dalmatian.usefulness}
                        }
                    },
                2: {
                    "name": "Rhodesian Rodgeback",
                    "characteristics":
                        {
                            1: {"name": "Description", "value": bc.rhodesian_rodgeback.description},
                            2: {"name": "Personality", "value": bc.rhodesian_rodgeback.personality},
                            3: {"name": "Grooming", "value": bc.rhodesian_rodgeback.grooming},
                            4: {"name": "Living condition", "value": bc.rhodesian_rodgeback.living_conditions},
                            5: {"name": "Training", "value": bc.rhodesian_rodgeback.training},
                            6: {"name": "Usefulness", "value": bc.rhodesian_rodgeback.usefulness}
                        }
                    },
                3: {
                    "name": "Basset Fauve De Bretagne",
                    "characteristics":
                        {
                            1: {"name": "Description", "value": bc.basset_fauve_de_bretagne.description},
                            2: {"name": "Personality", "value": bc.basset_fauve_de_bretagne.personality},
                            3: {"name": "Grooming", "value": bc.basset_fauve_de_bretagne.grooming},
                            4: {"name": "Living condition", "value": bc.basset_fauve_de_bretagne.living_conditions},
                            5: {"name": "Training", "value": bc.basset_fauve_de_bretagne.training},
                            6: {"name": "Usefulness", "value": bc.basset_fauve_de_bretagne.usefulness}
                        }
                    }
            }
    },
    7: {
        "name": "Pointing Dogs",
        "subgroups":
            {
                1: {
                    "name": "Gordon Setter",
                    "characteristics":
                        {
                            1: {"name": "Description", "value": bc.gordon_setter.description},
                            2: {"name": "Personality", "value": bc.gordon_setter.personality},
                            3: {"name": "Grooming", "value": bc.gordon_setter.grooming},
                            4: {"name": "Living condition", "value": bc.gordon_setter.living_conditions},
                            5: {"name": "Training", "value": bc.gordon_setter.training},
                            6: {"name": "Usefulness", "value": bc.gordon_setter.usefulness}
                        }
                    },
                2: {
                    "name": "Weimaraner",
                    "characteristics":
                        {
                            1: {"name": "Description", "value": bc.weimaraner.description},
                            2: {"name": "Personality", "value": bc.weimaraner.personality},
                            3: {"name": "Grooming", "value": bc.weimaraner.grooming},
                            4: {"name": "Living condition", "value": bc.weimaraner.living_conditions},
                            5: {"name": "Training", "value": bc.weimaraner.training},
                            6: {"name": "Usefulness", "value": bc.weimaraner.usefulness}
                        }
                    },
                3: {
                    "name": "Wetterhoun",
                    "characteristics":
                        {
                            1: {"name": "Description", "value": bc.wetterhoun.description},
                            2: {"name": "Personality", "value": bc.wetterhoun.personality},
                            3: {"name": "Grooming", "value": bc.wetterhoun.grooming},
                            4: {"name": "Living condition", "value": bc.wetterhoun.living_conditions},
                            5: {"name": "Training", "value": bc.wetterhoun.training},
                            6: {"name": "Usefulness", "value": bc.wetterhoun.usefulness}
                        }
                    }
            }
    },
    8: {
        "name": "Retrievers - Flushing Dogs - Water Dogs",
        "subgroups":
            {
                1: {
                    "name": "Welsh Springer Spaniel",
                    "characteristics":
                        {
                            1: {"name": "Description", "value": bc.welsh_springer_spaniel.description},
                            2: {"name": "Personality", "value": bc.welsh_springer_spaniel.personality},
                            3: {"name": "Grooming", "value": bc.welsh_springer_spaniel.grooming},
                            4: {"name": "Living condition", "value": bc.welsh_springer_spaniel.living_conditions},
                            5: {"name": "Training", "value": bc.welsh_springer_spaniel.training},
                            6: {"name": "Usefulness", "value": bc.welsh_springer_spaniel.usefulness}
                        }
                    },
                2: {
                    "name": "Clumber Spaniel",
                    "characteristics":
                        {
                            1: {"name": "Description", "value": bc.clumber_spaniel.description},
                            2: {"name": "Personality", "value": bc.clumber_spaniel.personality},
                            3: {"name": "Grooming", "value": bc.clumber_spaniel.grooming},
                            4: {"name": "Living condition", "value": bc.clumber_spaniel.living_conditions},
                            5: {"name": "Training", "value": bc.clumber_spaniel.training},
                            6: {"name": "Usefulness", "value": bc.clumber_spaniel.usefulness}
                        }
                    },
                3: {
                    "name": "Curly Coated Retriever",
                    "characteristics":
                        {
                            1: {"name": "Description", "value": bc.curly_coated_retriever.description},
                            2: {"name": "Personality", "value": bc.curly_coated_retriever.personality},
                            3: {"name": "Grooming", "value": bc.curly_coated_retriever.grooming},
                            4: {"name": "Living condition", "value": bc.curly_coated_retriever.living_conditions},
                            5: {"name": "Training", "value": bc.curly_coated_retriever.training},
                            6: {"name": "Usefulness", "value": bc.curly_coated_retriever.usefulness}
                        }
                    }
            }
    },
    9: {
        "name": "Companion and Toy Dogs",
        "subgroups":
            {
                1: {
                    "name": "Shih Tzu",
                    "characteristics":
                        {
                            1: {"name": "Description", "value": bc.shih_tzu.description},
                            2: {"name": "Personality", "value":  bc.shih_tzu.personality},
                            3: {"name": "Grooming", "value":  bc.shih_tzu.grooming},
                            4: {"name": "Living condition", "value":  bc.shih_tzu.living_conditions},
                            5: {"name": "Training", "value":  bc.shih_tzu.training},
                            6: {"name": "Usefulness", "value":  bc.shih_tzu.usefulness}
                        }
                    },
                2: {
                    "name": "Brussels Griffon",
                    "characteristics":
                        {
                            1: {"name": "Description", "value": bc.brussels_griffon.description},
                            2: {"name": "Personality", "value":  bc.brussels_griffon.personality},
                            3: {"name": "Grooming", "value":  bc.brussels_griffon.grooming},
                            4: {"name": "Living condition", "value":  bc.brussels_griffon.living_conditions},
                            5: {"name": "Training", "value":  bc.brussels_griffon.training},
                            6: {"name": "Usefulness", "value":  bc.brussels_griffon.usefulness}
                        }
                    },
                3: {
                    "name": "Cavalier King Charles Spaniel",
                    "characteristics":
                        {
                            1: {"name": "Description", "value": bc.cavalier_king_charles_spaniel.description},
                            2: {"name": "Personality", "value": bc.cavalier_king_charles_spaniel.personality},
                            3: {"name": "Grooming", "value": bc.cavalier_king_charles_spaniel.grooming},
                            4: {"name": "Living condition", "value": bc.cavalier_king_charles_spaniel.living_conditions},
                            5: {"name": "Training", "value": bc.cavalier_king_charles_spaniel.training},
                            6: {"name": "Usefulness", "value": bc.cavalier_king_charles_spaniel.usefulness}
                        }
                    }
            }
    },
    10: {
        "name": "Sighthounds",
        "subgroups":
            {
                1: {
                    "name": "Scottish Deerhound",
                    "characteristics":
                        {
                            1: {"name": "Description", "value": bc.scottish_deerhound.description},
                            2: {"name": "Personality", "value": bc.scottish_deerhound.personality},
                            3: {"name": "Grooming", "value": bc.scottish_deerhound.grooming},
                            4: {"name": "Living condition", "value": bc.scottish_deerhound.living_conditions},
                            5: {"name": "Training", "value": bc.scottish_deerhound.training},
                            6: {"name": "Usefulness", "value": bc.scottish_deerhound.usefulness}
                        }
                    },
                2: {
                    "name": "Irish Wolfhound",
                    "characteristics":
                        {
                            1: {"name": "Description", "value": bc.irish_wolfhound.description},
                            2: {"name": "Personality", "value": bc.irish_wolfhound.personality},
                            3: {"name": "Grooming", "value": bc.irish_wolfhound.grooming},
                            4: {"name": "Living condition", "value": bc.irish_wolfhound.living_conditions},
                            5: {"name": "Training", "value": bc.irish_wolfhound.training},
                            6: {"name": "Usefulness", "value": bc.irish_wolfhound.usefulness}
                        }
                    },
                3: {
                    "name": "Barzoi",
                    "characteristics":
                        {
                            1: {"name": "Description", "value": bc.barzoi.description},
                            2: {"name": "Personality", "value": bc.barzoi.personality},
                            3: {"name": "Grooming", "value": bc.barzoi.grooming},
                            4: {"name": "Living condition", "value": bc.barzoi.living_conditions},
                            5: {"name": "Training", "value": bc.barzoi.training},
                            6: {"name": "Usefulness", "value": bc.barzoi.usefulness}
                        }
                    }
            }
    }

}






