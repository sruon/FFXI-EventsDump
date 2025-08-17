# 17318613 - Secodiand

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Abyssea - La Theine (ID: 132) |
| Block Size       | 252 bytes                     |
| Total Events     | 4                             |
| References Count | 16                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |     11 |              3 |
| [161](#event-161)     | 0x000B       |     99 |             35 |
| [159](#event-159)     | 0x006E       |     13 |              7 |
| [160](#event-160)     | 0x007B       |     33 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0B4A      |        2890 |
|       1 | 0x0003      |           3 |
|       2 | 0x0000      |           0 |
|       3 | 0x1EE1      |        7905 |
|       4 | 0x1EE2      |        7906 |
|       5 | 0x1EE4      |        7908 |
|       6 | 0x1EE5      |        7909 |
|       7 | 0x1EE6      |        7910 |
|       8 | 0x0001      |           1 |
|       9 | 0x1EE7      |        7911 |
|      10 | 0x1EE8      |        7912 |
|      11 | 0x1EEB      |        7915 |
|      12 | 0x1EEC      |        7916 |
|      13 | 0x1EE9      |        7913 |
|      14 | 0x1EEA      |        7914 |
|      15 | 0x00C9      |         201 |

## String References

- **7905**: There's something foul in the air of late. Can you not feel it? Dark times have befallen us, yes, but this is something else altogether. This is...the "true darkness."
- **7906**: Could it be that I am the only soul who senses this wickedness...?
- **7908**: Such a charm would need to be made of $1 $0 ...
- **7909**: Might you bring me the materials I require?
- **7910**: Will you gather the materials? [As well as some for myself!/I don't think so...]
- **7911**: I am in your debt! I must have them to ward away the darkness... Remember, I need $1 $0 !
- **7912**: You do not share my fear... While we stand here debating, the true darkness creeps ever closer! I must do something!
- **7913**: My charm requires $1 $0 ... Make haste!
- **7914**: Thank you! This should hold the darkness at bay...if only for a while. Bring more, if you can.
- **7915**: I must have more charms! Please, bring me sets of $1 $0 !
- **7916**: I promise you shall not leave empty-handed!

## Events

### Event 65535

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0000   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 03 02 10 00 80 03 03 10  01 80 00                 ...........     
```

#### Opcodes

```
  0: 0x0000 [0x03] Work_Zone[2] = 2890*
  1: 0x0005 [0x03] Work_Zone[3] = 3*
  2: 0x000A [0x00] END_REQSTACK()
```

### Event 161

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000B   |
| Data Size    | 99 bytes |
| Instructions | 35       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   20 01 42 03 00              .B..
0010: 00 09 10 06 01 10 1E F0  FF FF 7F 6F 70 02 00 00  ...........op...
0020: 02 80 00 64 00 1D 03 80  23 1D 04 80 23 1D 05 80  ...d....#...#...
0030: 23 1D 06 80 23 24 07 80  08 80 02 80 25 02 00 10  #...#$......%...
0040: 02 80 00 52 00 42 1D 09  80 23 03 01 10 08 80 01  ...R.B...#......
0050: 61 00 02 00 10 08 80 00  61 00 1D 0A 80 23 01 61  a.......a....#.a
0060: 00 01 6C 00 1D 0B 80 23  1D 0C 80 23 21 00        ..l....#...#!.  
```

#### Opcodes

```
  0: 0x000B [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x000D [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x000E [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[9]
  3: 0x0013 [0x06] Work_Zone[1] = 0
  4: 0x0016 [0x1E] EventEntity looks at LocalPlayer and starts talking
  5: 0x001B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x001C [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  7: 0x001D [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x0064
  8: 0x0025 [0x1D] PRINT_EVENT_MESSAGE(message_id=7905*)
    → "There's something foul in the air of late. Can you not feel it? Dark times have befallen us, yes, but this is something else altogether. This is...the "true darkness.""
  9: 0x0028 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0029 [0x1D] PRINT_EVENT_MESSAGE(message_id=7906*)
    → "Could it be that I am the only soul who senses this wickedness...?"
 11: 0x002C [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x002D [0x1D] PRINT_EVENT_MESSAGE(message_id=7908*)
    → "Such a charm would need to be made of $1 $0 ..."
 13: 0x0030 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x0031 [0x1D] PRINT_EVENT_MESSAGE(message_id=7909*)
    → "Might you bring me the materials I require?"
 15: 0x0034 [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x0035 [0x24] CREATE_DIALOG(message_id=7910*, default_option=1*, option_flags=0*)
    → "Will you gather the materials? [As well as some for myself!/I don't think so...]"
 17: 0x003C [0x25] WAIT_DIALOG_SELECT()
 18: 0x003D [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0052
 19: 0x0045 [0x42] SET_CLI_EVENT_CANCEL_DATA()
 20: 0x0046 [0x1D] PRINT_EVENT_MESSAGE(message_id=7911*)
    → "I am in your debt! I must have them to ward away the darkness... Remember, I need $1 $0 !"
 21: 0x0049 [0x23] WAIT_FOR_DIALOG_INTERACTION
 22: 0x004A [0x03] Work_Zone[1] = 1*
 23: 0x004F [0x01] GOTO 0x0061
 24: 0x0052 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0061
 25: 0x005A [0x1D] PRINT_EVENT_MESSAGE(message_id=7912*)
    → "You do not share my fear... While we stand here debating, the true darkness creeps ever closer! I must do something!"
 26: 0x005D [0x23] WAIT_FOR_DIALOG_INTERACTION
 27: 0x005E [0x01] GOTO 0x0061

SUBROUTINE_0061:
 28: 0x0061 [0x01] GOTO 0x006C
 29: 0x0064 [0x1D] PRINT_EVENT_MESSAGE(message_id=7915*)
    → "I must have more charms! Please, bring me sets of $1 $0 !"
 30: 0x0067 [0x23] WAIT_FOR_DIALOG_INTERACTION
 31: 0x0068 [0x1D] PRINT_EVENT_MESSAGE(message_id=7916*)
    → "I promise you shall not leave empty-handed!"
 32: 0x006B [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_006C:
 33: 0x006C [0x21] END_EVENT
 34: 0x006D [0x00] END_REQSTACK()
```

### Event 159

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006E   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                            1E F0                ..
0070: FF FF 7F 6F 70 1D 0D 80  23 21 00                 ...op...#!.     
```

#### Opcodes

```
  0: 0x006E [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0073 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0074 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0075 [0x1D] PRINT_EVENT_MESSAGE(message_id=7913*)
    → "My charm requires $1 $0 ... Make haste!"
  4: 0x0078 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0079 [0x21] END_EVENT
  6: 0x007A [0x00] END_REQSTACK()
```

### Event 160

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007B   |
| Data Size    | 33 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                   20 01 42 1E F0              .B..
0080: FF FF 7F 6F 70 1D 0E 80  23 45 0F 80 F0 FF FF 7F  ...op...#E......
0090: F0 FF FF 7F 71 73 74 63  02 80 21 00              ....qstc..!.    
```

#### Opcodes

```
  0: 0x007B [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x007D [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x007E [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x0083 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0084 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  5: 0x0085 [0x1D] PRINT_EVENT_MESSAGE(message_id=7914*)
    → "Thank you! This should hold the darkness at bay...if only for a while. Bring more, if you can."
  6: 0x0088 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0089 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
  8: 0x009A [0x21] END_EVENT
  9: 0x009B [0x00] END_REQSTACK()
```
