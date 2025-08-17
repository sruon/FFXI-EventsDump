# 17162849 - Mhoti Pyiahrs

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Windurst Waters [S] (ID: 94) |
| Block Size       | 352 bytes                    |
| Total Events     | 17                           |
| References Count | 13                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [2](#event-2)         | 0x0001       |     17 |              7 |
| [3](#event-3)         | 0x0012       |     17 |              7 |
| [5](#event-5)         | 0x0023       |     21 |              9 |
| [4](#event-4)         | 0x0038       |    100 |             30 |
| [128](#event-128)     | 0x009C       |      7 |              2 |
| [129](#event-129)     | 0x00A3       |      7 |              2 |
| [133](#event-133)     | 0x00AA       |      7 |              2 |
| [134](#event-134)     | 0x00B1       |      7 |              2 |
| [103](#event-103)     | 0x00B8       |      7 |              2 |
| [106](#event-106)     | 0x00BF       |      7 |              2 |
| [168](#event-168)     | 0x00C6       |      7 |              2 |
| [158](#event-158)     | 0x00CD       |      7 |              2 |
| [31](#event-31)       | 0x00D4       |      1 |              1 |
| [32](#event-32)       | 0x00D5       |      1 |              1 |
| [42](#event-42)       | 0x00D6       |      1 |              1 |
| [43](#event-43)       | 0x00D7       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2DE5      |       11749 |
|       1 | 0x2DE2      |       11746 |
|       2 | 0x2DE8      |       11752 |
|       3 | 0x2DEB      |       11755 |
|       4 | 0x2DEE      |       11758 |
|       5 | 0x2DEF      |       11759 |
|       6 | 0x0078      |         120 |
|       7 | 0x0001      |           1 |
|       8 | 0x2DF1      |       11761 |
|       9 | 0x2DF2      |       11762 |
|      10 | 0x0000      |           0 |
|      11 | 0x40000000  |  1073741824 |
|      12 | 0x2DF3      |       11763 |

## String References

- **11746**: So you think you have what it takes to be a Cobra? Well, then talk to Miah Riyuh and hope that she's in a good mood!
- **11749**: Shouldn't you be out campaigning? Now get!
- **11752**: Says here you've already gone and joined some other nation's forces.
- **11755**: If you've finally come to your senses and decided on joining the Cobras then talk to Miah Riyuh...and hope that she's in a good mood!
- **11758**: But if you've finally come to your senses and decided to return to the Cobras, I think I can pull a few strings...for a price. You're carrying Allied Notes, right?
- **11759**: Please note that upon changing allegiance, you will be required to return the two most prestigious campaign medals you possess. There is no penalty if you have yet to earn any medals.
- **11761**: Exchange $2 Allied [Note/Notes] to transfer from [/the Knights of the Iron Ram/the Fourth Division/the Cobra Unit] to [/the Knights of the Iron Ram/the Fourth Division/the Cobra Unit]? You currently possess $3 [Allied Note/Allied Notes].
- **11762**: Proceed with the transaction? [Yes./No.]
- **11763**: Are you absolutely sure? [Yes./No.]

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
  3: 0x000C [0x1D] PRINT_EVENT_MESSAGE(message_id=11749*)
    → "Shouldn't you be out campaigning? Now get!"
  4: 0x000F [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0010 [0x21] END_EVENT
  6: 0x0011 [0x00] END_REQSTACK()
```

### Event 3

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
  3: 0x001D [0x1D] PRINT_EVENT_MESSAGE(message_id=11746*)
    → "So you think you have what it takes to be a Cobra? Well, then talk to Miah Riyuh and hope that she's in a good mood!"
  4: 0x0020 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0021 [0x21] END_EVENT
  6: 0x0022 [0x00] END_REQSTACK()
```

### Event 5

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
  3: 0x002E [0x1D] PRINT_EVENT_MESSAGE(message_id=11752*)
    → "Says here you've already gone and joined some other nation's forces."
  4: 0x0031 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0032 [0x1D] PRINT_EVENT_MESSAGE(message_id=11755*)
    → "If you've finally come to your senses and decided on joining the Cobras then talk to Miah Riyuh...and hope that she's in a good mood!"
  6: 0x0035 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0036 [0x21] END_EVENT
  8: 0x0037 [0x00] END_REQSTACK()
```

### Event 4

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
  4: 0x0044 [0x1D] PRINT_EVENT_MESSAGE(message_id=11752*)
    → "Says here you've already gone and joined some other nation's forces."
  5: 0x0047 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0048 [0x1D] PRINT_EVENT_MESSAGE(message_id=11758*)
    → "But if you've finally come to your senses and decided to return to the Cobras, I think I can pull a few strings...for a price. You're carrying Allied Notes, right?"
  7: 0x004B [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x004C [0x48] [System] [11759*]:
    → "Please note that upon changing allegiance, you will be required to return the two most prestigious campaign medals you possess. There is no penalty if you have yet to earn any medals."
  9: 0x004F [0x1C] WAIT(120* ticks)
 10: 0x0052 [0x03] Work_Zone[1] = 1*
 11: 0x0057 [0x43] SEND_EVENT_UPDATE: Send pending tag to server (packet 0x005B)
 12: 0x0059 [0x43] SEND_EVENT_UPDATE: Check pending flag (skip if not pending)
 13: 0x005B [0x48] [System] [11761*]:
    → "Exchange $2 Allied [Note/Notes] to transfer from [/the Knights of the Iron Ram/the Fourth Division/the Cobra Unit] to [/the Knights of the Iron Ram/the Fourth Division/the Cobra Unit]? You currently possess $3 [Allied Note/Allied Notes]."
 14: 0x005E [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x005F [0x24] CREATE_DIALOG(message_id=11762*, default_option=1*, option_flags=0*)
    → "Proceed with the transaction? [Yes./No.]"
 16: 0x0066 [0x25] WAIT_DIALOG_SELECT()
 17: 0x0067 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x007A
 18: 0x006F [0x03] Work_Zone[1] = 1073741824*
 19: 0x0074 [0x01] GOTO 0x009A

SUBROUTINE_007A:
 20: 0x007A [0x24] CREATE_DIALOG(message_id=11763*, default_option=1*, option_flags=0*)
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

### Event 128

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x009C  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                      92 01 F8 FF              ....
00A0: FF 7F 00                                          ...             
```

#### Opcodes

```
  0: 0x009C [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00A2 [0x00] END_REQSTACK()
```

### Event 129

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A3  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:          92 01 F8 FF FF  7F 00                       .......      
```

#### Opcodes

```
  0: 0x00A3 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00A9 [0x00] END_REQSTACK()
```

### Event 133

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00AA  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                92 01 F8 FF FF 7F            ......
00B0: 00                                                .               
```

#### Opcodes

```
  0: 0x00AA [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00B0 [0x00] END_REQSTACK()
```

### Event 134

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00B1  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:    92 01 F8 FF FF 7F 00                            .......        
```

#### Opcodes

```
  0: 0x00B1 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00B7 [0x00] END_REQSTACK()
```

### Event 103

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00B8  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                          92 01 F8 FF FF 7F 00             ....... 
```

#### Opcodes

```
  0: 0x00B8 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00BE [0x00] END_REQSTACK()
```

### Event 106

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00BF  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                               92                 .
00C0: 01 F8 FF FF 7F 00                                 ......          
```

#### Opcodes

```
  0: 0x00BF [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00C5 [0x00] END_REQSTACK()
```

### Event 168

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00C6  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                   92 01  F8 FF FF 7F 00                 .......   
```

#### Opcodes

```
  0: 0x00C6 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00CC [0x00] END_REQSTACK()
```

### Event 158

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00CD  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                         92 01 F8               ...
00D0: FF FF 7F 00                                       ....            
```

#### Opcodes

```
  0: 0x00CD [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00D3 [0x00] END_REQSTACK()
```

### Event 31

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00D4  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:             00                                        .           
```

#### Opcodes

```
  0: 0x00D4 [0x00] END_REQSTACK()
```

### Event 32

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00D5  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                00                                      .          
```

#### Opcodes

```
  0: 0x00D5 [0x00] END_REQSTACK()
```

### Event 42

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00D6  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                   00                                    .         
```

#### Opcodes

```
  0: 0x00D6 [0x00] END_REQSTACK()
```

### Event 43

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00D7  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                      00                                  .        
```

#### Opcodes

```
  0: 0x00D7 [0x00] END_REQSTACK()
```
