from src.preprocess.age import pp_age
from src.preprocess.area import pp_area
from src.preprocess.bathroom import pp_bathroom
from src.preprocess.contract import pp_contract
from src.preprocess.equipment import pp_equipment
from src.preprocess.floor_stories import pp_floor_stories
from src.preprocess.internet import pp_internet
from src.preprocess.kitchen import pp_kitchen
from src.preprocess.parking import pp_parking


def pp(df):
    df = pp_age(df)
    df = pp_area(df)
    df = pp_bathroom(df)
    df = pp_contract(df)
    df = pp_equipment(df)
    df = pp_floor_stories(df)
    df = pp_internet(df)
    df = pp_kitchen(df)
    df = pp_parking(df)

    # drop unused columns
    df = df.drop(
        [
            "access",
            "address",
            "bathroom",
            "equipment",
            "floor_stories",
            "internet",
            "kitchen",
            "parking",
        ],
        axis=1,
    )
    return df
