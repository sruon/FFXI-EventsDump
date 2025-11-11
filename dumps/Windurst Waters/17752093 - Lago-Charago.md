# 17752093 - Lago-Charago

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Windurst Waters (ID: 238) |
| Block Size       | 408 bytes                 |
| Total Events     | 12                        |
| References Count | 17                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |     22 |              4 |
| [65535.3](#event-655353) | 0x0027       |      9 |              3 |
| [300](#event-300)        | 0x0030       |     99 |             22 |
| [65535.4](#event-655354) | 0x0093       |     23 |              7 |
| [65535.5](#event-655355) | 0x00AA       |     19 |              5 |
| [65535.6](#event-655356) | 0x00BD       |      5 |              3 |
| [65535.7](#event-655357) | 0x00C2       |      5 |              3 |
| [65535.8](#event-655358) | 0x00C7       |      5 |              3 |
| [65535.9](#event-655359) | 0x00CC       |     19 |              5 |
| [940](#event-940)        | 0x00DF       |     52 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x001E      |          30 |
|       2 | 0x1F4B      |        8011 |
|       3 | 0x0001      |           1 |
|       4 | 0x0000      |           0 |
|       5 | 0xFFFFFFFC  |  4294967292 |
|       6 | 0x0002      |           2 |
|       7 | 0x1F49      |        8009 |
|       8 | 0x1F4A      |        8010 |
|       9 | 0x1F4C      |        8012 |
|      10 | 0x1F4D      |        8013 |
|      11 | 0x1F4E      |        8014 |
|      12 | 0x1F4F      |        8015 |
|      13 | 0x1F50      |        8016 |
|      14 | 0x2FFE      |       12286 |
|      15 | 0x3009      |       12297 |
|      16 | 0x300A      |       12298 |

## String References

- **8009**: Whaddaya want-want? Can'tya see I'm busy-busy preparing for my astronomic observations?
- **8010**: Hm. I infer somebody wants to see my stellar stellar map, perhaps?
- **8011**: See the stellar map? [Stellar!/Map-schmap!]
- **8012**: Then don't bug-bug me again! People's lives are but a fleeting moment when compared to the lives of the stars. There are so many stars to map, I don't wanna waste a second second!
- **8013**: Humph-humph. Good to see someone has an interest in the stars.
- **8014**: Climbing the northern sky is the famous Odin. The black point there is Odin's beloved steer, Sleipnir.
- **8015**: And above that--although in the actual night sky it appears below Sleipnir--is the North Star, the prominently bright star that sailors guide their ships by.
- **8016**: If you want to further further your interest in the stars, then you're always welcome to visit here and see my stellar stellar map.
- **12286**: <Player>'s badge flashes brightly.
- **12297**: Hm. I infer somebody wants to know-know about Aht Urhgan, perhaps? Then you should look up at this night's night sky.
- **12298**: Compared to the night sky, this world is small. Perhaps it holds that that you seek.

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

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0027  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      5E  69 64 6C 30 1C 01 80 00         ^idl0....
```

#### Opcodes

```
  0: 0x0027 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x002C [0x1C] WAIT(30* ticks)
  2: 0x002F [0x00] END_REQSTACK()
```

### Event 300

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 99 bytes |
| Instructions | 22       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 1E F0 FF FF 7F 6F 70 29  0B 1D E0 0E 01 05 24 02  .....op)......$.
0040: 80 03 80 04 80 25 02 00  10 04 80 00 78 00 03 01  .....%......x...
0050: 10 03 80 8D 05 80 04 80  29 0B 1D E0 0E 01 07 29  ........)......)
0060: 0B 1D E0 0E 01 08 29 0B  1D E0 0E 01 09 8A 29 0B  ......).......).
0070: 1D E0 0E 01 0A 01 8F 00  02 00 10 03 80 00 8F 00  ................
0080: 03 01 10 06 80 29 0B 1D  E0 0E 01 06 01 8F 00 20  .....)......... 
0090: 00 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x0030 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0035 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0036 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0037 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Lago-Charago (ID: 17752093/0x010EE01D), tag_num=0x05)
  4: 0x003E [0x24] CREATE_DIALOG(message_id=8011*, default_option=1*, option_flags=0*)
    → "See the stellar map? [Stellar!/Map-schmap!]"
  5: 0x0045 [0x25] WAIT_DIALOG_SELECT()
  6: 0x0046 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0078
  7: 0x004E [0x03] Work_Zone[1] = 1*
  8: 0x0053 [0x8D] OPEN_MAP_WITH_PROPERTIES(map_id=4294967292*, properties=0*)
  9: 0x0058 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Lago-Charago (ID: 17752093/0x010EE01D), tag_num=0x07)
 10: 0x005F [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Lago-Charago (ID: 17752093/0x010EE01D), tag_num=0x08)
 11: 0x0066 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Lago-Charago (ID: 17752093/0x010EE01D), tag_num=0x09)
 12: 0x006D [0x8A] CLOSE_MAP()
 13: 0x006E [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Lago-Charago (ID: 17752093/0x010EE01D), tag_num=0x0A)
 14: 0x0075 [0x01] GOTO 0x008F
 15: 0x0078 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x008F
 16: 0x0080 [0x03] Work_Zone[1] = 2*
 17: 0x0085 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Lago-Charago (ID: 17752093/0x010EE01D), tag_num=0x06)
 18: 0x008C [0x01] GOTO 0x008F

SUBROUTINE_008F:
 19: 0x008F [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 20: 0x0091 [0x21] END_EVENT
 21: 0x0092 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0093   |
| Data Size    | 23 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:          29 08 1D E0 0E  01 01 1D 07 80 23 1D 08     ).........#..
00A0: 80 23 29 08 1D E0 0E 01  02 00                    .#).......      
```

#### Opcodes

```
  0: 0x0093 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Lago-Charago (ID: 17752093/0x010EE01D), tag_num=0x01)
  1: 0x009A [0x1D] PRINT_EVENT_MESSAGE(message_id=8009*)
    → "Whaddaya want-want? Can'tya see I'm busy-busy preparing for my astronomic observations?"
  2: 0x009D [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x009E [0x1D] PRINT_EVENT_MESSAGE(message_id=8010*)
    → "Hm. I infer somebody wants to see my stellar stellar map, perhaps?"
  4: 0x00A1 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x00A2 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Lago-Charago (ID: 17752093/0x010EE01D), tag_num=0x02)
  6: 0x00A9 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AA   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                29 08 1D E0 0E 01            ).....
00B0: 01 1D 09 80 23 29 08 1D  E0 0E 01 02 00           ....#).......   
```

#### Opcodes

```
  0: 0x00AA [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Lago-Charago (ID: 17752093/0x010EE01D), tag_num=0x01)
  1: 0x00B1 [0x1D] PRINT_EVENT_MESSAGE(message_id=8012*)
    → "Then don't bug-bug me again! People's lives are but a fleeting moment when compared to the lives of the stars. There are so many stars to map, I don't wanna waste a second second!"
  2: 0x00B4 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00B5 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Lago-Charago (ID: 17752093/0x010EE01D), tag_num=0x02)
  4: 0x00BC [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00BD  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                         1D 0A 80               ...
00C0: 23 00                                             #.              
```

#### Opcodes

```
  0: 0x00BD [0x1D] PRINT_EVENT_MESSAGE(message_id=8013*)
    → "Humph-humph. Good to see someone has an interest in the stars."
  1: 0x00C0 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x00C1 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00C2  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:       1D 0B 80 23 00                                ...#.         
```

#### Opcodes

```
  0: 0x00C2 [0x1D] PRINT_EVENT_MESSAGE(message_id=8014*)
    → "Climbing the northern sky is the famous Odin. The black point there is Odin's beloved steer, Sleipnir."
  1: 0x00C5 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x00C6 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00C7  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                      1D  0C 80 23 00                     ...#.    
```

#### Opcodes

```
  0: 0x00C7 [0x1D] PRINT_EVENT_MESSAGE(message_id=8015*)
    → "And above that--although in the actual night sky it appears below Sleipnir--is the North Star, the prominently bright star that sailors guide their ships by."
  1: 0x00CA [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x00CB [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CC   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                      29 08 1D E0              )...
00D0: 0E 01 01 1D 0D 80 23 29  08 1D E0 0E 01 02 00     ......#)....... 
```

#### Opcodes

```
  0: 0x00CC [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Lago-Charago (ID: 17752093/0x010EE01D), tag_num=0x01)
  1: 0x00D3 [0x1D] PRINT_EVENT_MESSAGE(message_id=8016*)
    → "If you want to further further your interest in the stars, then you're always welcome to visit here and see my stellar stellar map."
  2: 0x00D6 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00D7 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Lago-Charago (ID: 17752093/0x010EE01D), tag_num=0x02)
  4: 0x00DE [0x00] END_REQSTACK()
```

### Event 940

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DF   |
| Data Size    | 52 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                               42                 B
00E0: 48 0E 80 1E F0 FF FF 7F  1C 01 80 1D 0F 80 23 66  H.............#f
00F0: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 1D 10  ..........tlk0..
0100: 80 23 66 00 80 F8 FF FF  7F F8 FF FF 7F 74 6C 6B  .#f..........tlk
0110: 31 21 00                                          1!.             
```

#### Opcodes

```
  0: 0x00DF [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x00E0 [0x48] [System] [12286*]:
    → "<Player>'s badge flashes brightly."
  2: 0x00E3 [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x00E8 [0x1C] WAIT(30* ticks)
  4: 0x00EB [0x1D] PRINT_EVENT_MESSAGE(message_id=12297*)
    → "Hm. I infer somebody wants to know-know about Aht Urhgan, perhaps? Then you should look up at this night's night sky."
  5: 0x00EE [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00EF [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  7: 0x00FE [0x1D] PRINT_EVENT_MESSAGE(message_id=12298*)
    → "Compared to the night sky, this world is small. Perhaps it holds that that you seek."
  8: 0x0101 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0102 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=40*
 10: 0x0111 [0x21] END_EVENT
 11: 0x0112 [0x00] END_REQSTACK()
```
