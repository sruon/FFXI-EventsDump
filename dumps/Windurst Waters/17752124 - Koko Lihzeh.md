# 17752124 - Koko Lihzeh

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Windurst Waters (ID: 238) |
| Block Size       | 528 bytes                 |
| Total Events     | 16                        |
| References Count | 13                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |     22 |              4 |
| [65535.3](#event-655353) | 0x0027       |     28 |              4 |
| [65535.4](#event-655354) | 0x0043       |     26 |              4 |
| [65535.5](#event-655355) | 0x005D       |     28 |              4 |
| [65535.6](#event-655356) | 0x0079       |     26 |              4 |
| [65535.7](#event-655357) | 0x0093       |     22 |              3 |
| [65535.8](#event-655358) | 0x00A9       |     28 |              5 |
| [65535.9](#event-655359) | 0x00C5       |      9 |              3 |
| [428](#event-428)        | 0x00CE       |     33 |             12 |
| [191](#event-191)        | 0x00EF       |     29 |             10 |
| [488](#event-488)        | 0x010C       |     33 |             12 |
| [506](#event-506)        | 0x012D       |     33 |             12 |
| [451](#event-451)        | 0x014E       |     33 |             12 |
| [471](#event-471)        | 0x016F       |     29 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0050      |          80 |
|       1 | 0x001E      |          30 |
|       2 | 0x0051      |          81 |
|       3 | 0x209C      |        8348 |
|       4 | 0x209D      |        8349 |
|       5 | 0x1E4C      |        7756 |
|       6 | 0x211E      |        8478 |
|       7 | 0x211F      |        8479 |
|       8 | 0x214B      |        8523 |
|       9 | 0x214C      |        8524 |
|      10 | 0x20D1      |        8401 |
|      11 | 0x20D2      |        8402 |
|      12 | 0x20FF      |        8447 |

## String References

- **7756**: I can't wait. I'm good at skills tests. Fighting's what I do best!
- **8348**: I'm Koko Lihzeh, the School of Magic's first Mithra student.
- **8349**: I'm studying real hard so I can prrrove that Mithra can become as skilled as anyone else in the use of magic.
- **8401**: I expect to get about 50%... That's 'cause I chose by intuition...not tuition.
- **8402**: But I got 90% in the test before last, so I don't have to worrrry about dropping down to beginnerrrs class.
- **8447**: I rrreceived frrruit seeds! I'll trrry and grrrow some $1.
- **8478**: Durrring our magical prrractice the otherrr day, Paku-Nakku and Foi-Mui brrroke the rrrules and got extra homeworrrk as punishment.
- **8479**: I don't underrrstand why boys love to do forrrbidden stuff all the time.
- **8523**: What, so you didn't know? Paku-Nakku was tirrred lately because he was hooked on the Agatha Crystalie mysterrry serrries.
- **8524**: They are so cool! I just love Detective Poiroto-Boiroto and Miss Marpelpel... Unforrrtunately, the librarrry doesn't have the last book in the series yet...

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
0000:    5B 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   [..........tlk0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=80*
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
| Data Size    | 28 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      7C  00 F8 FF FF 7F 81 00 F8         |........
0030: FF FF 7F 5B 02 80 F8 FF  FF 7F F8 FF FF 7F 68 61  ...[..........ha
0040: 69 30 00                                          i0.             
```

#### Opcodes

```
  0: 0x0027 [0x7C] EventEntity->Render.Flags2 |= 0x00
  1: 0x002D [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  2: 0x0033 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "hai0" with entities [EventEntity, EventEntity], work=81*
  3: 0x0042 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0043   |
| Data Size    | 26 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:          53 F8 FF FF 7F  F8 FF FF 7F 68 61 69 30     S........hai0
0050: 7C 01 F8 FF FF 7F 81 01  F8 FF FF 7F 00           |............   
```

#### Opcodes

```
  0: 0x0043 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "hai0" with entities [EventEntity, EventEntity]
  1: 0x0050 [0x7C] EventEntity->Render.Flags2 |= 0x01
  2: 0x0056 [0x81] SET_ENTITY_BLINKING(blink_flag=0x01, entity=EventEntity)
  3: 0x005C [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005D   |
| Data Size    | 28 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                         7C 00 F8               |..
0060: FF FF 7F 81 00 F8 FF FF  7F 5B 02 80 F8 FF FF 7F  .........[......
0070: F8 FF FF 7F 62 69 6B 30  00                       ....bik0.       
```

#### Opcodes

```
  0: 0x005D [0x7C] EventEntity->Render.Flags2 |= 0x00
  1: 0x0063 [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  2: 0x0069 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "bik0" with entities [EventEntity, EventEntity], work=81*
  3: 0x0078 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0079   |
| Data Size    | 26 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                             53 F8 FF FF 7F F8 FF           S......
0080: FF 7F 62 69 6B 30 7C 01  F8 FF FF 7F 81 01 F8 FF  ..bik0|.........
0090: FF 7F 00                                          ...             
```

#### Opcodes

```
  0: 0x0079 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "bik0" with entities [EventEntity, EventEntity]
  1: 0x0086 [0x7C] EventEntity->Render.Flags2 |= 0x01
  2: 0x008C [0x81] SET_ENTITY_BLINKING(blink_flag=0x01, entity=EventEntity)
  3: 0x0092 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0093   |
| Data Size    | 22 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:          81 00 F8 FF FF  7F 5B 00 80 F8 FF FF 7F     ......[......
00A0: F8 FF FF 7F 61 77 77 30  00                       ....aww0.       
```

#### Opcodes

```
  0: 0x0093 [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  1: 0x0099 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "aww0" with entities [EventEntity, EventEntity], work=80*
  2: 0x00A8 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A9   |
| Data Size    | 28 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                             53 F8 FF FF 7F F8 FF           S......
00B0: FF 7F 61 77 77 30 5E 69  64 6C 30 1C 01 80 81 01  ..aww0^idl0.....
00C0: F8 FF FF 7F 00                                    .....           
```

#### Opcodes

```
  0: 0x00A9 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "aww0" with entities [EventEntity, EventEntity]
  1: 0x00B6 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x00BB [0x1C] WAIT(30* ticks)
  3: 0x00BE [0x81] SET_ENTITY_BLINKING(blink_flag=0x01, entity=EventEntity)
  4: 0x00C4 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00C5  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                5E 69 64  6C 30 1C 01 80 00             ^idl0....  
```

#### Opcodes

```
  0: 0x00C5 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x00CA [0x1C] WAIT(30* ticks)
  2: 0x00CD [0x00] END_REQSTACK()
```

### Event 428

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CE   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                            1E F0                ..
00D0: FF FF 7F 6F 70 29 08 3C  E0 0E 01 01 1D 03 80 23  ...op).<.......#
00E0: 1D 04 80 23 29 08 3C E0  0E 01 02 20 00 21 00     ...#).<.... .!. 
```

#### Opcodes

```
  0: 0x00CE [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00D3 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00D4 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00D5 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Koko Lihzeh (ID: 17752124/0x010EE03C), tag_num=0x01)
  4: 0x00DC [0x1D] PRINT_EVENT_MESSAGE(message_id=8348*)
    → "I'm Koko Lihzeh, the School of Magic's first Mithra student."
  5: 0x00DF [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00E0 [0x1D] PRINT_EVENT_MESSAGE(message_id=8349*)
    → "I'm studying real hard so I can prrrove that Mithra can become as skilled as anyone else in the use of magic."
  7: 0x00E3 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00E4 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Koko Lihzeh (ID: 17752124/0x010EE03C), tag_num=0x02)
  9: 0x00EB [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x00ED [0x21] END_EVENT
 11: 0x00EE [0x00] END_REQSTACK()
```

### Event 191

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00EF   |
| Data Size    | 29 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                               1E                 .
00F0: F0 FF FF 7F 6F 70 29 08  3C E0 0E 01 01 1D 05 80  ....op).<.......
0100: 23 29 08 3C E0 0E 01 02  20 00 21 00              #).<.... .!.    
```

#### Opcodes

```
  0: 0x00EF [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00F4 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00F5 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00F6 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Koko Lihzeh (ID: 17752124/0x010EE03C), tag_num=0x01)
  4: 0x00FD [0x1D] PRINT_EVENT_MESSAGE(message_id=7756*)
    → "I can't wait. I'm good at skills tests. Fighting's what I do best!"
  5: 0x0100 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0101 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Koko Lihzeh (ID: 17752124/0x010EE03C), tag_num=0x02)
  7: 0x0108 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x010A [0x21] END_EVENT
  9: 0x010B [0x00] END_REQSTACK()
```

### Event 488

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x010C   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                      1E F0 FF FF              ....
0110: 7F 6F 70 29 08 3C E0 0E  01 01 1D 06 80 23 1D 07  .op).<.......#..
0120: 80 23 29 08 3C E0 0E 01  02 20 00 21 00           .#).<.... .!.   
```

#### Opcodes

```
  0: 0x010C [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0111 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0112 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0113 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Koko Lihzeh (ID: 17752124/0x010EE03C), tag_num=0x01)
  4: 0x011A [0x1D] PRINT_EVENT_MESSAGE(message_id=8478*)
    → "Durrring our magical prrractice the otherrr day, Paku-Nakku and Foi-Mui brrroke the rrrules and got extra homeworrrk as punishment."
  5: 0x011D [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x011E [0x1D] PRINT_EVENT_MESSAGE(message_id=8479*)
    → "I don't underrrstand why boys love to do forrrbidden stuff all the time."
  7: 0x0121 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0122 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Koko Lihzeh (ID: 17752124/0x010EE03C), tag_num=0x02)
  9: 0x0129 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x012B [0x21] END_EVENT
 11: 0x012C [0x00] END_REQSTACK()
```

### Event 506

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x012D   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                         1E F0 FF               ...
0130: FF 7F 6F 70 29 08 3C E0  0E 01 01 1D 08 80 23 1D  ..op).<.......#.
0140: 09 80 23 29 08 3C E0 0E  01 02 20 00 21 00        ..#).<.... .!.  
```

#### Opcodes

```
  0: 0x012D [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0132 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0133 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0134 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Koko Lihzeh (ID: 17752124/0x010EE03C), tag_num=0x01)
  4: 0x013B [0x1D] PRINT_EVENT_MESSAGE(message_id=8523*)
    → "What, so you didn't know? Paku-Nakku was tirrred lately because he was hooked on the Agatha Crystalie mysterrry serrries."
  5: 0x013E [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x013F [0x1D] PRINT_EVENT_MESSAGE(message_id=8524*)
    → "They are so cool! I just love Detective Poiroto-Boiroto and Miss Marpelpel... Unforrrtunately, the librarrry doesn't have the last book in the series yet..."
  7: 0x0142 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0143 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Koko Lihzeh (ID: 17752124/0x010EE03C), tag_num=0x02)
  9: 0x014A [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x014C [0x21] END_EVENT
 11: 0x014D [0x00] END_REQSTACK()
```

### Event 451

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x014E   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                                            1E F0                ..
0150: FF FF 7F 6F 70 29 08 3C  E0 0E 01 01 1D 0A 80 23  ...op).<.......#
0160: 1D 0B 80 23 29 08 3C E0  0E 01 02 20 00 21 00     ...#).<.... .!. 
```

#### Opcodes

```
  0: 0x014E [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0153 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0154 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0155 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Koko Lihzeh (ID: 17752124/0x010EE03C), tag_num=0x01)
  4: 0x015C [0x1D] PRINT_EVENT_MESSAGE(message_id=8401*)
    → "I expect to get about 50%... That's 'cause I chose by intuition...not tuition."
  5: 0x015F [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0160 [0x1D] PRINT_EVENT_MESSAGE(message_id=8402*)
    → "But I got 90% in the test before last, so I don't have to worrrry about dropping down to beginnerrrs class."
  7: 0x0163 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0164 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Koko Lihzeh (ID: 17752124/0x010EE03C), tag_num=0x02)
  9: 0x016B [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x016D [0x21] END_EVENT
 11: 0x016E [0x00] END_REQSTACK()
```

### Event 471

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x016F   |
| Data Size    | 29 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                                               1E                 .
0170: F0 FF FF 7F 6F 70 29 08  3C E0 0E 01 01 1D 0C 80  ....op).<.......
0180: 23 29 08 3C E0 0E 01 02  20 00 21 00              #).<.... .!.    
```

#### Opcodes

```
  0: 0x016F [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0174 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0175 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0176 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Koko Lihzeh (ID: 17752124/0x010EE03C), tag_num=0x01)
  4: 0x017D [0x1D] PRINT_EVENT_MESSAGE(message_id=8447*)
    → "I rrreceived frrruit seeds! I'll trrry and grrrow some $1."
  5: 0x0180 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0181 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Koko Lihzeh (ID: 17752124/0x010EE03C), tag_num=0x02)
  7: 0x0188 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x018A [0x21] END_EVENT
  9: 0x018B [0x00] END_REQSTACK()
```
