from age import pp_age
from area import pp_area
from contract import pp_contract
from equipment import pp_equipment
from floor_stories import pp_floor_stories
from internet import pp_internet
from kitchen import pp_kitchen
from parking import pp_parking
from read_file import read_file

df = read_file(INPUT_FILE_PATH="./../input")
df = pp_age(df)
df = pp_area(df)
df = pp_contract(df)
df = pp_equipment(df)
df = pp_floor_stories(df)
df = pp_internet(df)
df = pp_kitchen(df)
df = pp_parking(df)

print(df)
