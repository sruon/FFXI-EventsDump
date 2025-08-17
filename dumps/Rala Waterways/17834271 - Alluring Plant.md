# 17834271 - Alluring Plant

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Rala Waterways (ID: 258) |
| Block Size       | 452 bytes                |
| Total Events     | 2                        |
| References Count | 20                       |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [322](#event-322)     | 0x0001       |    345 |             41 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00C8      |         200 |
|       1 | 0x0000      |           0 |
|       2 | 0x001B      |          27 |
|       3 | 0xFFFB1EA5  |  4294647461 |
|       4 | 0xFFFAF713  |  4294637331 |
|       5 | 0xFFFFFBE6  |  4294966246 |
|       6 | 0x0815      |        2069 |
|       7 | 0xFFFB18D7  |  4294645975 |
|       8 | 0xFFFB111E  |  4294643998 |
|       9 | 0xFFFFFC18  |  4294966296 |
|      10 | 0x0370      |         880 |
|      11 | 0x022E      |         558 |
|      12 | 0x000F      |          15 |
|      13 | 0x001E      |          30 |
|      14 | 0x0002      |           2 |
|      15 | 0x1EFA      |        7930 |
|      16 | 0x1EFB      |        7931 |
|      17 | 0x1EFC      |        7932 |
|      18 | 0x0028      |          40 |
|      19 | 0x1EFD      |        7933 |

## String References

- **7930**: The leaves of this plant are [bulky/thin/bulky] and its fruit is covered with a [hard/hard/soft] shell.
- **7931**: Pluck the fruit? [Yes./No.]

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

### Event 322

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 345 bytes |
| Instructions | 41        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 45 00 80 F0 FF FF  7F F0 FF FF 7F 66 64 6F   BE..........fdo
0010: 31 01 80 55 00 80 F0 FF  FF 7F F0 FF FF 7F 66 64  1..U..........fd
0020: 6F 31 46 01 38 02 80 92  01 40 21 10 01 BA F0 FF  o1F.8....@!.....
0030: FF 7F 03 80 04 80 05 80  06 80 BA 40 21 10 01 07  ...........@!...
0040: 80 08 80 09 80 0A 80 80  F0 FF FF 7F 80 40 21 10  .............@!.
0050: 01 45 0B 80 F0 FF FF 7F  F0 FF FF 7F 73 30 35 30  .E..........s050
0060: 01 80 1C 0C 80 45 00 80  F0 FF FF 7F F0 FF FF 7F  .....E..........
0070: 66 64 69 31 01 80 1C 0D  80 03 02 10 0E 80 48 0F  fdi1..........H.
0080: 80 23 24 10 80 01 80 01  80 25 02 00 10 01 80 00  .#$......%......
0090: 07 01 27 05 40 21 10 01  05 1C 0C 80 52 0B 80 F0  ..'.@!......R...
00A0: FF FF 7F F0 FF FF 7F 73  30 35 30 45 0B 80 F0 FF  .......s050E....
00B0: FF 7F F0 FF FF 7F 73 30  35 31 01 80 4A F0 FF FF  ......s051..J...
00C0: 7F 40 21 10 01 2B 40 21  10 01 11 80 23 52 0B 80  .@!..+@!....#R..
00D0: F0 FF FF 7F F0 FF FF 7F  73 30 35 31 45 0B 80 F0  ........s051E...
00E0: FF FF 7F F0 FF FF 7F 73  30 35 32 01 80 66 12 80  .......s052..f..
00F0: 40 21 10 01 40 21 10 01  74 6C 6B 30 2B 40 21 10  @!..@!..tlk0+@!.
0100: 01 13 80 23 01 07 01 45  00 80 F0 FF FF 7F F0 FF  ...#...E........
0110: FF 7F 66 64 6F 31 01 80  55 00 80 F0 FF FF 7F F0  ..fdo1..U.......
0120: FF FF 7F 66 64 6F 31 52  0B 80 F0 FF FF 7F F0 FF  ...fdo1R........
0130: FF 7F 73 30 35 30 52 0B  80 F0 FF FF 7F F0 FF FF  ..s050R.........
0140: 7F 73 30 35 32 46 00 45  00 80 F0 FF FF 7F F0 FF  .s052F.E........
0150: FF 7F 66 64 69 32 01 80  21 00                    ..fdi2..!.      
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  2: 0x0013 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
  3: 0x0022 [0x46] CAMERA_CONTROL: Disable user control
  4: 0x0024 [0x38] SET_CLIENT_EVENT_MODE(mode=27*)
  5: 0x0027 [0x92] Chalvava (ID: 17834304/0x01102140)->Render.Flags3 ^= 0x01
  6: 0x002D [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=-319.835*, pos_z=-329.965*, pos_y=-1.050*, direction=181.8°*)
  7: 0x003A [0xBA] SET_ENTITY_POSITION(entity_id=Chalvava (ID: 17834304/0x01102140), pos_x=-321.321*, pos_z=-323.298*, pos_y=-1.000*, direction=77.3°*)
  8: 0x0047 [0x80] LOAD_WAIT(entity=LocalPlayer)
  9: 0x004C [0x80] LOAD_WAIT(entity=Chalvava (ID: 17834304/0x01102140))
 10: 0x0051 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s050" with entities [LocalPlayer, LocalPlayer], work=[558*, 0*]
 11: 0x0062 [0x1C] WAIT(15* ticks)
 12: 0x0065 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 13: 0x0076 [0x1C] WAIT(30* ticks)
 14: 0x0079 [0x03] Work_Zone[2] = 2*
 15: 0x007E [0x48] [System] [7930*]:
    → "The leaves of this plant are [bulky/thin/bulky] and its fruit is covered with a [hard/hard/soft] shell."
 16: 0x0081 [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x0082 [0x24] CREATE_DIALOG(message_id=7931*, default_option=0*, option_flags=0*)
    → "Pluck the fruit? [Yes./No.]"
 18: 0x0089 [0x25] WAIT_DIALOG_SELECT()
 19: 0x008A [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0107
 20: 0x0092 [0x27] REQ_SET(priority=0x05, entity_id=Chalvava (ID: 17834304/0x01102140), tag_num=0x05)
 21: 0x0099 [0x1C] WAIT(15* ticks)
 22: 0x009C [0x52] END_LOAD_SCHEDULER: End scheduler "s050" with entities [LocalPlayer, LocalPlayer], work=558*
 23: 0x00AB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s051" with entities [LocalPlayer, LocalPlayer], work=[558*, 0*]
 24: 0x00BC [0x4A] LocalPlayer looks at Chalvava (ID: 17834304/0x01102140)
 25: 0x00C5 [0x2B] Chalvava (ID: 17834304/0x01102140) [7932*]:
    → "Just who do you think you are, messing with someone's vegetables?"
 26: 0x00CC [0x23] WAIT_FOR_DIALOG_INTERACTION
 27: 0x00CD [0x52] END_LOAD_SCHEDULER: End scheduler "s051" with entities [LocalPlayer, LocalPlayer], work=558*
 28: 0x00DC [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s052" with entities [LocalPlayer, LocalPlayer], work=[558*, 0*]
 29: 0x00ED [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Chalvava (ID: 17834304/0x01102140), Chalvava (ID: 17834304/0x01102140)], work=40*
 30: 0x00FC [0x2B] Chalvava (ID: 17834304/0x01102140) [7933*]:
    → "We've carefully grown them since they were mere seedlings! What gives you the right to lay so much as a finger on them?"
 31: 0x0103 [0x23] WAIT_FOR_DIALOG_INTERACTION
 32: 0x0104 [0x01] GOTO 0x0107

SUBROUTINE_0107:
 33: 0x0107 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 34: 0x0118 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 35: 0x0127 [0x52] END_LOAD_SCHEDULER: End scheduler "s050" with entities [LocalPlayer, LocalPlayer], work=558*
 36: 0x0136 [0x52] END_LOAD_SCHEDULER: End scheduler "s052" with entities [LocalPlayer, LocalPlayer], work=558*
 37: 0x0145 [0x46] CAMERA_CONTROL: Restore default settings
 38: 0x0147 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 39: 0x0158 [0x21] END_EVENT
 40: 0x0159 [0x00] END_REQSTACK()
```
