from src.preprocess.access import pp_access
from src.preprocess.address import pp_address
from src.preprocess.age import pp_age
from src.preprocess.area import pp_area
from src.preprocess.bathroom import pp_bathroom
from src.preprocess.contract import pp_contract
from src.preprocess.equipment import pp_equipment
from src.preprocess.floor_stories import pp_floor_stories
from src.preprocess.internet import pp_internet
from src.preprocess.kitchen import pp_kitchen
from src.preprocess.layout import pp_layout
from src.preprocess.parking import pp_parking


def pp(df):
    df = pp_age(df)
    df = pp_area(df)
    df = pp_access(df)
    df = pp_address(df)
    df = pp_bathroom(df)
    df = pp_contract(df)
    df = pp_equipment(df)
    df = pp_floor_stories(df)
    df = pp_internet(df)
    df = pp_kitchen(df)
    df = pp_layout(df)
    df = pp_parking(df)

    df["building"] = df["stories"].astype(str) + "階" + df["address_1_2"] + df["age"]

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
