# 17764445 - Hae Jakkya

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Woods (ID: 241) |
| Block Size       | 752 bytes                |
| Total Events     | 26                       |
| References Count | 13                       |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |     16 |              2 |
| [65535.2](#event-655352)   | 0x0011       |     22 |              4 |
| [65535.3](#event-655353)   | 0x0027       |     16 |              2 |
| [65535.4](#event-655354)   | 0x0037       |     14 |              2 |
| [65535.5](#event-655355)   | 0x0045       |     22 |              3 |
| [65535.6](#event-655356)   | 0x005B       |     14 |              2 |
| [65535.7](#event-655357)   | 0x0069       |     16 |              2 |
| [65535.8](#event-655358)   | 0x0079       |     20 |              3 |
| [65535.9](#event-655359)   | 0x008D       |     22 |              3 |
| [65535.10](#event-6553510) | 0x00A3       |     20 |              3 |
| [65535.11](#event-6553511) | 0x00B7       |     22 |              3 |
| [65535.12](#event-6553512) | 0x00CD       |     20 |              3 |
| [65535.13](#event-6553513) | 0x00E1       |     16 |              2 |
| [65535.14](#event-6553514) | 0x00F1       |     14 |              2 |
| [65535.15](#event-6553515) | 0x00FF       |     16 |              2 |
| [65535.16](#event-6553516) | 0x010F       |     14 |              2 |
| [65535.17](#event-6553517) | 0x011D       |     16 |              2 |
| [65535.18](#event-6553518) | 0x012D       |     14 |              2 |
| [65535.19](#event-6553519) | 0x013B       |     28 |              4 |
| [65535.20](#event-6553520) | 0x0157       |     26 |              4 |
| [65535.21](#event-6553521) | 0x0171       |      9 |              3 |
| [41](#event-41)            | 0x017A       |     29 |             10 |
| [402](#event-402)          | 0x0197       |     58 |             17 |
| [403](#event-403)          | 0x01D1       |     47 |             14 |
| [406](#event-406)          | 0x0200       |     65 |             18 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0166      |         358 |
|       1 | 0x001E      |          30 |
|       2 | 0x016C      |         364 |
|       3 | 0x0168      |         360 |
|       4 | 0x1D84      |        7556 |
|       5 | 0x2123      |        8483 |
|       6 | 0x2124      |        8484 |
|       7 | 0x2125      |        8485 |
|       8 | 0x2126      |        8486 |
|       9 | 0x2127      |        8487 |
|      10 | 0x212A      |        8490 |
|      11 | 0x212B      |        8491 |
|      12 | 0x212C      |        8492 |

## String References

- **7556**: Yowl! You've got guts to come to me auction house! I'm the one who's in charrrge 'ere! If you 'ave any trouble 'ere, come see me!
- **8483**: Wot's that you sez? Give you back the book I borrrrowed from the library?
- **8484**: Why, I always returrrn any books I borrow right on time, thank you! You sure you ain't got the wrong girrrl? Why would they think I've still got a book out?
- **8485**: Yo\`wl! Wot's that...? $3!? Do you think I'm the type to read a book like that? 'ow embarrrrassin'!
- **8486**: You nincompoop! Never in all me life 'as anyone even suggested I'd borrrrow an embarrassin' book like $3!
- **8487**: It's not just obstruction of business, why, it's violatin' me rights, that's what it is! Get the 'ell outta 'ere before I scrrratch ya eyes out!
- **8490**: Hae Jakhya!? Now you mention it, that is exactly like my name, ain't it?
- **8491**: Yowl! But 'ow the 'ell could someone mix up a girrrly princess kitten like 'er with a rough and tough lioness like me! That's just not on!
- **8492**: But, anyways, I'm glad that little matta is overrr! Quite relieved!

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
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=358*
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
0020:                      5B  00 80 F8 FF FF 7F F8 FF         [........
0030: FF 7F 74 6C 6B 32 00                              ..tlk2.         
```

#### Opcodes

```
  0: 0x0027 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk2" with entities [EventEntity, EventEntity], work=358*
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
0040: 74 6C 6B 32 00                                    tlk2.           
```

#### Opcodes

```
  0: 0x0037 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk2" with entities [EventEntity, EventEntity]
  1: 0x0044 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0045   |
| Data Size    | 22 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                81 00 F8  FF FF 7F 5B 00 80 F8 FF       ......[....
0050: FF 7F F8 FF FF 7F 74 68  6B 31 00                 ......thk1.     
```

#### Opcodes

```
  0: 0x0045 [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  1: 0x004B [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=358*
  2: 0x005A [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005B   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                   53 F8 FF FF 7F             S....
0060: F8 FF FF 7F 74 68 6B 31  00                       ....thk1.       
```

#### Opcodes

```
  0: 0x005B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  1: 0x0068 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0069   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                             5B 00 80 F8 FF FF 7F           [......
0070: F8 FF FF 7F 74 68 6B 32  00                       ....thk2.       
```

#### Opcodes

```
  0: 0x0069 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=358*
  1: 0x0078 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0079   |
| Data Size    | 20 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                             53 F8 FF FF 7F F8 FF           S......
0080: FF 7F 74 68 6B 32 81 01  F8 FF FF 7F 00           ..thk2.......   
```

#### Opcodes

```
  0: 0x0079 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  1: 0x0086 [0x81] SET_ENTITY_BLINKING(blink_flag=0x01, entity=EventEntity)
  2: 0x008C [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008D   |
| Data Size    | 22 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                         81 00 F8               ...
0090: FF FF 7F 5B 00 80 F8 FF  FF 7F F8 FF FF 7F 73 69  ...[..........si
00A0: 73 30 00                                          s0.             
```

#### Opcodes

```
  0: 0x008D [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  1: 0x0093 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sis0" with entities [EventEntity, EventEntity], work=358*
  2: 0x00A2 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A3   |
| Data Size    | 20 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:          53 F8 FF FF 7F  F8 FF FF 7F 73 69 73 30     S........sis0
00B0: 81 01 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x00A3 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sis0" with entities [EventEntity, EventEntity]
  1: 0x00B0 [0x81] SET_ENTITY_BLINKING(blink_flag=0x01, entity=EventEntity)
  2: 0x00B6 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B7   |
| Data Size    | 22 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                      7C  00 F8 FF FF 7F 5B 00 80         |.....[..
00C0: F8 FF FF 7F F8 FF FF 7F  67 75 74 30 00           ........gut0.   
```

#### Opcodes

```
  0: 0x00B7 [0x7C] EventEntity->Render.Flags2 |= 0x00
  1: 0x00BD [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "gut0" with entities [EventEntity, EventEntity], work=358*
  2: 0x00CC [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00CD   |
| Data Size    | 20 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                         53 F8 FF               S..
00D0: FF 7F F8 FF FF 7F 67 75  74 30 7C 01 F8 FF FF 7F  ......gut0|.....
00E0: 00                                                .               
```

#### Opcodes

```
  0: 0x00CD [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "gut0" with entities [EventEntity, EventEntity]
  1: 0x00DA [0x7C] EventEntity->Render.Flags2 |= 0x01
  2: 0x00E0 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E1   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:    5B 02 80 F8 FF FF 7F  F8 FF FF 7F 70 6F 69 30   [..........poi0
00F0: 00                                                .               
```

#### Opcodes

```
  0: 0x00E1 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "poi0" with entities [EventEntity, EventEntity], work=364*
  1: 0x00F0 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F1   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:    53 F8 FF FF 7F F8 FF  FF 7F 70 6F 69 30 00      S........poi0. 
```

#### Opcodes

```
  0: 0x00F1 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "poi0" with entities [EventEntity, EventEntity]
  1: 0x00FE [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00FF   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                               5B                 [
0100: 03 80 F8 FF FF 7F F8 FF  FF 7F 70 6F 69 31 00     ..........poi1. 
```

#### Opcodes

```
  0: 0x00FF [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "poi1" with entities [EventEntity, EventEntity], work=360*
  1: 0x010E [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x010F   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                               53                 S
0110: F8 FF FF 7F F8 FF FF 7F  70 6F 69 31 00           ........poi1.   
```

#### Opcodes

```
  0: 0x010F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "poi1" with entities [EventEntity, EventEntity]
  1: 0x011C [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x011D   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                                         5B 03 80               [..
0120: F8 FF FF 7F F8 FF FF 7F  70 6F 69 33 00           ........poi3.   
```

#### Opcodes

```
  0: 0x011D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "poi3" with entities [EventEntity, EventEntity], work=360*
  1: 0x012C [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x012D   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                         53 F8 FF               S..
0130: FF 7F F8 FF FF 7F 70 6F  69 33 00                 ......poi3.     
```

#### Opcodes

```
  0: 0x012D [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "poi3" with entities [EventEntity, EventEntity]
  1: 0x013A [0x00] END_REQSTACK()
```

### Event 65535.19

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x013B   |
| Data Size    | 28 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                   7C 00 F8 FF FF             |....
0140: 7F 81 00 F8 FF FF 7F 5B  02 80 F8 FF FF 7F F8 FF  .......[........
0150: FF 7F 61 6E 67 30 00                              ..ang0.         
```

#### Opcodes

```
  0: 0x013B [0x7C] EventEntity->Render.Flags2 |= 0x00
  1: 0x0141 [0x81] SET_ENTITY_BLINKING(blink_flag=0x00, entity=EventEntity)
  2: 0x0147 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ang0" with entities [EventEntity, EventEntity], work=364*
  3: 0x0156 [0x00] END_REQSTACK()
```

### Event 65535.20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0157   |
| Data Size    | 26 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                      53  F8 FF FF 7F F8 FF FF 7F         S........
0160: 61 6E 67 30 7C 01 F8 FF  FF 7F 81 01 F8 FF FF 7F  ang0|...........
0170: 00                                                .               
```

#### Opcodes

```
  0: 0x0157 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ang0" with entities [EventEntity, EventEntity]
  1: 0x0164 [0x7C] EventEntity->Render.Flags2 |= 0x01
  2: 0x016A [0x81] SET_ENTITY_BLINKING(blink_flag=0x01, entity=EventEntity)
  3: 0x0170 [0x00] END_REQSTACK()
```

### Event 65535.21

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0171  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:    5E 69 64 6C 30 1C 01  80 00                     ^idl0....      
```

#### Opcodes

```
  0: 0x0171 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0176 [0x1C] WAIT(30* ticks)
  2: 0x0179 [0x00] END_REQSTACK()
```

### Event 41

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x017A   |
| Data Size    | 29 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                                1E F0 FF FF 7F 6F            .....o
0180: 70 29 08 5D 10 0F 01 0B  1D 04 80 23 29 08 5D 10  p).].......#).].
0190: 0F 01 0C 20 00 21 00                              ... .!.         
```

#### Opcodes

```
  0: 0x017A [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x017F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0180 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0181 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Hae Jakkya (ID: 17764445/0x010F105D), tag_num=0x0B)
  4: 0x0188 [0x1D] PRINT_EVENT_MESSAGE(message_id=7556*)
    → "Yowl! You've got guts to come to me auction house! I'm the one who's in charrrge 'ere! If you 'ave any trouble 'ere, come see me!"
  5: 0x018B [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x018C [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Hae Jakkya (ID: 17764445/0x010F105D), tag_num=0x0C)
  7: 0x0193 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x0195 [0x21] END_EVENT
  9: 0x0196 [0x00] END_REQSTACK()
```

### Event 402

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0197   |
| Data Size    | 58 bytes |
| Instructions | 17       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                      1E  F0 FF FF 7F 6F 70 29 08         .....op).
01A0: 5D 10 0F 01 13 1D 05 80  23 29 08 5D 10 0F 01 0A  ].......#).]....
01B0: 29 08 5D 10 0F 01 01 1D  06 80 23 1D 07 80 23 29  ).].......#...#)
01C0: 08 5D 10 0F 01 03 29 08  5D 10 0F 01 04 20 00 21  .]....).].... .!
01D0: 00                                                .               
```

#### Opcodes

```
  0: 0x0197 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x019C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x019D [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x019E [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Hae Jakkya (ID: 17764445/0x010F105D), tag_num=0x13)
  4: 0x01A5 [0x1D] PRINT_EVENT_MESSAGE(message_id=8483*)
    → "Wot's that you sez? Give you back the book I borrrrowed from the library?"
  5: 0x01A8 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x01A9 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Hae Jakkya (ID: 17764445/0x010F105D), tag_num=0x0A)
  7: 0x01B0 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Hae Jakkya (ID: 17764445/0x010F105D), tag_num=0x01)
  8: 0x01B7 [0x1D] PRINT_EVENT_MESSAGE(message_id=8484*)
    → "Why, I always returrrn any books I borrow right on time, thank you! You sure you ain't got the wrong girrrl? Why would they think I've still got a book out?"
  9: 0x01BA [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x01BB [0x1D] PRINT_EVENT_MESSAGE(message_id=8485*)
    → "Yo`wl! Wot's that...? $3!? Do you think I'm the type to read a book like that? 'ow embarrrrassin'!"
 11: 0x01BE [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x01BF [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Hae Jakkya (ID: 17764445/0x010F105D), tag_num=0x03)
 13: 0x01C6 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Hae Jakkya (ID: 17764445/0x010F105D), tag_num=0x04)
 14: 0x01CD [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 15: 0x01CF [0x21] END_EVENT
 16: 0x01D0 [0x00] END_REQSTACK()
```

### Event 403

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01D1   |
| Data Size    | 47 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01D0:    1E F0 FF FF 7F 6F 70  29 08 5D 10 0F 01 13 1D   .....op).].....
01E0: 08 80 23 29 08 5D 10 0F  01 14 29 08 5D 10 0F 01  ..#).]....).]...
01F0: 09 1D 09 80 23 29 08 5D  10 0F 01 0A 20 00 21 00  ....#).].... .!.
```

#### Opcodes

```
  0: 0x01D1 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x01D6 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x01D7 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x01D8 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Hae Jakkya (ID: 17764445/0x010F105D), tag_num=0x13)
  4: 0x01DF [0x1D] PRINT_EVENT_MESSAGE(message_id=8486*)
    → "You nincompoop! Never in all me life 'as anyone even suggested I'd borrrrow an embarrassin' book like $3!"
  5: 0x01E2 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x01E3 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Hae Jakkya (ID: 17764445/0x010F105D), tag_num=0x14)
  7: 0x01EA [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Hae Jakkya (ID: 17764445/0x010F105D), tag_num=0x09)
  8: 0x01F1 [0x1D] PRINT_EVENT_MESSAGE(message_id=8487*)
    → "It's not just obstruction of business, why, it's violatin' me rights, that's what it is! Get the 'ell outta 'ere before I scrrratch ya eyes out!"
  9: 0x01F4 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x01F5 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Hae Jakkya (ID: 17764445/0x010F105D), tag_num=0x0A)
 11: 0x01FC [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 12: 0x01FE [0x21] END_EVENT
 13: 0x01FF [0x00] END_REQSTACK()
```

### Event 406

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0200   |
| Data Size    | 65 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0200: 1E F0 FF FF 7F 6F 70 29  08 5D 10 0F 01 0B 1D 0A  .....op).]......
0210: 80 23 29 08 5D 10 0F 01  0C 29 08 5D 10 0F 01 05  .#).]....).]....
0220: 1D 0B 80 23 29 08 5D 10  0F 01 06 29 08 5D 10 0F  ...#).]....).]..
0230: 01 07 1D 0C 80 23 29 08  5D 10 0F 01 08 20 00 21  .....#).].... .!
0240: 00                                                .               
```

#### Opcodes

```
  0: 0x0200 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0205 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0206 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0207 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Hae Jakkya (ID: 17764445/0x010F105D), tag_num=0x0B)
  4: 0x020E [0x1D] PRINT_EVENT_MESSAGE(message_id=8490*)
    → "Hae Jakhya!? Now you mention it, that is exactly like my name, ain't it?"
  5: 0x0211 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0212 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Hae Jakkya (ID: 17764445/0x010F105D), tag_num=0x0C)
  7: 0x0219 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Hae Jakkya (ID: 17764445/0x010F105D), tag_num=0x05)
  8: 0x0220 [0x1D] PRINT_EVENT_MESSAGE(message_id=8491*)
    → "Yowl! But 'ow the 'ell could someone mix up a girrrly princess kitten like 'er with a rough and tough lioness like me! That's just not on!"
  9: 0x0223 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0224 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Hae Jakkya (ID: 17764445/0x010F105D), tag_num=0x06)
 11: 0x022B [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Hae Jakkya (ID: 17764445/0x010F105D), tag_num=0x07)
 12: 0x0232 [0x1D] PRINT_EVENT_MESSAGE(message_id=8492*)
    → "But, anyways, I'm glad that little matta is overrr! Quite relieved!"
 13: 0x0235 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x0236 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Hae Jakkya (ID: 17764445/0x010F105D), tag_num=0x08)
 15: 0x023D [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 16: 0x023F [0x21] END_EVENT
 17: 0x0240 [0x00] END_REQSTACK()
```
