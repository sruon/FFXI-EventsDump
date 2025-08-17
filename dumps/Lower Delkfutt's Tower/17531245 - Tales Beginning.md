# 17531245 - Tales Beginning

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Lower Delkfutt's Tower (ID: 184) |
| Block Size       | 296 bytes                        |
| Total Events     | 2                                |
| References Count | 12                               |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [53](#event-53)       | 0x0001       |    222 |             47 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x0007      |           7 |
|       2 | 0x2E6A      |       11882 |
|       3 | 0x2E6B      |       11883 |
|       4 | 0x0000      |           0 |
|       5 | 0x2E68      |       11880 |
|       6 | 0x2E69      |       11881 |
|       7 | 0x0002      |           2 |
|       8 | 0x0003      |           3 |
|       9 | 0x0004      |           4 |
|      10 | 0x0005      |           5 |
|      11 | 0x0006      |           6 |

## String References

- **11880**: Would you like to start a new storyline that you previously postponed?
- **11881**: Start which? [None for now./Rise of the Zilart./A Crystallinbe Prophecy./A Shantotto Ascension./Chains of Promathia./Abyssea./Seekers of Adoulin./Rhapsodies of Vana'diel.]
- **11882**: Start the previously postponed storyline [Rise of the Zilart/A Crystalline Prophecy/A Shantotto Ascenaion/Chains of Promthia/Abyssea/Seekers of Adoulin/Rhapsodies of Vana'diel]?
- **11883**: Start the storyline? [Yes, please./No, thank you.]

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

### Event 53

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 222 bytes |
| Instructions | 47        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    03 00 00 02 10 07 00  00 00 80 02 00 00 01 80   ...............
0010: 02 18 00 03 00 00 01 80  02 03 10 00 80 03 4F 00  ..............O.
0020: 48 02 80 23 24 03 80 00  80 04 80 25 02 00 10 04  H..#$......%....
0030: 80 00 3C 00 03 01 10 00  00 01 4C 00 02 00 10 00  ..<.......L.....
0040: 80 00 4C 00 03 01 10 04  80 01 4C 00 01 DB 00 48  ..L.......L....H
0050: 05 80 23 24 06 80 04 80  03 10 25 02 00 10 04 80  ..#$......%.....
0060: 00 6B 00 03 01 10 04 80  01 DB 00 02 00 10 00 80  .k..............
0070: 00 7B 00 03 01 10 00 80  01 DB 00 02 00 10 07 80  .{..............
0080: 00 8B 00 03 01 10 07 80  01 DB 00 02 00 10 08 80  ................
0090: 00 9B 00 03 01 10 08 80  01 DB 00 02 00 10 09 80  ................
00A0: 00 AB 00 03 01 10 09 80  01 DB 00 02 00 10 0A 80  ................
00B0: 00 BB 00 03 01 10 0A 80  01 DB 00 02 00 10 0B 80  ................
00C0: 00 CB 00 03 01 10 0B 80  01 DB 00 02 00 10 01 80  ................
00D0: 00 DB 00 03 01 10 01 80  01 DB 00 20 00 21 00     ........... .!. 
```

#### Opcodes

```
  0: 0x0001 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  1: 0x0006 [0x07] ExtData[1]->WorkLocal[0] += 1*
  2: 0x000B [0x02] IF !(ExtData[1]->WorkLocal[0] <= 7*) GOTO 0x0018
  3: 0x0013 [0x03] ExtData[1]->WorkLocal[0] = 7*
  4: 0x0018 [0x02] IF !(Work_Zone[3] >= 1*) GOTO 0x004F
  5: 0x0020 [0x48] [System] [11882*]:
    → "Start the previously postponed storyline [Rise of the Zilart/A Crystalline Prophecy/A Shantotto Ascenaion/Chains of Promthia/Abyssea/Seekers of Adoulin/Rhapsodies of Vana'diel]?"
  6: 0x0023 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0024 [0x24] CREATE_DIALOG(message_id=11883*, default_option=1*, option_flags=0*)
    → "Start the storyline? [Yes, please./No, thank you.]"
  8: 0x002B [0x25] WAIT_DIALOG_SELECT()
  9: 0x002C [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x003C
 10: 0x0034 [0x03] Work_Zone[1] = ExtData[1]->WorkLocal[0]
 11: 0x0039 [0x01] GOTO 0x004C
 12: 0x003C [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x004C
 13: 0x0044 [0x03] Work_Zone[1] = 0*
 14: 0x0049 [0x01] GOTO 0x004C

SUBROUTINE_004C:
 15: 0x004C [0x01] GOTO 0x00DB
 16: 0x004F [0x48] [System] [11880*]:
    → "Would you like to start a new storyline that you previously postponed?"
 17: 0x0052 [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x0053 [0x24] CREATE_DIALOG(message_id=11881*, default_option=0*, option_flags=Work_Zone[3])
    → "Start which? [None for now./Rise of the Zilart./A Crystallinbe Prophecy./A Shantotto Ascension./Chains of Promathia./Abyssea./Seekers of Adoulin./Rhapsodies of Vana'diel.]"
 19: 0x005A [0x25] WAIT_DIALOG_SELECT()
 20: 0x005B [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x006B
 21: 0x0063 [0x03] Work_Zone[1] = 0*
 22: 0x0068 [0x01] GOTO 0x00DB
 23: 0x006B [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x007B
 24: 0x0073 [0x03] Work_Zone[1] = 1*
 25: 0x0078 [0x01] GOTO 0x00DB
 26: 0x007B [0x02] IF !(Work_Zone[0] == 2*) GOTO 0x008B
 27: 0x0083 [0x03] Work_Zone[1] = 2*
 28: 0x0088 [0x01] GOTO 0x00DB
 29: 0x008B [0x02] IF !(Work_Zone[0] == 3*) GOTO 0x009B
 30: 0x0093 [0x03] Work_Zone[1] = 3*
 31: 0x0098 [0x01] GOTO 0x00DB
 32: 0x009B [0x02] IF !(Work_Zone[0] == 4*) GOTO 0x00AB
 33: 0x00A3 [0x03] Work_Zone[1] = 4*
 34: 0x00A8 [0x01] GOTO 0x00DB
 35: 0x00AB [0x02] IF !(Work_Zone[0] == 5*) GOTO 0x00BB
 36: 0x00B3 [0x03] Work_Zone[1] = 5*
 37: 0x00B8 [0x01] GOTO 0x00DB
 38: 0x00BB [0x02] IF !(Work_Zone[0] == 6*) GOTO 0x00CB
 39: 0x00C3 [0x03] Work_Zone[1] = 6*
 40: 0x00C8 [0x01] GOTO 0x00DB
 41: 0x00CB [0x02] IF !(Work_Zone[0] == 7*) GOTO 0x00DB
 42: 0x00D3 [0x03] Work_Zone[1] = 7*
 43: 0x00D8 [0x01] GOTO 0x00DB

SUBROUTINE_00DB:
 44: 0x00DB [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 45: 0x00DD [0x21] END_EVENT
 46: 0x00DE [0x00] END_REQSTACK()
```
