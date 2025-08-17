# 17747980 - Savae E Paleade

## Common Data

| Field            | Value                |
|------------------|----------------------|
| Zone             | Metalworks (ID: 237) |
| Block Size       | 444 bytes            |
| Total Events     | 14                   |
| References Count | 26                   |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [200](#event-200)        | 0x0001       |     11 |              5 |
| [208](#event-208)        | 0x000C       |     11 |              5 |
| [209](#event-209)        | 0x0017       |     11 |              5 |
| [207](#event-207)        | 0x0022       |     10 |              2 |
| [65535.1](#event-655351) | 0x002C       |     61 |             11 |
| [65535.2](#event-655352) | 0x0069       |     49 |              8 |
| [65535.3](#event-655353) | 0x009A       |     24 |              5 |
| [65535.4](#event-655354) | 0x00B2       |     23 |              5 |
| [65535.5](#event-655355) | 0x00C9       |     35 |              7 |
| [65535.6](#event-655356) | 0x00EC       |     31 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1D29      |        7465 |
|       1 | 0x1D2A      |        7466 |
|       2 | 0x1D2B      |        7467 |
|       3 | 0x5CAC      |       23724 |
|       4 | 0xFFFF56A0  |  4294923936 |
|       5 | 0xFFFFBFFA  |  4294950906 |
|       6 | 0x026D      |         621 |
|       7 | 0x001E      |          30 |
|       8 | 0x000D      |          13 |
|       9 | 0x66F4      |       26356 |
|      10 | 0xFFFF5635  |  4294923829 |
|      11 | 0x6A3F      |       27199 |
|      12 | 0xFFFF58C3  |  4294924483 |
|      13 | 0x5E9B      |       24219 |
|      14 | 0xFFFF5660  |  4294923872 |
|      15 | 0x5E30      |       24112 |
|      16 | 0xFFFF58D2  |  4294924498 |
|      17 | 0x4FF0      |       20464 |
|      18 | 0xFFFF67D6  |  4294928342 |
|      19 | 0x0665      |        1637 |
|      20 | 0x4AE4      |       19172 |
|      21 | 0xFFFF6C7E  |  4294929534 |
|      22 | 0x00B4      |         180 |
|      23 | 0x661C      |       26140 |
|      24 | 0xFFFF66B5  |  4294928053 |
|      25 | 0xFFFFBFE9  |  4294950889 |

## String References

- **7465**: Do we look like we have time to chitchat with every adventurer who comes in here?
- **7466**: Good luck on your mission. Bastokers like to do things by the book, so stay out of trouble and follow their rules.
- **7467**: You've successfully completed your mission. Congratulations, and keep up the good work.

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

### Event 200

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1D 00  80 23 21 00               ........#!.    
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=7465*)
    → "Do we look like we have time to chitchat with every adventurer who comes in here?"
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x21] END_EVENT
  4: 0x000B [0x00] END_REQSTACK()
```

### Event 208

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000C   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      1E F0 FF FF              ....
0010: 7F 1D 01 80 23 21 00                              ....#!.         
```

#### Opcodes

```
  0: 0x000C [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0011 [0x1D] PRINT_EVENT_MESSAGE(message_id=7466*)
    → "Good luck on your mission. Bastokers like to do things by the book, so stay out of trouble and follow their rules."
  2: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0015 [0x21] END_EVENT
  4: 0x0016 [0x00] END_REQSTACK()
```

### Event 209

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0017   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      1E  F0 FF FF 7F 1D 02 80 23         ........#
0020: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0017 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x001C [0x1D] PRINT_EVENT_MESSAGE(message_id=7467*)
    → "You've successfully completed your mission. Congratulations, and keep up the good work."
  2: 0x001F [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0020 [0x21] END_EVENT
  4: 0x0021 [0x00] END_REQSTACK()
```

### Event 207

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0022   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:       37 03 80 04 80 05  80 06 80 00                7.........    
```

#### Opcodes

```
  0: 0x0022 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=23.724*, z=-43.360*, y=-16.390*, direction=54.6°*
  1: 0x002B [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002C   |
| Data Size    | 61 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                      53 0D D0 0E              S...
0030: 01 0D D0 0E 01 73 6C 30  30 1C 07 80 7B F8 FF FF  .....sl00...{...
0040: 7F 32 08 80 1F 00 09 80  0A 80 05 80 1F 01 1F 00  .2..............
0050: 0B 80 0C 80 05 80 1F 01  6F 66 07 80 F8 FF FF 7F  ........of......
0060: F8 FF FF 7F 74 68 6B 31  00                       ....thk1.       
```

#### Opcodes

```
  0: 0x002C [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sl00" with entities [Riault (ID: 17747981/0x010ED00D), Riault (ID: 17747981/0x010ED00D)]
  1: 0x0039 [0x1C] WAIT(30* ticks)
  2: 0x003C [0x7B] EventEntity stops talking
  3: 0x0041 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  4: 0x0044 [0x1F] MOVE_ENTITY: EventEntity moves to X=26.356*, Z=-43.467*, Y=-16.390*
  5: 0x004C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x004E [0x1F] MOVE_ENTITY: EventEntity moves to X=27.199*, Z=-42.813*, Y=-16.390*
  7: 0x0056 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  8: 0x0058 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  9: 0x0059 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=30*
 10: 0x0068 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0069   |
| Data Size    | 49 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                             66 07 80 F8 FF FF 7F           f......
0070: F8 FF FF 7F 74 68 6B 32  32 08 80 1F 00 09 80 0A  ....thk22.......
0080: 80 05 80 1F 01 1F 00 0D  80 0E 80 05 80 1F 01 79  ...............y
0090: 00 F8 FF FF 7F 0F D0 0E  01 00                    ..........      
```

#### Opcodes

```
  0: 0x0069 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=30*
  1: 0x0078 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x007B [0x1F] MOVE_ENTITY: EventEntity moves to X=26.356*, Z=-43.467*, Y=-16.390*
  3: 0x0083 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0085 [0x1F] MOVE_ENTITY: EventEntity moves to X=24.219*, Z=-43.424*, Y=-16.390*
  5: 0x008D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x008F [0x79] EventEntity looks at Chantain (ID: 17747983/0x010ED00F) (Basic look)
  7: 0x0099 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009A   |
| Data Size    | 24 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                79 00 F8 FF FF 7F            y.....
00A0: F0 FF FF 7F 32 08 80 1F  00 0F 80 10 80 05 80 1F  ....2...........
00B0: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x009A [0x79] EventEntity looks at LocalPlayer (Basic look)
  1: 0x00A4 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x00A7 [0x1F] MOVE_ENTITY: EventEntity moves to X=24.112*, Z=-42.798*, Y=-16.390*
  3: 0x00AF [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x00B1 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B2   |
| Data Size    | 23 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:       32 08 80 37 11 80  12 80 05 80 13 80 1F 00    2..7..........
00C0: 14 80 15 80 05 80 1F 01  00                       .........       
```

#### Opcodes

```
  0: 0x00B2 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00B5 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=20.464*, z=-38.954*, y=-16.390*, direction=143.9°*
  2: 0x00BE [0x1F] MOVE_ENTITY: EventEntity moves to X=19.172*, Z=-37.762*, Y=-16.390*
  3: 0x00C6 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x00C8 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C9   |
| Data Size    | 35 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                             1C 16 80 53 0D D0 0E           ...S...
00D0: 01 0D D0 0E 01 73 6C 30  30 32 08 80 1F 00 17 80  .....sl002......
00E0: 18 80 19 80 1F 01 1E F0  FF FF 7F 00              ............    
```

#### Opcodes

```
  0: 0x00C9 [0x1C] WAIT(180* ticks)
  1: 0x00CC [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sl00" with entities [Riault (ID: 17747981/0x010ED00D), Riault (ID: 17747981/0x010ED00D)]
  2: 0x00D9 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  3: 0x00DC [0x1F] MOVE_ENTITY: EventEntity moves to X=26.140*, Z=-39.243*, Y=-16.407*
  4: 0x00E4 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x00E6 [0x1E] EventEntity looks at LocalPlayer and starts talking
  6: 0x00EB [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00EC   |
| Data Size    | 31 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                      32 08 80 1F              2...
00F0: 00 17 80 18 80 19 80 1F  01 1E F0 FF FF 7F 6F 70  ..............op
0100: 79 00 F0 FF FF 7F 0C D0  0E 01 00                 y..........     
```

#### Opcodes

```
  0: 0x00EC [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00EF [0x1F] MOVE_ENTITY: EventEntity moves to X=26.140*, Z=-39.243*, Y=-16.407*
  2: 0x00F7 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00F9 [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x00FE [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x00FF [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  6: 0x0100 [0x79] LocalPlayer looks at Savae E Paleade (ID: 17747980/0x010ED00C) (Basic look)
  7: 0x010A [0x00] END_REQSTACK()
```
