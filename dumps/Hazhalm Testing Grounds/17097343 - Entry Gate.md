# 17097343 - Entry Gate

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Hazhalm Testing Grounds (ID: 78) |
| Block Size       | 420 bytes                        |
| Total Events     | 5                                |
| References Count | 29                               |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [2](#event-2)            | 0x0001       |    259 |             74 |
| [19](#event-19)          | 0x0104       |      2 |              2 |
| [65535.1](#event-655351) | 0x0106       |      2 |              2 |
| [65535.2](#event-655352) | 0x0108       |      2 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x40000000  |  1073741824 |
|       1 | 0x1F71      |        8049 |
|       2 | 0x0000      |           0 |
|       3 | 0x1F72      |        8050 |
|       4 | 0x0001      |           1 |
|       5 | 0x1F73      |        8051 |
|       6 | 0x1F7B      |        8059 |
|       7 | 0x0003      |           3 |
|       8 | 0x0002      |           2 |
|       9 | 0x0005      |           5 |
|      10 | 0x0004      |           4 |
|      11 | 0x0007      |           7 |
|      12 | 0x1F91      |        8081 |
|      13 | 0x1F92      |        8082 |
|      14 | 0x1F93      |        8083 |
|      15 | 0x1F94      |        8084 |
|      16 | 0x1F95      |        8085 |
|      17 | 0x1F96      |        8086 |
|      18 | 0x1F97      |        8087 |
|      19 | 0x1F98      |        8088 |
|      20 | 0x1F99      |        8089 |
|      21 | 0x1F9A      |        8090 |
|      22 | 0x1FA8      |        8104 |
|      23 | 0x1FA9      |        8105 |
|      24 | 0x1FAA      |        8106 |
|      25 | 0x1FAB      |        8107 |
|      26 | 0x1FAC      |        8108 |
|      27 | 0x1FAD      |        8109 |
|      28 | 0x1FAF      |        8111 |

## String References

- **8049**: Record time and destination on the $6?
- **8050**: Select option: [Confirm destination./Cancel recording./Confirm entry conditions./Confirm re-entry conditions./Confirm battle conditions.]
- **8051**: Select [Quit./Rossweisse's Chamber./Grimgerde's Chamber./Siegrune's Chamber./Helmwige's Chamber./Schwertleite's Chamber./Waltraute's Chamber./Ortlinde's Chamber./Gerhilde's Chamber./Brunhilde's Chamber./Odin's Chamber./Odin's Chamber II.]
- **8059**: Gathering data...
- **8081**: When traded to the Hazhalm Testing Grounds' Entry Gate, $6 will light and become $7.
- **8082**: From that moment, the owner of the $7 will reserve and gain access to one of the facility's many chambers.
- **8083**: By using the $7 it will produce a replica of itself which can be given to another, granting him or her access to the same chamber.
- **8084**: Though an infinite number of lamps can be produced using this method, only a maximum of thirty-six people can venture into the same chamber.
- **8085**: Once thirty-six souls have crossed the seal, all lamps outside the grounds will cease to function.
- **8086**: These lamps will also cease to function the instant any adventurer within the chamber engages in battle, regardless of how many people have already passed through the gates.
- **8087**: To teleport to the reserved chamber, one must simply trade their $7 to the Entry Gate.
- **8088**: However, please note that not everyone in possession of a lamp will be allowed into Hazhalm.
- **8089**: As mentioned before, only up to thirty-six people may enter a chamber. Even those with a valid $7 will not be allowed entry if the chamber has reached its maximum capacity.
- **8090**: Also, as a safety precaution, players below level sixty and those with the Battlefield status in effect will be denied entry.
- **8104**: After visiting the testing grounds, one must wait $3 [hour/hours] (Earth time) before he is granted access again.
- **8105**: This not only pertains to the chamber previously visited, but all areas within the testing grounds.
- **8106**: The amount of waiting time remaining before re-entry is permitted can be viewed by checking Hazhalm's Entry Gate.
- **8107**: All monsters dwelling in the testing grounds can be attacked by anyone, regardless of party or alliance.
- **8108**: In addition, any items dropped by a foe can be lotted on by anyone in the chamber.
- **8109**: However, please be aware that any items that have not been lotted on when a chamber's reservation is up will be distributed at random.
- **8111**: Also, if everyone in a chamber remains KO'd for longer than $2 [minute/minutes], they will all be automatically teleported from the grounds.

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 00                                                .               
```

#### Opcodes

```
  0: 0x0000 [0x00] END_REQSTACK()
```

### Event 2

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 259 bytes |
| Instructions | 74        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    03 01 10 00 80 48 01  80 23 03 01 00 02 80 02   .....H..#......
0010: 01 00 02 80 00 02 01 24  03 80 04 80 02 80 25 02  .......$......%.
0020: 00 10 02 80 00 8A 00 24  05 80 02 80 07 10 25 02  .......$......%.
0030: 00 10 02 80 00 3A 00 01  3A 00 02 00 10 02 80 01  .....:..:.......
0040: 87 00 48 06 80 42 03 01  10 00 10 A7 00 A7 01 00  ..H..B..........
0050: 00 02 02 10 04 80 80 61  00 03 00 00 07 80 01 71  .......a.......q
0060: 00 02 02 10 08 80 80 71  00 03 00 00 09 80 01 71  .......q.......q
0070: 00 40 0A 80 0B 80 01 10  00 00 02 00 00 0A 80 00  .@..............
0080: 82 00 03 01 00 04 80 01  FF 00 02 00 10 04 80 00  ................
0090: 9A 00 03 01 00 04 80 01  FF 00 02 00 10 08 80 00  ................
00A0: CD 00 48 0C 80 23 48 0D  80 23 48 0E 80 23 48 0F  ..H..#H..#H..#H.
00B0: 80 23 48 10 80 23 48 11  80 23 48 12 80 23 48 13  .#H..#H..#H..#H.
00C0: 80 23 48 14 80 23 48 15  80 23 01 FF 00 02 00 10  .#H..#H..#......
00D0: 07 80 00 E4 00 48 16 80  23 48 17 80 23 48 18 80  .....H..#H..#H..
00E0: 23 01 FF 00 02 00 10 0A  80 00 FF 00 48 19 80 23  #...........H..#
00F0: 48 1A 80 23 48 1B 80 23  48 1C 80 23 01 FF 00 01  H..#H..#H..#....
0100: 0F 00 21 00                                       ..!.            
```

#### Opcodes

```
  0: 0x0001 [0x03] Work_Zone[1] = 1073741824*
  1: 0x0006 [0x48] [System] [8049*]:
    → "Record time and destination on the $6?"
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x03] ExtData[1]->WorkLocal[1] = 0*
  4: 0x000F [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x0102
  5: 0x0017 [0x24] CREATE_DIALOG(message_id=8050*, default_option=1*, option_flags=0*)
    → "Select option: [Confirm destination./Cancel recording./Confirm entry conditions./Confirm re-entry conditions./Confirm battle conditions.]"
  6: 0x001E [0x25] WAIT_DIALOG_SELECT()
  7: 0x001F [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x008A
  8: 0x0027 [0x24] CREATE_DIALOG(message_id=8051*, default_option=0*, option_flags=Work_Zone[7])
    → "Select [Quit./Rossweisse's Chamber./Grimgerde's Chamber./Siegrune's Chamber./Helmwige's Chamber./Schwertleite's Chamber./Waltraute's Chamber./Ortlinde's Chamber./Gerhilde's Chamber./Brunhilde's Chamber./Odin's Chamber./Odin's Chamber II.]"
  9: 0x002E [0x25] WAIT_DIALOG_SELECT()
 10: 0x002F [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x003A
 11: 0x0037 [0x01] GOTO 0x003A

SUBROUTINE_003A:
 12: 0x003A [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0087
 13: 0x0042 [0x48] [System] [8059*]:
    → "Gathering data..."
 14: 0x0045 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 15: 0x0046 [0x03] Work_Zone[1] = Work_Zone[0]
 16: 0x004B [0xA7] BATTLEFIELD_RESPONSE_WAIT: Wait for server response (Dynamis/MMM/Salvage), mode=0x00
 17: 0x004D [0xA7] BATTLEFIELD_RESPONSE_WAIT: Wait for server response with parameter (Dynamis/MMM/Salvage), param=ExtData[1]->WorkLocal[0]
 18: 0x0051 [0x02] IF !(Work_Zone[2] == 1*) GOTO 0x0061
 19: 0x0059 [0x03] ExtData[1]->WorkLocal[0] = 3*
 20: 0x005E [0x01] GOTO 0x0071
 21: 0x0061 [0x02] IF !(Work_Zone[2] == 2*) GOTO 0x0071
 22: 0x0069 [0x03] ExtData[1]->WorkLocal[0] = 5*
 23: 0x006E [0x01] GOTO 0x0071

SUBROUTINE_0071:
 24: 0x0071 [0x40] SET_BIT_WORK_RANGE(start_bit=4*, end_bit=7*, target=Work_Zone[1], source=ExtData[1]->WorkLocal[0])
 25: 0x007A [0x02] IF !(ExtData[1]->WorkLocal[0] == 4*) GOTO 0x0082
 26: 0x0082 [0x03] ExtData[1]->WorkLocal[1] = 1*
 27: 0x0087 [0x01] GOTO 0x00FF
 28: 0x008A [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x009A
 29: 0x0092 [0x03] ExtData[1]->WorkLocal[1] = 1*
 30: 0x0097 [0x01] GOTO 0x00FF
 31: 0x009A [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x00CD
 32: 0x00A2 [0x48] [System] [8081*]:
    → "When traded to the Hazhalm Testing Grounds' Entry Gate, $6 will light and become $7."
 33: 0x00A5 [0x23] WAIT_FOR_DIALOG_INTERACTION
 34: 0x00A6 [0x48] [System] [8082*]:
    → "From that moment, the owner of the $7 will reserve and gain access to one of the facility's many chambers."
 35: 0x00A9 [0x23] WAIT_FOR_DIALOG_INTERACTION
 36: 0x00AA [0x48] [System] [8083*]:
    → "By using the $7 it will produce a replica of itself which can be given to another, granting him or her access to the same chamber."
 37: 0x00AD [0x23] WAIT_FOR_DIALOG_INTERACTION
 38: 0x00AE [0x48] [System] [8084*]:
    → "Though an infinite number of lamps can be produced using this method, only a maximum of thirty-six people can venture into the same chamber."
 39: 0x00B1 [0x23] WAIT_FOR_DIALOG_INTERACTION
 40: 0x00B2 [0x48] [System] [8085*]:
    → "Once thirty-six souls have crossed the seal, all lamps outside the grounds will cease to function."
 41: 0x00B5 [0x23] WAIT_FOR_DIALOG_INTERACTION
 42: 0x00B6 [0x48] [System] [8086*]:
    → "These lamps will also cease to function the instant any adventurer within the chamber engages in battle, regardless of how many people have already passed through the gates."
 43: 0x00B9 [0x23] WAIT_FOR_DIALOG_INTERACTION
 44: 0x00BA [0x48] [System] [8087*]:
    → "To teleport to the reserved chamber, one must simply trade their $7 to the Entry Gate."
 45: 0x00BD [0x23] WAIT_FOR_DIALOG_INTERACTION
 46: 0x00BE [0x48] [System] [8088*]:
    → "However, please note that not everyone in possession of a lamp will be allowed into Hazhalm."
 47: 0x00C1 [0x23] WAIT_FOR_DIALOG_INTERACTION
 48: 0x00C2 [0x48] [System] [8089*]:
    → "As mentioned before, only up to thirty-six people may enter a chamber. Even those with a valid $7 will not be allowed entry if the chamber has reached its maximum capacity."
 49: 0x00C5 [0x23] WAIT_FOR_DIALOG_INTERACTION
 50: 0x00C6 [0x48] [System] [8090*]:
    → "Also, as a safety precaution, players below level sixty and those with the Battlefield status in effect will be denied entry."
 51: 0x00C9 [0x23] WAIT_FOR_DIALOG_INTERACTION
 52: 0x00CA [0x01] GOTO 0x00FF
 53: 0x00CD [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x00E4
 54: 0x00D5 [0x48] [System] [8104*]:
    → "After visiting the testing grounds, one must wait $3 [hour/hours] (Earth time) before he is granted access again."
 55: 0x00D8 [0x23] WAIT_FOR_DIALOG_INTERACTION
 56: 0x00D9 [0x48] [System] [8105*]:
    → "This not only pertains to the chamber previously visited, but all areas within the testing grounds."
 57: 0x00DC [0x23] WAIT_FOR_DIALOG_INTERACTION
 58: 0x00DD [0x48] [System] [8106*]:
    → "The amount of waiting time remaining before re-entry is permitted can be viewed by checking Hazhalm's Entry Gate."
 59: 0x00E0 [0x23] WAIT_FOR_DIALOG_INTERACTION
 60: 0x00E1 [0x01] GOTO 0x00FF
 61: 0x00E4 [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x00FF
 62: 0x00EC [0x48] [System] [8107*]:
    → "All monsters dwelling in the testing grounds can be attacked by anyone, regardless of party or alliance."
 63: 0x00EF [0x23] WAIT_FOR_DIALOG_INTERACTION
 64: 0x00F0 [0x48] [System] [8108*]:
    → "In addition, any items dropped by a foe can be lotted on by anyone in the chamber."
 65: 0x00F3 [0x23] WAIT_FOR_DIALOG_INTERACTION
 66: 0x00F4 [0x48] [System] [8109*]:
    → "However, please be aware that any items that have not been lotted on when a chamber's reservation is up will be distributed at random."
 67: 0x00F7 [0x23] WAIT_FOR_DIALOG_INTERACTION
 68: 0x00F8 [0x48] [System] [8111*]:
    → "Also, if everyone in a chamber remains KO'd for longer than $2 [minute/minutes], they will all be automatically teleported from the grounds."
 69: 0x00FB [0x23] WAIT_FOR_DIALOG_INTERACTION
 70: 0x00FC [0x01] GOTO 0x00FF

SUBROUTINE_00FF:
 71: 0x00FF [0x01] GOTO 0x000F
 72: 0x0102 [0x21] END_EVENT
 73: 0x0103 [0x00] END_REQSTACK()
```

### Event 19

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0104  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:             4D 00                                     M.          
```

#### Opcodes

```
  0: 0x0104 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x0105 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0106  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                   4C 00                                 L.        
```

#### Opcodes

```
  0: 0x0106 [0x4C] EventEntity->StatusEvent = 8 // Open door
  1: 0x0107 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0108  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                          4D 00                            M.      
```

#### Opcodes

```
  0: 0x0108 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x0109 [0x00] END_REQSTACK()
```
