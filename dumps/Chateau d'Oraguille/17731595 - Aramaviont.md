# 17731595 - Aramaviont

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Chateau d'Oraguille (ID: 233) |
| Block Size       | 660 bytes                     |
| Total Events     | 25                            |
| References Count | 26                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [11](#event-11)          | 0x0001       |     13 |              7 |
| [14](#event-14)          | 0x000E       |     13 |              7 |
| [13](#event-13)          | 0x001B       |     13 |              7 |
| [15](#event-15)          | 0x0028       |     13 |              7 |
| [12](#event-12)          | 0x0035       |     13 |              7 |
| [9](#event-9)            | 0x0042       |      1 |              1 |
| [65535.1](#event-655351) | 0x0043       |     10 |              2 |
| [518](#event-518)        | 0x004D       |     43 |             13 |
| [89](#event-89)          | 0x0078       |     18 |              4 |
| [65535.2](#event-655352) | 0x008A       |     90 |             17 |
| [65535.3](#event-655353) | 0x00E4       |     87 |             16 |
| [121](#event-121)        | 0x013B       |      1 |              1 |
| [120](#event-120)        | 0x013C       |      1 |              1 |
| [65535.4](#event-655354) | 0x013D       |     40 |              5 |
| [65535.5](#event-655355) | 0x0165       |     16 |              2 |
| [65535.6](#event-655356) | 0x0175       |     10 |              2 |
| [65535.7](#event-655357) | 0x017F       |     16 |              2 |
| [65535.8](#event-655358) | 0x018F       |     34 |              8 |
| [579](#event-579)        | 0x01B1       |      1 |              1 |
| [580](#event-580)        | 0x01B2       |      1 |              1 |
| [597](#event-597)        | 0x01B3       |      1 |              1 |
| [598](#event-598)        | 0x01B4       |      1 |              1 |
| [605](#event-605)        | 0x01B5       |      1 |              1 |
| [606](#event-606)        | 0x01B6       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1EC9      |        7881 |
|       1 | 0x1EC8      |        7880 |
|       2 | 0x1EC7      |        7879 |
|       3 | 0x1EC6      |        7878 |
|       4 | 0x1EC5      |        7877 |
|       5 | 0xFFFFF52E  |  4294964526 |
|       6 | 0xFFFFF5FC  |  4294964732 |
|       7 | 0x0000      |           0 |
|       8 | 0x0014      |          20 |
|       9 | 0x1C2E      |        7214 |
|      10 | 0x001E      |          30 |
|      11 | 0x1C2F      |        7215 |
|      12 | 0xFFFF7190  |  4294930832 |
|      13 | 0x1410E     |       82190 |
|      14 | 0xFFFFF14C  |  4294963532 |
|      15 | 0x07C4      |        1988 |
|      16 | 0x000D      |          13 |
|      17 | 0x0001      |           1 |
|      18 | 0xFFFF9130  |  4294938928 |
|      19 | 0xFFFFE829  |  4294961193 |
|      20 | 0x0F44      |        3908 |
|      21 | 0x001A      |          26 |
|      22 | 0x0C0F      |        3087 |
|      23 | 0xFFFF970B  |  4294940427 |
|      24 | 0xFFFFE87B  |  4294961275 |
|      25 | 0x001D      |          29 |

## String References

- **7214**: Royal Knight Aramaviont reporting! I've returned from Windurst. Maybe it's just me, but the wee folk there are hiding something, I know it!
- **7215**: Why else would they let Yagudo run wild over the countryside? I'd lock those nasty feathered fowl up in cages if I were them!
- **7877**: The defeat of the Shadow Lord should improve the situation in the Northlands and improve our odds in the war with the Orcs.
- **7878**: There's not a knight in San d'Oria that doesn't wish to take Lightbringer in his hands. However, there are still many mysteries that surround it...
- **7879**: It's now time to show those Orcs the true force of the Royal Knights. The battle will go down in history as the day we put an end to their fiendish plots!
- **7880**: When I was in the Northlands, I didn't know if I would ever be back here, sipping tea in the comforts of my quarters. I raise my glass to my colleagues who were not as fortunate...
- **7881**: I never knew His Highness felt that way about the Kingdom... To put the stability of the country ahead of bloodlines and tradition...the royaulais is truly a great leader.

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

### Event 11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  1D 00 80 23 21 00         .....op...#!.  
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x1D] PRINT_EVENT_MESSAGE(message_id=7881*)
    → "I never knew His Highness felt that way about the Kingdom... To put the stability of the country ahead of bloodlines and tradition...the royaulais is truly a great leader."
  4: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000C [0x21] END_EVENT
  6: 0x000D [0x00] END_REQSTACK()
```

### Event 14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000E   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            1E F0                ..
0010: FF FF 7F 6F 70 1D 01 80  23 21 00                 ...op...#!.     
```

#### Opcodes

```
  0: 0x000E [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0013 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0014 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0015 [0x1D] PRINT_EVENT_MESSAGE(message_id=7880*)
    → "When I was in the Northlands, I didn't know if I would ever be back here, sipping tea in the comforts of my quarters. I raise my glass to my colleagues who were not as fortunate..."
  4: 0x0018 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0019 [0x21] END_EVENT
  6: 0x001A [0x00] END_REQSTACK()
```

### Event 13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001B   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                   1E F0 FF FF 7F             .....
0020: 6F 70 1D 02 80 23 21 00                           op...#!.        
```

#### Opcodes

```
  0: 0x001B [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0020 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0021 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0022 [0x1D] PRINT_EVENT_MESSAGE(message_id=7879*)
    → "It's now time to show those Orcs the true force of the Royal Knights. The battle will go down in history as the day we put an end to their fiendish plots!"
  4: 0x0025 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0026 [0x21] END_EVENT
  6: 0x0027 [0x00] END_REQSTACK()
```

### Event 15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0028   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                          1E F0 FF FF 7F 6F 70 1D          .....op.
0030: 03 80 23 21 00                                    ..#!.           
```

#### Opcodes

```
  0: 0x0028 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x002D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x002E [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x002F [0x1D] PRINT_EVENT_MESSAGE(message_id=7878*)
    → "There's not a knight in San d'Oria that doesn't wish to take Lightbringer in his hands. However, there are still many mysteries that surround it..."
  4: 0x0032 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0033 [0x21] END_EVENT
  6: 0x0034 [0x00] END_REQSTACK()
```

### Event 12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0035   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                1E F0 FF  FF 7F 6F 70 1D 04 80 23       .....op...#
0040: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0035 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x003A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x003B [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x003C [0x1D] PRINT_EVENT_MESSAGE(message_id=7877*)
    → "The defeat of the Shadow Lord should improve the situation in the Northlands and improve our odds in the war with the Orcs."
  4: 0x003F [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0040 [0x21] END_EVENT
  6: 0x0041 [0x00] END_REQSTACK()
```

### Event 9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0042  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:       00                                            .             
```

#### Opcodes

```
  0: 0x0042 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0043   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:          37 05 80 06 80  07 80 07 80 00              7.........   
```

#### Opcodes

```
  0: 0x0043 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-2.770*, z=-2.564*, y=0.000*, direction=0.0°*
  1: 0x004C [0x00] END_REQSTACK()
```

### Event 518

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004D   |
| Data Size    | 43 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         1E F0 FF               ...
0050: FF 7F 6F 70 66 08 80 F8  FF FF 7F F8 FF FF 7F 74  ..opf..........t
0060: 6C 6B 30 1D 09 80 23 1C  0A 80 1D 0B 80 23 5E 69  lk0...#......#^i
0070: 64 6C 30 1C 0A 80 21 00                           dl0...!.        
```

#### Opcodes

```
  0: 0x004D [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0052 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0053 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0054 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  4: 0x0063 [0x1D] PRINT_EVENT_MESSAGE(message_id=7214*)
    → "Royal Knight Aramaviont reporting! I've returned from Windurst. Maybe it's just me, but the wee folk there are hiding something, I know it!"
  5: 0x0066 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0067 [0x1C] WAIT(30* ticks)
  7: 0x006A [0x1D] PRINT_EVENT_MESSAGE(message_id=7215*)
    → "Why else would they let Yagudo run wild over the countryside? I'd lock those nasty feathered fowl up in cages if I were them!"
  8: 0x006D [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x006E [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 10: 0x0073 [0x1C] WAIT(30* ticks)
 11: 0x0076 [0x21] END_EVENT
 12: 0x0077 [0x00] END_REQSTACK()
```

### Event 89

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0078   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                          22 01 92 01 F8 FF FF 7F          ".......
0080: 37 0C 80 0D 80 0E 80 0F  80 00                    7.........      
```

#### Opcodes

```
  0: 0x0078 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x007A [0x92] EventEntity->Render.Flags3 ^= 0x01
  2: 0x0080 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-36.464*, z=82.190*, y=-3.764*, direction=174.7°*
  3: 0x0089 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008A   |
| Data Size    | 90 bytes |
| Instructions | 17       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                6E F8 FF FF 7F 10            n.....
0090: 80 99 F8 FF FF 7F 06 04  00 3B F8 FF FF 7F 00 00  .........;......
00A0: 02 00 03 00 3B 34 90 0E  01 00 00 01 00 03 00 02  ....;4..........
00B0: 01 00 02 00 03 C8 00 3B  34 90 0E 01 00 00 01 00  .......;4.......
00C0: 03 00 1C 11 80 01 AF 00  5E 69 64 6C 30 1C 0A 80  ........^idl0...
00D0: 1E 34 90 0E 01 6F 70 6E  F8 FF FF 7F 10 80 99 F8  .4...opn........
00E0: FF FF 7F 00                                       ....            
```

#### Opcodes

```
  0: 0x008A [0x6E] EventEntity uses emote 13*
  1: 0x0091 [0x99] Wait for EventEntity animation to complete
  2: 0x0096 [0x06] ExtData[1]->WorkLocal[4] = 0
  3: 0x0099 [0x3B] GET_ENTITY_POSITION(entity=EventEntity, x_destination=ExtData[1]->WorkLocal[0], y_destination=ExtData[1]->WorkLocal[2], z_destination=ExtData[1]->WorkLocal[3])
  4: 0x00A4 [0x3B] GET_ENTITY_POSITION(entity=Exoroche (ID: 17731636/0x010E9034), x_destination=ExtData[1]->WorkLocal[0], y_destination=ExtData[1]->WorkLocal[1], z_destination=ExtData[1]->WorkLocal[3])
  5: 0x00AF [0x02] IF !(ExtData[1]->WorkLocal[1] >= ExtData[1]->WorkLocal[2]) GOTO 0x00C8
  6: 0x00B7 [0x3B] GET_ENTITY_POSITION(entity=Exoroche (ID: 17731636/0x010E9034), x_destination=ExtData[1]->WorkLocal[0], y_destination=ExtData[1]->WorkLocal[1], z_destination=ExtData[1]->WorkLocal[3])
  7: 0x00C2 [0x1C] WAIT(1* ticks)
  8: 0x00C5 [0x01] GOTO 0x00AF
  9: 0x00C8 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 10: 0x00CD [0x1C] WAIT(30* ticks)
 11: 0x00D0 [0x1E] EventEntity looks at Exoroche (ID: 17731636/0x010E9034) and starts talking
 12: 0x00D5 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 13: 0x00D6 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 14: 0x00D7 [0x6E] EventEntity uses emote 13*
 15: 0x00DE [0x99] Wait for EventEntity animation to complete
 16: 0x00E3 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E4   |
| Data Size    | 87 bytes |
| Instructions | 16       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:             6E F8 FF FF  7F 10 80 99 F8 FF FF 7F      n...........
00F0: 3B F8 FF FF 7F 00 00 02  00 03 00 3B 34 90 0E 01  ;..........;4...
0100: 00 00 01 00 03 00 02 01  00 02 00 02 1F 01 3B 34  ..............;4
0110: 90 0E 01 00 00 01 00 03  00 1C 11 80 01 06 01 5E  ...............^
0120: 69 64 6C 30 1C 0A 80 1E  34 90 0E 01 6F 70 6E F8  idl0....4...opn.
0130: FF FF 7F 10 80 99 F8 FF  FF 7F 00                 ...........     
```

#### Opcodes

```
  0: 0x00E4 [0x6E] EventEntity uses emote 13*
  1: 0x00EB [0x99] Wait for EventEntity animation to complete
  2: 0x00F0 [0x3B] GET_ENTITY_POSITION(entity=EventEntity, x_destination=ExtData[1]->WorkLocal[0], y_destination=ExtData[1]->WorkLocal[2], z_destination=ExtData[1]->WorkLocal[3])
  3: 0x00FB [0x3B] GET_ENTITY_POSITION(entity=Exoroche (ID: 17731636/0x010E9034), x_destination=ExtData[1]->WorkLocal[0], y_destination=ExtData[1]->WorkLocal[1], z_destination=ExtData[1]->WorkLocal[3])
  4: 0x0106 [0x02] IF !(ExtData[1]->WorkLocal[1] <= ExtData[1]->WorkLocal[2]) GOTO 0x011F
  5: 0x010E [0x3B] GET_ENTITY_POSITION(entity=Exoroche (ID: 17731636/0x010E9034), x_destination=ExtData[1]->WorkLocal[0], y_destination=ExtData[1]->WorkLocal[1], z_destination=ExtData[1]->WorkLocal[3])
  6: 0x0119 [0x1C] WAIT(1* ticks)
  7: 0x011C [0x01] GOTO 0x0106
  8: 0x011F [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  9: 0x0124 [0x1C] WAIT(30* ticks)
 10: 0x0127 [0x1E] EventEntity looks at Exoroche (ID: 17731636/0x010E9034) and starts talking
 11: 0x012C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 12: 0x012D [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 13: 0x012E [0x6E] EventEntity uses emote 13*
 14: 0x0135 [0x99] Wait for EventEntity animation to complete
 15: 0x013A [0x00] END_REQSTACK()
```

### Event 121

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x013B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                   00                         .    
```

#### Opcodes

```
  0: 0x013B [0x00] END_REQSTACK()
```

### Event 120

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x013C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                      00                       .   
```

#### Opcodes

```
  0: 0x013C [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x013D   |
| Data Size    | 40 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                         37 12 80               7..
0140: 13 80 07 80 14 80 80 F8  FF FF 7F 66 15 80 F8 FF  ...........f....
0150: FF 7F F8 FF FF 7F 6F 72  6F 30 79 00 F8 FF FF 7F  ......oro0y.....
0160: 20 90 0E 01 00                                     ....           
```

#### Opcodes

```
  0: 0x013D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-28.368*, z=-6.103*, y=0.000*, direction=343.5°*
  1: 0x0146 [0x80] LOAD_WAIT(entity=EventEntity)
  2: 0x014B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "oro0" with entities [EventEntity, EventEntity], work=26*
  3: 0x015A [0x79] EventEntity looks at Unnamed NPC (ID: 17731616/0x010E9020) (Basic look)
  4: 0x0164 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0165   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                66 15 80  F8 FF FF 7F F8 FF FF 7F       f..........
0170: 6F 72 6F 30 00                                    oro0.           
```

#### Opcodes

```
  0: 0x0165 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "oro0" with entities [EventEntity, EventEntity], work=26*
  1: 0x0174 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0175   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                37 12 80  13 80 07 80 16 80 00          7......... 
```

#### Opcodes

```
  0: 0x0175 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-28.368*, z=-6.103*, y=0.000*, direction=271.3°*
  1: 0x017E [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x017F   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                                               66                 f
0180: 15 80 F8 FF FF 7F F8 FF  FF 7F 6F 72 6F 31 00     ..........oro1. 
```

#### Opcodes

```
  0: 0x017F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "oro1" with entities [EventEntity, EventEntity], work=26*
  1: 0x018E [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x018F   |
| Data Size    | 34 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0180:                                               1F                 .
0190: 00 17 80 18 80 07 80 1F  01 6F 1E 20 90 0E 01 6F  .........o. ...o
01A0: 70 66 19 80 F8 FF FF 7F  F8 FF FF 7F 73 68 61 30  pf..........sha0
01B0: 00                                                .               
```

#### Opcodes

```
  0: 0x018F [0x1F] MOVE_ENTITY: EventEntity moves to X=-26.869*, Z=-6.021*, Y=0.000*
  1: 0x0197 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0199 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x019A [0x1E] EventEntity looks at Unnamed NPC (ID: 17731616/0x010E9020) and starts talking
  4: 0x019F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x01A0 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  6: 0x01A1 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sha0" with entities [EventEntity, EventEntity], work=29*
  7: 0x01B0 [0x00] END_REQSTACK()
```

### Event 579

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01B1  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:    00                                              .              
```

#### Opcodes

```
  0: 0x01B1 [0x00] END_REQSTACK()
```

### Event 580

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01B2  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:       00                                            .             
```

#### Opcodes

```
  0: 0x01B2 [0x00] END_REQSTACK()
```

### Event 597

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01B3  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:          00                                          .            
```

#### Opcodes

```
  0: 0x01B3 [0x00] END_REQSTACK()
```

### Event 598

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01B4  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:             00                                        .           
```

#### Opcodes

```
  0: 0x01B4 [0x00] END_REQSTACK()
```

### Event 605

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01B5  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:                00                                      .          
```

#### Opcodes

```
  0: 0x01B5 [0x00] END_REQSTACK()
```

### Event 606

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x01B6  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:                   00                                    .         
```

#### Opcodes

```
  0: 0x01B6 [0x00] END_REQSTACK()
```
