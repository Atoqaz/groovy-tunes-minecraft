advancement revoke @s only tunes:use_horn

stopsound @a[distance=..128] record minecraft:item.goat_horn.sound.7

scoreboard players set @s tunes.tact -1
execute if data entity @s {SelectedItem:{id:"minecraft:goat_horn",tag:{display:{Lore:['[{"text":"Her på R","italic":false,"color":"dark_purple"}]']}}}} run scoreboard players set @s tunes.id 1
execute if data entity @s {SelectedItem:{id:"minecraft:goat_horn",tag:{display:{Lore:['[{"text":"Ghostbusters","italic":false,"color":"dark_purple"}]']}}}} run scoreboard players set @s tunes.id 2
execute if data entity @s {SelectedItem:{id:"minecraft:goat_horn",tag:{display:{Lore:['[{"text":"All I Want For Christmas","italic":false,"color":"dark_purple"}]']}}}} run scoreboard players set @s tunes.id 3
execute if data entity @s {SelectedItem:{id:"minecraft:goat_horn",tag:{display:{Lore:['[{"text":"Pokémon","italic":false,"color":"dark_purple"}]']}}}} run scoreboard players set @s tunes.id 4
execute if data entity @s {SelectedItem:{id:"minecraft:goat_horn",tag:{display:{Lore:['[{"text":"Last Christmas","italic":false,"color":"dark_purple"}]']}}}} run scoreboard players set @s tunes.id 5
