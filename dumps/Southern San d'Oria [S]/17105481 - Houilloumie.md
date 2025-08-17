# 17105481 - Houilloumie

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Southern San d'Oria [S] (ID: 80) |
| Block Size       | 256 bytes                        |
| Total Events     | 7                                |
| References Count | 13                               |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [102](#event-102)     | 0x0001       |     17 |              7 |
| [103](#event-103)     | 0x0012       |     17 |              7 |
| [105](#event-105)     | 0x0023       |     21 |              9 |
| [104](#event-104)     | 0x0038       |    100 |             30 |
| [165](#event-165)     | 0x009C       |      1 |              1 |
| [170](#event-170)     | 0x009D       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2F6C      |       12140 |
|       1 | 0x2F69      |       12137 |
|       2 | 0x2F6F      |       12143 |
|       3 | 0x2F72      |       12146 |
|       4 | 0x2F75      |       12149 |
|       5 | 0x2F78      |       12152 |
|       6 | 0x0078      |         120 |
|       7 | 0x0001      |           1 |
|       8 | 0x2F7A      |       12154 |
|       9 | 0x2F7B      |       12155 |
|      10 | 0x0000      |           0 |
|      11 | 0x40000000  |  1073741824 |
|      12 | 0x2F7C      |       12156 |

## String References

- **12137**: If you seek admission to the Knights of the Iron Ram, speak with Sir Mainchelite.
- **12140**: For the lion!
- **12143**: I see you serve under another nation.
- **12146**: If you seek admission to the Knights of the Iron Ram, speak with Sir Mainchelite.
- **12149**: If you seek to regain admission to the Knights of the Iron Ram, you must first sever ties with your nation of allegiance...and that will require Allied Notes.
- **12152**: Please note that upon changing allegiance, you will be required to return the two most prestigious campaign medals you possess. There is no penalty if you have yet to earn any medals.
- **12154**: Exchange $2 Allied [Note/Notes] to transfer from [/the Knights of the Iron Ram/the Fourth Division/the Cobra Unit] to [/the Knights of the Iron Ram/the Fourth Division/the Cobra Unit]? You currently possess $3 [Allied Note/Allied Notes].
- **12155**: Proceed with the transaction? [Yes./No.]
- **12156**: Are you absolutely sure? [Yes./No.]

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

### Event 102

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 17 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 76  F8 FF FF 7F 1D 00 80 23   .....ov.......#
0010: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
  3: 0x000C [0x1D] PRINT_EVENT_MESSAGE(message_id=12140*)
    → "For the lion!"
  4: 0x000F [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0010 [0x21] END_EVENT
  6: 0x0011 [0x00] END_REQSTACK()
```

### Event 103

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0012   |
| Data Size    | 17 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:       1E F0 FF FF 7F 6F  76 F8 FF FF 7F 1D 01 80    .....ov.......
0020: 23 21 00                                          #!.             
```

#### Opcodes

```
  0: 0x0012 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0017 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0018 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
  3: 0x001D [0x1D] PRINT_EVENT_MESSAGE(message_id=12137*)
    → "If you seek admission to the Knights of the Iron Ram, speak with Sir Mainchelite."
  4: 0x0020 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0021 [0x21] END_EVENT
  6: 0x0022 [0x00] END_REQSTACK()
```

### Event 105

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0023   |
| Data Size    | 21 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:          1E F0 FF FF 7F  6F 76 F8 FF FF 7F 1D 02     .....ov......
0030: 80 23 1D 03 80 23 21 00                           .#...#!.        
```

#### Opcodes

```
  0: 0x0023 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0028 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0029 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
  3: 0x002E [0x1D] PRINT_EVENT_MESSAGE(message_id=12143*)
    → "I see you serve under another nation."
  4: 0x0031 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0032 [0x1D] PRINT_EVENT_MESSAGE(message_id=12146*)
    → "If you seek admission to the Knights of the Iron Ram, speak with Sir Mainchelite."
  6: 0x0035 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0036 [0x21] END_EVENT
  8: 0x0037 [0x00] END_REQSTACK()
```

### Event 104

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0038    |
| Data Size    | 100 bytes |
| Instructions | 28        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                          42 1E F0 FF FF 7F 6F 76          B.....ov
0040: F8 FF FF 7F 1D 02 80 23  1D 04 80 23 48 05 80 1C  .......#...#H...
0050: 06 80 03 01 10 07 80 43  00 43 01 48 08 80 23 24  .......C.C.H..#$
0060: 09 80 07 80 0A 80 25 02  00 10 07 80 00 7A 00 03  ......%......z..
0070: 01 10 0B 80 01 9A 00 01  7A 00 24 0C 80 07 80 0A  ........z.$.....
0080: 80 25 02 00 10 07 80 00  95 00 03 01 10 0B 80 01  .%..............
0090: 9A 00 01 95 00 03 01 10  07 80 21 00              ..........!.    
```

#### Opcodes

```
  0: 0x0038 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0039 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x003E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x003F [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
  4: 0x0044 [0x1D] PRINT_EVENT_MESSAGE(message_id=12143*)
    → "I see you serve under another nation."
  5: 0x0047 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0048 [0x1D] PRINT_EVENT_MESSAGE(message_id=12149*)
    → "If you seek to regain admission to the Knights of the Iron Ram, you must first sever ties with your nation of allegiance...and that will require Allied Notes."
  7: 0x004B [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x004C [0x48] [System] [12152*]:
    → "Please note that upon changing allegiance, you will be required to return the two most prestigious campaign medals you possess. There is no penalty if you have yet to earn any medals."
  9: 0x004F [0x1C] WAIT(120* ticks)
 10: 0x0052 [0x03] Work_Zone[1] = 1*
 11: 0x0057 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 12: 0x0059 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 13: 0x005B [0x48] [System] [12154*]:
    → "Exchange $2 Allied [Note/Notes] to transfer from [/the Knights of the Iron Ram/the Fourth Division/the Cobra Unit] to [/the Knights of the Iron Ram/the Fourth Division/the Cobra Unit]? You currently possess $3 [Allied Note/Allied Notes]."
 14: 0x005E [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x005F [0x24] CREATE_DIALOG(message_id=12155*, default_option=1*, option_flags=0*)
    → "Proceed with the transaction? [Yes./No.]"
 16: 0x0066 [0x25] WAIT_DIALOG_SELECT()
 17: 0x0067 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x007A
 18: 0x006F [0x03] Work_Zone[1] = 1073741824*
 19: 0x0074 [0x01] GOTO 0x009A

SUBROUTINE_007A:
 20: 0x007A [0x24] CREATE_DIALOG(message_id=12156*, default_option=1*, option_flags=0*)
    → "Are you absolutely sure? [Yes./No.]"
 21: 0x0081 [0x25] WAIT_DIALOG_SELECT()
 22: 0x0082 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0095
 23: 0x008A [0x03] Work_Zone[1] = 1073741824*
 24: 0x008F [0x01] GOTO 0x009A

SUBROUTINE_0095:
 25: 0x0095 [0x03] Work_Zone[1] = 1*

SUBROUTINE_009A:
 26: 0x009A [0x21] END_EVENT
 27: 0x009B [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0077 [0x01] GOTO 0x007A
# Dead code (unreachable instructions):
     0x0092 [0x01] GOTO 0x0095
```

### Event 165

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x009C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                      00                       .   
```

#### Opcodes

```
  0: 0x009C [0x00] END_REQSTACK()
```

### Event 170

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x009D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                         00                     .  
```

#### Opcodes

```
  0: 0x009D [0x00] END_REQSTACK()
```
