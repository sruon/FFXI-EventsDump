# 17752149 - Chyuk-Kochak

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Windurst Waters (ID: 238) |
| Block Size       | 452 bytes                 |
| Total Events     | 15                        |
| References Count | 13                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |     22 |              4 |
| [65535.3](#event-655353) | 0x0027       |     16 |              2 |
| [65535.4](#event-655354) | 0x0037       |     14 |              2 |
| [65535.5](#event-655355) | 0x0045       |     16 |              2 |
| [65535.6](#event-655356) | 0x0055       |     14 |              2 |
| [65535.7](#event-655357) | 0x0063       |      9 |              3 |
| [664](#event-664)        | 0x006C       |     33 |             12 |
| [680](#event-680)        | 0x008D       |      1 |              1 |
| [667](#event-667)        | 0x008E       |     29 |             10 |
| [672](#event-672)        | 0x00AB       |     33 |             12 |
| [675](#event-675)        | 0x00CC       |     33 |             12 |
| [679](#event-679)        | 0x00ED       |     54 |             15 |
| [682](#event-682)        | 0x0123       |     33 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x001E      |          30 |
|       2 | 0x2379      |        9081 |
|       3 | 0x237A      |        9082 |
|       4 | 0x2382      |        9090 |
|       5 | 0x2396      |        9110 |
|       6 | 0x2397      |        9111 |
|       7 | 0x239A      |        9114 |
|       8 | 0x239B      |        9115 |
|       9 | 0x23A2      |        9122 |
|      10 | 0x23A3      |        9123 |
|      11 | 0x23B3      |        9139 |
|      12 | 0x23B4      |        9140 |

## String References

- **9081**: Our editor is all fired up...more so than usual.
- **9082**: All our staff are tired and worn out from our last special report, "What Happened to the Star Reading Ceremony?". He's just wasting his breath and annoying us all.
- **9090**: There should be a reporter in each of the four districts of Windurst.
- **9110**: Heh. Looks like we scooped quite a story here.
- **9111**: We've all got to get cracking now! We've got to get this baby into production!
- **9114**: No matter how great and sensational the story is, it's totally useless if it turns out to be a bunch of lies.
- **9115**: A good reporter needs a good nose for uncovering the story, then good legs to go check [his/her] sources. Learn that and you'll go far.
- **9122**: The Cat Burglar must have smelt a rat... Nanaa Mihgo didn't want us to expose her hideaway, so she stole the story before it could go into circulation. Agh...someone really let the cat outta the bag!
- **9123**: Aa\`ah! This week's edition of the "Magic Paradise Weekly" is going to be canceled as well. It happens so often, though, that nobody's going to notice anyway...<Sigh>
- **9139**: The Cat Burglar must have caught wind of us... Nanaa Mihgo didn't want us to expose her hideaway, so she stole the story before it could go into circulation.
- **9140**: But you did real well to get the magic doll back off of her! It's practically impossible to retrieve anything stolen by the Cat Burglar!

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   f..........tlk0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    53 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 5E 69   S........tlk0^i
0020: 64 6C 30 1C 01 80 00                              dl0....         
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x001E [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x0023 [0x1C] WAIT(30* ticks)
  3: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0027   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      66  00 80 F8 FF FF 7F F8 FF         f........
0030: FF 7F 74 68 6B 31 00                              ..thk1.         
```

#### Opcodes

```
  0: 0x0027 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=40*
  1: 0x0036 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0037   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      53  F8 FF FF 7F F8 FF FF 7F         S........
0040: 74 68 6B 31 00                                    thk1.           
```

#### Opcodes

```
  0: 0x0037 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  1: 0x0044 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0045   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                66 00 80  F8 FF FF 7F F8 FF FF 7F       f..........
0050: 74 68 6B 32 00                                    thk2.           
```

#### Opcodes

```
  0: 0x0045 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=40*
  1: 0x0054 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0055   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                53 F8 FF  FF 7F F8 FF FF 7F 74 68       S........th
0060: 6B 32 00                                          k2.             
```

#### Opcodes

```
  0: 0x0055 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  1: 0x0062 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0063  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:          5E 69 64 6C 30  1C 01 80 00                 ^idl0....    
```

#### Opcodes

```
  0: 0x0063 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0068 [0x1C] WAIT(30* ticks)
  2: 0x006B [0x00] END_REQSTACK()
```

### Event 664

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006C   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                      1E F0 FF FF              ....
0070: 7F 6F 70 29 08 55 E0 0E  01 01 1D 02 80 23 1D 03  .op).U.......#..
0080: 80 23 29 08 55 E0 0E 01  07 20 00 21 00           .#).U.... .!.   
```

#### Opcodes

```
  0: 0x006C [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0071 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0072 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0073 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Chyuk-Kochak (ID: 17752149/0x010EE055), tag_num=0x01)
  4: 0x007A [0x1D] PRINT_EVENT_MESSAGE(message_id=9081*)
    → "Our editor is all fired up...more so than usual."
  5: 0x007D [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x007E [0x1D] PRINT_EVENT_MESSAGE(message_id=9082*)
    → "All our staff are tired and worn out from our last special report, "What Happened to the Star Reading Ceremony?". He's just wasting his breath and annoying us all."
  7: 0x0081 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0082 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Chyuk-Kochak (ID: 17752149/0x010EE055), tag_num=0x07)
  9: 0x0089 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x008B [0x21] END_EVENT
 11: 0x008C [0x00] END_REQSTACK()
```

### Event 680

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x008D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                         00                     .  
```

#### Opcodes

```
  0: 0x008D [0x00] END_REQSTACK()
```

### Event 667

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008E   |
| Data Size    | 29 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                            1E F0                ..
0090: FF FF 7F 6F 70 29 08 55  E0 0E 01 01 1D 04 80 23  ...op).U.......#
00A0: 29 08 55 E0 0E 01 07 20  00 21 00                 ).U.... .!.     
```

#### Opcodes

```
  0: 0x008E [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0093 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0094 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0095 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Chyuk-Kochak (ID: 17752149/0x010EE055), tag_num=0x01)
  4: 0x009C [0x1D] PRINT_EVENT_MESSAGE(message_id=9090*)
    → "There should be a reporter in each of the four districts of Windurst."
  5: 0x009F [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00A0 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Chyuk-Kochak (ID: 17752149/0x010EE055), tag_num=0x07)
  7: 0x00A7 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x00A9 [0x21] END_EVENT
  9: 0x00AA [0x00] END_REQSTACK()
```

### Event 672

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AB   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                   1E F0 FF FF 7F             .....
00B0: 6F 70 29 08 55 E0 0E 01  01 1D 05 80 23 1D 06 80  op).U.......#...
00C0: 23 29 08 55 E0 0E 01 07  20 00 21 00              #).U.... .!.    
```

#### Opcodes

```
  0: 0x00AB [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00B0 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00B1 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00B2 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Chyuk-Kochak (ID: 17752149/0x010EE055), tag_num=0x01)
  4: 0x00B9 [0x1D] PRINT_EVENT_MESSAGE(message_id=9110*)
    → "Heh. Looks like we scooped quite a story here."
  5: 0x00BC [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00BD [0x1D] PRINT_EVENT_MESSAGE(message_id=9111*)
    → "We've all got to get cracking now! We've got to get this baby into production!"
  7: 0x00C0 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00C1 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Chyuk-Kochak (ID: 17752149/0x010EE055), tag_num=0x07)
  9: 0x00C8 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x00CA [0x21] END_EVENT
 11: 0x00CB [0x00] END_REQSTACK()
```

### Event 675

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CC   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                      1E F0 FF FF              ....
00D0: 7F 6F 70 29 08 55 E0 0E  01 01 1D 07 80 23 1D 08  .op).U.......#..
00E0: 80 23 29 08 55 E0 0E 01  07 20 00 21 00           .#).U.... .!.   
```

#### Opcodes

```
  0: 0x00CC [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00D1 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00D2 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00D3 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Chyuk-Kochak (ID: 17752149/0x010EE055), tag_num=0x01)
  4: 0x00DA [0x1D] PRINT_EVENT_MESSAGE(message_id=9114*)
    → "No matter how great and sensational the story is, it's totally useless if it turns out to be a bunch of lies."
  5: 0x00DD [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00DE [0x1D] PRINT_EVENT_MESSAGE(message_id=9115*)
    → "A good reporter needs a good nose for uncovering the story, then good legs to go check [his/her] sources. Learn that and you'll go far."
  7: 0x00E1 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00E2 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Chyuk-Kochak (ID: 17752149/0x010EE055), tag_num=0x07)
  9: 0x00E9 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x00EB [0x21] END_EVENT
 11: 0x00EC [0x00] END_REQSTACK()
```

### Event 679

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00ED   |
| Data Size    | 54 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                         1E F0 FF               ...
00F0: FF 7F 6F 70 29 08 55 E0  0E 01 01 1D 09 80 23 29  ..op).U.......#)
0100: 08 55 E0 0E 01 07 29 08  55 E0 0E 01 03 1D 0A 80  .U....).U.......
0110: 23 29 08 55 E0 0E 01 05  29 08 55 E0 0E 01 06 20  #).U....).U.... 
0120: 00 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x00ED [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00F2 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00F3 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00F4 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Chyuk-Kochak (ID: 17752149/0x010EE055), tag_num=0x01)
  4: 0x00FB [0x1D] PRINT_EVENT_MESSAGE(message_id=9122*)
    → "The Cat Burglar must have smelt a rat... Nanaa Mihgo didn't want us to expose her hideaway, so she stole the story before it could go into circulation. Agh...someone really let the cat outta the bag!"
  5: 0x00FE [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00FF [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Chyuk-Kochak (ID: 17752149/0x010EE055), tag_num=0x07)
  7: 0x0106 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Chyuk-Kochak (ID: 17752149/0x010EE055), tag_num=0x03)
  8: 0x010D [0x1D] PRINT_EVENT_MESSAGE(message_id=9123*)
    → "Aa`ah! This week's edition of the "Magic Paradise Weekly" is going to be canceled as well. It happens so often, though, that nobody's going to notice anyway...<Sigh>"
  9: 0x0110 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0111 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Chyuk-Kochak (ID: 17752149/0x010EE055), tag_num=0x05)
 11: 0x0118 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Chyuk-Kochak (ID: 17752149/0x010EE055), tag_num=0x06)
 12: 0x011F [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 13: 0x0121 [0x21] END_EVENT
 14: 0x0122 [0x00] END_REQSTACK()
```

### Event 682

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0123   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:          1E F0 FF FF 7F  6F 70 29 08 55 E0 0E 01     .....op).U...
0130: 01 1D 0B 80 23 1D 0C 80  23 29 08 55 E0 0E 01 07  ....#...#).U....
0140: 20 00 21 00                                        .!.            
```

#### Opcodes

```
  0: 0x0123 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0128 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0129 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x012A [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Chyuk-Kochak (ID: 17752149/0x010EE055), tag_num=0x01)
  4: 0x0131 [0x1D] PRINT_EVENT_MESSAGE(message_id=9139*)
    → "The Cat Burglar must have caught wind of us... Nanaa Mihgo didn't want us to expose her hideaway, so she stole the story before it could go into circulation."
  5: 0x0134 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0135 [0x1D] PRINT_EVENT_MESSAGE(message_id=9140*)
    → "But you did real well to get the magic doll back off of her! It's practically impossible to retrieve anything stolen by the Cat Burglar!"
  7: 0x0138 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0139 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Chyuk-Kochak (ID: 17752149/0x010EE055), tag_num=0x07)
  9: 0x0140 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x0142 [0x21] END_EVENT
 11: 0x0143 [0x00] END_REQSTACK()
```
